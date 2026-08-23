# Evidencias, screenshots e logs

## Screenshots de teste

As chamadas `oHelper.Screenshot("Pasta/arquivo")` usam caminhos relativos a `screenshot/`. A pasta e organizada por entidade ou rotina funcional, como `Produto`, `Fornecedor`, `Cargo`, `Sindicato`, `CentroCusto`, `Funcao`, `Verba` e `TURNO_TRABALHO`.

O numero sequencial normalmente indica a ordem da etapa no fluxo, mas a convencao nao e uniforme entre todos os testes.

## Logs nativos

O TIR grava artefatos em `Log/<maquina>/`, com nomes contendo usuario, data/hora, rotina e nome do teste. Esses arquivos sao diagnosticos da execucao e nao substituem o relatorio consolidado.

## Videos e evidencias avulsas

`screenhots/VIDEOS` armazena gravacoes de demonstracao. Tambem existem imagens isoladas na raiz de `screenshot`, usadas para registrar erros ou evidencias especificas.

## Relacao com relatorios

O `TirReportAgent` conta chamadas de screenshot e grava somente essa metrica. O relatorio Markdown nao incorpora imagens nem cria links automaticos para os arquivos. O `gerador_relatorio.py` possui comportamento diferente: tenta localizar as imagens e embuti-las em Base64 no guia HTML.

## Leitura recomendada de uma execucao

1. Consultar `docs/reports/index.md`.
2. Abrir o relatorio do modulo.
3. Consultar `resultados.json` para dados estruturados e traceback.
4. Localizar screenshots pela pasta funcional.
5. Consultar `Log` quando for necessario diagnosticar o TIR ou o navegador.
