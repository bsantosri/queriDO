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

	// especifico da curadoria:
	$clean = preg_replace(
		'#Cons[óo]rcio\s+Concremat.Arcadis(?:\s+Logos)?(?:\s+S.A)?|CONCREMAT(?:\s+ENGENHARIA)?(\s+E\s+TECO?NOLOGIA)?(\s+(?:S[/\.]A\.?|Ltda\.))?#uis',
		'<span class="organization_name">$0</span>',
		$clean
	);

	// homologados
	$clean = preg_replace('#(?:CNPJ[\s:\-\.]*)?\d\d\.\d\d\d\.\d\d\d/\d\d\d\d\-\d\d#uis', '<span class="organization_vatID">$0</span>', $clean);
	$clean = preg_replace('#Artigo\s+[\d\.]+\sInciso\s+.+?\s+da\s+Lei\s+n?º?\s*\d[\d\.]+\d[/\s]+\d\d\d\d#uis', '<span class="lexml_cite">$0</span>', $clean);
	$clean = preg_replace('#Artigo\s+[\d\.]+\sda\s+Lei\s+n?º?\s*\d[\d\.]+\d[/\s]+\d\d\d\d#uis', '<span class="lexml_cite">$0</span>', $clean);
	$clean = preg_replace('#(?:Lei|Descreto\s+Lei|Decreto|Portaria)\s+n?º?\s*\d[\d\.]+\d[/\s]+\d\d(\d\d)?#uis', '<span class="lexml_cite">$0</span>', $clean);

	$clean = preg_replace('#Contrato\s+(?:N\.?º?\s*)?\d[\d\-\./]+(/\d\d\d\d)?#uis', '<span class="contract_cite">$0</span>', $clean);
	$clean = preg_replace('#Processo(?:\s+INSTRUTIVO|\s+administrativo)?\s*(?:N\.?º?\s*|:\s*)?\d[\d\-\./]+#uis', '<span class="govProcess_cite">$0</span>', $clean);
	$clean = preg_replace('#matr(?:\.|[ií]cula)\s+(?:N\.?º?\s*)?\d[\d\-\./]+#uis', '<span class="matricula_cite">$0</span>', $clean);

	$clean = preg_replace('#(?:\s*<[ubi]>\s*)*Valor(?:\s*</[ubi]>\s*)*[\s:]*(de\s)?R\$\s*\d[\d\,\.]+#uis', '<span class="valor_cite">$0</span>', $clean);
	$clean = preg_replace('#\d\d?\s+de\s+(?:janeiro|fevereiro|mar[çc]o|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro)\s+de\s+\d\d\d\d#uis', '<span class="date_cite">$0</span>', $clean);

	// sem efeito (e ainda não-testados)
	$clean = preg_replace('#(?:CPF[\s:\.]*)?\d\d\d\.\d\d\d\.\d\d\d\-\d\d\d#uis', '<span class="person_vatID">$0</span>', $clean);
	$clean = preg_replace('#RG[\s:\.]*\d\d[\d\-\.]+#uis', '<span class="person_rg">$0</span>', $clean);
	$clean = preg_replace('#CEP[\s:\-\.]*\d\d\.\d\d\d\.\d\d\d/\d\d\d\d\-\d\d#uis', '<span class="postalCode">$0</span>', $clean);

	return $clean;
}
