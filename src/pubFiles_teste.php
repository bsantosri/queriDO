<?php

$dir = dirname(__DIR__); //

/* auxiliar para sh 
	foreach (scandir("$dir/html") as $f) if (substr($f,-5,5)=='.html') {
		$f2 = preg_replace('/^\d+-/','',$f);
		$f2 = str_replace('.html','.htm',$f2);
		echo "\ngit mv $f $f2";
		//file_put_contents("html_clean/$f",$htm2);
	}
*/


?>
Resto no Javascript, via jQuery-load.


