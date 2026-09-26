# CT01_GPEA370 – Inclusão, Visualização e Alteração de Cargos

## 1. Nome do Caso de Teste

**CT01_GPEA370 – Inclusão, Visualização e Alteração de Cargos**

## 2. Nome da Rotina

**GPEA370 – Cadastro de Cargos**

## 3. Caminho da Rotina

**Protheus → SIGAGPE → Atualizações → Cadastros → Cargos**

## 4. Objetivo

Validar a inclusão, visualização e alteração de um Cargo na rotina **GPEA370**, garantindo que os dados sejam registrados corretamente, permaneçam persistidos após a gravação e possam ser alterados conforme permitido pela rotina.

## 5. Passo a Passo

### CREATE – Inclusão de Cargo

| Nº | Ação                                                                           | Resultado Esperado                                                  |
| -: | ------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| 01 | Acessar a rotina **GPEA370 – Cargos** pelo caminho informado.                  | A rotina é carregada corretamente, sem erros.                       |
| 02 | Selecionar a opção **Incluir**.                                                | O formulário de cadastro de Cargo é apresentado.                    |
| 03 | Preencher os campos obrigatórios do Cargo e as demais informações necessárias. | Os dados são aceitos pelo sistema sem inconsistências.              |
| 04 | Confirmar a inclusão do registro.                                              | O sistema realiza a gravação do Cargo com sucesso.                  |
| 05 | Validar a mensagem apresentada após a gravação.                                | O sistema apresenta a mensagem **"Registro inserido com sucesso"**. |

### READ – Visualização do Cargo

| Nº | Ação                                                      | Resultado Esperado                                                                |
| -: | --------------------------------------------------------- | --------------------------------------------------------------------------------- |
| 06 | Localizar o Cargo recém-cadastrado na listagem da rotina. | O registro incluído é localizado corretamente.                                    |
| 07 | Selecionar o Cargo e acessar a opção **Visualizar**.      | A tela de visualização do registro é apresentada.                                 |
| 08 | Conferir as informações cadastradas.                      | Os dados apresentados correspondem às informações registradas durante a inclusão. |

### UPDATE – Alteração de Cargo

| Nº | Ação                                                         | Resultado Esperado                                                  |
| -: | ------------------------------------------------------------ | ------------------------------------------------------------------- |
| 09 | Selecionar o Cargo cadastrado e acessar a opção **Alterar**. | O formulário do Cargo é aberto para edição.                         |
| 10 | Alterar uma ou mais informações permitidas pela rotina.      | Os novos valores são aceitos pelo sistema.                          |
| 11 | Confirmar a alteração do registro.                           | O sistema grava as alterações realizadas.                           |
| 12 | Validar a mensagem apresentada após a gravação.              | O sistema apresenta a mensagem **"Registro alterado com sucesso"**. |
| 13 | Acessar novamente a visualização do Cargo alterado.          | O registro é apresentado com os dados atualizados.                  |
| 14 | Conferir os campos modificados.                              | Os valores alterados permanecem corretamente persistidos.           |

## 6. Validação de Campos Obrigatórios

| Nº | Ação                                                              | Resultado Esperado                                                                                |
| -: | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| 15 | Tentar realizar a inclusão sem preencher os campos obrigatórios.  | O sistema impede a gravação e apresenta a validação correspondente aos campos obrigatórios.       |
| 16 | Preencher os campos obrigatórios e realizar novamente a inclusão. | O sistema permite a gravação do Cargo quando os campos necessários estão devidamente preenchidos. |

## 7. Validação da Persistência dos Dados

| Nº | Ação                                                   | Resultado Esperado                                                           |
| -: | ------------------------------------------------------ | ---------------------------------------------------------------------------- |
| 17 | Após a inclusão, sair da rotina e acessá-la novamente. | A rotina é carregada normalmente.                                            |
| 18 | Localizar o Cargo cadastrado.                          | O registro permanece disponível na base de dados.                            |
| 19 | Visualizar o Cargo.                                    | Todos os dados cadastrados são apresentados corretamente.                    |
| 20 | Verificar os campos alterados no processo de UPDATE.   | As alterações permanecem salvas e consistentes após novo acesso ao registro. |

## 8. Resultado Esperado

A rotina **GPEA370 – Cargos** deve permitir:

* Inclusão de um novo Cargo;
* Validação dos campos obrigatórios;
* Gravação correta das informações;
* Visualização dos dados cadastrados;
* Alteração das informações permitidas;
* Persistência dos dados após a gravação;
* Apresentação das mensagens de sucesso correspondentes;
* Execução das operações sem erros, falhas, travamentos ou inconsistências.

## 9. Critério de Aprovação

O caso de teste será considerado **APROVADO** quando as operações de **CREATE, READ e UPDATE** forem executadas conforme o fluxo esperado, os dados forem corretamente persistidos e as mensagens de sucesso forem apresentadas sem ocorrência de erros ou inconsistências.

---


