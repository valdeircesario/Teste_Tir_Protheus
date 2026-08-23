# Utilitarios e extensoes

## Pasta `utilis`

### `md_reporter.py`

Implementa `TirReportAgent`, proxy do helper TIR que coleta metricas e gera relatorios Markdown. Tambem possui escrita atomica e atualizacao do indice geral.

### `poui_utilis.py`

Implementa `clicar_busca_avancada`, localizando o link PO-UI com `WebDriverWait` e disparando o clique via JavaScript. Aceita `Poui` e `Webapp` como fontes alternativas do driver.

### `selenium_utilis.py`

Implementa `click_child_by_id`, que encontra um elemento filho por XPath a partir do ID do componente.

### `grid_combobox.py`

Seleciona opcoes, le valores e verifica celulas de grids, inclusive em estruturas que exigem acesso ao Shadow DOM.

### `click_pageview.py`

Localiza botoes de relatorios/PageView por titulo, inclusive quando existem elementos visiveis concorrentes.

### `cpf_utilis.py`

Gera CPF para uso em massas de teste, formatado ou nao formatado.

## Pasta `tools`

### `Selenium_commands.py`

Agrupa comandos Selenium para XPath, CSS, classes, teclas, espera explicita e clique direito com `ActionChains`.

### `click_helper.py`

Fornece clique por ID com espera explicita.

### `click_css.py`

Implementa clique em alvo dentro de Shadow DOM usando host CSS, alvo CSS, Selenium e JavaScript.

### `gerador_relatorio.py`

Le o codigo-fonte de um teste, extrai comandos TIR por expressoes regulares, localiza screenshots, converte imagens para Base64 e cria um guia HTML autocontido em `C:\Relatorios_Homologacao`.

## Limites dos helpers

Os utilitarios acessam atributos internos do TIR e dependem da estrutura atual do DOM. Alteracoes de versao do Protheus, PO-UI ou TIR podem exigir ajustes nos seletores.
