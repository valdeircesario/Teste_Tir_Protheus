# Automacao PO-UI

## Quando usar

`Webapp` atende telas tradicionais do Protheus. `Poui` atende telas construidas com PO-UI/THF, como `po-input`, `po-combo`, `po-table`, `po-tabs` e switches.

As instancias nao devem ser misturadas: comandos de componentes PO-UI devem ser chamados em `oHelper_Poui`, enquanto login, ambiente e navegacao tradicional normalmente usam `oHelper`.

## Fluxo existente

O arquivo `tests/test_fluxo_necessidade_compra_poui.py`:

1. Cria `Webapp` e `Poui` com o mesmo `config.json`.
2. Executa `Setup` no ambiente Protheus.
3. Trata avisos de homologacao e moedas.
4. Navega ate Novo Fluxo de Compras.
5. Abre o menu PO-UI de Necessidade de Compra.
6. Usa busca avancada, filtro, botao, icone, switch, aba, tabela e select.
7. Finaliza com `AssertTrue` e encerra a sessao.

## Metodos usados

- `ClickMenu`
- `InputValue`
- `ClickButton`
- `ClickIcon`
- `ClickSwitch`
- `POtabs`
- `ClickTable`
- `ClickSelect`

## Helper de busca avancada

`utilis/poui_utilis.py` obtem o driver interno, aguarda `.po-page-list-filter-search-link` e executa clique JavaScript. Esse recurso existe para contornar sobreposicao, timing e comportamento Angular.

## Riscos tecnicos

A implementacao usa atributos privados do TIR, como `_Poui__poui` e `_Webapp__webapp`. Isso e pratico para diagnostico, mas pode quebrar com mudancas internas do framework. Os seletores tambem dependem do DOM atual da aplicacao.
