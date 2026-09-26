# CT01_GPEA340 – CRUD de Sindicatos

## 1. Nome do Caso de Teste

**CT01_GPEA340 – Inclusão, Visualização, Alteração e Exclusão de Sindicato**

## 2. Nome da Rotina

**GPEA340 – Cadastro de Sindicatos**

## 3. Caminho da Rotina

**Protheus → SIGAGPE → Atualizações → Cadastros → Sindicatos**

## 4. Objetivo

Validar o funcionamento da rotina **GPEA340 – Cadastro de Sindicatos**, realizando o fluxo completo de **inclusão, visualização, alteração e exclusão** de um sindicato.

O teste deve garantir que o sistema permita cadastrar um sindicato com os dados necessários, visualizar e validar as informações cadastradas, alterar dados do registro, confirmar a alteração e posteriormente excluir o sindicato, garantindo a correta persistência e remoção dos dados sem apresentar erros, falhas ou inconsistências.

## 5. Cenário de Teste

Realizar o ciclo completo de manutenção de um Sindicato:

* Incluir um novo sindicato;
* Informar os dados necessários no formulário;
* Confirmar a inclusão;
* Validar a mensagem de sucesso;
* Localizar e visualizar o sindicato cadastrado;
* Validar os dados informados;
* Alterar uma informação permitida;
* Confirmar a alteração;
* Validar a mensagem de alteração;
* Validar os dados após a alteração;
* Excluir o sindicato;
* Confirmar a exclusão;
* Validar a mensagem de exclusão;
* Verificar se o registro foi efetivamente removido.

---

# 6. Passo a Passo

## CREATE – Inclusão de Sindicato

| Nº | Ação                                                    | Resultado Esperado                                                            |
| -: | ------------------------------------------------------- | ----------------------------------------------------------------------------- |
| 01 | Acessar a rotina **GPEA340 – Cadastro de Sindicatos**.  | A rotina deve ser apresentada corretamente, sem erros ou falhas.              |
| 02 | Clicar na opção **Incluir**.                            | O sistema deve abrir o formulário para cadastro de um novo sindicato.         |
| 03 | Informar o **Código** do sindicato.                     | O sistema deve permitir o preenchimento do código.                            |
| 04 | Informar a **Descrição** do sindicato.                  | O sistema deve permitir o preenchimento da descrição.                         |
| 05 | Informar o **CNPJ**.                                    | O sistema deve permitir o preenchimento do CNPJ conforme as regras da rotina. |
| 06 | Informar o **Endereço**.                                | O sistema deve permitir o preenchimento do endereço.                          |
| 07 | Informar o **CEP**.                                     | O sistema deve permitir o preenchimento do CEP.                               |
| 08 | Preencher os demais campos necessários para o cadastro. | O sistema deve permitir o preenchimento das informações válidas.              |
| 09 | Conferir todos os dados informados.                     | Os dados devem estar apresentados corretamente antes da confirmação.          |
| 10 | Clicar em **Confirmar**.                                | O sistema deve processar a inclusão sem apresentar erros ou falhas.           |
| 11 | Verificar a mensagem apresentada.                       | O sistema deve apresentar a mensagem **"Registro inserido com sucesso"**.     |

---

## READ – Visualização do Sindicato

| Nº | Ação                                              | Resultado Esperado                                                               |
| -: | ------------------------------------------------- | -------------------------------------------------------------------------------- |
| 12 | Localizar o sindicato recém-incluído na listagem. | O registro deve ser localizado corretamente.                                     |
| 13 | Selecionar o sindicato cadastrado.                | O registro correto deve ficar selecionado.                                       |
| 14 | Acessar a opção de **Visualizar**.                | O sistema deve abrir o cadastro do sindicato.                                    |
| 15 | Validar o **Código**.                             | O código apresentado deve corresponder ao informado durante a inclusão.          |
| 16 | Validar a **Descrição**.                          | A descrição apresentada deve corresponder ao valor informado.                    |
| 17 | Validar o **CNPJ**.                               | O CNPJ apresentado deve corresponder ao informado durante a inclusão.            |
| 18 | Validar o **Endereço**.                           | O endereço apresentado deve corresponder ao informado.                           |
| 19 | Validar o **CEP**.                                | O CEP apresentado deve corresponder ao informado.                                |
| 20 | Validar os demais dados cadastrados.              | As informações apresentadas devem corresponder aos dados utilizados na inclusão. |
| 21 | Sair da tela de visualização.                     | O sistema deve retornar à listagem sem apresentar erros ou falhas.               |

---

## UPDATE – Alteração do Sindicato

| Nº | Ação                                           | Resultado Esperado                                                        |
| -: | ---------------------------------------------- | ------------------------------------------------------------------------- |
| 22 | Localizar e selecionar o sindicato incluído.   | O sistema deve selecionar corretamente o registro.                        |
| 23 | Clicar na opção **Alterar**.                   | O sistema deve abrir o cadastro para edição.                              |
| 24 | Alterar uma informação permitida do sindicato. | O sistema deve permitir a alteração do campo selecionado.                 |
| 25 | Conferir os dados após a alteração.            | O novo valor deve ser apresentado corretamente.                           |
| 26 | Clicar em **Confirmar**.                       | O sistema deve processar a alteração sem apresentar erros ou falhas.      |
| 27 | Verificar a mensagem apresentada.              | O sistema deve apresentar a mensagem **"Registro alterado com sucesso"**. |
| 28 | Localizar novamente o sindicato alterado.      | O registro deve permanecer disponível na listagem.                        |
| 29 | Visualizar o sindicato alterado.               | O sistema deve apresentar os dados atualizados.                           |
| 30 | Validar o campo que foi alterado.              | O valor apresentado deve corresponder à alteração realizada.              |

