# CT01_CSAA100 – Cadastro de Departamentos

## 1. Nome do Caso de Teste

**CT08_CSAA100 – Cadastro de Departamentos**

## 2. Nome da Rotina

**CSAA100 – Cadastro de Departamentos**

## 3. Caminho da Rotina

**Protheus → Gestão de Pessoal → Cadastros → Departamentos**

## 4. Objetivo

Validar o cadastro e o gerenciamento de **Departamentos** na rotina **CSAA100**, garantindo que os registros possam ser incluídos, consultados, alterados e excluídos quando permitido, mantendo a integridade das informações cadastradas.

## 5. Passo a Passo

### CREATE – Inclusão de Departamento

| Nº | Ação                                                      | Resultado Esperado                                                      |
| -: | --------------------------------------------------------- | ----------------------------------------------------------------------- |
| 01 | Acessar a rotina **CSAA100 – Cadastro de Departamentos**. | A rotina deve ser apresentada corretamente.                             |
| 02 | Selecionar a opção **Incluir**.                           | O sistema deve abrir a tela para cadastro de um novo departamento.      |
| 03 | Informar o código do departamento, quando solicitado.     | O sistema deve aceitar o código informado conforme as regras da rotina. |
| 04 | Informar a descrição do departamento.                     | O sistema deve aceitar a descrição informada.                           |
| 05 | Preencher os demais campos obrigatórios.                  | O sistema deve validar e aceitar os dados informados.                   |
| 06 | Confirmar a inclusão do departamento.                     | O sistema deve gravar o cadastro sem apresentar erros.                  |
| 07 | Registrar o código e a descrição do departamento.         | As informações devem permanecer gravadas corretamente.                  |

### READ – Consulta de Departamento

| Nº | Ação                                             | Resultado Esperado                                                                |
| -: | ------------------------------------------------ | --------------------------------------------------------------------------------- |
| 08 | Pesquisar o departamento recém-cadastrado.       | O sistema deve localizar o departamento corretamente.                             |
| 09 | Abrir o cadastro do departamento.                | O sistema deve apresentar os dados cadastrados.                                   |
| 10 | Conferir código, descrição e demais informações. | Os dados apresentados devem corresponder aos dados informados durante a inclusão. |

### UPDATE – Alteração de Departamento

| Nº | Ação                                                                | Resultado Esperado                                                  |
| -: | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| 11 | Selecionar o departamento cadastrado e acessar a opção **Alterar**. | O sistema deve abrir o cadastro para edição.                        |
| 12 | Alterar a descrição ou outro campo permitido.                       | O sistema deve permitir a alteração conforme as regras da rotina.   |
| 13 | Confirmar a alteração.                                              | O sistema deve validar e gravar as alterações sem apresentar erros. |
| 14 | Consultar novamente o departamento.                                 | O sistema deve apresentar os dados atualizados.                     |
| 15 | Conferir os campos alterados.                                       | Os novos valores devem estar gravados corretamente.                 |

### DELETE – Exclusão de Departamento

| Nº | Ação                                               | Resultado Esperado                                                                                       |
| -: | -------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| 16 | Selecionar um departamento que possa ser excluído. | O sistema deve permitir a seleção do registro.                                                           |
| 17 | Acessar a opção **Excluir**.                       | O sistema deve apresentar a confirmação da exclusão, quando aplicável.                                   |
| 18 | Confirmar a exclusão.                              | O sistema deve excluir o registro conforme as regras da rotina.                                          |
| 19 | Pesquisar novamente o departamento excluído.       | O departamento não deve estar disponível para utilização, conforme o comportamento definido pela rotina. |

## 6. Validação de Campos Obrigatórios

| Nº | Ação                                           | Resultado Esperado                                                        |
| -: | ---------------------------------------------- | ------------------------------------------------------------------------- |
| 20 | Iniciar a inclusão de um novo departamento.    | A tela de cadastro deve ser apresentada.                                  |
| 21 | Deixar um campo obrigatório sem preenchimento. | O sistema deve identificar a ausência da informação.                      |
| 22 | Tentar confirmar o cadastro.                   | O sistema deve impedir a gravação e apresentar uma mensagem de validação. |
| 23 | Preencher corretamente o campo obrigatório.    | O sistema deve permitir a continuidade do cadastro.                       |

## 7. Validação de Duplicidade

| Nº | Ação                                                                | Resultado Esperado                                                                      |
| -: | ------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| 24 | Tentar cadastrar um departamento utilizando um código já existente. | O sistema deve identificar a duplicidade.                                               |
| 25 | Confirmar o cadastro.                                               | O sistema deve impedir a criação de um registro duplicado conforme as regras da rotina. |

## 8. Resultado Esperado

A rotina **CSAA100 – Cadastro de Departamentos** deve permitir o correto gerenciamento dos departamentos cadastrados.

O sistema deve:

* Permitir a inclusão de departamentos com dados válidos.
* Permitir a consulta dos departamentos cadastrados.
* Apresentar corretamente os dados armazenados.
* Permitir a alteração dos campos autorizados.
* Gravar corretamente as alterações realizadas.
* Permitir a exclusão quando não houver impedimentos.
* Validar os campos obrigatórios.
* Impedir a criação de registros duplicados.
* Manter a integridade das informações durante as operações realizadas.

## 9. Critério de Aprovação

O caso de teste será considerado **APROVADO** quando as operações de **CREATE, READ, UPDATE e DELETE**, quando aplicáveis, forem executadas conforme esperado, sem erros ou inconsistências nos dados cadastrados.

**Status:** `A definir durante a execução`

**Evidências:** `A anexar durante a execução`

**Responsável:** `A definir`

**Data de Execução:** `A definir`
