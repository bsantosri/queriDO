<?php
/**
 * Extrae template do DOM-Rio, específico dele.
 */

ini_set("default_charset", 'utf-8');

$basedir = dirname(__DIR__);  //  clone root
$dirTree = 'htmLinks'; 		// csv
$originais = 'newhtml'; 	// html original com UTF8 homologado

foreach (scandir("$basedir/$originais") as $f) if (substr($f,-5,5)=='.html') {
	echo "\n- $f";
	$htm2 = superClen("$basedir/$originais/$f",true);
	file_put_contents("$basedir/html_clean/$f",$htm2);
}

// // // // // // // // //

function superClen($file) {
	$META = '<meta charset="UTF-8"/>';
	$clean = file_get_contents($file);
	$clean = preg_replace('/^\s*<html>/s', "<html>$META", $clean);
	$clean = XMLpretty($clean);
	$clean = strip_tags($clean, '<html><p><b><i><u><br><sub><sup><td><tr><table><blockquote><q><li><ol><ul>');
	$clean = preg_replace('/\n\s*\n\s*/s', "\n\n", $clean);
	return "<html>$META\n$clean</html>";
}

function x2dom($xml) {
	$dom = new DOMDocument('1.0', 'UTF-8');
	$dom->formatOutput = true;
	$dom->preserveWhiteSpace = false;
	$dom->resolveExternals = false; // external entities from a (HTML) doctype declaration
	$dom->recover = true; // Libxml2 proprietary behaviour. Enables recovery mode, i.e. trying to parse non-well formed documents
	$ok = @$dom->loadHTML($xml, LIBXML_NOENT | LIBXML_NOCDATA);
	if ($ok) return $dom; else return NULL;
}

function XMLpretty($xml) {
	$dom = x2dom($xml);
	if (!$dom) die("\nOPS, confira ERRO DOM.\n");
	$dom->preserveWhiteSpace = false;
	$dom->resolveExternals = false; // external entities from a (HTML) doctype declaration
	$dom->formatOutput = true;
	foreach ($dom->getElementsByTagName('meta') as $e) $e->nodeValue = '';
	foreach ($dom->getElementsByTagName('script') as $e) $e->nodeValue = '';
	foreach ($dom->getElementsByTagName('style') as $e) $e->nodeValue = '';
	foreach ($dom->getElementsByTagName('head') as $e) $e->nodeValue = '';
	$xpath = new DOMXPath($dom);
	foreach ($xpath->query('//comment()') as $e) $e->nodeValue = '';
	foreach ($xpath->query('//*[@style]') as $at) $at->removeAttribute('style');
	$tabtopo = $xpath->query('//table[@class="topo_materia"]');
	$htm = '';
	if (strlen(trim($tabtopo->item(0)->nodeValue))>100){
		$div = $xpath->query('//td//div[@id="pagina"]');
		if (strlen(trim($div->item(0)->nodeValue))>100) {
			print ".. div id-pagina..";
			$htm = $dom->saveXML($div->item(0));
		}
	}
	if (!$htm) {
		print ".. full lixo!..";
		$htm = $dom->saveXML($dom->documentElement);
	}
	return  $htm;
}
