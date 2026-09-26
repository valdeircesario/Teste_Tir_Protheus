# CT01_GPEA645 – Inclusão, Visualização, Alteração e Exclusão de Disciplina

## 1. Nome do Caso de Teste

**CT01_GPEA645 – Inclusão, Visualização, Alteração e Exclusão de Disciplina**

## 2. Nome da Rotina

**GPEA645 – Cadastro de Disciplinas**

## 3. Caminho da Rotina

**Protheus → SIGAGPE → Atualizações → Controle Disciplinar → Disciplina**

## 4. Objetivo

Validar as operações de inclusão, visualização, alteração e exclusão de uma Disciplina na rotina **GPEA645**, garantindo que o registro seja criado corretamente, seus dados possam ser consultados e alterados, e que a exclusão seja realizada com sucesso e confirmada posteriormente.

## 5. Passo a Passo

### CREATE – Inclusão de Disciplina

| Nº | Ação                                                          | Resultado Esperado                                                  |
| -: | ------------------------------------------------------------- | ------------------------------------------------------------------- |
| 01 | Acessar o módulo **Gestão de Pessoal**.                       | O módulo é carregado corretamente, sem erros.                       |
| 02 | Acessar **Atualizações → Controle Disciplinar → Disciplina**. | A tela **Cadastro de Disciplinas** é apresentada.                   |
| 03 | Selecionar a opção **Incluir**.                               | A tela **Tipo de Disciplina - INCLUIR** é apresentada.              |
| 04 | Informar o tipo de disciplina **1 - Punição**.                | O tipo de disciplina é preenchido corretamente.                     |
| 05 | Informar a descrição **TESTE DE DISCIPLINA**.                 | A descrição é preenchida corretamente.                              |
| 06 | Confirmar a inclusão do registro.                             | O sistema grava a nova Disciplina.                                  |
| 07 | Validar a mensagem apresentada.                               | O sistema apresenta a mensagem **"Registro inserido com sucesso."** |
| 08 | Fechar a mensagem e retornar à tela de cadastro.              | A tela **Cadastro de Disciplinas** é apresentada novamente.         |

### READ – Visualização da Disciplina

| Nº | Ação                                      | Resultado Esperado                                        |
| -: | ----------------------------------------- | --------------------------------------------------------- |
| 09 | Selecionar a Disciplina recém-cadastrada. | O registro correto é selecionado.                         |
| 10 | Selecionar a opção **Visualizar**.        | A tela **Tipo de Disciplina - VISUALIZAR** é apresentada. |
| 11 | Validar o tipo da Disciplina.             | O campo apresenta **1 - Punição**.                        |
| 12 | Validar o código gerado para o registro.  | O código corresponde ao código gerado durante a inclusão. |
| 13 | Validar a descrição da Disciplina.        | O campo apresenta **TESTE DE DISCIPLINA**.                |
| 14 | Fechar a tela de visualização.            | O sistema retorna à tela **Cadastro de Disciplinas**.     |

### UPDATE – Alteração da Disciplina

| Nº | Ação                                                                       | Resultado Esperado                                                  |
| -: | -------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| 15 | Selecionar a Disciplina cadastrada e acessar **Alterar**.                  | A tela **Tipo de Disciplina - ALTERAR** é apresentada.              |
| 16 | Validar o tipo da Disciplina.                                              | O campo apresenta **1 - Punição**.                                  |
| 17 | Validar o código do registro.                                              | O código corresponde ao registro incluído anteriormente.            |
| 18 | Alterar a descrição de **TESTE DE DISCIPLINA** para **ABANDONO AO POSTO**. | O novo valor é aceito pelo sistema.                                 |
| 19 | Confirmar a alteração.                                                     | O sistema grava a alteração realizada.                              |
| 20 | Validar a mensagem apresentada.                                            | O sistema apresenta a mensagem **"Registro alterado com sucesso."** |
| 21 | Fechar a mensagem e retornar ao cadastro.                                  | A tela **Cadastro de Disciplinas** é apresentada novamente.         |

### DELETE – Exclusão da Disciplina

| Nº | Ação                                                                                           | Resultado Esperado                                                                   |
| -: | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| 22 | Selecionar a Disciplina alterada.                                                              | O registro correto é selecionado.                                                    |
| 23 | Acessar **Outras Ações → Excluir**.                                                            | A tela de confirmação da exclusão é apresentada.                                     |
| 24 | Validar a mensagem **"Tem certeza que deseja excluir o item abaixo?"**.                        | A mensagem de confirmação é apresentada corretamente.                                |
| 25 | Validar a mensagem **"Esta operação não poderá ser desfeita após a confirmação da exclusão"**. | O sistema informa que a operação não poderá ser desfeita após a confirmação.         |
| 26 | Validar os dados apresentados na tela de exclusão.                                             | O tipo **1 - Punição** e o código do registro correspondem à Disciplina selecionada. |
| 27 | Confirmar a exclusão.                                                                          | O sistema realiza a exclusão do registro.                                            |
| 28 | Validar a mensagem apresentada.                                                                | O sistema apresenta a mensagem **"Registro excluido com sucesso."**                  |
| 29 | Fechar a mensagem e retornar ao **Cadastro de Disciplinas**.                                   | O sistema retorna corretamente à tela principal da rotina.                           |

## 6. Validação da Exclusão

| Nº | Ação                                                                                  | Resultado Esperado                                                |
| -: | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| 30 | Pesquisar pelo código da Disciplina excluída utilizando a opção de pesquisa da grade. | O registro excluído não deve mais estar disponível para consulta. |
| 31 | Verificar o resultado da pesquisa.                                                    | A Disciplina excluída não é localizada na grade.                  |

## 7. Validação da Persistência dos Dados

| Nº | Ação                                                                         | Resultado Esperado                                                |
| -: | ---------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| 32 | Durante a visualização após a inclusão, conferir o tipo, código e descrição. | Os dados cadastrados são apresentados corretamente.               |
| 33 | Após a alteração, consultar novamente o registro.                            | A descrição **ABANDONO AO POSTO** permanece gravada corretamente. |
| 34 | Após a exclusão, pesquisar pelo código do registro.                          | O registro não está mais disponível para consulta.                |

## 8. Resultado Esperado

A rotina **GPEA645 – Cadastro de Disciplinas** deve permitir:

* Inclusão de uma nova Disciplina;
* Geração e identificação do código do registro;
* Visualização dos dados cadastrados;
* Alteração das informações permitidas;
* Exclusão do registro mediante confirmação;
* Apresentação das mensagens de sucesso correspondentes;
* Persistência correta dos dados durante o ciclo de vida do registro;
* Remoção efetiva do registro após a exclusão;
* Execução das operações sem erros, falhas ou inconsistências.

## 9. Critério de Aprovação

O caso de teste será considerado **APROVADO** quando as operações de **CREATE, READ, UPDATE e DELETE** forem executadas com sucesso, os dados apresentados forem correspondentes às informações cadastradas e alteradas, as mensagens esperadas forem exibidas e o registro não estiver mais disponível após a exclusão.

---

