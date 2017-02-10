<?php
/**
 * Marca texto com padrões previamente analisados.
 */

ini_set("default_charset", 'utf-8');

$basedir = dirname(__DIR__);  //  clone root

// $dirTree = 'data/do-info'; 		// csv
// $originais = 'content/original'; 	// html original com UTF8 homologado
$filtrados = 'content/filtrado'; 	// html limpo
$marcados = 'content/marcado'; 	// destino!

foreach (scandir("$basedir/$filtrados") as $f) if (substr($f,-5,5)=='.html') {
	echo "\n- $f";
	$htm2 = mark("$basedir/$filtrados/$f",true);
	file_put_contents("$basedir/$marcados/$f",$htm2);
}

// // // // // // // // //

function mark($file) {
	$clean = file_get_contents($file);
	$clean = preg_replace('#Cons[óo]rcio\s+Concremat.Arcadis(?:\s+Logos)?(?:\s+S.A)?|CONCREMAT(?:\s+ENGENHARIA)?(\s+E\s+TECNOLOGIA)?(\s+S.A)?#us', '<span class="organization_name">$0</span>', $clean);
	return $clean;
}


