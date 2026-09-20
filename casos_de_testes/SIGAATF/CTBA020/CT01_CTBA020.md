
# CT01 – Cadastro de Plano de Contas

## 1. Nome do Caso de Teste

**CT01 – Cadastro de Plano de Contas**

## 1. Módulo

**Ativo Fiscal**

## 3. Nome da Rotina

**Cadastro de Plano de Contas**

## 4. Caminho da Rotina

**Protheus → Atualizações → Cadastros → Plano de Contas**

## 5. Objetivo

Validar o funcionamento da rotina de **Cadastro de Plano de Contas**, verificando o fluxo completo de **inclusão, visualização, alteração e exclusão** de uma conta, garantindo que os dados sejam gravados, consultados, atualizados e excluídos corretamente, sem apresentar erros, falhas, travamentos ou impedimentos durante a execução.

## 6. Cenário de Teste

Realizar o ciclo completo de manutenção de um plano de contas:

* Incluir uma nova conta;
* Informar os dados necessários para o cadastro;
* Salvar e validar a mensagem de sucesso;
* Localizar e visualizar a conta incluída;
* Validar os dados cadastrados;
* Alterar um dos dados da conta;
* Salvar e validar a mensagem de alteração;
* Excluir a conta após a alteração;
* Confirmar a exclusão;
* Validar a mensagem de exclusão;
* Confirmar que o fluxo foi executado sem erros ou falhas.

---

## 7. Passo a Passo

### 7.1 CREATE – Inclusão de Plano de Contas

| Nº | Ação                                                         | Resultado Esperado                                                        |
| -: | ------------------------------------------------------------ | ------------------------------------------------------------------------- |
| 01 | Acessar a rotina **Cadastro de Plano de Contas**.            | A rotina deve ser carregada corretamente, sem apresentar erros.           |
| 02 | Clicar na opção **Incluir**.                                 | O sistema deve apresentar a tela de inclusão de uma nova conta.           |
| 03 | Informar o **Código da Conta**.                              | O sistema deve permitir o preenchimento do código.                        |
| 04 | Informar a **Descrição** da conta.                           | O sistema deve permitir o preenchimento da descrição.                     |
| 05 | Informar a **Classe da Conta**.                              | O sistema deve permitir o preenchimento/seleção da classe da conta.       |
| 06 | Informar se a conta é **Sintética ou Analítica**.            | O sistema deve permitir selecionar o tipo correspondente.                 |
| 07 | Informar a **Condição Normal** como **Credora ou Devedora**. | O sistema deve permitir selecionar a condição normal da conta.            |
| 08 | Conferir todos os dados informados.                          | Os dados devem permanecer preenchidos corretamente antes da gravação.     |
| 09 | Clicar em **Salvar/Confirmar**.                              | O sistema deve processar a inclusão sem apresentar erros ou falhas.       |
| 10 | Verificar a mensagem apresentada pelo sistema.               | O sistema deve apresentar a mensagem **"Registro inserido com sucesso"**. |

---

### 7.2 READ – Visualização da Conta

| Nº | Ação                                          | Resultado Esperado                                                                   |
| -: | --------------------------------------------- | ------------------------------------------------------------------------------------ |
| 11 | Localizar a conta recém-incluída na listagem. | A conta cadastrada deve ser localizada corretamente.                                 |
| 12 | Selecionar a conta incluída.                  | O registro correto deve ficar selecionado.                                           |
| 13 | Acessar **Outras Ações → Visualizar**.        | O sistema deve abrir a tela de visualização da conta.                                |
| 14 | Validar o **Código da Conta**.                | O código apresentado deve corresponder ao informado na inclusão.                     |
| 15 | Validar a **Descrição**.                      | A descrição apresentada deve corresponder ao valor informado.                        |
| 16 | Validar a **Classe da Conta**.                | A classe apresentada deve corresponder ao valor informado.                           |
| 17 | Validar o tipo **Sintética ou Analítica**.    | O tipo apresentado deve corresponder à opção selecionada na inclusão.                |
| 18 | Validar a **Condição Normal**.                | A condição apresentada deve corresponder à opção informada: **Credora ou Devedora**. |
| 19 | Conferir os demais dados apresentados.        | Os dados devem estar íntegros e consistentes com o cadastro realizado.               |
| 20 | Sair da tela de visualização.                 | O sistema deve retornar à listagem da rotina sem apresentar erros ou falhas.         |

---

### 7.3 UPDATE – Alteração do Plano de Contas

| Nº | Ação                                                    | Resultado Esperado                                                        |
| -: | ------------------------------------------------------- | ------------------------------------------------------------------------- |
| 21 | Selecionar novamente a conta incluída.                  | O registro correto deve ser selecionado.                                  |
| 22 | Acessar a opção de **Alterar**.                         | O sistema deve abrir a conta para edição.                                 |
| 23 | Alterar um dos campos permitidos, como a **Descrição**. | O sistema deve permitir a alteração do campo selecionado.                 |
| 24 | Conferir o dado alterado antes de salvar.               | O novo valor deve estar apresentado corretamente.                         |
| 25 | Clicar em **Salvar/Confirmar**.                         | O sistema deve processar a alteração sem apresentar erros ou falhas.      |
| 26 | Verificar a mensagem apresentada.                       | O sistema deve apresentar a mensagem **"Registro alterado com sucesso"**. |
| 27 | Localizar novamente a conta alterada.                   | A conta deve permanecer disponível na listagem.                           |
| 28 | Visualizar a conta novamente.                           | O sistema deve apresentar os dados atualizados.                           |
| 29 | Validar o campo alterado.                               | O campo deve apresentar o novo valor informado durante a alteração.       |

