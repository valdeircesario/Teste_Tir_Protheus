# CT01_MATA110 – Criação e Visualização de Solicitação de Compras

## 1. Nome do Caso de Teste

**CT07_MATA110 – Solicitação de Compras**

## 2. Nome da Rotina

**MATA110 – Solicitação de Compras**

## 3. Caminho da Rotina

**Protheus → SIGACOM → Atualizações → Solicitações → Solicitação de Compras**

## 4. Objetivo

Validar a **criação e visualização de uma Solicitação de Compras** na rotina **MATA110**, garantindo que a solicitação seja incluída corretamente com os dados informados e posteriormente localizada e visualizada no sistema.

## 5. Passo a Passo

### CREATE – Criação de Solicitação de Compras

| Nº | Ação                                                                                                | Resultado Esperado                                                           |
| -: | --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| 01 | Acessar a rotina **MATA110 – Solicitação de Compras**.                                              | A rotina deve ser apresentada corretamente.                                  |
| 02 | Selecionar a opção **Incluir**.                                                                     | O sistema deve abrir a tela para criação de uma nova Solicitação de Compras. |
| 03 | Preencher os campos obrigatórios da Solicitação de Compras.                                         | O sistema deve aceitar os dados válidos informados.                          |
| 04 | Informar os dados necessários para o item da solicitação, conforme os campos disponíveis na rotina. | O sistema deve permitir o preenchimento das informações do item.             |
| 05 | Informar a quantidade e demais informações necessárias para a solicitação.                          | O sistema deve aceitar os valores válidos informados.                        |
| 06 | Confirmar a inclusão da Solicitação de Compras.                                                     | O sistema deve validar os dados e gravar a solicitação sem apresentar erros. |
| 07 | Registrar o número ou identificação da Solicitação de Compras criada.                               | O sistema deve disponibilizar a identificação da solicitação cadastrada.     |

### READ – Visualização da Solicitação de Compras

| Nº | Ação                                                                                | Resultado Esperado                                                                             |
| -: | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| 08 | Acessar novamente a rotina **MATA110** e localizar a Solicitação de Compras criada. | A solicitação deve ser localizada corretamente.                                                |
| 09 | Abrir a Solicitação de Compras cadastrada.                                          | O sistema deve apresentar os dados da solicitação.                                             |
| 10 | Conferir os dados informados durante a inclusão.                                    | Os dados apresentados devem corresponder às informações utilizadas na criação da solicitação.  |
| 11 | Conferir os dados do item incluído na solicitação.                                  | O sistema deve apresentar corretamente o produto, quantidade e demais informações cadastradas. |
| 12 | Conferir a identificação da Solicitação de Compras.                                 | O sistema deve apresentar corretamente o número ou identificação gerada para a solicitação.    |

## 6. Validação de Campos Obrigatórios

| Nº | Ação                                                   | Resultado Esperado                                                                             |
| -: | ------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| 13 | Iniciar a inclusão de uma nova Solicitação de Compras. | A tela de inclusão deve ser apresentada.                                                       |
| 14 | Deixar um campo obrigatório sem preenchimento.         | O sistema deve identificar a ausência da informação.                                           |
| 15 | Tentar confirmar a inclusão da solicitação.            | O sistema deve impedir a gravação e apresentar uma mensagem de validação.                      |
| 16 | Preencher o campo obrigatório e confirmar novamente.   | O sistema deve permitir a continuidade da inclusão, desde que os demais dados estejam válidos. |

## 7. Validação da Persistência dos Dados

| Nº | Ação                                                                       | Resultado Esperado                                                       |
| -: | -------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| 17 | Após a inclusão, sair da tela da Solicitação de Compras.                   | O sistema deve retornar à tela anterior sem apresentar erros.            |
| 18 | Pesquisar novamente a Solicitação de Compras utilizando sua identificação. | A solicitação deve ser localizada corretamente.                          |
| 19 | Abrir a solicitação localizada.                                            | O sistema deve apresentar os dados anteriormente cadastrados.            |
| 20 | Comparar os dados apresentados com os dados informados durante a inclusão. | As informações devem permanecer consistentes e sem alterações indevidas. |

## 8. Resultado Esperado

A rotina **MATA110 – Solicitação de Compras** deve permitir realizar corretamente a **criação e visualização de Solicitações de Compras**.

O sistema deve:

* Permitir a inclusão de uma Solicitação de Compras com dados válidos.
* Validar os campos obrigatórios antes da gravação.
* Permitir o preenchimento dos dados necessários da solicitação e de seus itens.
* Gravar corretamente a Solicitação de Compras.
* Gerar e disponibilizar a identificação da solicitação cadastrada.
* Permitir localizar a solicitação após sua inclusão.
* Apresentar corretamente os dados cadastrados durante a visualização.
* Manter a integridade e consistência dos dados após a gravação.

## 9. Critério de Aprovação

O caso de teste será considerado **APROVADO** quando a **Solicitação de Compras for criada e posteriormente localizada e visualizada corretamente**, apresentando os mesmos dados informados durante a inclusão, sem erros ou inconsistências.

**Status:** `A definir durante a execução`

**Evidências:** `A anexar durante a execução`

**Responsável:** `A definir`

**Data de Execução:** `A definir`
