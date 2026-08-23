# Agente de relatorios Markdown

O agente esta em `utilis/md_reporter.py` e e usado como uma camada intermediaria entre o teste e o `Webapp` do TIR.

```text
Teste -> TirReportAgent -> Webapp/TIR -> Selenium -> Protheus
```

## Construcao

O teste cria um `Webapp` e o passa ao agente junto com codigo, nome do modulo, identificador do caso e descricao. O agente cria uma pasta em:

```text
docs/reports/<codigo>_<nome>/
├── resultados.json
└── Relatorio_Consolidado.md
```

## Encaminhamento de chamadas

`__getattr__` recupera metodos do helper real. Quando o atributo e chamavel, retorna um wrapper que registra informacoes e executa a chamada original.

Metodos contabilizados:

- `SetButton`: cliques e confirmacoes.
- `WaitShow`: validacoes de telas/mensagens.
- `SetValue`: insercoes e alteracoes.
- `GetValue`: leituras.
- `Screenshot*`: capturas.
- `SetLateralMenu`: caminho da rotina, sem entrar nos contadores.

## Persistencia

Ao salvar, o agente:

1. Carrega o JSON existente.
2. Sobrescreve somente a chave do teste atual.
3. Registra status, data, duracao, descricao, rotina, contadores e traceback.
4. Regera integralmente o Markdown do modulo.
5. Atualiza `docs/reports/index.md`.

A funcao `_escrever_atomico` grava em arquivo temporario e usa `os.replace`, reduzindo o risco de deixar relatorios parciais.

## Falhas

`registrar_erro` marca `FALHOU` e guarda `traceback.format_exc()`. O teste deve relancar a excecao para que `pytest`/`unittest` mantenha o resultado de falha.

## Indice geral

`atualizar_indice_geral` varre todos os `resultados.json`, calcula aprovados/reprovados, identifica a ultima execucao e cria links para cada relatorio.

## Limites atuais

O agente mede chamadas, mas nao associa automaticamente cada screenshot a um link no Markdown. Tambem nao e um gerenciador de massa de dados: os registros sao criados pelos proprios fluxos de teste. Resultados persistidos representam a ultima execucao de cada chave de teste.
