# CT01_CSAA030 – Cadastro de Competências

## 1. Nome do Caso de Teste

**CT06_CSAA030 – Cadastro de Competências**

## 2. Nome da Rotina

**CSAA030 – Cadastro de Competências**

## 3. Caminho da Rotina

**Protheus → Gestão de Pessoal → Cadastros → Competências**

## 4. Objetivo

Validar o processo de **Cadastro de Competências** na rotina **CSAA030**, garantindo que seja possível incluir, consultar, alterar e excluir competências, quando permitido, mantendo a integridade das informações cadastradas.

## 5. Passo a Passo

### CREATE – Inclusão de Competência

| Nº | Ação                                                        | Resultado Esperado                                                          |
| -: | ----------------------------------------------------------- | --------------------------------------------------------------------------- |
| 01 | Acessar a rotina **CSAA030 – Cadastro de Competências**.    | A rotina deve ser apresentada corretamente.                                 |
| 02 | Selecionar a opção **Incluir**.                             | O sistema deve abrir a tela para cadastro de uma nova competência.          |
| 03 | Informar o código da competência, quando solicitado.        | O sistema deve aceitar o código válido.                                     |
| 04 | Informar a descrição da competência.                        | O sistema deve aceitar a descrição informada.                               |
| 05 | Preencher os demais campos obrigatórios.                    | O sistema deve validar e aceitar os dados informados.                       |
| 06 | Confirmar a inclusão da competência.                        | O sistema deve gravar o cadastro sem apresentar erros.                      |
| 07 | Registrar o código e a descrição da competência cadastrada. | A competência deve possuir identificação e descrição corretamente gravadas. |

### READ – Consulta de Competência

| Nº | Ação                                             | Resultado Esperado                                                                |
| -: | ------------------------------------------------ | --------------------------------------------------------------------------------- |
| 08 | Pesquisar a competência recém-cadastrada.        | O sistema deve localizar a competência corretamente.                              |
| 09 | Abrir o cadastro da competência.                 | O sistema deve apresentar os dados cadastrados.                                   |
| 10 | Conferir código, descrição e demais informações. | Os dados apresentados devem corresponder aos dados informados durante a inclusão. |

### UPDATE – Alteração de Competência

| Nº | Ação                                                               | Resultado Esperado                                                  |
| -: | ------------------------------------------------------------------ | ------------------------------------------------------------------- |
| 11 | Selecionar a competência cadastrada e acessar a opção **Alterar**. | O sistema deve abrir o cadastro para edição.                        |
| 12 | Alterar a descrição da competência ou outro campo permitido.       | O sistema deve permitir a alteração do campo.                       |
| 13 | Confirmar a alteração.                                             | O sistema deve validar e gravar as alterações sem apresentar erros. |
| 14 | Consultar novamente a competência.                                 | O sistema deve apresentar os dados atualizados.                     |
| 15 | Conferir os campos alterados.                                      | Os novos valores devem estar gravados corretamente.                 |

### DELETE – Exclusão de Competência

| Nº | Ação                                               | Resultado Esperado                                                                                      |
| -: | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| 16 | Selecionar uma competência que possa ser excluída. | O sistema deve permitir a seleção do registro.                                                          |
| 17 | Acessar a opção **Excluir**.                       | O sistema deve apresentar a confirmação da exclusão, quando aplicável.                                  |
| 18 | Confirmar a exclusão.                              | O sistema deve excluir o registro conforme as regras da rotina.                                         |
| 19 | Pesquisar novamente a competência excluída.        | A competência não deve estar disponível para utilização, conforme o comportamento definido pela rotina. |

## 6. Validação de Campos Obrigatórios

| Nº | Ação                                           | Resultado Esperado                                                        |
| -: | ---------------------------------------------- | ------------------------------------------------------------------------- |
| 20 | Iniciar a inclusão de uma nova competência.    | A tela de cadastro deve ser apresentada.                                  |
| 21 | Deixar um campo obrigatório sem preenchimento. | O sistema deve identificar a ausência da informação.                      |
| 22 | Tentar confirmar o cadastro.                   | O sistema deve impedir a gravação e apresentar uma mensagem de validação. |
| 23 | Preencher corretamente o campo obrigatório.    | O sistema deve permitir a continuidade do cadastro.                       |

## 7. Validação de Duplicidade

| Nº | Ação                                                                | Resultado Esperado                                                                       |
| -: | ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| 24 | Tentar cadastrar uma competência utilizando um código já existente. | O sistema deve identificar a duplicidade.                                                |
| 25 | Confirmar o cadastro.                                               | O sistema deve impedir a criação de um registro duplicado, conforme as regras da rotina. |

## 8. Resultado Esperado

A rotina **CSAA030 – Cadastro de Competências** deve permitir o gerenciamento correto das competências cadastradas.

O sistema deve:

* Permitir a inclusão de uma nova competência com dados válidos.
* Permitir a consulta das competências cadastradas.
* Apresentar corretamente os dados armazenados.
* Permitir a alteração dos campos autorizados.
* Gravar corretamente as alterações realizadas.
* Permitir a exclusão quando não houver impedimentos.
* Validar os campos obrigatórios.
* Impedir a criação de registros duplicados.
* Manter a integridade dos dados durante as operações realizadas.

## 9. Critério de Aprovação

O caso de teste será considerado **APROVADO** quando as operações de **CREATE, READ, UPDATE e DELETE**, quando aplicáveis, forem executadas conforme esperado, sem erros ou inconsistências nos dados cadastrados.

**Status:** `A definir durante a execução`

**Evidências:** `A anexar durante a execução`

**Responsável:** `A definir`

**Data de Execução:** `A definir`
