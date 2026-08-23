# CT04_MATA020 – CRUD de Fornecedores

## 1. Nome do Caso de Teste

**CT04_MATA020 – CRUD de Fornecedores**

## 2. Nome da Rotina

**MATA020 – Cadastro de Fornecedores**

## 3. Caminho da Rotina

**Protheus → SIGACOM → Atualizações → Cadastros → Fornecedores**

## 4. Objetivo

Validar as operações de **CRUD (Create, Read, Update e Delete)** no cadastro de fornecedores da rotina **MATA020**, garantindo a inclusão, consulta, alteração e exclusão de registros conforme as regras de negócio do Protheus.

## 5. Passo a Passo

### CREATE – Inclusão de Fornecedor

| Nº | Ação                                                     | Resultado Esperado                                                        |
| -: | -------------------------------------------------------- | ------------------------------------------------------------------------- |
| 01 | Acessar a rotina **MATA020 – Cadastro de Fornecedores**. | A rotina deve ser apresentada corretamente.                               |
| 02 | Selecionar a opção **Incluir**.                          | O sistema deve abrir a tela de cadastro de um novo fornecedor.            |
| 03 | Preencher os campos obrigatórios do fornecedor.          | O sistema deve aceitar os dados válidos informados.                       |
| 04 | Preencher os demais campos necessários do cadastro.      | O sistema deve permitir o preenchimento das informações.                  |
| 05 | Confirmar a inclusão do fornecedor.                      | O sistema deve validar os dados e gravar o cadastro sem apresentar erros. |
| 06 | Registrar o código e a loja do fornecedor criado.        | O sistema deve disponibilizar a identificação do fornecedor cadastrado.   |

### READ – Consulta de Fornecedor

| Nº | Ação                                                              | Resultado Esperado                                                                |
| -: | ----------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| 07 | Acessar a rotina **MATA020** e localizar o fornecedor cadastrado. | O fornecedor deve ser localizado corretamente.                                    |
| 08 | Abrir o cadastro do fornecedor.                                   | O sistema deve apresentar os dados do fornecedor.                                 |
| 09 | Conferir as informações cadastradas.                              | Os dados apresentados devem corresponder aos dados informados durante a inclusão. |

### UPDATE – Alteração de Fornecedor

| Nº | Ação                                                              | Resultado Esperado                                                                              |
| -: | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| 10 | Selecionar o fornecedor cadastrado e acessar a opção **Alterar**. | O sistema deve abrir o cadastro para edição.                                                    |
| 11 | Alterar uma informação permitida do fornecedor.                   | O sistema deve permitir a alteração do campo.                                                   |
| 12 | Confirmar a alteração.                                            | O sistema deve validar e gravar as alterações sem apresentar erros.                             |
| 13 | Consultar novamente o fornecedor.                                 | O sistema deve apresentar as informações atualizadas.                                           |
| 14 | Conferir os campos alterados e não alterados.                     | Os campos alterados devem apresentar os novos valores e os demais devem permanecer inalterados. |

### DELETE – Exclusão de Fornecedor

| Nº | Ação                                                              | Resultado Esperado                                                                                     |
| -: | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| 15 | Selecionar o fornecedor cadastrado e acessar a opção **Excluir**. | O sistema deve apresentar a confirmação da exclusão, quando aplicável.                                 |
| 16 | Confirmar a exclusão do fornecedor.                               | O sistema deve realizar a exclusão conforme as regras da rotina.                                       |
| 17 | Pesquisar novamente o fornecedor excluído.                        | O fornecedor não deve estar disponível para utilização, conforme o comportamento definido pela rotina. |

## 6. Validação de Campos Obrigatórios

| Nº | Ação                                                 | Resultado Esperado                                                                             |
| -: | ---------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| 18 | Iniciar a inclusão de um novo fornecedor.            | A tela de inclusão deve ser apresentada.                                                       |
| 19 | Deixar um campo obrigatório sem preenchimento.       | O sistema deve identificar a ausência da informação.                                           |
| 20 | Tentar confirmar a inclusão.                         | O sistema deve impedir a gravação e apresentar uma mensagem de validação.                      |
| 21 | Preencher o campo obrigatório e confirmar novamente. | O sistema deve permitir a continuidade do cadastro, desde que os demais dados estejam válidos. |

## 7. Validação de Duplicidade

| Nº | Ação                                                                | Resultado Esperado                                                                        |
| -: | ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| 22 | Tentar incluir um fornecedor utilizando um documento já cadastrado. | O sistema deve identificar a duplicidade conforme as regras configuradas.                 |
| 23 | Confirmar o cadastro.                                               | O sistema deve impedir ou tratar a duplicidade de acordo com a regra de negócio definida. |

## 8. Resultado Esperado

A rotina **MATA020 – Cadastro de Fornecedores** deve permitir realizar corretamente as operações de **inclusão, consulta, alteração e exclusão** de fornecedores.

O sistema deve:

* Permitir a inclusão de fornecedores com dados válidos.
* Permitir a consulta dos fornecedores cadastrados.
* Apresentar corretamente os dados armazenados.
* Permitir a alteração dos campos autorizados.
* Gravar corretamente as alterações realizadas.
* Permitir a exclusão quando não houver impedimentos.
* Validar campos obrigatórios.
* Tratar corretamente situações de duplicidade.
* Impedir operações que estejam em desacordo com as regras de negócio.
* Manter a integridade dos dados durante todo o ciclo CRUD.

## 9. Critério de Aprovação

O caso de teste será considerado **APROVADO** quando todas as operações previstas de **CREATE, READ, UPDATE e DELETE** forem executadas conforme esperado, sem erros ou inconsistências nos dados.

**Status:** `A definir durante a execução`

**Evidências:** `A anexar durante a execução`

**Responsável:** `A definir`

**Data de Execução:** `A definir`
