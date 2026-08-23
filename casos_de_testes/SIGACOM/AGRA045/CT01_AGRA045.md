# CT01_AGRA045 – Inclusão, Visualização, Alteração e Exclusão de Local de Estoque

## 1. Nome do Caso de Teste

**CT04_AGRA045 – CRUD de Locais de Estoque**

## 2. Nome da Rotina

**AGRA045 – Cadastro de Locais de Estoque**

## 3. Caminho da Rotina

**Protheus → SIGAAGR → Atualizações → Cadastros → Locais de Estoque**

## 4. Objetivo

Validar as operações de **CRUD (Create, Read, Update e Delete)** no cadastro de **Locais de Estoque** da rotina **AGRA045**, garantindo a inclusão, visualização, alteração e exclusão dos registros conforme as regras de negócio do Protheus.

## 5. Passo a Passo

### CREATE – Inclusão de Local de Estoque

| Nº | Ação                                                  | Resultado Esperado                                                        |
| -: | ----------------------------------------------------- | ------------------------------------------------------------------------- |
| 01 | Acessar a rotina **AGRA045 – Locais de Estoque**.     | A rotina deve ser apresentada corretamente.                               |
| 02 | Selecionar a opção **Incluir**.                       | O sistema deve abrir a tela de cadastro de um novo local de estoque.      |
| 03 | Preencher os campos obrigatórios do local de estoque. | O sistema deve aceitar os dados válidos informados.                       |
| 04 | Preencher os demais campos necessários do cadastro.   | O sistema deve permitir o preenchimento das informações.                  |
| 05 | Confirmar a inclusão do local de estoque.             | O sistema deve validar os dados e gravar o cadastro sem apresentar erros. |
| 06 | Registrar a identificação do local de estoque criado. | O sistema deve disponibilizar a identificação do local cadastrado.        |

### READ – Visualização de Local de Estoque

| Nº | Ação                                                                    | Resultado Esperado                                                        |
| -: | ----------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| 07 | Acessar a rotina **AGRA045** e localizar o local de estoque cadastrado. | O local de estoque deve ser localizado corretamente.                      |
| 08 | Abrir o cadastro do local de estoque.                                   | O sistema deve apresentar os dados cadastrados.                           |
| 09 | Conferir as informações apresentadas.                                   | Os dados devem corresponder às informações utilizadas durante a inclusão. |

### UPDATE – Alteração de Local de Estoque

| Nº | Ação                                                                    | Resultado Esperado                                                                              |
| -: | ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| 10 | Selecionar o local de estoque cadastrado e acessar a opção **Alterar**. | O sistema deve abrir o cadastro para edição.                                                    |
| 11 | Alterar uma informação permitida do local de estoque.                   | O sistema deve permitir a alteração do campo.                                                   |
| 12 | Confirmar a alteração.                                                  | O sistema deve validar e gravar as alterações sem apresentar erros.                             |
| 13 | Consultar novamente o local de estoque.                                 | O sistema deve apresentar as informações atualizadas.                                           |
| 14 | Conferir os campos alterados e não alterados.                           | Os campos alterados devem apresentar os novos valores e os demais devem permanecer inalterados. |

### DELETE – Exclusão de Local de Estoque

| Nº | Ação                                                                    | Resultado Esperado                                                                                           |
| -: | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| 15 | Selecionar o local de estoque cadastrado e acessar a opção **Excluir**. | O sistema deve apresentar a confirmação da exclusão, quando aplicável.                                       |
| 16 | Confirmar a exclusão do local de estoque.                               | O sistema deve realizar a exclusão conforme as regras da rotina.                                             |
| 17 | Pesquisar novamente o local de estoque excluído.                        | O local de estoque não deve estar disponível para utilização, conforme o comportamento definido pela rotina. |

## 6. Validação de Campos Obrigatórios

| Nº | Ação                                                 | Resultado Esperado                                                                             |
| -: | ---------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| 18 | Iniciar a inclusão de um novo local de estoque.      | A tela de inclusão deve ser apresentada.                                                       |
| 19 | Deixar um campo obrigatório sem preenchimento.       | O sistema deve identificar a ausência da informação.                                           |
| 20 | Tentar confirmar a inclusão.                         | O sistema deve impedir a gravação e apresentar uma mensagem de validação.                      |
| 21 | Preencher o campo obrigatório e confirmar novamente. | O sistema deve permitir a continuidade do cadastro, desde que os demais dados estejam válidos. |

## 7. Validação de Duplicidade

| Nº | Ação                                                                           | Resultado Esperado                                                                        |
| -: | ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| 22 | Tentar incluir um local de estoque utilizando uma identificação já cadastrada. | O sistema deve identificar a duplicidade conforme as regras configuradas.                 |
| 23 | Confirmar o cadastro.                                                          | O sistema deve impedir ou tratar a duplicidade de acordo com a regra de negócio definida. |

## 8. Resultado Esperado

A rotina **AGRA045 – Locais de Estoque** deve permitir realizar corretamente as operações de **inclusão, visualização, alteração e exclusão** de locais de estoque.

O sistema deve:

* Permitir a inclusão de locais de estoque com dados válidos.
* Permitir a visualização dos locais de estoque cadastrados.
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
