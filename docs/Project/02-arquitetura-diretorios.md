# Arquitetura e diretorios

```text
Teste_Tir_Protheus/
├── tests/                 testes executaveis
├── casos_de_testes/       especificacoes funcionais em Markdown
├── utilis/                helpers reutilizaveis e agente Markdown
├── tools/                 extensoes Selenium e gerador HTML
├── screenshot/            evidencias organizadas por rotina
├── Log/                   artefatos nativos do TIR
├── docs/reports/          resultados consolidados por modulo
├── reports/               relatorios HTML do pytest
├── report/                artefato HTML adicional
├── assets/                recursos visuais
├── config.json            configuracao local, com credenciais
├── config.template.json   modelo de configuracao
├── setup.ps1              preparacao do ambiente virtual
└── run_test.py            atalho de execucao legado
```

## `tests`

Agrupa os testes por modulo do Protheus: `SIGAGPE`, `SIGACOM`, `SIGAATF`, `SIGACSA`, `SIGACTB` e `Outros`. O fluxo PO-UI de necessidade de compra fica na raiz de `tests` por ter um modelo de automacao diferente.

## `casos_de_testes`

Representa a camada funcional/documental. Os diretorios seguem o modulo e a rotina, por exemplo `casos_de_testes/SIGACOM/MATA010/`.

## `utilis` e `tools`

`utilis` contem funcoes de apoio diretamente consumidas pelos testes. `tools` contem componentes de extensao e automacao auxiliar, incluindo o gerador de guia de homologacao HTML.

## Saidas

`docs/reports` e a saida do agente Markdown. `reports` e `report` contem saidas HTML. `screenshot` e `Log` armazenam evidencias de tela e diagnosticos do TIR.
