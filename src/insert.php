<?php
/**
 * Insere texto marcado na base de dados, como XML.
 * Check     php --info | grep pdo
 * Install   apt install php7.0-pgsql
 * USE:  php src/insert.php | more
 */


// CONFIG:
 $marcados = 'content/marcado';
 $db = new PDO('pgsql:host=localhost;dbname=restest', 'postgres', 'postgres');
 // or try ... catch (PDOException $e) die ('Connection failed: ' . $e->getMessage()."\n");

ini_set("default_charset", 'utf-8');
$basedir = dirname(__DIR__);    //  clone root
$dir = "$basedir/$marcados";

echo "
....
   LEMBRETE: antes de rodar aqui precisa preparar a base restest com 
   psql -h localhost -U postgres restest < step1.sql
....
RODANDO INSERTS!
";


foreach (scandir($dir) as $f) if (preg_match('/^(.+)\.html$/',$f,$m)) {
	$urn = "br;rj;rio.janeiro:gov-exe:2015-02-02:materia:$m[1]";
	$content = file_get_contents("$dir/$f");
	$st = $db->prepare("INSERT INTO content (urn_do,content,info) VALUES (:urn,:content,to_jsonb(:info))");
	$res = $st->execute([ "urn" => $urn, "content" => $content, "info"=>"{\"do_materia\":$m[1],\"do_data\":'2017-02-02'}" ]);
	$res = $res? "(sucesso)": "(FALHOU, talvez já exista)";
	echo "\n-- matéria $m[1] = $res";
}
echo "\n-- fim, mas falta fazer UPDATE para carregar o cache, use o comando

   psql -h localhost -U postgres restest -c \"UPDATE content SET kx = content_count(content)\"

";

