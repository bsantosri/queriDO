Descrição informal e detalhes adicionais sobre o **Projeto `queriDO`** ou  **"nosso Querido Diario Oficial"**.

(lixo **revisar** e linkar com [curadoria001](../report/curadoria001.md) e cia)

## Equipe

O projeto ainda "gratis" e inscipiente. Precisamos de voluntários.

Estamos aguardando a sua participação!  Participe para sentir a "mão-na-massa", dar sua opinião... E se gostar, escolha suas metas-pé-no-chão... E continue participando: mesmo que pouco, é importante preservar a frequência mínima de participação, de todos os envolvidos numa meta: sempre aparece mais um para ajudar, se ver os envolvidos por perto, acolhendo e tomando conta.

## Objetivo
Até que a equipe deixe de ser flutuante, as metas permanecerão meio indefinidas. Por hora as principais:

1. Criar uma metadologia para obter matérias de um Diário Oficial (por hora do Rio de Janeiro e assemelhados), dentro de um determinado escopo.

2. Automatizar o que for possível da metodologia, garantindo fontes de matéria com máxima fidelidade (bater com o original publicado), em formato aberto (UTF-8 HTML) e bem estruturado (sem perda de informação estrutural tal como títulos, itens, seções, negritos, itálicos, tabelas, etc.).

3. Criar metodologia para compensar perdas de estrutura (ex. perda de seções, títulos, identificadores, etc.) ou informação (ex. caso de PDF convertido por OCR).

4. Criar convençes para armazenar aqui no *git* os originais fornecidos, e os textos processados para recuperação de estrutura.

5. Criar convençes para a marcação adicional: extração de endereços (ex. CEP e rua), CPF, CNPJ, RG, nomes de empresa, códigos de contrato, citações de leis, etc.

6. Automatizar o que for possível no processo de marcação adicional.

## Origem e motivações do projeto

O [acidente da ciclovia Tim Maia, obra da Concremat](http://brasil.elpais.com/brasil/2016/04/21/politica/1461256688_847248.html), fez com que um grupo de amigos passasse a noite tentando extrair do diário oficial da cidade do Rio informações sobre os contratos do município com a empreiteira. A tarefa hercúlea nos alertou para o quão valioso seria um script capaz de extrair sistematicamente informações do diário e torná-las verdadeiramente abertas. As possibilidades a partir daí seriam inúmeras. Em excel, gráfico, verso e prosa.

O Diário Oficial é como um blog, importantíssimo, mas que "ninguém" lê.
Um Diário que é "aberto" apenas por alguns usuários descontentes.
Na tentativa de torná-lo aberto e reutilizável, não só no formato, mas na linguagem, iniciamos uma saga não só de programação, mas de idealização desse projeto que chamamos carinhosamente de *"nosso querido diário oficial"* e que chamou a atenção do Govlab em NY,  onde foi realizado um *coaching*, entre agosto e outubro de 2016.  

Entre agosto e setembro de 2016 houve contato da Bruna e do Henrique, do grupo de amigos, com a [OKBr](http://br.okfn.org/)... Até que o Peter ficou sabendo, e sugeriu unificar os requisitos do *QueriDO* com o [Diário Livre](http://devcolab.each.usp.br/do/), desenvolvido pelo COLAB-USP e apoiado pela OKBr, criando aqui no *git coletivo `okfn-brasil`* uma iniciativa mais ampla... Partes do código do Diário Livre,  como o [trazdia](https://github.com/andresmrm/trazdia) do Andres é semelhante ao que vinham desenvolvendo no *QueriDO*.

No final de dezembro de 2016, com chegada de um voluntário animado, o Marco, decidimos criar um plano de metas para 2017: é o que está resumido na seção acima dos objetivos.

## Situação (*roadmap*)

Apesar de não termos documentado, nos sentimos bem maduros quanto à metodologia do item 1 dos objetivos, e já fizemos vários testes de automação para o item 2. A meta em janeiro de 2017  é fechar a automação (provavelmente tudo em Python) e manter o fluxo de processamento num banco PostgreSQL, gravando no *git* apenas documentos originais e finais.
