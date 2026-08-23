# CT09_MATA103 – Inclusão e Exclusão de Documento de Entrada

## 1. Nome do Caso de Teste

**CT09_MATA103 – Inclusão e Exclusão de Documento de Entrada**

## 2. Nome da Rotina

**MATA103 – Documento de Entrada**

## 3. Caminho da Rotina

**Protheus → SIGACOM → Atualizações → Movimentos → Documento Entrada**

## 4. Objetivo

Validar as operações de **inclusão e exclusão de um Documento de Entrada** na rotina **MATA103**, garantindo que o documento seja incluído corretamente com os dados informados e posteriormente excluído conforme as regras de negócio do Protheus.

## 5. Passo a Passo

### CREATE – Inclusão de Documento de Entrada

| Nº | Ação                                                                           | Resultado Esperado                                                         |
| -: | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| 01 | Acessar a rotina **MATA103 – Documento de Entrada**.                           | A rotina deve ser apresentada corretamente.                                |
| 02 | Selecionar a opção **Incluir**.                                                | O sistema deve abrir a tela para inclusão de um novo Documento de Entrada. |
| 03 | Preencher os campos obrigatórios do documento.                                 | O sistema deve aceitar os dados válidos informados.                        |
| 04 | Informar os dados necessários do fornecedor e demais informações do documento. | O sistema deve permitir o preenchimento das informações.                   |
| 05 | Informar os dados do item do documento de entrada.                             | O sistema deve permitir a inclusão do item com os dados válidos.           |
| 06 | Informar a quantidade e demais informações necessárias do item.                | O sistema deve aceitar os valores informados.                              |
| 07 | Confirmar a inclusão do Documento de Entrada.                                  | O sistema deve validar os dados e gravar o documento sem apresentar erros. |
| 08 | Registrar a identificação do Documento de Entrada criado.                      | O sistema deve disponibilizar a identificação do documento cadastrado.     |

### DELETE – Exclusão de Documento de Entrada

| Nº | Ação                                                                              | Resultado Esperado                                                                                    |
| -: | --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| 09 | Acessar novamente a rotina **MATA103** e localizar o Documento de Entrada criado. | O documento deve ser localizado corretamente.                                                         |
| 10 | Selecionar o Documento de Entrada e acessar a opção **Excluir**.                  | O sistema deve apresentar a confirmação da exclusão, quando aplicável.                                |
| 11 | Confirmar a exclusão do Documento de Entrada.                                     | O sistema deve realizar a exclusão conforme as regras da rotina.                                      |
| 12 | Pesquisar novamente o Documento de Entrada excluído.                              | O documento não deve estar disponível para utilização, conforme o comportamento definido pela rotina. |

## 6. Validação de Campos Obrigatórios

| Nº | Ação                                                 | Resultado Esperado                                                                             |
| -: | ---------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| 13 | Iniciar a inclusão de um novo Documento de Entrada.  | A tela de inclusão deve ser apresentada.                                                       |
| 14 | Deixar um campo obrigatório sem preenchimento.       | O sistema deve identificar a ausência da informação.                                           |
| 15 | Tentar confirmar a inclusão do documento.            | O sistema deve impedir a gravação e apresentar uma mensagem de validação.                      |
| 16 | Preencher o campo obrigatório e confirmar novamente. | O sistema deve permitir a continuidade da inclusão, desde que os demais dados estejam válidos. |

## 7. Validação da Persistência e Exclusão dos Dados

| Nº | Ação                                                           | Resultado Esperado                                                                                                     |
| -: | -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| 17 | Após a inclusão, sair da tela do Documento de Entrada.         | O sistema deve retornar à tela anterior sem apresentar erros.                                                          |
| 18 | Pesquisar o Documento de Entrada utilizando sua identificação. | O documento deve ser localizado corretamente antes da exclusão.                                                        |
| 19 | Conferir os dados do documento antes da exclusão.              | Os dados apresentados devem corresponder às informações utilizadas durante a inclusão.                                 |
| 20 | Realizar a exclusão do Documento de Entrada.                   | O sistema deve concluir a exclusão conforme as regras da rotina.                                                       |
| 21 | Pesquisar novamente o documento após a exclusão.               | O documento não deve ser localizado ou disponibilizado para utilização, conforme o comportamento definido pela rotina. |

## 8. Resultado Esperado

A rotina **MATA103 – Documento de Entrada** deve permitir realizar corretamente as operações de **inclusão e exclusão de Documentos de Entrada**.

O sistema deve:

* Permitir a inclusão de um Documento de Entrada com dados válidos.
* Validar os campos obrigatórios antes da gravação.
* Permitir o preenchimento dos dados necessários do documento e de seus itens.
* Gravar corretamente o Documento de Entrada.
* Disponibilizar a identificação do documento cadastrado.
* Permitir localizar o documento após sua inclusão.
* Permitir a exclusão do documento quando não houver impedimentos.
* Solicitar confirmação da exclusão, quando aplicável.
* Não disponibilizar o documento excluído para utilização, conforme o comportamento definido pela rotina.
* Manter a integridade dos dados durante as operações de inclusão e exclusão.

## 9. Critério de Aprovação

O caso de teste será considerado **APROVADO** quando o **Documento de Entrada for incluído corretamente, localizado e posteriormente excluído**, sem erros ou inconsistências nos dados e conforme as regras de negócio da rotina.

**Status:** `A definir durante a execução`

**Evidências:** `A anexar durante a execução`

**Responsável:** `A definir`

**Data de Execução:** `A definir`
