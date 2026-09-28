# CT02_GPEM020_VTR – Cálculo por Roteiro VTR

## 1. Nome do Caso de Teste

**CT02_GPEM020_VTR – Cálculo por Roteiro VTR**

## 2. Nome da Rotina

**GPEM020 – Cálculo por Roteiros**

## 3. Caminho da Rotina

**Protheus → SIGAGPE → Miscelânea → Cálculos → Por Roteiros**

## 4. Objetivo

Validar a execução do processo de cálculo utilizando o roteiro **VTR** na rotina **GPEM020**, garantindo que os parâmetros do processo sejam informados e confirmados corretamente, que o sistema permita iniciar o cálculo e que o processamento seja concluído com a apresentação do respectivo log de ocorrências.

## 5. Passo a Passo

### PARAMETRIZAÇÃO – Processo de Cálculo

| Nº | Ação                                                                                                  | Resultado Esperado                                                        |
| -: | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| 01 | Acessar o módulo **Gestão de Pessoal**.                                                               | O módulo é carregado corretamente, sem erros.                             |
| 02 | Acessar **Miscelânea → Cálculos → Por Roteiros**.                                                     | A rotina **Processo de Cálculo** é apresentada.                           |
| 03 | Caso seja apresentada a mensagem **"Este ambiente utiliza base de Homologação."**, fechar a mensagem. | A mensagem é fechada e o sistema permanece na rotina.                     |
| 04 | Caso seja apresentada a tela **Moedas**, validar o valor do campo **Dolar**.                          | O valor apresentado é **0,0000**.                                         |
| 05 | Confirmar a tela de Moedas.                                                                           | O sistema prossegue para o processo de cálculo.                           |
| 06 | Aguardar a apresentação da tela **Processo de Cálculo**.                                              | A tela é apresentada corretamente.                                        |
| 07 | Validar a mensagem **"Este programa realiza processos de calculos"**.                                 | A mensagem informativa é apresentada corretamente.                        |
| 08 | Selecionar a opção **Parâmetros**.                                                                    | A tela de parametrização é apresentada.                                   |
| 09 | Informar o **Processo = 00001**.                                                                      | O processo informado é aceito pelo sistema.                               |
| 10 | Informar o **Roteiro = VTR**.                                                                         | O roteiro VTR é aceito pelo sistema.                                      |
| 11 | Selecionar **OK** para confirmar os parâmetros.                                                       | O sistema processa os parâmetros informados.                              |
| 12 | Aguardar a apresentação da tela **Parâmetros**.                                                       | A tela de parâmetros é apresentada corretamente.                          |
| 13 | Confirmar os parâmetros selecionando **OK**.                                                          | Os parâmetros são confirmados e o sistema retorna ao processo de cálculo. |

### PROCESSAMENTO – Cálculo do Roteiro VTR

| Nº | Ação                                                                             | Resultado Esperado                                                         |
| -: | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| 14 | Selecionar a opção **Calcular**.                                                 | O sistema inicia a preparação do cálculo utilizando o roteiro VTR.         |
| 15 | Aguardar a apresentação da mensagem **"Confirma configuração dos parametros?"**. | A mensagem de confirmação é apresentada.                                   |
| 16 | Selecionar **Sim**.                                                              | O sistema confirma a configuração dos parâmetros e inicia o processamento. |
| 17 | Aguardar a execução do cálculo.                                                  | O sistema realiza o processamento sem erros ou travamentos.                |
| 18 | Aguardar a apresentação do **Log de Ocorrências no Processo de Cálculo**.        | O log de ocorrências é apresentado após o processamento.                   |
| 19 | Validar a apresentação do log de ocorrências.                                    | O sistema apresenta as ocorrências geradas durante o processo de cálculo.  |
| 20 | Selecionar **OK** no log de ocorrências.                                         | O log é fechado e o sistema prossegue normalmente.                         |
| 21 | Aguardar a conclusão do processamento.                                           | O sistema conclui o processo sem apresentar falhas.                        |
| 22 | Selecionar **Sair**.                                                             | O sistema encerra a operação e retorna corretamente da rotina.             |

## 6. Validação dos Parâmetros

| Nº | Ação                                            | Resultado Esperado                                                  |
| -: | ----------------------------------------------- | ------------------------------------------------------------------- |
| 23 | Verificar o processo utilizado no cálculo.      | O processo corresponde ao **00001**.                                |
| 24 | Verificar o roteiro utilizado no cálculo.       | O roteiro corresponde ao **VTR**.                                   |
| 25 | Confirmar os parâmetros antes do processamento. | O sistema mantém os parâmetros informados para execução do cálculo. |

## 7. Validação do Processamento

| Nº | Ação                                                                       | Resultado Esperado                                                        |
| -: | -------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| 26 | Iniciar o cálculo após a confirmação dos parâmetros.                       | O sistema inicia o processamento do roteiro VTR.                          |
| 27 | Aguardar o processamento.                                                  | O cálculo é executado sem erros, travamentos ou interrupções inesperadas. |
| 28 | Verificar a apresentação do **Log de Ocorrências no Processo de Cálculo**. | O log é apresentado ao término do processamento.                          |
| 29 | Confirmar o fechamento do log.                                             | O sistema fecha o log e permanece em condição de finalizar o processo.    |
| 30 | Selecionar **Sair**.                                                       | A rotina é encerrada corretamente.                                        |

## 8. Resultado Esperado

A rotina **GPEM020 – Cálculo por Roteiros** deve permitir:

* Acesso ao processo de cálculo por roteiros;
* Configuração do **Processo 00001**;
* Seleção do roteiro **VTR**;
* Confirmação dos parâmetros configurados;
* Execução do cálculo utilizando o roteiro VTR;
* Confirmação da configuração antes do processamento;
* Processamento do cálculo sem erros ou travamentos;
* Apresentação do **Log de Ocorrências no Processo de Cálculo**;
* Encerramento correto da operação após a conclusão do processamento.

## 9. Critério de Aprovação

O caso de teste será considerado **APROVADO** quando o sistema permitir configurar o **Processo 00001** e o roteiro **VTR**, confirmar os parâmetros, executar o cálculo com sucesso, apresentar o **Log de Ocorrências no Processo de Cálculo** e permitir o encerramento da operação sem erros ou inconsistências.

---


