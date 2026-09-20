# CT01_ATFA025 – Locais

## 1. Nome do Caso de Teste

**CT01_ATFA025 – Locais**

## 2. Módulo

**Ativo Fiscal**

## 3. Nome da Rotina

**ATFA025 – Locais**

## 4. Caminho da Rotina

**Protheus → Ativo Fiscal → Atualizações → Cadastros → Locais**

## 5. Objetivo

Validar o funcionamento da rotina **ATFA025 – Locais**, verificando a capacidade do sistema de **incluir, visualizar, alterar e excluir um local**, garantindo a correta gravação, apresentação, atualização e exclusão dos dados, sem ocorrência de erros, falhas ou inconsistências durante a execução.

## 6. Cenário de Teste

Realizar o ciclo completo de manutenção de um local:

* Inclusão de um novo local;
* Visualização do registro incluído;
* Validação dos dados cadastrados;
* Alteração dos dados do local;
* Validação da alteração;
* Exclusão do registro;
* Confirmação da exclusão.

---

## 7. Passo a Passo

### 7.1 CREATE – Inclusão de Local

| Nº | Ação                                                   | Resultado Esperado                                                        |
| -: | ------------------------------------------------------ | ------------------------------------------------------------------------- |
| 01 | Acessar o módulo **Ativo Fiscal**.                     | O sistema deve apresentar o módulo corretamente, sem erros.               |
| 02 | Acessar **Atualizações → Cadastros → Locais**.         | A rotina **ATFA025 – Locais** deve ser carregada corretamente.            |
| 03 | Clicar na opção **Incluir**.                           | O sistema deve apresentar a tela de inclusão de um novo local.            |
| 04 | Informar o **Código** do local.                        | O sistema deve permitir o preenchimento do código.                        |
| 05 | Informar a **Descrição** do local.                     | O sistema deve permitir o preenchimento da descrição.                     |
| 06 | Informar o **Tipo** do local.                          | O sistema deve permitir a seleção/informação do tipo.                     |
| 07 | Informar o campo **Bloqueio** como **Sim** ou **Não**. | O sistema deve permitir a seleção da situação de bloqueio.                |
| 08 | Conferir os dados informados.                          | Os dados devem permanecer preenchidos corretamente antes da confirmação.  |
| 09 | Confirmar a inclusão do registro.                      | O sistema deve processar a inclusão sem apresentar erros ou falhas.       |
| 10 | Verificar a mensagem apresentada pelo sistema.         | O sistema deve apresentar a mensagem **"Registro inserido com sucesso"**. |

---

### 7.2 READ – Visualização do Local

| Nº | Ação                                                              | Resultado Esperado                                                               |
| -: | ----------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| 11 | Localizar o local recém-incluído na listagem da rotina.           | O registro incluído deve ser apresentado na listagem.                            |
| 12 | Selecionar o registro incluído e acessar a opção de visualização. | O sistema deve abrir os dados do local selecionado.                              |
| 13 | Validar o **Código**.                                             | O código apresentado deve corresponder ao informado durante a inclusão.          |
| 14 | Validar a **Descrição**.                                          | A descrição apresentada deve corresponder ao valor informado durante a inclusão. |
| 15 | Validar o **Tipo**.                                               | O tipo apresentado deve corresponder ao valor informado durante a inclusão.      |
| 16 | Validar o campo **Bloqueio**.                                     | A situação apresentada deve corresponder à opção selecionada durante a inclusão. |
| 17 | Conferir os demais dados apresentados na tela.                    | Os dados devem estar íntegros e consistentes com o registro cadastrado.          |

---

### 7.3 UPDATE – Alteração do Local

| Nº | Ação                                                                                                | Resultado Esperado                                                            |
| -: | --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| 18 | Selecionar o mesmo local e acessar a opção de **Alterar**.                                          | O sistema deve abrir o registro para edição.                                  |
| 19 | Alterar a **Descrição** do local.                                                                   | O sistema deve permitir a alteração da descrição.                             |
| 20 | Alterar o campo **Bloqueio**, quando aplicável, de **Sim** para **Não** ou de **Não** para **Sim**. | O sistema deve permitir a alteração da situação de bloqueio.                  |
| 21 | Conferir os dados alterados.                                                                        | Os dados modificados devem estar apresentados corretamente antes da gravação. |
| 22 | Salvar/confirmar a alteração.                                                                       | O sistema deve processar a alteração sem apresentar erros ou falhas.          |
| 23 | Verificar a mensagem apresentada pelo sistema.                                                      | O sistema deve apresentar a mensagem **"Registro alterado com sucesso"**.     |
| 24 | Localizar novamente o registro alterado.                                                            | O registro deve permanecer disponível na listagem.                            |
| 25 | Visualizar o registro novamente.                                                                    | O sistema deve apresentar os dados atualizados.                               |
| 26 | Validar a **Descrição** e o campo **Bloqueio** após a alteração.                                    | Os dados devem corresponder exatamente às alterações realizadas.              |

---

### 7.4 DELETE – Exclusão do Local

