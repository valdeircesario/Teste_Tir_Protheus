# Casos de teste

## Papel

`casos_de_testes` e a camada de especificacao funcional. Ela descreve o comportamento esperado independentemente da implementacao Python.

## Organizacao

Os casos sao agrupados por modulo e rotina:

```text
casos_de_testes/
├── SIGAATF/<rotina>/CT01_<rotina>.md
├── SIGACOM/<rotina>/CT01_<rotina>.md
├── SIGACSA/<rotina>/CT01_<rotina>.md
└── SIGAGPE/<rotina>/CT01_<rotina>.md
```

## Conteudo tipico

- Identificacao do caso e rotina.
- Caminho funcional no Protheus.
- Objetivo.
- Passos `CREATE`, `READ` e `UPDATE`.
- Validacao de campos obrigatorios.
- Validacao de duplicidade.
- Resultado esperado.
- Criterio de aprovacao.
- Status, evidencias, responsavel e data de execucao.

## Relacao com os testes Python

O Markdown e a intencao funcional; o arquivo Python e a implementacao automatizada. O alinhamento ideal e um caso documentado para cada teste executavel, com o mesmo identificador, rotina, campos e evidencias.

## Estado observado

A cobertura documental e menor que a quantidade de testes Python. Existem arquivos em `tests/Outros` sem caso Markdown correspondente e alguns casos ainda possuem campos de execucao como `A definir`. Tambem ha divergencias pontuais de identificacao em documentos, que devem ser tratadas como manutencao documental quando o caso for homologado.

## Exemplo

`casos_de_testes/SIGACOM/MATA010/CT01_MATA010.md` descreve inclusao, visualizacao e alteracao de produto, incluindo obrigatoriedade e duplicidade. O teste correspondente implementa principalmente o fluxo CRUD automatizado.
