# CT01_MATA360 – CRUD de Condição de Pagamento

## 1. Nome do Caso de Teste

**CT08_MATA360 – CRUD de Condição de Pagamento**

## 2. Nome da Rotina

**MATA360 – Condições de Pagamento**

## 3. Caminho da Rotina

**Protheus → SIGACOM → Atualizações → Cadastros → Condição de Pagamento**

## 4. Objetivo

Validar o **CRUD completo de uma Condição de Pagamento** na rotina **MATA360**, contemplando as operações de **inclusão, visualização, alteração e exclusão**, garantindo que os dados sejam corretamente cadastrados, consultados, modificados e removidos do sistema.

## 5. Passo a Passo

### CREATE – Inclusão de Condição de Pagamento

| Nº | Ação                                                                          | Resultado Esperado                                                           |
| -: | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| 01 | Acessar a rotina **MATA360 – Condições de Pagamento**.                        | A rotina deve ser apresentada corretamente.                                  |
| 02 | Selecionar a opção **Incluir**.                                               | O sistema deve abrir a tela para cadastro de uma nova Condição de Pagamento. |
| 03 | Preencher os campos obrigatórios da Condição de Pagamento.                    | O sistema deve aceitar os dados válidos informados.                          |
| 04 | Informar os demais dados necessários para configurar a Condição de Pagamento. | O sistema deve permitir o preenchimento das informações.                     |
| 05 | Confirmar a inclusão da Condição de Pagamento.                                | O sistema deve validar os dados e gravar o cadastro sem apresentar erros.    |
| 06 | Registrar a identificação da Condição de Pagamento criada.                    | O sistema deve disponibilizar a identificação da condição cadastrada.        |

### READ – Visualização da Condição de Pagamento

| Nº | Ação                                                                               | Resultado Esperado                                                           |
| -: | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| 07 | Acessar novamente a rotina **MATA360** e localizar a Condição de Pagamento criada. | A condição deve ser localizada corretamente.                                 |
| 08 | Abrir o cadastro da Condição de Pagamento.                                         | O sistema deve apresentar os dados cadastrados.                              |
| 09 | Conferir as informações apresentadas.                                              | Os dados devem corresponder às informações utilizadas durante a inclusão.    |
| 10 | Conferir a identificação da Condição de Pagamento.                                 | O sistema deve apresentar corretamente o código ou identificação cadastrada. |

### UPDATE – Alteração da Condição de Pagamento

| Nº | Ação                                                                    | Resultado Esperado                                                                   |
| -: | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| 11 | Localizar e selecionar a Condição de Pagamento incluída anteriormente.  | O sistema deve localizar e selecionar corretamente o registro cadastrado.            |
| 12 | Acessar a opção **Alterar**.                                            | O sistema deve abrir o cadastro da Condição de Pagamento para edição.                |
| 13 | Alterar um ou mais campos permitidos da Condição de Pagamento.          | O sistema deve permitir a alteração dos dados selecionados.                          |
| 14 | Conferir os dados alterados antes da gravação.                          | Os novos valores devem ser apresentados corretamente.                                |
| 15 | Confirmar/salvar a alteração.                                           | O sistema deve validar os dados e gravar a alteração sem apresentar erros ou falhas. |
| 16 | Verificar a mensagem apresentada após a gravação.                       | O sistema deve informar que o **registro foi alterado com sucesso**.                 |
| 17 | Localizar novamente a Condição de Pagamento alterada.                   | O registro deve permanecer disponível para consulta.                                 |
| 18 | Abrir o cadastro alterado.                                              | O sistema deve apresentar os dados atualizados.                                      |
| 19 | Comparar os dados alterados com os valores informados durante a edição. | Os dados devem corresponder às alterações realizadas e permanecer consistentes.      |

### DELETE – Exclusão da Condição de Pagamento

| Nº | Ação                                                                      | Resultado Esperado                                                       |
| -: | ------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| 20 | Localizar e selecionar a Condição de Pagamento que será excluída.         | O sistema deve selecionar corretamente o registro.                       |
| 21 | Acessar a opção **Outras Ações → Excluir**.                               | O sistema deve apresentar a tela ou mensagem de confirmação da exclusão. |
| 22 | Conferir os dados da Condição de Pagamento apresentada para exclusão.     | Os dados devem corresponder ao registro selecionado.                     |
| 23 | Confirmar a exclusão da Condição de Pagamento.                            | O sistema deve processar a exclusão sem apresentar erros ou falhas.      |
| 24 | Verificar a mensagem apresentada após a exclusão.                         | O sistema deve informar que o **registro foi excluído com sucesso**.     |
| 25 | Pesquisar novamente pela identificação da Condição de Pagamento excluída. | O registro excluído não deve estar disponível para consulta.             |

## 6. Validação de Campos Obrigatórios

