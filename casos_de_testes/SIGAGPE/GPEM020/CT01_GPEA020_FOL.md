# CT01_GPEM020 – Cálculo de Folha por Roteiro FOL

## 1. Nome do Caso de Teste

**CT01_GPEM020 – Cálculo de Folha por Roteiro FOL**

## 2. Nome da Rotina

**GPEM020 – Cálculo por Roteiros**

## 3. Caminho da Rotina

**Protheus → SIGAGPE → Miscelânea → Cálculos (13) → Por Roteiros**

## 4. Objetivo

Validar a execução do processo de cálculo da folha de pagamento por roteiro na rotina **GPEM020**, utilizando o roteiro **FOL**, um processo de cálculo válido e o filtro por matrícula, garantindo que os parâmetros sejam aceitos, o cálculo seja processado corretamente e o sistema apresente o log de ocorrências do processo.

## 5. Passo a Passo

### PARAMETRIZAÇÃO – Processo de Cálculo

| Nº | Ação                                                                                                  | Resultado Esperado                                                        |
| -: | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| 01 | Acessar o módulo **Gestão de Pessoal**.                                                               | O módulo é carregado corretamente, sem erros.                             |
| 02 | Acessar **Miscelânea → Cálculos (13) → Por Roteiros**.                                                | A rotina de cálculo por roteiros é apresentada.                           |
| 03 | Caso seja apresentada a mensagem **"Este ambiente utiliza base de Homologação."**, fechar a mensagem. | A mensagem é fechada e o sistema permanece na rotina.                     |
| 04 | Caso seja apresentada a tela **Moedas**, validar o valor do campo **Dolar**.                          | O valor apresentado é **0,0000**.                                         |
| 05 | Confirmar a tela de Moedas.                                                                           | O sistema prossegue para a rotina.                                        |
| 06 | Caso seja apresentada a tela **Novidades do Produto**, fechá-la.                                      | A tela é fechada e o sistema prossegue para o processo de cálculo.        |
| 07 | Aguardar a apresentação da tela **Processo de Calculo**.                                              | A tela é apresentada corretamente.                                        |
| 08 | Validar a mensagem informativa **"Este programa realiza processos de calculos"**.                     | A mensagem informativa é apresentada corretamente.                        |
| 09 | Selecionar a opção **Parâmetros**.                                                                    | A tela de parametrização do processo é apresentada.                       |
| 10 | Informar o **Processo = 00001**.                                                                      | O processo informado é aceito pelo sistema.                               |
| 11 | Informar o **Roteiro = FOL**.                                                                         | O roteiro FOL é aceito pelo sistema.                                      |
| 12 | Confirmar os parâmetros selecionando **OK**.                                                          | Os parâmetros são confirmados e o sistema retorna ao processo de cálculo. |

### FILTRO – Matrícula do Funcionário

| Nº | Ação                                                            | Resultado Esperado                                                                   |
| -: | --------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| 13 | Selecionar a opção **Filtro Rápido**.                           | A tela de configuração do filtro é apresentada.                                      |
| 14 | No campo **Campos**, selecionar/informar **Matrícula**.         | O campo de filtro é configurado para utilizar a matrícula.                           |
| 15 | Informar a expressão correspondente à matrícula do funcionário. | A matrícula informada é aceita como critério de filtro.                              |
| 16 | Selecionar **OK**.                                              | O filtro é aplicado corretamente.                                                    |
| 17 | Verificar os registros apresentados após a aplicação do filtro. | O sistema apresenta os registros correspondentes ao critério de matrícula informado. |

### PROCESSAMENTO – Cálculo do Roteiro FOL

| Nº | Ação                                                                                              | Resultado Esperado                                                          |
| -: | ------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| 18 | Selecionar a opção **Calcular**.                                                                  | O sistema inicia o processo de cálculo conforme os parâmetros configurados. |
| 19 | Caso seja apresentada a mensagem **"Confirma configuração dos parametros?"**, selecionar **Sim**. | O sistema confirma a configuração e prossegue com o cálculo.                |
| 20 | Aguardar a execução do processo de cálculo.                                                       | O cálculo é processado sem erros ou travamentos.                            |
| 21 | Aguardar a apresentação da tela **Log de Ocorrências no Processo de Cálculo**.                    | O log de ocorrências é apresentado ao final do processamento.               |
| 22 | Validar o log apresentado pelo sistema.                                                           | O sistema apresenta o resultado das ocorrências geradas durante o processo. |
| 23 | Selecionar **OK** no log de ocorrências.                                                          | O sistema fecha o log e prossegue normalmente.                              |
| 24 | Selecionar **Sair** após a conclusão do processamento.                                            | O sistema encerra o processo e retorna corretamente à rotina.               |

## 6. Validação dos Parâmetros

| Nº | Ação                                       | Resultado Esperado                                                             |
| -: | ------------------------------------------ | ------------------------------------------------------------------------------ |
| 25 | Verificar o processo utilizado no cálculo. | O processo utilizado corresponde ao **00001**.                                 |
| 26 | Verificar o roteiro utilizado no cálculo.  | O roteiro utilizado corresponde ao **FOL**.                                    |
| 27 | Verificar o filtro aplicado.               | O filtro utilizado corresponde ao campo **Matrícula** e à expressão informada. |

## 7. Validação do Processamento

| Nº | Ação                                                                       | Resultado Esperado                                             |
| -: | -------------------------------------------------------------------------- | -------------------------------------------------------------- |
| 28 | Verificar a apresentação do **Log de Ocorrências no Processo de Cálculo**. | O sistema apresenta o log após o processamento.                |
| 29 | Analisar as ocorrências apresentadas no log.                               | As ocorrências são apresentadas corretamente pelo sistema.     |
| 30 | Finalizar o processo de cálculo.                                           | O sistema permite sair da rotina sem erros ou inconsistências. |

## 8. Resultado Esperado

A rotina **GPEM020 – Cálculo por Roteiros** deve permitir:

* Acesso ao processo de cálculo por roteiros;
* Configuração do **Processo 00001**;
* Seleção do roteiro **FOL**;
* Aplicação de filtro por **Matrícula**;
* Execução do cálculo somente conforme os parâmetros e filtro configurados;
* Confirmação dos parâmetros antes do processamento, quando solicitada;
* Execução do cálculo sem erros ou travamentos;
* Apresentação do **Log de Ocorrências no Processo de Cálculo** após o processamento;
* Encerramento correto do processo após a conclusão do cálculo.

## 9. Critério de Aprovação

O caso de teste será considerado **APROVADO** quando os parâmetros **Processo 00001** e **Roteiro FOL** forem aceitos, o filtro por matrícula for aplicado corretamente, o cálculo for executado com sucesso e o sistema apresentar o **Log de Ocorrências no Processo de Cálculo**, permitindo finalizar a operação sem erros ou inconsistências.

---
