# CT01_PONA160 – Inclusão, Visualização, Alteração e Exclusão de Turno de Trabalho

## 1. Nome do Caso de Teste

**CT01_PONA160 – Inclusão, Visualização, Alteração e Exclusão de Turno de Trabalho**

## 2. Nome da Rotina

**PONA160 – Turnos de Trabalho**

## 3. Caminho da Rotina

**Protheus → SIGAGPE → Atualizações → Ponto Eletrônico → Turnos de Trabalho**

## 4. Objetivo

Validar o cadastro de um Turno de Trabalho na rotina **PONA160**, contemplando as operações de inclusão, visualização, alteração e exclusão, garantindo que os dados sejam registrados corretamente, possam ser consultados e alterados e que o registro seja removido mediante confirmação.

## 5. Passo a Passo

### CREATE – Inclusão do Turno de Trabalho

| Nº | Ação                                                              | Resultado Esperado                                               |
| -: | ----------------------------------------------------------------- | ---------------------------------------------------------------- |
| 01 | Acessar o módulo **Gestão de Pessoal**.                           | O módulo é carregado corretamente, sem erros.                    |
| 02 | Acessar **Atualizações → Ponto Eletrônico → Turnos de Trabalho**. | A tela **Turnos de Trabalho** é apresentada.                     |
| 03 | Selecionar a opção **Incluir**.                                   | A tela **Turnos de Trabalho - INCLUIR** é apresentada.           |
| 04 | Informar o código do turno **03** no campo correspondente.        | O código do turno é aceito pelo sistema.                         |
| 05 | Informar a descrição **MEIO PERIODO**.                            | A descrição é preenchida corretamente.                           |
| 06 | Acessar a aba **Informações Ponto**.                              | Os campos relacionados às informações de ponto são apresentados. |
| 07 | Informar o tipo de jornada **09**.                                | O tipo de jornada é aceito pelo sistema.                         |
| 08 | Informar a descrição do tipo de jornada **TESTE**.                | A descrição é preenchida corretamente.                           |
| 09 | Retornar à aba **Gerais**.                                        | A tela retorna às informações gerais do turno.                   |
| 10 | Selecionar **Salvar**.                                            | O sistema grava o Turno de Trabalho informado.                   |
| 11 | Cancelar/encerrar a tela de inclusão conforme o fluxo da rotina.  | O sistema retorna à tela **Turnos de Trabalho**.                 |

### READ – Visualização do Turno de Trabalho

| Nº | Ação                                                | Resultado Esperado                                                                |
| -: | --------------------------------------------------- | --------------------------------------------------------------------------------- |
| 12 | Selecionar o Turno de Trabalho cadastrado.          | O registro correspondente ao turno **03** é selecionado.                          |
| 13 | Selecionar a opção **Visualizar**.                  | A tela **Turnos de Trabalho - VISUALIZAR** é apresentada.                         |
| 14 | Validar o código do turno.                          | O campo apresenta o código **03**.                                                |
| 15 | Validar a descrição do turno.                       | O campo apresenta **MEIO PERIODO**.                                               |
| 16 | Conferir as demais informações cadastradas.         | Os dados apresentados correspondem às informações registradas durante a inclusão. |
| 17 | Selecionar **Cancelar** para fechar a visualização. | O sistema retorna à tela **Turnos de Trabalho**.                                  |

### UPDATE – Alteração do Turno de Trabalho

| Nº | Ação                                                                   | Resultado Esperado                                              |
| -: | ---------------------------------------------------------------------- | --------------------------------------------------------------- |
| 18 | Selecionar o Turno de Trabalho cadastrado.                             | O registro correto é selecionado.                               |
| 19 | Selecionar a opção **Alterar**.                                        | A tela **Turnos de Trabalho - ALTERAR** é apresentada.          |
| 20 | Alterar a descrição de **MEIO PERIODO** para **MEIO PERIODO EDITADO**. | O novo valor é aceito pelo sistema.                             |
| 21 | Selecionar **Salvar**.                                                 | O sistema grava a alteração realizada.                          |
| 22 | Retornar à tela **Turnos de Trabalho**.                                | O sistema retorna corretamente à listagem dos turnos.           |
| 23 | Consultar o registro alterado.                                         | O turno é apresentado com a descrição **MEIO PERIODO EDITADO**. |

### DELETE – Exclusão do Turno de Trabalho

| Nº | Ação                                                         | Resultado Esperado                                    |
| -: | ------------------------------------------------------------ | ----------------------------------------------------- |
| 24 | Selecionar o Turno de Trabalho cadastrado.                   | O registro correto é selecionado.                     |
| 25 | Acessar **Outras Ações → Excluir**.                          | O sistema apresenta a confirmação de exclusão.        |
| 26 | Validar a mensagem **"Confirma a exclusão do Turno?"**.      | A mensagem de confirmação é apresentada corretamente. |
| 27 | Selecionar **Sim**.                                          | O sistema confirma a solicitação de exclusão.         |
| 28 | Aguardar a apresentação da mensagem **"Deseja gerar Log?"**. | A solicitação de geração de log é apresentada.        |
| 29 | Selecionar **Não**.                                          | O sistema prossegue sem gerar o log.                  |
| 30 | Selecionar **Confirmar**.                                    | A operação de exclusão é concluída.                   |
| 31 | Retornar à tela **Turnos de Trabalho**.                      | O sistema retorna corretamente à rotina.              |

## 6. Validação dos Dados

| Nº | Ação                                                   | Resultado Esperado                                                                      |
| -: | ------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| 32 | Consultar o turno após a inclusão.                     | O código **03** e a descrição **MEIO PERIODO** são apresentados corretamente.           |
| 33 | Consultar o turno após a alteração.                    | A descrição apresenta **MEIO PERIODO EDITADO**.                                         |
| 34 | Verificar as informações da aba **Informações Ponto**. | O tipo de jornada **09** e a descrição **TESTE** são apresentados conforme cadastrados. |

## 7. Validação da Exclusão

| Nº | Ação                                                               | Resultado Esperado                                                   |
| -: | ------------------------------------------------------------------ | -------------------------------------------------------------------- |
| 35 | Após a exclusão, pesquisar o Turno de Trabalho pelo código **03**. | O registro excluído não deve mais estar disponível para consulta.    |
| 36 | Verificar a listagem de Turnos de Trabalho.                        | O registro excluído não é apresentado como registro ativo na rotina. |

## 8. Resultado Esperado

A rotina **PONA160 – Turnos de Trabalho** deve permitir:

* Inclusão de um novo Turno de Trabalho;
* Cadastro do código **03**;
* Cadastro da descrição **MEIO PERIODO**;
* Preenchimento das informações da aba **Informações Ponto**;
* Cadastro do tipo de jornada **09**;
* Cadastro da descrição do tipo de jornada **TESTE**;
* Visualização dos dados cadastrados;
* Alteração da descrição para **MEIO PERIODO EDITADO**;
* Exclusão do Turno de Trabalho mediante confirmação;
* Tratamento da opção de geração de log;
* Remoção do registro após a confirmação da exclusão;
* Execução das operações sem erros, falhas ou inconsistências.

## 9. Critério de Aprovação

O caso de teste será considerado **APROVADO** quando o Turno de Trabalho **03 – MEIO PERIODO** puder ser incluído e visualizado corretamente, sua descrição puder ser alterada para **MEIO PERIODO EDITADO**, e o registro puder ser excluído mediante confirmação, não permanecendo disponível para consulta após a exclusão.

---