| Nº | Ação                                                  | Resultado Esperado                                                                             |
| -: | ----------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| 26 | Iniciar a inclusão de uma nova Condição de Pagamento. | A tela de inclusão deve ser apresentada.                                                       |
| 27 | Deixar um campo obrigatório sem preenchimento.        | O sistema deve identificar a ausência da informação.                                           |
| 28 | Tentar confirmar a inclusão.                          | O sistema deve impedir a gravação e apresentar uma mensagem de validação.                      |
| 29 | Preencher o campo obrigatório e confirmar novamente.  | O sistema deve permitir a continuidade da inclusão, desde que os demais dados estejam válidos. |

## 7. Validação da Persistência dos Dados

| Nº | Ação                                                                          | Resultado Esperado                                                       |
| -: | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| 30 | Após a inclusão, sair da tela da Condição de Pagamento.                       | O sistema deve retornar à tela anterior sem apresentar erros.            |
| 31 | Pesquisar novamente a Condição de Pagamento utilizando sua identificação.     | A condição deve ser localizada corretamente.                             |
| 32 | Abrir a condição localizada.                                                  | O sistema deve apresentar os dados anteriormente cadastrados.            |
| 33 | Comparar os dados apresentados com os dados informados durante a inclusão.    | As informações devem permanecer consistentes e sem alterações indevidas. |
| 34 | Após realizar a alteração, sair da tela do cadastro.                          | O sistema deve retornar à tela anterior sem apresentar erros.            |
| 35 | Pesquisar novamente a Condição de Pagamento alterada.                         | A condição deve ser localizada corretamente.                             |
| 36 | Abrir a condição alterada.                                                    | O sistema deve apresentar os dados atualizados.                          |
| 37 | Comparar os dados apresentados com os valores informados durante a alteração. | As alterações devem estar corretamente persistidas.                      |

## 8. Validação da Exclusão

| Nº | Ação                                                                        | Resultado Esperado                                                             |
| -: | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| 38 | Selecionar a Condição de Pagamento para exclusão.                           | O registro correto deve ser selecionado.                                       |
| 39 | Acessar **Outras Ações → Excluir**.                                         | O sistema deve apresentar a confirmação da exclusão.                           |
| 40 | Conferir os dados apresentados antes da confirmação.                        | Os dados devem corresponder ao registro selecionado.                           |
| 41 | Confirmar a exclusão.                                                       | O sistema deve excluir o registro corretamente.                                |
| 42 | Verificar a mensagem de confirmação.                                        | O sistema deve informar que o **registro foi excluído com sucesso**.           |
| 43 | Realizar uma nova pesquisa utilizando a identificação do registro excluído. | A Condição de Pagamento excluída não deve mais estar disponível para consulta. |

## 9. Resultado Esperado

A rotina **MATA360 – Condições de Pagamento** deve permitir realizar corretamente o **CRUD completo** de uma Condição de Pagamento.

O sistema deve:

* Permitir a inclusão de uma Condição de Pagamento com dados válidos;
* Validar os campos obrigatórios antes da gravação;
* Gravar corretamente a Condição de Pagamento;
* Disponibilizar a identificação da condição cadastrada;
* Permitir localizar e visualizar a condição incluída;
* Apresentar corretamente os dados cadastrados;
* Permitir alterar os dados do registro;
* Gravar corretamente as alterações realizadas;
* Informar que o **registro foi alterado com sucesso**;
* Permitir localizar e visualizar os dados após a alteração;
* Permitir excluir a Condição de Pagamento;
* Apresentar os dados do registro antes da confirmação da exclusão;
* Permitir confirmar a exclusão;
* Informar que o **registro foi excluído com sucesso**;
* Impedir que o registro excluído permaneça disponível para consulta;
* Manter a integridade e consistência dos dados durante todo o ciclo CRUD.

Todas as operações devem ser executadas **sem erros, falhas, travamentos, inconsistências ou impedimentos** que comprometam o funcionamento da rotina.

## 10. Critério de Aprovação

O caso de teste será considerado **APROVADO** quando:

1. A Condição de Pagamento for incluída corretamente;
2. Os campos obrigatórios forem devidamente validados;
3. A condição puder ser localizada e visualizada após a inclusão;
4. Os dados visualizados corresponderem aos dados cadastrados;
5. A Condição de Pagamento puder ser alterada;
6. A alteração for gravada corretamente;
7. O sistema informar o sucesso da alteração;
8. Os dados alterados permanecerem persistidos após nova consulta;
9. A Condição de Pagamento puder ser excluída;
10. O sistema solicitar e processar corretamente a confirmação da exclusão;
11. O sistema informar o sucesso da exclusão;
12. O registro excluído não estiver mais disponível para consulta;
13. Todo o fluxo de **CREATE, READ, UPDATE e DELETE** for executado sem erros, falhas ou impedimentos.

**Status:** `A definir durante a execução`

**Evidências:** `A anexar durante a execução`

**Responsável:** `A definir`

**Data de Execução:** `A definir`