---

## DELETE – Exclusão do Sindicato

| Nº | Ação                                              | Resultado Esperado                                                        |
| -: | ------------------------------------------------- | ------------------------------------------------------------------------- |
| 31 | Localizar e selecionar o sindicato alterado.      | O registro correto deve ser selecionado.                                  |
| 32 | Acessar **Outras Ações → Excluir**.               | O sistema deve abrir a tela ou mensagem de confirmação da exclusão.       |
| 33 | Conferir os dados do sindicato que será excluído. | Os dados apresentados devem corresponder ao registro selecionado.         |
| 34 | Confirmar a exclusão do registro.                 | O sistema deve processar a exclusão sem apresentar erros ou falhas.       |
| 35 | Verificar a mensagem apresentada.                 | O sistema deve apresentar a mensagem **"Registro excluído com sucesso"**. |
| 36 | Pesquisar novamente pelo sindicato excluído.      | O registro excluído não deve mais estar disponível para consulta.         |

---

# 7. Validação da Persistência dos Dados

| Nº | Ação                                                                | Resultado Esperado                                            |
| -: | ------------------------------------------------------------------- | ------------------------------------------------------------- |
| 37 | Após a inclusão, sair da tela do cadastro.                          | O sistema deve retornar à tela anterior sem apresentar erros. |
| 38 | Pesquisar novamente o sindicato utilizando sua identificação.       | O registro deve ser localizado corretamente.                  |
| 39 | Visualizar o sindicato localizado.                                  | O sistema deve apresentar os dados cadastrados anteriormente. |
| 40 | Comparar os dados apresentados com os dados utilizados na inclusão. | As informações devem permanecer consistentes.                 |
| 41 | Após a alteração, realizar nova consulta do sindicato.              | O registro deve ser localizado corretamente.                  |
| 42 | Visualizar o sindicato após a alteração.                            | O sistema deve apresentar os dados atualizados.               |
| 43 | Comparar o campo alterado com o novo valor informado.               | A alteração deve permanecer corretamente persistida.          |

---

# 8. Validação da Exclusão

| Nº | Ação                                            | Resultado Esperado                                                            |
| -: | ----------------------------------------------- | ----------------------------------------------------------------------------- |
| 44 | Selecionar o sindicato para exclusão.           | O registro correto deve ser selecionado.                                      |
| 45 | Acessar **Outras Ações → Excluir**.             | O sistema deve apresentar a confirmação da exclusão.                          |
| 46 | Conferir os dados antes da confirmação.         | Os dados devem corresponder ao sindicato selecionado.                         |
| 47 | Confirmar a exclusão.                           | O sistema deve excluir o registro corretamente.                               |
| 48 | Verificar a mensagem apresentada.               | O sistema deve apresentar a mensagem **"Registro excluído com sucesso"**.     |
| 49 | Realizar nova pesquisa pelo sindicato excluído. | O registro não deve mais estar disponível para consulta.                      |
| 50 | Validar a situação final do cadastro.           | O sistema deve confirmar que o sindicato foi efetivamente removido da rotina. |

---

# 9. Resultado Esperado

A rotina **GPEA340 – Cadastro de Sindicatos** deve permitir realizar corretamente o fluxo completo de **inclusão, visualização, alteração e exclusão** de um sindicato.

O sistema deve:

* Permitir acessar a rotina GPEA340;
* Permitir incluir um novo sindicato;
* Permitir informar **Código, Descrição, CNPJ, Endereço, CEP** e demais informações necessárias;
* Permitir confirmar a inclusão;
* Apresentar a mensagem **"Registro inserido com sucesso"**;
* Permitir localizar e visualizar o sindicato cadastrado;
* Apresentar corretamente os dados informados durante a inclusão;
* Permitir alterar informações do sindicato;
* Permitir confirmar as alterações;
* Apresentar a mensagem **"Registro alterado com sucesso"**;
* Persistir corretamente os dados alterados;
* Permitir acessar **Outras Ações → Excluir**;
* Apresentar os dados do sindicato antes da exclusão;
* Permitir confirmar a exclusão;
* Apresentar a mensagem **"Registro excluído com sucesso"**;
* Não disponibilizar o registro após sua exclusão.

Todo o fluxo deve ser executado sem **erros, falhas, travamentos, inconsistências ou impedimentos** que comprometam o funcionamento da rotina.

# 10. Critério de Aprovação

O caso de teste será considerado **APROVADO** quando:

1. O sindicato puder ser incluído corretamente;
2. O sistema apresentar a mensagem **"Registro inserido com sucesso"**;
3. O registro puder ser localizado e visualizado;
4. Os dados apresentados corresponderem aos dados cadastrados;
5. O sindicato puder ser alterado;
6. O sistema apresentar a mensagem **"Registro alterado com sucesso"**;
7. Os dados alterados permanecerem corretamente persistidos;
8. O sindicato puder ser excluído mediante confirmação;
9. O sistema apresentar a mensagem **"Registro excluído com sucesso"**;
10. O registro excluído não estiver mais disponível para consulta;
11. Todo o fluxo de **CREATE, READ, UPDATE e DELETE** for executado sem erros, falhas ou impedimentos.

**Status:** `A definir durante a execução`

**Evidências:** `A anexar durante a execução`

**Responsável:** `A definir`

**Data de Execução:** `A definir`