---

### 7.4 DELETE – Exclusão do Plano de Contas

| Nº | Ação                                          | Resultado Esperado                                                        |
| -: | --------------------------------------------- | ------------------------------------------------------------------------- |
| 30 | Selecionar a conta alterada.                  | O registro correto deve ser selecionado.                                  |
| 31 | Acessar **Outras Ações → Excluir**.           | O sistema deve apresentar a tela ou mensagem de confirmação da exclusão.  |
| 32 | Conferir os dados da conta que será excluída. | Os dados apresentados devem corresponder à conta selecionada.             |
| 33 | Clicar em **Confirmar**.                      | O sistema deve processar a exclusão sem apresentar erros ou falhas.       |
| 34 | Verificar a mensagem apresentada.             | O sistema deve apresentar a mensagem **"Registro excluído com sucesso"**. |
| 35 | Pesquisar novamente a conta excluída.         | O registro não deve mais estar disponível para consulta na rotina.        |

---

## 8. Validação da Inclusão

| Nº | Validação                                              | Resultado Esperado                                                   |
| -: | ------------------------------------------------------ | -------------------------------------------------------------------- |
| 36 | Confirmar a gravação da conta com os dados informados. | A conta deve ser registrada corretamente.                            |
| 37 | Verificar a mensagem de inclusão.                      | Deve ser apresentada a mensagem **"Registro inserido com sucesso"**. |
| 38 | Localizar a conta cadastrada.                          | A conta deve estar disponível para consulta.                         |
| 39 | Visualizar os dados cadastrados.                       | Os dados devem corresponder às informações utilizadas na inclusão.   |

---

## 9. Validação da Alteração

| Nº | Validação                                  | Resultado Esperado                                                   |
| -: | ------------------------------------------ | -------------------------------------------------------------------- |
| 40 | Alterar um dos campos permitidos da conta. | O sistema deve permitir a alteração.                                 |
| 41 | Salvar a alteração realizada.              | A alteração deve ser gravada corretamente.                           |
| 42 | Verificar a mensagem apresentada.          | Deve ser apresentada a mensagem **"Registro alterado com sucesso"**. |
| 43 | Consultar novamente a conta.               | O registro deve apresentar os dados atualizados.                     |

---

## 10. Validação da Exclusão

| Nº | Validação                                   | Resultado Esperado                                                   |
| -: | ------------------------------------------- | -------------------------------------------------------------------- |
| 44 | Selecionar a conta que será excluída.       | O registro correto deve ser selecionado.                             |
| 45 | Acessar **Outras Ações → Excluir**.         | O sistema deve apresentar a confirmação da exclusão.                 |
| 46 | Conferir os dados da conta.                 | Os dados devem corresponder ao registro selecionado.                 |
| 47 | Confirmar a exclusão.                       | O sistema deve excluir o registro corretamente.                      |
| 48 | Verificar a mensagem apresentada.           | Deve ser apresentada a mensagem **"Registro excluído com sucesso"**. |
| 49 | Realizar nova pesquisa pela conta excluída. | A conta não deve mais estar disponível para consulta.                |

---

## 11. Resultado Esperado

A rotina **Cadastro de Plano de Contas** deve permitir realizar corretamente o fluxo completo de **inclusão, visualização, alteração e exclusão** de uma conta.

O sistema deve permitir:

* Informar o **Código da Conta**;
* Informar a **Descrição**;
* Informar a **Classe da Conta**;
* Definir a conta como **Sintética ou Analítica**;
* Definir a **Condição Normal** como **Credora ou Devedora**;
* Salvar a conta sem apresentar erros ou falhas;
* Apresentar a mensagem **"Registro inserido com sucesso"**;
* Localizar e visualizar a conta cadastrada;
* Validar os dados apresentados na visualização;
* Alterar os dados permitidos;
* Apresentar a mensagem **"Registro alterado com sucesso"**;
* Persistir corretamente os dados alterados;
* Excluir a conta por meio de **Outras Ações → Excluir**;
* Permitir conferir os dados antes da exclusão;
* Confirmar a exclusão;
* Apresentar a mensagem **"Registro excluído com sucesso"**;
* Não disponibilizar o registro após sua exclusão.

Todo o fluxo deve ser executado sem **erros, falhas, travamentos, inconsistências ou impedimentos** que comprometam o funcionamento da rotina.

## 12. Critério de Aprovação

O caso de teste será considerado **APROVADO** quando:

1. A conta puder ser incluída com sucesso;
2. A mensagem de inclusão for apresentada corretamente;
3. A conta puder ser localizada e visualizada;
4. Os dados visualizados corresponderem aos dados cadastrados;
5. A conta puder ser alterada;
6. A mensagem de alteração for apresentada corretamente;
7. Os dados alterados forem persistidos;
8. A conta puder ser excluída mediante confirmação;
9. A mensagem de exclusão for apresentada corretamente;
10. A conta excluída não estiver mais disponível para consulta;
11. Todas as operações forem executadas sem erros ou falhas.

---

## 13. Status da Execução

**Status:** ☐ Aprovado ☐ Reprovado ☐ Bloqueado

## 14. Evidências

* Evidência da inclusão;
* Evidência da mensagem **"Registro inserido com sucesso"**;
* Evidência da visualização e dos dados cadastrados;
* Evidência da alteração;
* Evidência da mensagem **"Registro alterado com sucesso"**;
* Evidência da exclusão;
* Evidência da mensagem **"Registro excluído com sucesso"**.

