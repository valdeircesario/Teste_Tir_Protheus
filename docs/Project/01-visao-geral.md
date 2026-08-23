# Visao geral

## Objetivo

Automatizar cenarios funcionais do TOTVS Protheus, registrar evidencias da execucao e disponibilizar resultados para analistas, desenvolvedores e homologadores.

## Tecnologias

- Python 3.12 ou superior.
- TIR Framework para login, navegacao, preenchimento, validacao e encerramento.
- Selenium/WebDriver para interacoes de baixo nivel.
- `unittest.TestCase` como estrutura dos testes.
- `pytest` como executor e gerador opcional de HTML.
- PO-UI para telas Angular e componentes como tabelas, abas, combos e switches.
- Markdown, JSON e HTML para documentacao e relatorios.

## Tipos de automacao

### Rotinas tradicionais

Usam `tir.Webapp` e comandos como `Setup`, `SetLateralMenu`, `SetButton`, `SetValue`, `WaitShow`, `CheckResult`, `Screenshot` e `TearDown`.

### Rotinas PO-UI

Usam `Webapp` para preparar o ambiente Protheus e `Poui` para componentes da interface Angular. O projeto tambem possui helpers Selenium para elementos encapsulados em Shadow DOM.

## Resultado esperado de um teste

Um caso deve abrir a rotina, preparar a massa, executar o fluxo funcional, validar o resultado, capturar evidencias e liberar o navegador mesmo quando ocorre uma falha.