| Nº | Ação                                               | Resultado Esperado                                                        |
| -: | -------------------------------------------------- | ------------------------------------------------------------------------- |
| 27 | Selecionar o local alterado na listagem.           | O registro correto deve ser selecionado.                                  |
| 28 | Acessar a opção **Outras Ações → Excluir**.        | O sistema deve apresentar a tela ou mensagem de confirmação da exclusão.  |
| 29 | Conferir os dados do registro que será excluído.   | Os dados apresentados devem corresponder ao local selecionado.            |
| 30 | Confirmar a exclusão do registro.                  | O sistema deve processar a exclusão sem apresentar erros ou falhas.       |
| 31 | Verificar a mensagem apresentada pelo sistema.     | O sistema deve apresentar a mensagem **"Registro excluído com sucesso"**. |
| 32 | Pesquisar/localizar novamente o registro excluído. | O registro não deve mais estar disponível para consulta na rotina.        |

---

## 8. Validação da Inclusão

| Nº | Validação                                     | Resultado Esperado                                                   |
| -: | --------------------------------------------- | -------------------------------------------------------------------- |
| 33 | Confirmar a inclusão com os dados informados. | O registro deve ser gravado corretamente.                            |
| 34 | Verificar a mensagem de sucesso.              | Deve ser apresentada a mensagem **"Registro inserido com sucesso"**. |
| 35 | Localizar o registro após a inclusão.         | O registro deve estar disponível para visualização.                  |

---

## 9. Validação da Alteração

| Nº | Validação                                      | Resultado Esperado                                                   |
| -: | ---------------------------------------------- | -------------------------------------------------------------------- |
| 36 | Alterar a descrição e/ou situação de bloqueio. | O sistema deve permitir a alteração dos dados.                       |
| 37 | Salvar as alterações.                          | O registro deve ser atualizado corretamente.                         |
| 38 | Verificar a mensagem de sucesso.               | Deve ser apresentada a mensagem **"Registro alterado com sucesso"**. |
| 39 | Consultar o registro após a alteração.         | Os dados alterados devem estar persistidos corretamente.             |

---

## 10. Validação da Exclusão

| Nº | Validação                                      | Resultado Esperado                                                   |
| -: | ---------------------------------------------- | -------------------------------------------------------------------- |
| 40 | Selecionar o registro para exclusão.           | O sistema deve apresentar o registro correto.                        |
| 41 | Confirmar a exclusão.                          | O sistema deve excluir o registro corretamente.                      |
| 42 | Verificar a mensagem apresentada.              | Deve ser apresentada a mensagem **"Registro excluído com sucesso"**. |
| 43 | Realizar nova consulta pelo registro excluído. | O registro não deve estar disponível na rotina.                      |

---

## 11. Resultado Esperado

A rotina **ATFA025 – Locais** deve permitir realizar corretamente o ciclo completo de **inclusão, visualização, alteração e exclusão** de um local.

Durante a execução, o sistema deve:

* Permitir o preenchimento dos campos **Código, Descrição, Tipo e Bloqueio**;
* Gravar corretamente o novo local;
* Apresentar a mensagem **"Registro inserido com sucesso"**;
* Permitir localizar e visualizar o registro incluído;
* Apresentar os dados cadastrados de forma íntegra;
* Permitir alterar os dados do local;
* Apresentar a mensagem **"Registro alterado com sucesso"**;
* Persistir corretamente as alterações realizadas;
* Permitir excluir o registro por meio de **Outras Ações → Excluir**;
* Solicitar a confirmação da exclusão;
* Apresentar a mensagem **"Registro excluído com sucesso"**;
* Impedir que o registro excluído permaneça disponível para consulta;
* Executar todas as operações sem apresentar erros, falhas, travamentos ou inconsistências.

## 12. Critério de Aprovação

O caso de teste será considerado **APROVADO** quando:

1. O local for incluído com sucesso;
2. A mensagem de inclusão for apresentada corretamente;
3. O registro puder ser localizado e visualizado;
4. Os dados apresentados corresponderem aos dados informados;
5. O registro puder ser alterado sem erros ou falhas;
6. A mensagem de alteração for apresentada corretamente;
7. Os dados alterados forem persistidos;
8. O registro puder ser excluído mediante confirmação;
9. A mensagem de exclusão for apresentada corretamente;
10. O registro excluído não estiver mais disponível para consulta;
11. Nenhuma operação apresentar erros, falhas, travamentos ou inconsistências que comprometam o funcionamento da rotina.

---

## 13. Status da Execução

**Status:** ☐ Aprovado ☐ Reprovado ☐ Bloqueado

## 14. Evidências

* Evidência da inclusão;
* Evidência da mensagem **"Registro inserido com sucesso"**;
* Evidência da visualização;
* Evidência da alteração;
* Evidência da mensagem **"Registro alterado com sucesso"**;
* Evidência da exclusão;
* Evidência da mensagem **"Registro excluído com sucesso"**.

## 15. Responsável

**Responsável:** __________________________________

## 16. Data de Execução

**Data:** ****/****/________
