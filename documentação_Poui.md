# Documentação da Classe `Poui`

A classe `Poui` é um wrapper de automação para componentes da biblioteca **PO-UI** (Portinari UI / THF), utilizada para criação de testes automatizados de interfaces web dentro do framework **TIR** (Totvs Interface Robot). Ela encapsula uma instância interna (`PouiInternal`) e expõe métodos de alto nível para interagir com os principais componentes visuais do framework (menus, inputs, combos, tabelas, botões, etc.).

> **Documentação oficial do PO-UI:** https://po-ui.io/documentation

---

## ⚠️ LEIA ANTES DE TUDO: Como instanciar e chamar os comandos corretamente

Este é o ponto **mais importante** de toda a documentação e a causa mais comum de erros ao usar a classe `Poui`. Leia com atenção antes de usar qualquer método listado abaixo.

### 1. `Poui` é uma classe diferente de `Webapp`

O TIR trabalha com duas classes principais:

| Classe | Uso | Componentes que testa |
|---|---|---|
| `Webapp` | Telas do Protheus tradicionais (padrão TIR clássico) | Componentes clássicos do Protheus |
| `Poui` | Telas construídas com **PO-UI / THF** | `po-input`, `po-combo`, `po-table`, `thf-grid`, `po-tabs`, etc. |

Essas duas classes **não compartilham métodos entre si**. Ou seja:

```python
self.oHelper.ClickTable(...)   # ❌ ERRO: Webapp não tem ClickTable
```

```
AttributeError: 'Webapp' object has no attribute 'ClickTable'. Did you mean: 'ClickLabel'?
```

Isso acontece porque `self.oHelper` normalmente é uma instância de `Webapp`, e os métodos documentados aqui (`ClickTable`, `POtabs`, `ClickCombo`, `ClickLookUp`, etc.) **pertencem exclusivamente à classe `Poui`**.

### 2. Nunca instancie `Poui()` "solta" dentro do teste

Criar uma nova instância de `Poui()` manualmente, sem passar o `config_path`, gera erro, pois o construtor tenta iniciar uma sessão de navegador do zero sem configuração:

```python
Poui().ClickTable(...)   # ❌ ERRO
```

```
Exception: config.json file not found!
```

### 3. A instância correta é sempre `self.oHelper_Poui`

No projeto, a instância da classe `Poui` já é criada corretamente (geralmente no `setUp()` do caso de teste, com o `config_path` apontando para o `config.json` do projeto) e fica disponível como atributo da classe de teste, com o nome padrão:

```python
self.oHelper_Poui
```

**Toda chamada de método da classe `Poui` deve, obrigatoriamente, seguir este padrão:**

```python
self.oHelper_Poui.NomeDoMetodo(parâmetros)
```

### 4. Resumo da regra de ouro

| ✅ Correto | ❌ Errado | Motivo do erro |
|---|---|---|
| `self.oHelper_Poui.ClickTable(...)` | `self.oHelper.ClickTable(...)` | `self.oHelper` é `Webapp`, não tem esse método |
| `self.oHelper_Poui.POtabs(...)` | `Poui().POtabs(...)` | Cria instância nova sem `config_path` → erro |
| `self.oHelper_Poui.ClickCombo(...)` | `self.ohelper_poui.ClickCombo(...)` | Nome do atributo é *case sensitive*: `oHelper_Poui`, com "H" e "P" maiúsculos |

> 💡 **Regra prática para lembrar:** sempre que for usar um comando de uma tela feita em **PO-UI/THF** (abas, combos, tabelas com checkbox, switches, lookups avançados, etc.), o comando começa assim:
> ```python
> self.oHelper_Poui.
> ```
> E **todo exemplo desta documentação, a partir daqui, já segue esse padrão.**

---

## Índice

