# CT01_MATA010 – Inclusão, Visualização e Alteração de Produto

## 1. Nome do Caso de Teste

**CT05_MATA010 – Cadastro de Produtos**

## 2. Nome da Rotina

**MATA010 – Cadastro de Produtos**

## 3. Caminho da Rotina

**Protheus → SIGACOM → Atualizações → Cadastros → Produtos**

## 4. Objetivo

Validar as operações de **inclusão, visualização e alteração** no cadastro de produtos da rotina **MATA010**, garantindo que os registros sejam cadastrados, consultados e alterados corretamente, conforme as regras de negócio do Protheus.

## 5. Passo a Passo

### CREATE – Inclusão de Produto

| Nº | Ação                                                 | Resultado Esperado                                                        |
| -: | ---------------------------------------------------- | ------------------------------------------------------------------------- |
| 01 | Acessar a rotina **MATA010 – Cadastro de Produtos**. | A rotina deve ser apresentada corretamente.                               |
| 02 | Selecionar a opção **Incluir**.                      | O sistema deve abrir a tela de cadastro de um novo produto.               |
| 03 | Preencher os campos obrigatórios do produto.         | O sistema deve aceitar os dados válidos informados.                       |
| 04 | Preencher os demais campos necessários do cadastro.  | O sistema deve permitir o preenchimento das informações.                  |
| 05 | Confirmar a inclusão do produto.                     | O sistema deve validar os dados e gravar o cadastro sem apresentar erros. |
| 06 | Registrar o código do produto criado.                | O sistema deve disponibilizar a identificação do produto cadastrado.      |

### READ – Visualização de Produto

| Nº | Ação                                                           | Resultado Esperado                                                        |
| -: | -------------------------------------------------------------- | ------------------------------------------------------------------------- |
| 07 | Acessar a rotina **MATA010** e localizar o produto cadastrado. | O produto deve ser localizado corretamente.                               |
| 08 | Abrir o cadastro do produto.                                   | O sistema deve apresentar os dados cadastrados.                           |
| 09 | Conferir as informações apresentadas.                          | Os dados devem corresponder às informações utilizadas durante a inclusão. |

### UPDATE – Alteração de Produto

| Nº | Ação                                                           | Resultado Esperado                                                                              |
| -: | -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| 10 | Selecionar o produto cadastrado e acessar a opção **Alterar**. | O sistema deve abrir o cadastro para edição.                                                    |
| 11 | Alterar uma informação permitida do produto.                   | O sistema deve permitir a alteração do campo.                                                   |
| 12 | Confirmar a alteração.                                         | O sistema deve validar e gravar as alterações sem apresentar erros.                             |
| 13 | Consultar novamente o produto.                                 | O sistema deve apresentar as informações atualizadas.                                           |
| 14 | Conferir os campos alterados e não alterados.                  | Os campos alterados devem apresentar os novos valores e os demais devem permanecer inalterados. |

## 6. Validação de Campos Obrigatórios

| Nº | Ação                                                 | Resultado Esperado                                                                             |
| -: | ---------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| 15 | Iniciar a inclusão de um novo produto.               | A tela de inclusão deve ser apresentada.                                                       |
| 16 | Deixar um campo obrigatório sem preenchimento.       | O sistema deve identificar a ausência da informação.                                           |
| 17 | Tentar confirmar a inclusão.                         | O sistema deve impedir a gravação e apresentar uma mensagem de validação.                      |
| 18 | Preencher o campo obrigatório e confirmar novamente. | O sistema deve permitir a continuidade do cadastro, desde que os demais dados estejam válidos. |

## 7. Validação de Duplicidade

| Nº | Ação                                                                            | Resultado Esperado                                                                        |
| -: | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| 19 | Tentar incluir um produto utilizando uma identificação ou código já cadastrado. | O sistema deve identificar a duplicidade conforme as regras configuradas.                 |
| 20 | Confirmar o cadastro.                                                           | O sistema deve impedir ou tratar a duplicidade de acordo com a regra de negócio definida. |

## 8. Resultado Esperado

A rotina **MATA010 – Cadastro de Produtos** deve permitir realizar corretamente as operações de **inclusão, visualização e alteração** de produtos.

O sistema deve:

* Permitir a inclusão de produtos com dados válidos.
* Permitir a visualização dos produtos cadastrados.
* Apresentar corretamente os dados armazenados.
* Permitir a alteração dos campos autorizados.
* Gravar corretamente as alterações realizadas.
* Validar campos obrigatórios.
* Tratar corretamente situações de duplicidade.
* Impedir operações que estejam em desacordo com as regras de negócio.
* Manter a integridade dos dados durante as operações de cadastro.

## 9. Critério de Aprovação

O caso de teste será considerado **APROVADO** quando todas as operações previstas de **CREATE, READ e UPDATE** forem executadas conforme esperado, sem erros ou inconsistências nos dados.

**Status:** `A definir durante a execução`

**Evidências:** `A anexar durante a execução`

**Responsável:** `A definir`

**Data de Execução:** `A definir`
