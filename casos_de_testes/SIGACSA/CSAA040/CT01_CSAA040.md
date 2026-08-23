# CT01_CSAA040 – Escala e Grau de Importância

## 1. Nome do Caso de Teste

**CT07_CSAA040 – Escala e Grau de Importância**

## 2. Nome da Rotina

**CSAA040 – Escala e Grau de Importância**

## 3. Caminho da Rotina

**Protheus → Gestão de Pessoal → Cadastros → Escala e Grau de Importância**

## 4. Objetivo

Validar o cadastro e o gerenciamento das informações de **Escala e Grau de Importância** na rotina **CSAA040**, garantindo que os registros possam ser incluídos, consultados, alterados e excluídos quando permitido, mantendo a consistência das informações utilizadas pelo sistema.

## 5. Passo a Passo

### CREATE – Inclusão de Escala e Grau de Importância

| Nº | Ação                                                             | Resultado Esperado                                                                |
| -: | ---------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| 01 | Acessar a rotina **CSAA040 – Escala e Grau de Importância**.     | A rotina deve ser apresentada corretamente.                                       |
| 02 | Selecionar a opção **Incluir**.                                  | O sistema deve abrir a tela para cadastro de uma nova escala/grau de importância. |
| 03 | Informar o código da escala, quando solicitado.                  | O sistema deve aceitar o código informado conforme as regras da rotina.           |
| 04 | Informar a descrição da escala.                                  | O sistema deve aceitar a descrição informada.                                     |
| 05 | Informar o **Grau de Importância** correspondente.               | O sistema deve aceitar e validar o grau informado.                                |
| 06 | Preencher os demais campos obrigatórios.                         | O sistema deve validar os campos e aceitar informações válidas.                   |
| 07 | Confirmar a inclusão.                                            | O sistema deve gravar o registro sem apresentar erros.                            |
| 08 | Registrar o código, descrição e grau de importância cadastrados. | As informações devem permanecer gravadas corretamente.                            |

### READ – Consulta

| Nº | Ação                                                      | Resultado Esperado                                                                |
| -: | --------------------------------------------------------- | --------------------------------------------------------------------------------- |
| 09 | Pesquisar o registro recém-cadastrado.                    | O sistema deve localizar o registro corretamente.                                 |
| 10 | Abrir o cadastro.                                         | O sistema deve apresentar as informações cadastradas.                             |
| 11 | Conferir código, descrição, escala e grau de importância. | Os dados apresentados devem corresponder aos dados informados durante a inclusão. |

### UPDATE – Alteração

| Nº | Ação                                                            | Resultado Esperado                                                  |
| -: | --------------------------------------------------------------- | ------------------------------------------------------------------- |
| 12 | Selecionar o registro cadastrado e acessar a opção **Alterar**. | O sistema deve abrir o cadastro para edição.                        |
| 13 | Alterar a descrição ou o grau de importância, quando permitido. | O sistema deve permitir a alteração conforme as regras da rotina.   |
| 14 | Confirmar a alteração.                                          | O sistema deve validar e gravar as alterações sem apresentar erros. |
| 15 | Consultar novamente o registro.                                 | O sistema deve apresentar os dados atualizados.                     |
| 16 | Conferir as informações alteradas.                              | Os novos valores devem estar gravados corretamente.                 |

### DELETE – Exclusão

| Nº | Ação                                           | Resultado Esperado                                                                                   |
| -: | ---------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| 17 | Selecionar um registro que possa ser excluído. | O sistema deve permitir a seleção do registro.                                                       |
| 18 | Acessar a opção **Excluir**.                   | O sistema deve apresentar a confirmação da exclusão, quando aplicável.                               |
| 19 | Confirmar a exclusão.                          | O sistema deve excluir o registro conforme as regras da rotina.                                      |
| 20 | Pesquisar novamente o registro excluído.       | O registro não deve estar disponível para utilização, conforme o comportamento definido pela rotina. |

## 6. Validação de Campos Obrigatórios

| Nº | Ação                                                                                   | Resultado Esperado                                                                         |
| -: | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| 21 | Iniciar a inclusão de um novo registro.                                                | A tela de cadastro deve ser apresentada.                                                   |
| 22 | Deixar um campo obrigatório, como descrição ou grau de importância, sem preenchimento. | O sistema deve identificar a ausência da informação.                                       |
| 23 | Tentar confirmar o cadastro.                                                           | O sistema deve impedir a gravação e apresentar uma mensagem de validação.                  |
| 24 | Preencher corretamente o campo obrigatório e confirmar novamente.                      | O sistema deve permitir a gravação do registro, desde que os demais dados estejam válidos. |

## 7. Validação do Grau de Importância

| Nº | Ação                                                                     | Resultado Esperado                                                      |
| -: | ------------------------------------------------------------------------ | ----------------------------------------------------------------------- |
| 25 | Informar um grau de importância válido.                                  | O sistema deve aceitar o valor conforme as regras configuradas.         |
| 26 | Informar um valor inválido ou fora da faixa permitida, quando aplicável. | O sistema deve rejeitar o valor e apresentar uma mensagem de validação. |
| 27 | Corrigir o valor para um grau válido.                                    | O sistema deve permitir a continuidade do cadastro.                     |

## 8. Validação de Duplicidade

| Nº | Ação                                                            | Resultado Esperado                                                                   |
| -: | --------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| 28 | Tentar cadastrar um registro utilizando um código já existente. | O sistema deve identificar a duplicidade.                                            |
| 29 | Confirmar o cadastro.                                           | O sistema deve impedir a criação de registro duplicado conforme as regras da rotina. |

## 9. Resultado Esperado

A rotina **CSAA040 – Escala e Grau de Importância** deve permitir o correto gerenciamento dos registros de escala e grau de importância.

O sistema deve:

* Permitir a inclusão de registros com informações válidas.
* Permitir a consulta dos registros cadastrados.
* Apresentar corretamente os dados armazenados.
* Permitir a alteração dos campos autorizados.
* Gravar corretamente as alterações realizadas.
* Permitir a exclusão quando não houver impedimentos.
* Validar os campos obrigatórios.
* Validar corretamente o grau de importância informado.
* Impedir a criação de registros duplicados.
* Manter a integridade das informações durante as operações realizadas.

## 10. Critério de Aprovação

O caso de teste será considerado **APROVADO** quando as operações de **CREATE, READ, UPDATE e DELETE**, quando aplicáveis, forem executadas conforme esperado e o sistema realizar corretamente as validações de **Escala e Grau de Importância**, sem erros ou inconsistências nos dados.

**Status:** `A definir durante a execução`

**Evidências:** `A anexar durante a execução`

**Responsável:** `A definir`

**Data de Execução:** `A definir`