1. [Visão geral e comportamento interno](#visão-geral-e-comportamento-interno)
2. [Inicialização](#inicialização)
3. [Métodos de navegação e menu](#métodos-de-navegação-e-menu)
4. [Métodos de preenchimento de campos](#métodos-de-preenchimento-de-campos)
5. [Métodos de clique em componentes](#métodos-de-clique-em-componentes)
6. [Métodos de tabela / grid](#métodos-de-tabela--grid)
7. [Métodos de espera (wait)](#métodos-de-espera-wait)
8. [Métodos de verificação e asserção](#métodos-de-verificação-e-asserção)
9. [Métodos de localizadores customizados](#métodos-de-localizadores-customizados)
10. [Encerramento do teste](#encerramento-do-teste)
11. [Erros comuns e como resolver](#erros-comuns-e-como-resolver)

---

## Visão geral e comportamento interno

### Construtor

```python
Poui(config_path="", autostart=True)
```

**Parâmetros:**
- `config_path` (`str`): Caminho para o arquivo de configuração do teste (`config.json`). Se vazio ou incorreto, a instanciação **falha** com `Exception: config.json file not found!`.
- `autostart` (`bool`): Define se o navegador/driver deve iniciar automaticamente ao instanciar a classe. **Padrão:** `True`.

> ⚠️ Na prática, **você não deve chamar este construtor diretamente** no corpo dos seus testes. A instância já vem pronta como `self.oHelper_Poui`. Veja a seção [LEIA ANTES DE TUDO](#️-leia-antes-de-tudo-como-instanciar-e-chamar-os-comandos-corretamente) acima.

**O que acontece internamente ao instanciar:**
- É criada uma instância interna `PouiInternal`, responsável pela execução real das ações no navegador (Selenium).
- É criado um `ConfigLoader`, responsável por carregar as configurações do teste.
- O atributo `self.coverage` é definido a partir da configuração de cobertura de testes (`self.config.coverage`).

### Comportamento de `__getattribute__` (importante entender)

A classe sobrescreve o método mágico `__getattribute__` para controlar automaticamente uma *flag* interna chamada `_flag_is_new_browse`.

**Regra de funcionamento:**
- Sempre que um método **público** (que não começa com `_`) da classe é acessado/chamado,
- **e** esse método **não** está na lista de métodos preservados (`SearchBrowse`, `FilterBrowse`, `SetButton`),
- então a flag `self.config._flag_is_new_browse` é redefinida para `None`.

**Por que isso existe?**
Essa flag é usada para controlar se o teste está atuando sobre uma tela de "Browse" no novo padrão (THF/kendo-grid). Ao chamar `FilterBrowse`, a flag é marcada como `True` (ver seção correspondente). Qualquer outra chamada de método (exceto as da lista de preservação) reseta esse estado, garantindo que o comportamento de filtro de browse não "vaze" indevidamente para chamadas subsequentes não relacionadas.

Isso é um detalhe de implementação interna — o usuário do framework normalmente **não precisa se preocupar** com isso, mas é útil saber caso o comportamento de `FilterBrowse` pareça inconsistente ao intercalar chamadas de outros métodos.

---

## Inicialização

> Lembre-se: em todos os exemplos abaixo, `self.oHelper_Poui` é a instância já pronta e configurada da classe `Poui` dentro do seu caso de teste.

### `self.oHelper_Poui.GetUrl(url)`

Carrega uma página web na sessão atual do navegador.

**Parâmetros:**
- `url` (`str`): Endereço da página a ser carregada.

**Uso:**
```python
self.oHelper_Poui.GetUrl("https://po-ui.io")
```

### `self.oHelper_Poui.Program(program_name='', module='')`

Define o programa/rotina a ser aberto no campo de busca do menu inicial. Utilizado apenas quando o programa inicial é o módulo (ex: `SIGAFAT`).

**Parâmetros:**
- `program_name` (`str`): Nome do programa a ser buscado.
- `module` (`str`): Sigla do módulo, usada para diferenciar rotinas com o mesmo nome. **Padrão:** `""`.

**Uso:**
```python
self.oHelper_Poui.Program("MATA020")
self.oHelper_Poui.Program("CRDA200", module="CRD")
```

---

## Métodos de navegação e menu

### `self.oHelper_Poui.ClickMenu(menu_item)`

Clica em um item de menu do componente `po-menu`.
🔗 https://po-ui.io/documentation/po-menu

**Parâmetros:**
- `menu_item` (`str`): Nome do item de menu.

**Uso:**
```python
self.oHelper_Poui.ClickMenu("Contracts")
```

### `self.oHelper_Poui.POtabs(label='')`

Clica em uma aba (label) dentro de um componente `po-tabs`.
🔗 https://po-ui.io/documentation/po-tabs

**Parâmetros:**
- `label` (`str`): Nome da aba a ser clicada.

**Uso (exemplo real validado):**
```python
# Clicar na aba "Em aberto"
self.oHelper_Poui.POtabs(label='Em Aberto')

# Clicar na aba "Atendidas"
self.oHelper_Poui.POtabs(label='Atendidas')

# Clicar na aba "Parcialmente atendidas"
self.oHelper_Poui.POtabs(label='Parcialmente atendidas')
```

### `self.oHelper_Poui.ClickAvatar(position=1)`

Clica no ícone de avatar de perfil do usuário (`po-avatar`).
🔗 https://po-ui.io/documentation/po-avatar

**Parâmetros:**
- `position` (`int`): Posição do elemento, caso existam múltiplos. **Padrão:** `1`.

**Uso:**
```python
self.oHelper_Poui.ClickAvatar()
self.oHelper_Poui.ClickAvatar(position=1)
```

### `self.oHelper_Poui.ClickPopup(label)`

Clica em um item dentro de um popup (`po-popup`), geralmente utilizado junto ao avatar de perfil.
🔗 https://po-ui.io/documentation/po-popup

**Parâmetros:**
- `label` (`str`): Nome do item do popup.

**Uso:**
```python
self.oHelper_Poui.ClickPopup(label="Popup Item")
```

### `self.oHelper_Poui.ClickLink(text='', href='', position=1, contains=False)`

Clica em um link (`po-link`).

**Parâmetros:**
- `text` (`str`): Texto visível do link. Se vazio, a busca por texto é ignorada.
- `href` (`str`): Atributo `href` de destino do link (pode ser URL relativa ou absoluta).
- `position` (`int`): Índice (base 1) da ocorrência a ser clicada, quando houver múltiplos elementos correspondentes. **Padrão:** `1`.
- `contains` (`bool`): Se `False` (padrão), exige correspondência exata de `text` ou `href`. Se `True`, aceita correspondência parcial (substring).

**Comportamento:**
- Se apenas `text` for informado, a busca é feita pelo texto visível.
- Se apenas `href` for informado, a busca é feita apenas pelo atributo `href`.
- Se ambos forem informados, primeiro filtra pelo texto e depois pelo `href`.

**Uso:**
```python
# Clicar pelo texto visível
self.oHelper_Poui.ClickLink('PO Link')

# Clicar pelo href
self.oHelper_Poui.ClickLink(href='https://po-ui.io')

# Clicar no segundo link cujo texto contenha 'More'
self.oHelper_Poui.ClickLink(text='Link', position=2, contains=True)
```
🔗 https://po-ui.io/documentation/po-link?view=web

---

## Métodos de preenchimento de campos

### `self.oHelper_Poui.InputValue(field='', value='', position=1)`

Preenche um componente de input (`po-input`).
🔗 https://po-ui.io/documentation/po-input

**Parâmetros:**
- `field` (`str`): Título/label do campo de input a preencher.
- `value` (`str`): Valor a ser preenchido.
- `position` (`int`): Posição do elemento, caso haja duplicidade. **Padrão:** `1`.

**Uso:**
```python
self.oHelper_Poui.InputValue('Name', 'Test')
```

### `self.oHelper_Poui.ClickCombo(field='', value='', position=1, second_value='', match_case=True)`

Clica em um componente combo (`po-combo`) e seleciona um valor.
🔗 https://po-ui.io/documentation/po-combo

**Parâmetros:**
- `field` (`str`): Título do combo a ser clicado.
- `value` (`str`): Valor a ser selecionado.
- `position` (`int`): Posição do elemento. **Padrão:** `1`.
- `second_value` (`str`): Valor secundário exibido abaixo do valor principal. **Padrão:** `""`.
- `match_case` (`bool`): Se `True`, exige correspondência exata (normalizada); se `False`, permite correspondência parcial. **Padrão:** `True`.

**Uso:**
```python
self.oHelper_Poui.ClickCombo('Visão', 'Compras')
```

### `self.oHelper_Poui.ClickSelect(field='', value='', position=1)`

Clica em um componente `po-select` e seleciona um valor.
🔗 https://po-ui.io/documentation/po-select

**Parâmetros:**
- `field` (`str`): Título do select a ser clicado.
- `value` (`str`): Valor a ser selecionado.
- `position` (`int`): Posição do elemento. **Padrão:** `1`.

**Uso:**
```python
self.oHelper_Poui.ClickSelect('Espécie', 'Compra')
```

### `self.oHelper_Poui.ClickCheckBox(label)`

Marca ou desmarca um componente `po-checkbox`.
🔗 https://po-ui.io/documentation/po-checkbox

**Parâmetros:**
- `label` (`str`): Rótulo do checkbox.

**Uso:**
```python
self.oHelper_Poui.ClickCheckBox("Processing")
```

> 💡 **Diferença importante:** `ClickCheckBox` é usado para um checkbox **avulso**, identificado por rótulo próprio na tela. Já o parâmetro `checkbox=True/False` do método `ClickTable` (ver seção de tabelas) é usado para marcar o checkbox **de uma linha específica dentro de uma tabela/grid**.

### `self.oHelper_Poui.ClickSwitch(label='', value=True, position=1)`

Interage com um componente `po-switch`.
🔗 https://po-ui.io/documentation/po-switch

**Parâmetros:**
- `label` (`str`): Rótulo do campo switch.
- `value` (`bool`): Valor desejado para o switch. **Padrão:** `True`.
- `position` (`int`): Posição do elemento duplicado. **Padrão:** `1`.

**Uso:**
```python
self.oHelper_Poui.ClickSwitch(label='Codigo')
self.oHelper_Poui.ClickSwitch(label='Ativo', position=2)
self.oHelper_Poui.ClickSwitch(label='Ver Sld Alt', value=False)

# Exemplo prático: desligar o switch "Validar grupo de produto?"
self.oHelper_Poui.ClickSwitch(label='Validar grupo de produto?', value=False)
```

### `self.oHelper_Poui.ClickLookUp(label='', search_value='')`

Abre uma janela de busca (lookup) que lista dados vindos de um serviço.
🔗 https://po-ui.io/documentation/po-lookup

**Parâmetros:**
- `label` (`str`): Rótulo do campo de lookup.
- `search_value` (`str`): Valor a ser inserido no campo de busca.

**Uso:**
```python
self.oHelper_Poui.ClickLookUp("Base de Atendimento", "006TE - PLS_08")
self.oHelper_Poui.ClickLookUp("Base de Atendimento")
```

### `self.oHelper_Poui.ClickLookUpThf(label, search_value, search_column='', position=1)`

Executa o fluxo completo de um lookup avançado THF (Totvs Lookup Field): abre o diálogo de busca avançada, filtra opcionalmente por coluna, digita o critério de busca, executa a busca e seleciona o registro desejado.

**Fluxo de execução interno:**
1. Clica no campo de input do lookup.
2. Aciona o diálogo de busca avançada.
3. Filtra opcionalmente por coluna (se `search_column` for informado).
4. Preenche o campo de busca com `search_value`.
5. Clica no ícone de busca.
6. Seleciona a primeira linha correspondente nos resultados.
7. Confirma a seleção clicando no botão "Selecionar".

**Parâmetros:**
- `label` (`str`): Rótulo/nome do campo de lookup. Deve corresponder ao rótulo visível na tela.
- `search_value` (`str`): Valor a ser buscado no diálogo de busca avançada.
- `search_column` (`str`): Nome da coluna para aplicar filtro antes da busca. Se vazio, nenhum filtro de coluna é aplicado. **Padrão:** `""`.
- `position` (`int`): Posição do campo quando existem múltiplos campos com o mesmo rótulo na tela (base 1). **Padrão:** `1`.

**Uso:**
```python
# Busca simples - apenas pelo valor
self.oHelper_Poui.ClickLookUpThf(label='Supplier', search_value='ABC123')

# Busca com filtro de coluna
self.oHelper_Poui.ClickLookUpThf(label='Product', search_value='Widget', search_column='Code')

# Busca em posição específica - quando há campos duplicados
self.oHelper_Poui.ClickLookUpThf(label='Item', search_value='Item1', position=2)

# Exemplo completo
self.oHelper_Poui.ClickLookUpThf(label='Customer', search_value='Acme Corp', search_column='Name', position=1)
```

> ⚠️ **Atenção:** Se o campo de lookup não for encontrado ou a interação falhar, uma exceção é lançada e o erro é registrado em log.

### `self.oHelper_Poui.InputByLocator(selector='', locator=None, value='')`

Preenche um campo utilizando um localizador customizado (CSS, XPath, ID, etc.), quando não é possível utilizar rótulo ou atributo `name`.

**Parâmetros:**
- `selector` (`str`): Tipo de seletor a ser utilizado (ex: `'css'`, `'xpath'`, `'id'`).
- `locator` (`By`): Expressão do localizador (ex: `By.CSS_SELECTOR`, `By.ID`).
- `value` (`str`): Valor a ser preenchido/utilizado.

> ⚠️ **Aviso:** Utilize apenas em casos onde não é possível usar rótulo ou atributo `name`. Qualquer mudança na interface pode impactar diretamente o script. Avalie a possibilidade de alterar a interface antes de usar este método.

> **Nota:** É necessário importar a classe `By` no script:
> ```python
> from tir.technologies.core.base import By
> ```
> Referência: https://selenium-python.readthedocs.io/locating-elements.html

**Uso:**
```python
self.oHelper_Poui.InputByLocator(
    selector='[p-label="PO Select"] [class="po-field-container-content"] > select',
    locator=By.CSS_SELECTOR,
    value='Option 2'
)
```

---

## Métodos de clique em componentes

### `self.oHelper_Poui.ClickButton(button='', position=1)`

Clica em um botão (`po-button`).
🔗 https://po-ui.io/documentation/po-button

**Parâmetros:**
- `button` (`str`): Nome do botão a ser clicado.
- `position` (`int`): Posição do elemento. **Padrão:** `1`.

**Uso:**
```python
self.oHelper_Poui.ClickButton('Cancelar')

# Exemplo prático: botão do topo da tela de "Necessidade de Compra"
self.oHelper_Poui.ClickButton('Compra Centralizada')
```

### `self.oHelper_Poui.ClickDropdown(label='', subitems='', position=1)`

Clica em um componente dropdown (`po-dropdown`) e, opcionalmente, seleciona um subitem.
🔗 https://po-ui.io/documentation/po-dropdown

**Parâmetros:**
- `label` (`str`): Rótulo do botão dropdown.
- `subitems` (`str`): Texto do subitem a ser clicado após abrir o dropdown. **Padrão:** `""`.
- `position` (`int`): Posição do elemento. **Padrão:** `1`.

**Uso:**
```python
self.oHelper_Poui.ClickDropdown(label='Actions', subitems='Edit')
self.oHelper_Poui.ClickDropdown(label='Ações de registro')
```

### `self.oHelper_Poui.ClickWidget(title='', action='', position=1)`

Clica em um widget ou em uma ação de widget (`po-widget`).
🔗 https://po-ui.io/documentation/po-widget

**Parâmetros:**
- `title` (`str`): Título do widget a ser clicado.
- `action` (`str`): Nome da ação a ser clicada.
- `position` (`int`): Posição do elemento. **Padrão:** `1`.

**Uso:**
```python
self.oHelper_Poui.ClickWidget(title='Lead Time SC x PC', action='Detalhes', position=1)
```

### `self.oHelper_Poui.ClickIcon(label='', class_name='', position=1)`

Clica em um ícone POUI, por rótulo (tooltip), classe CSS, ou ambos.
🔗 https://po-ui.io/guides/icons

**Parâmetros:**
- `label` (`str`): Nome do tooltip do ícone.
- `class_name` (`str`): Classe CSS do ícone POUI.
- `position` (`int`): Posição do elemento. **Padrão:** `1`.

**Uso:**
```python
self.oHelper_Poui.ClickIcon(label='Delete')
self.oHelper_Poui.ClickIcon(class_name='po-icon po-icon-delete')
self.oHelper_Poui.ClickIcon(label='Delete', class_name='po-icon po-icon-delete')

# Exemplo prático: ícone de engrenagem (configurações) no rodapé da tela
self.oHelper_Poui.ClickIcon(class_name='po-icon po-icon-settings')
```

### `self.oHelper_Poui.ClickByLocator(selector='', locator=None, right_click=False)`

Clica em um elemento utilizando um localizador customizado.

**Parâmetros:**
- `selector` (`str`): Tipo de seletor (ex: `'css'`, `'xpath'`, `'id'`).
- `locator` (`By`): Expressão do localizador.
- `right_click` (`bool`): Se `True`, realiza clique com o botão direito. **Padrão:** `False`.

> ⚠️ **Aviso:** Assim como `InputByLocator`, use apenas quando não for possível utilizar rótulo ou atributo `name`.

**Uso:**
```python
self.oHelper_Poui.ClickByLocator(
    selector='.po-page-header-actions > po-button:nth-child(1) > button:nth-child(1)',
    locator=By.CSS_SELECTOR
)
```

---

## Métodos de tabela / grid

### `self.oHelper_Poui.ClickTable(...)`

Interage com componentes de tabela `po-table` e `thf-grid`. Suporta a sintaxe legada (deprecated) e a nova sintaxe recomendada.

🔗 https://po-ui.io/documentation/po-table
🔗 https://thf.dev.totvs.app/v19/documentation/thf-grid

**Assinatura completa:**
```python
self.oHelper_Poui.ClickTable(first_column=None, second_column=None, first_content=None, second_content=None,
                              table_number=1, itens=False, click_cell=None, checkbox=None, radio_input=None,
                              columns=None, values=None, match_all=False, icon_class=None)
```

**Parâmetros:**

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `first_column` | `str` | **[DEPRECATED]** Nome da primeira coluna para filtrar. |
| `second_column` | `str` | **[DEPRECATED]** Nome da segunda coluna para filtrar. |
| `first_content` | `str` | **[DEPRECATED]** Valor a corresponder na primeira coluna. |
| `second_content` | `str` | **[DEPRECATED]** Valor a corresponder na segunda coluna. |
| `table_number` | `int` | Posição da tabela quando há múltiplas na tela. **Padrão:** `1`. |
| `itens` | `bool` | **[DEPRECATED]** Clica em todos os itens que corresponderem ao critério. **Padrão:** `False`. |
| `click_cell` | `str` | Nome da coluna onde a ação de clique deve ocorrer. Se precisar selecionar linhas, considere usar `checkbox` ou `radio_input`. |
| `checkbox` | `bool` | Se `True`/`False`, alterna o checkbox **daquela linha** para esse estado. |
| `radio_input` | `bool` | Estado desejado do radio button. O método clica até atingir esse estado. |
| `columns` | `str` ou `list` | Nome(s) da(s) coluna(s) a filtrar (usado para localizar a linha). |
| `values` | `str` ou `list` | Valor(es) a corresponder nas colunas (usado para localizar a linha). |
| `match_all` | `bool` | Se `True`, executa a ação em todas as linhas correspondentes. Se `False`, apenas na primeira. **Padrão:** `False`. |
| `icon_class` | `str` | Nome (ou parte) da classe do ícone a ser clicado na linha. Suporta correspondência parcial (ex: `'arrow-up-right'`). |

**Notas importantes:**
- Quando `columns` e `values` são `None`, o método clica na **primeira linha** da tabela.
- `click_cell` especifica em qual célula (coluna) o clique deve ocorrer.
- `checkbox` só funciona em colunas do tipo checkbox.
- `radio_input` só funciona em colunas do tipo radio button.
- Use `match_all=True` para interagir com todas as linhas que atendem ao filtro.

> ⚠️ **Atenção:** Não misture a sintaxe legada com a nova sintaxe na mesma chamada. Os parâmetros legados serão removidos em versões futuras.

**Exemplos — sintaxe legada (deprecated):**
```python
self.oHelper_Poui.ClickTable("Code", "", "000001", "", click_cell="Edit")
self.oHelper_Poui.ClickTable("Code", "Name", "000001", "John", click_cell="Edit")
self.oHelper_Poui.ClickTable("Branch", "", "D MG 01", "", click_cell="Edit")
self.oHelper_Poui.ClickTable("Code", "", "000001", "", itens=True)
```

**Exemplos — sintaxe nova (recomendada):**
```python
# Clicar na linha filtrando por coluna
self.oHelper_Poui.ClickTable(columns='Code', values='000001', click_cell='Edit')

# Filtrar por múltiplas colunas
self.oHelper_Poui.ClickTable(columns=['Code', 'Name'], values=['000001', 'John'], click_cell='Actions')

# ✅ Exemplo real validado: marcar o checkbox da linha onde a coluna
# "Solicitação" é igual a '000001'
self.oHelper_Poui.ClickTable(columns='Solicitação', values='000001', checkbox=True)

# Marcar radio button
self.oHelper_Poui.ClickTable(columns='Filial', values='D MG 01', radio_input=True)

# Desmarcar radio button
self.oHelper_Poui.ClickTable(columns='Filial', values='D MG 01', radio_input=False)

# Marcar checkbox de todas as linhas que atendem ao filtro
self.oHelper_Poui.ClickTable(columns='Status', values='Active', checkbox=True, match_all=True)

# Clicar em ícone da linha
self.oHelper_Poui.ClickTable(columns='Code', values='000001', icon_class='an an-arrow-up-right')

# Clicar em ícone dentro de uma coluna específica
self.oHelper_Poui.ClickTable(columns='Code', values='000001', click_cell='Actions', icon_class='an an-arrow-up-right')
```

> 💡 **Dica prática:** quando existem valores repetidos em uma coluna (por exemplo, o mesmo "Código do produto" em linhas diferentes), use **duas ou mais colunas** em `columns`/`values` para garantir que a linha correta seja localizada, evitando marcar/clicar na linha errada:
> ```python
> self.oHelper_Poui.ClickTable(
>     columns=['Solicitação', 'Código do produto'],
>     values=['000002', '000000000000001'],
>     checkbox=True
> )
> ```

### `self.oHelper_Poui.ClearTableSelection(table_number=1, selection_type='all')`

Remove linhas selecionadas de uma tabela THF/Kendo.

**Parâmetros:**
- `table_number` (`int`): Posição da tabela quando há múltiplas na tela. **Padrão:** `1`.
- `selection_type` (`str`): Tipo de seleção a limpar. Valores disponíveis: `'checkbox'`, `'radio'`, `'all'`. **Padrão:** `'all'`.

**Retorno:**
- `bool`: `True` se a seleção foi removida antes do tempo limite (timeout), caso contrário `False`.

**Uso:**
```python
self.oHelper_Poui.ClearTableSelection()
self.oHelper_Poui.ClearTableSelection(table_number=2)
self.oHelper_Poui.ClearTableSelection(selection_type='radio')
self.oHelper_Poui.ClearTableSelection(selection_type='checkbox')
```

### `self.oHelper_Poui.FilterBrowse(filters)`

Preenche o componente de filtro do Browse (kendo-grid/THF) com os filtros fornecidos.

**Parâmetros:**
- `filters` (`list[dict[str, str]]`): Lista contendo um dicionário com os rótulos dos campos como chaves e os valores de filtro como valores.

**Comportamento especial:**
Ao ser chamado, este método define `self.config._flag_is_new_browse = True`, marcando que a tela está operando no novo padrão de Browse. Esse é um dos métodos "preservados" — ou seja, sua própria chamada **não** reseta essa flag (ver seção [Comportamento interno](#comportamento-de-__getattribute__-importante-entender)).

**Uso:**
```python
filters = [
    {
        'Filial': 'D MG 01',
        'Cod Grupo': 'SQA2'
    }
]
self.oHelper_Poui.FilterBrowse(filters)
```

### `self.oHelper_Poui.RemoveBrowseFilters()`

Remove todos os filtros ativos do componente Browse (kendo-grid) THF.

**Uso:**
```python
self.oHelper_Poui.RemoveBrowseFilters()
```

### `self.oHelper_Poui.POSearch(content='', placeholder='')`

Preenche o componente de busca (`po-page-dynamic-search`).
🔗 https://po-ui.io/documentation/po-page-dynamic-search

**Parâmetros:**
- `content` (`str`): Conteúdo a ser buscado.
- `placeholder` (`str`): Texto de placeholder do campo de busca.

**Uso:**
```python
self.oHelper_Poui.POSearch(content='Content to be Search')

# Exemplo prático: buscar por código de produto na tela de Necessidade de Compra
self.oHelper_Poui.POSearch(content='000000000000001', placeholder='Busque por código de produto')
```

---

## Métodos de espera (wait)

### `self.oHelper_Poui.WaitShow(string, timeout=None, throw_error=True)`

Aguarda até que os elementos correspondentes à string informada sejam exibidos na tela.

**Parâmetros:**
- `string` (`str`): Texto/string que será utilizado para aguardar a exibição.
- `timeout` (`int`/`str`): Tempo limite de espera antes de retornar.
- `throw_error` (`bool`): Se `True` (padrão), lança um erro caso o elemento não seja encontrado dentro do timeout.

**Uso:**
```python
self.oHelper_Poui.WaitShow("Processing")
```

### `self.oHelper_Poui.WaitProcessing(itens, timeout=None)`

Utiliza `WaitShow` e `WaitHide` internamente para aguardar uma tela de processamento (loading) aparecer e desaparecer.

**Parâmetros:**
- `itens` (`str` ou `list`): Lista (ou string) de itens que devem ser aguardados.
- `timeout` (`int`): Tempo limite de espera.

**Uso:**
```python
self.oHelper_Poui.WaitProcessing("Processing")
```

### `self.oHelper_Poui.IfExists(string='', timeout=5)`

Verifica se um elemento existe na tela dentro do tempo limite, sem lançar erro caso não exista.

**Parâmetros:**
- `string` (`str`): Texto/string a ser verificado.
- `timeout` (`int`): Tempo limite de espera. **Padrão:** `5`.

**Retorno:**
- `bool`: `True` se o elemento existir dentro do timeout, `False` caso contrário.

**Uso:**
```python
existe = self.oHelper_Poui.IfExists("Aviso", timeout=10)

if self.oHelper_Poui.IfExists("Aviso", timeout=10):
    print('Found!')
```

> **Observação:** Internamente, este método chama `WaitShow` com `throw_error=False`, ou seja, não interrompe a execução do teste caso o elemento não seja encontrado.

---

## Métodos de verificação e asserção

### `self.oHelper_Poui.CheckResult(field=None, user_value=None, po_component='po-input', position=1)`

Verifica se um campo contém o valor esperado pelo usuário.

**Parâmetros:**
- `field` (`str`): Campo ou rótulo do campo a ser verificado.
- `user_value` (`str`): Valor esperado no campo.
- `po_component` (`str`): Nome do componente POUI a ser verificado na tela. **Padrão:** `'po-input'`.
- `position` (`int`): Posição do elemento. **Padrão:** `1`.

**Uso:**
```python
self.oHelper_Poui.CheckResult("Código", "000001", 'po-input')
```

### `self.oHelper_Poui.AssertTrue(expected=True, script_message='')`

Define que o caso de teste espera uma resposta **verdadeira (`True`)** para passar.

**Parâmetros:**
- `expected` (`bool`): Valor esperado. **Padrão:** `True`.
- `script_message` (`str`): Mensagem customizada para exibição no relatório do teste.

**Uso:**
```python
self.oHelper_Poui.AssertTrue()
```

### `self.oHelper_Poui.AssertFalse(expected=False, script_message='')`

Define que o caso de teste espera uma resposta **falsa (`False`)** para passar.

**Parâmetros:**
- `expected` (`bool`): Valor esperado. **Padrão:** `False`.
- `script_message` (`str`): Mensagem customizada para exibição no relatório do teste.

**Uso:**
```python
self.oHelper_Poui.AssertFalse()
```

---

## Métodos de localizadores customizados

Já detalhados nas seções anteriores:

- [`self.oHelper_Poui.InputByLocator(selector='', locator=None, value='')`](#selfohelper_pouiinputbylocatorselector-locatornone-value)
- [`self.oHelper_Poui.ClickByLocator(selector='', locator=None, right_click=False)`](#selfohelper_pouiclickbylocatorselector-locatornone-right_clickfalse)

> ⚠️ **Recomendação geral:** Os métodos que utilizam localizadores customizados (CSS, XPath, ID) devem ser usados **apenas como último recurso**, quando não for possível localizar o elemento por rótulo, nome ou atributos semânticos do PO-UI. Como dependem diretamente da estrutura HTML da página, qualquer mudança na interface pode quebrar o script.

---

## Encerramento do teste

### `self.oHelper_Poui.TearDown()`

Encerra o webdriver e finaliza o caso de teste. Deve ser chamado ao final de cada script de teste para garantir o encerramento correto da sessão do navegador.

**Uso:**
```python
self.oHelper_Poui.TearDown()
```

---

## Erros comuns e como resolver

Esta seção reúne, de forma direta, os problemas mais frequentes ao usar a classe `Poui`, com base em casos reais.

### ❌ Erro 1: `AttributeError: 'Webapp' object has no attribute 'NomeDoMetodo'`

```
AttributeError: 'Webapp' object has no attribute 'ClickTable'. Did you mean: 'ClickLabel'?
```

**Causa:** você chamou o método a partir de `self.oHelper` (instância de `Webapp`), mas o método pertence à classe `Poui`.

**Solução:** troque para `self.oHelper_Poui`:
```python
# ❌ Errado
self.oHelper.ClickTable(columns='Solicitação', values='000001')

# ✅ Correto
self.oHelper_Poui.ClickTable(columns='Solicitação', values='000001')
```

### ❌ Erro 2: `Exception: config.json file not found!`

```
Exception: config.json file not found!
```

**Causa:** você instanciou `Poui()` diretamente no meio do script (ex: `Poui().ClickTable(...)`), criando uma instância nova sem `config_path`, o que tenta abrir uma sessão de navegador do zero sem configuração válida.

**Solução:** nunca instancie `Poui()` manualmente dentro dos testes. Use sempre a instância já existente `self.oHelper_Poui`, criada previamente (normalmente no `setUp()` da classe de teste):
```python
# ❌ Errado
Poui().ClickTable(columns='Solicitação', values='000001')

# ✅ Correto
self.oHelper_Poui.ClickTable(columns='Solicitação', values='000001')
```

### ❌ Erro 3: Import duplicado

```python
from tir import Webapp, Poui
from tir.technologies.core.base import By
from tir import Poui   # redundante
```

**Causa:** `Poui` foi importado duas vezes.

**Solução:** remova a linha duplicada. Isso não gera erro de execução, mas é uma boa prática de organização do código:
```python
from tir import Webapp, Poui
from tir.technologies.core.base import By
```

### ✅ Checklist rápido antes de rodar um comando `Poui`

1. A tela que estou testando é feita em **PO-UI/THF**? → use `self.oHelper_Poui`.
2. Estou usando exatamente `self.oHelper_Poui` (com "H" e "P" maiúsculos)? → confira a grafia.
3. Não estou instanciando `Poui()` "na mão" dentro do teste? → a instância já existe, não crie outra.
4. Coloquei `self.` antes do nome do método? → **todo** comando desta documentação exige `self.oHelper_Poui.` na frente.

---

## Resumo Rápido de Todos os Métodos

> Todos os comandos abaixo devem ser precedidos por `self.oHelper_Poui.`

| Método | Categoria | Descrição resumida |
|---|---|---|
| `GetUrl` | Inicialização | Carrega uma URL |
| `Program` | Inicialização | Define programa/rotina no menu |
| `ClickMenu` | Navegação | Clica em item de menu |
| `POtabs` | Navegação | Clica em aba |
| `ClickAvatar` | Navegação | Clica no avatar de perfil |
| `ClickPopup` | Navegação | Clica em item de popup |
| `ClickLink` | Navegação | Clica em link |
| `InputValue` | Preenchimento | Preenche campo de input |
| `ClickCombo` | Preenchimento | Seleciona valor em combo |
| `ClickSelect` | Preenchimento | Seleciona valor em select |
| `ClickCheckBox` | Preenchimento | Marca/desmarca checkbox avulso |
| `ClickSwitch` | Preenchimento | Ativa/desativa switch |
| `ClickLookUp` | Preenchimento | Abre busca lookup |
| `ClickLookUpThf` | Preenchimento | Executa lookup avançado THF |
| `InputByLocator` | Localizador | Preenche via seletor customizado |
| `ClickButton` | Clique | Clica em botão |
| `ClickDropdown` | Clique | Clica em dropdown/subitem |
| `ClickWidget` | Clique | Clica em widget/ação |
| `ClickIcon` | Clique | Clica em ícone |
| `ClickByLocator` | Localizador | Clica via seletor customizado |
| `ClickTable` | Tabela | Interage com tabelas/grids (linha, checkbox, radio, ícone) |
| `ClearTableSelection` | Tabela | Limpa seleção de linhas |
| `FilterBrowse` | Tabela | Preenche filtros do Browse |
| `RemoveBrowseFilters` | Tabela | Remove filtros do Browse |
| `POSearch` | Busca | Preenche campo de busca dinâmica |
| `WaitShow` | Espera | Aguarda exibição de elemento |
| `WaitProcessing` | Espera | Aguarda tela de processamento |
| `IfExists` | Espera | Verifica existência sem erro |
| `CheckResult` | Asserção | Verifica valor de um campo |
| `AssertTrue` | Asserção | Espera resultado verdadeiro |
| `AssertFalse` | Asserção | Espera resultado falso |
| `TearDown` | Encerramento | Finaliza o teste |

---

*Documento gerado a partir do código-fonte da classe `Poui` e de casos reais de uso e depuração de erros.*