`queriDO` ou  **"nosso Querido Diario Oficial"**... Por uma versão *machine-readable* dos Diários Oficiais do Brasil. Municipais, estaduais e da união.

A **comunudade mantenedora deste projeto** é formada por fois grupos:

* **curadorias**: definem os "alvos", estabelcem para quais assuntos e diários oficiais desejam voltar seus olhares, fazer suas explorações, e mais tarde entregar seus relatórios e pareceres.

* **experts**: programadores, linguístas, ou simples entusiastas do [data scraping](https://en.wikipedia.org/wiki/Data_scraping), colaborador, interessados em ajudar a curadoria a achar a "agulha no palheiro", e preparar milhares de separatas de diários oficiais para constituir um [corpus textual](https://en.wikipedia.org/wiki/Corpus_linguistics) de análise bem estruturado e suficientemente completo para cada alvo definido pelas curadoriais. Curadores experientes também são *experts* e podem oferecer seus conhecimentos aos novos curadores.

[Clique aqui](https://okfn-brasil.github.io/queriDO/) para testar as separatas elecandas para a *Curadoria da ciclovia Tim Maia*.

Maiores detalhes ver um [breve histórico do projeto](_docs/README.md).

-----

## Dinâmica de um ciclo de registros

Dinâmica da formação de alvos e conteúdos neste projeto:

**Passo-1**. **Formação de uma _curadoria_ e seu _alvo_**. Um grupo de pessoas (curadores), acolhido por pelo menos um [membro da OKBr](https://br.okfn.org/membros/). A curadoria recebe um registro formal [nesta planilha](data/curadoria.csv) (editável [neste GDoc](https://docs.google.com/spreadsheets/d/1-LqoLFCMPWs0UHrY3WXSV10S9eYIxpshOzDXsIFXlJA/edit#gid=770195002)) e se apresenta com a lista de participantes e todos os detalhes sobre motivações e metas, [num relatório como este](_docs/README.md).

**Passo-2**.  **Testes, prospecção e avaliação da viabilidade**. Com apoio do grupo de *experts*, a nova curadoria faz testes de prospecção (usando outras ferramentas como o Diário Livre, os diversos diários oficiais, etc.) e define com mais precisão seu alvo, reformulando-os se necessário. Com os testes também refina o seu relatório e "bate martelo" sobre qual Diário Oficial e quais anos prospectar.

**Passo-3**.  **Resgate dos origiais**. A equipe de *experts* recupera os conteúdos oficiais (separatas de Diários Oficiais) de forma o mais fiel possível, armazenando no *git* do presente projeto todos os [conteúdos originais](conteudo/original).

**Passo-4**.  **Filtragen**. A equipe de *experts* avalia a melhor forma de "limpar" os originais e armazená-los como   [conteúdos filtrados](conteudo/filtrado). Com este conteúdo disponibilizado em ferramentas de busca e visualização, torna-se possível decidir quais elementos precisam ser marcados. Nesta etapa a *curadoria*  também já pode se manifestar sobre a fidelidade e completeza do material obtido.

**Passo-5**.  **Marcação**. A equipe de *experts* avalia a melhor forma de "marcar" os conteúdos filtrados para destacar e organizar com precisão todas as informações a serem extraídas e relacionadas entre si.

**Passo-6**.  **Revisão do levantamento e da marcação**. A curadoria avalia o material marcado e seu uso, eventualmente solicitando mais conteúdos, por exemplo matérias citadas (adendos que citam contratos, leis que citam outras leis, etc.)

**Passo-7**.  **Relatório da curadoria**. Em posse de toda a informação a *curadoria* emite um parecer e um ou mais relatórios onde faz uso das informações para as finalidades desejadas.

Todos os conteúdos, originais e marcados, são preservados no git por tempo indeterminado (horizonte de *anos*). O ciclo pode se repetir para aprofundamentos ou ampliação das pesquisas.

NOTA: os passos 3 a 5 são indicados nas visualizações de conteúdo dos Diários Oficiais como "resultantes de processameto" 1, 2 ou 3 respectivamente.

------

## Licensas livres

Esta iniciativa é mantida pela [Plataforma de Projetos da OKBr](https://br.okfn.org/projetos/).

Todos os softwares e conteúdos deste projeto são livres, em conformidade com a [OpenDefinition](http://openDefinition.org/od/2.0/pt-br/):

* *conteúdos dos Diários Oficiais* são [implicitamente de domínio público (licensa **CC0**)](https://github.com/ppKrauss/licenses/blob/master/reports/implied-lex-BR-v1.md).

* os *softwares* produzidos pela OKBr e seus colaboradores do projeto queriDO receberam [licensa **MIT**](https://opensource.org/licenses/MIT).

* os *demais conteúdos* receberam licensa [**CC-BY-3.0**](https://creativecommons.org/licenses/by/3.0/br/)
