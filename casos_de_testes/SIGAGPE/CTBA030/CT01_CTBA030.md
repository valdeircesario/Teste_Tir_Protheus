# CT01_CTBA030 – CRUD de Centro de Custos

## 1. Nome do Caso de Teste

**CT01_CTBA030 – CRUD de Centro de Custos**

## 2. Nome da Rotina

**CTBA030 – Cadastro de Centro de Custos**

## 3. Caminho da Rotina

**Protheus → Atualizações → Cadastros → Centro de Custos**

## 4. Objetivo

Validar o funcionamento da rotina **CTBA030 – Cadastro de Centro de Custos**, realizando o ciclo completo de **inclusão, visualização, alteração e exclusão** de um Centro de Custo, garantindo a correta gravação, consulta, atualização e exclusão dos dados, sem apresentar erros, falhas ou impedimentos durante a execução.

## 5. Cenário de Teste

Realizar o CRUD completo de um Centro de Custo:

* Incluir um novo Centro de Custo;
* Visualizar o registro incluído;
* Validar os dados cadastrados;
* Alterar um ou mais dados do registro;
* Validar os dados após a alteração;
* Excluir o Centro de Custo;
* Confirmar a exclusão;
* Validar que o registro não esteja mais disponível para consulta.

## 6. Passo a Passo

### CREATE – Inclusão de Centro de Custo

| Nº | Ação                                                         | Resultado Esperado                                                    |
| -: | ------------------------------------------------------------ | --------------------------------------------------------------------- |
| 01 | Acessar a rotina **CTBA030 – Cadastro de Centro de Custos**. | A rotina deve ser apresentada corretamente, sem erros.                |
| 02 | Selecionar a opção **Incluir**.                              | O sistema deve abrir a tela para inclusão de um novo Centro de Custo. |
| 03 | Preencher os campos obrigatórios do Centro de Custo.         | O sistema deve permitir o preenchimento dos campos com dados válidos. |
| 04 | Informar os demais dados necessários para o cadastro.        | O sistema deve permitir o preenchimento das informações.              |
| 05 | Conferir os dados informados antes da gravação.              | Os dados devem estar apresentados corretamente.                       |
| 06 | Clicar em **Salvar/Confirmar**.                              | O sistema deve gravar o registro sem apresentar erros ou falhas.      |
| 07 | Verificar a mensagem apresentada pelo sistema.               | O sistema deve informar que o **registro foi inserido com sucesso**.  |

### READ – Visualização do Centro de Custo

| Nº | Ação                                         | Resultado Esperado                                                                |
| -: | -------------------------------------------- | --------------------------------------------------------------------------------- |
| 08 | Localizar o Centro de Custo recém-incluído.  | O registro deve ser localizado corretamente.                                      |
| 09 | Selecionar o Centro de Custo incluído.       | O registro correto deve ficar selecionado.                                        |
| 10 | Acessar a opção **Visualizar**.              | O sistema deve abrir o cadastro do Centro de Custo.                               |
| 11 | Conferir os dados cadastrados.               | Os dados apresentados devem corresponder aos dados informados durante a inclusão. |
| 12 | Conferir a identificação do Centro de Custo. | O sistema deve apresentar corretamente a identificação do registro.               |
| 13 | Sair da tela de visualização.                | O sistema deve retornar à listagem sem apresentar erros ou falhas.                |

### UPDATE – Alteração do Centro de Custo

| Nº | Ação                                               | Resultado Esperado                                                   |
| -: | -------------------------------------------------- | -------------------------------------------------------------------- |
| 14 | Localizar e selecionar o Centro de Custo incluído. | O sistema deve selecionar corretamente o registro.                   |
| 15 | Acessar a opção **Alterar**.                       | O sistema deve abrir o cadastro para edição.                         |
| 16 | Alterar um ou mais campos permitidos.              | O sistema deve permitir a alteração dos dados.                       |
| 17 | Conferir os dados alterados.                       | Os novos valores devem estar apresentados corretamente.              |
| 18 | Clicar em **Salvar/Confirmar**.                    | O sistema deve gravar a alteração sem apresentar erros ou falhas.    |
| 19 | Verificar a mensagem apresentada.                  | O sistema deve informar que o **registro foi alterado com sucesso**. |
| 20 | Localizar novamente o Centro de Custo alterado.    | O registro deve permanecer disponível para consulta.                 |
| 21 | Visualizar o registro novamente.                   | O sistema deve apresentar os dados atualizados.                      |
| 22 | Validar os campos alterados.                       | Os valores devem corresponder às alterações realizadas.              |

### DELETE – Exclusão do Centro de Custo

| Nº | Ação                                                    | Resultado Esperado                                                   |
| -: | ------------------------------------------------------- | -------------------------------------------------------------------- |
| 23 | Selecionar o Centro de Custo que será excluído.         | O registro correto deve ser selecionado.                             |
| 24 | Acessar **Outras Ações → Excluir**.                     | O sistema deve apresentar a confirmação da exclusão.                 |
| 25 | Conferir os dados do Centro de Custo antes da exclusão. | Os dados devem corresponder ao registro selecionado.                 |
| 26 | Confirmar a exclusão.                                   | O sistema deve processar a exclusão sem apresentar erros ou falhas.  |
| 27 | Verificar a mensagem apresentada.                       | O sistema deve informar que o **registro foi excluído com sucesso**. |
| 28 | Pesquisar novamente pelo Centro de Custo excluído.      | O registro não deve mais estar disponível para consulta.             |

