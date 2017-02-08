<?php
/**
 * Marca texto com padrões previamente analisados.
 */

ini_set("default_charset", 'utf-8');

$basedir = dirname(__DIR__);  //  clone root
$dirTree = 'htmLinks'; 		// csv
$originais = 'html'; 	// html original com UTF8 homologado

foreach (scandir("$basedir/$originais") as $f) if (substr($f,-5,5)=='.html') {
	echo "\n- $f";
	$htm2 = mark("$basedir/$originais/$f",true);
	file_put_contents("$basedir/html_mark/$f",$htm2);
}

// // // // // // // // //

function mark($file) {
	$clean = file_get_contents($file);
	$clean = preg_replace('#Cons[óo]rcio\s+Concremat.Arcadis(?:\s+Logos)?(?:\s+S.A)?|CONCREMAT(?:\s+ENGENHARIA)?(\s+E\s+TECNOLOGIA)?(\s+S.A)?#us', '<span class="organization_name">$0</span>', $clean);
	return $clean;
}