## 7. Validação de Campos Obrigatórios

| Nº | Ação                                                 | Resultado Esperado                                                                             |
| -: | ---------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| 29 | Iniciar a inclusão de um novo Centro de Custo.       | A tela de inclusão deve ser apresentada.                                                       |
| 30 | Deixar um campo obrigatório sem preenchimento.       | O sistema deve identificar a ausência da informação.                                           |
| 31 | Tentar confirmar a inclusão.                         | O sistema deve impedir a gravação e apresentar uma mensagem de validação.                      |
| 32 | Preencher o campo obrigatório e confirmar novamente. | O sistema deve permitir a continuidade da inclusão, desde que os demais dados estejam válidos. |

## 8. Validação da Persistência dos Dados

| Nº | Ação                                                                        | Resultado Esperado                                            |
| -: | --------------------------------------------------------------------------- | ------------------------------------------------------------- |
| 33 | Após a inclusão, sair da tela do cadastro.                                  | O sistema deve retornar à tela anterior sem apresentar erros. |
| 34 | Pesquisar novamente o Centro de Custo utilizando sua identificação.         | O registro deve ser localizado corretamente.                  |
| 35 | Abrir o registro localizado.                                                | O sistema deve apresentar os dados anteriormente cadastrados. |
| 36 | Comparar os dados apresentados com os dados utilizados na inclusão.         | Os dados devem permanecer consistentes.                       |
| 37 | Após a alteração, sair da tela do cadastro.                                 | O sistema deve retornar à tela anterior sem apresentar erros. |
| 38 | Pesquisar novamente o Centro de Custo alterado.                             | O registro deve ser localizado corretamente.                  |
| 39 | Abrir o registro alterado.                                                  | O sistema deve apresentar os dados atualizados.               |
| 40 | Comparar os dados apresentados com os dados informados durante a alteração. | As alterações devem permanecer corretamente persistidas.      |

## 9. Validação da Exclusão

| Nº | Ação                                               | Resultado Esperado                                                   |
| -: | -------------------------------------------------- | -------------------------------------------------------------------- |
| 41 | Selecionar o Centro de Custo para exclusão.        | O registro correto deve ser selecionado.                             |
| 42 | Acessar **Outras Ações → Excluir**.                | O sistema deve apresentar a confirmação da exclusão.                 |
| 43 | Conferir os dados apresentados.                    | Os dados devem corresponder ao Centro de Custo selecionado.          |
| 44 | Confirmar a exclusão.                              | O sistema deve excluir o registro corretamente.                      |
| 45 | Verificar a mensagem apresentada.                  | O sistema deve informar que o **registro foi excluído com sucesso**. |
| 46 | Realizar uma nova pesquisa pelo registro excluído. | O Centro de Custo não deve mais estar disponível para consulta.      |

## 10. Resultado Esperado

A rotina **CTBA030 – Cadastro de Centro de Custos** deve permitir realizar corretamente o **CRUD completo** de um Centro de Custo.

O sistema deve:

* Permitir a inclusão de um Centro de Custo com dados válidos;
* Validar os campos obrigatórios antes da gravação;
* Gravar corretamente o registro;
* Apresentar a mensagem de sucesso da inclusão;
* Permitir localizar e visualizar o Centro de Custo;
* Apresentar corretamente os dados cadastrados;
* Permitir alterar os dados do registro;
* Gravar corretamente as alterações realizadas;
* Apresentar a mensagem de sucesso da alteração;
* Manter os dados alterados após nova consulta;
* Permitir excluir o Centro de Custo;
* Apresentar os dados do registro antes da exclusão;
* Solicitar a confirmação da exclusão;
* Gravar corretamente a exclusão;
* Apresentar a mensagem de sucesso da exclusão;
* Impedir que o registro excluído permaneça disponível para consulta.

Todo o fluxo deve ser executado sem **erros, falhas, travamentos, inconsistências ou impedimentos** que comprometam o funcionamento da rotina.

## 11. Critério de Aprovação

O caso de teste será considerado **APROVADO** quando:

1. O Centro de Custo for incluído corretamente;
2. Os campos obrigatórios forem devidamente validados;
3. O registro puder ser localizado e visualizado após a inclusão;
4. Os dados apresentados corresponderem aos dados cadastrados;
5. O registro puder ser alterado;
6. As alterações forem gravadas corretamente;
7. O sistema informar o sucesso da alteração;
8. Os dados alterados permanecerem persistidos;
9. O registro puder ser excluído mediante confirmação;
10. O sistema informar o sucesso da exclusão;
11. O registro excluído não estiver mais disponível para consulta;
12. Todo o fluxo de **CREATE, READ, UPDATE e DELETE** for executado sem erros ou falhas.

**Status:** `A definir durante a execução`

**Evidências:** `A anexar durante a execução`

**Responsável:** `A definir`

**Data de Execução:** `A definir`
