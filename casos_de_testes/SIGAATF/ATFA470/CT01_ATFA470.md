# CT01_ATFA470 – Fechamento Mensal do Ativo Fixo

## 1. Nome do Caso de Teste

**CT01_ATFA470 – Fechamento Mensal do Ativo Fixo**

## 2. Nome da Rotina

**ATFA470 – Fechamento Mensal do Ativo Fixo**

## 3. Caminho da Rotina

**Protheus → SIGAATF – Ativo Fixo → Atualizações → Fechamento Mensal**

> **Observação:** A nomenclatura dos menus pode variar conforme a versão do Protheus, configuração do menu e localização/customização do ambiente.

## 4. Objetivo

Validar a execução do **Fechamento Mensal do Ativo Fixo**, garantindo que o sistema processe corretamente o encerramento do período contábil do módulo de Ativo Fixo, considerando os ativos cadastrados, cálculos de depreciação e demais movimentações existentes no período.

O teste também deve verificar se o sistema apresenta corretamente a confirmação da execução e se os dados do período são atualizados de acordo com as regras da rotina.

## 5. Pré-condições

* Usuário com permissão de acesso à rotina **ATFA470**.
* Ambiente Protheus disponível e conectado ao banco de dados.
* Módulo **SIGAATF – Ativo Fixo** configurado.
* Existência de ativos cadastrados e ativos com movimentações no período.
* Período a ser fechado devidamente configurado.
* Depreciações e demais movimentações do período disponíveis para processamento.
* Backup ou massa de dados preparada para execução do teste.

## 6. Passo a Passo

| Nº | Ação                                                                                   | Resultado Esperado                                                                                                                    |
| -: | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| 01 | Acessar o ambiente **Protheus** com um usuário autorizado.                             | O sistema deve permitir o acesso ao ambiente.                                                                                         |
| 02 | Acessar o módulo **SIGAATF – Ativo Fixo**.                                             | O módulo Ativo Fixo deve ser apresentado corretamente.                                                                                |
| 03 | Acessar o menu **Atualizações**.                                                       | O sistema deve apresentar as opções disponíveis para o módulo.                                                                        |
| 04 | Selecionar a rotina **Fechamento Mensal**.                                             | A rotina **ATFA470 – Fechamento Mensal do Ativo Fixo** deve ser aberta.                                                               |
| 05 | Informar/selecionar o período que será encerrado, conforme a configuração do ambiente. | O sistema deve aceitar o período informado e apresentar os parâmetros correspondentes.                                                |
| 06 | Confirmar os parâmetros necessários para o processamento.                              | O sistema deve validar os parâmetros informados.                                                                                      |
| 07 | Executar o processamento do **Fechamento Mensal**.                                     | O sistema deve iniciar o processamento da rotina sem apresentar erros inesperados.                                                    |
| 08 | Aguardar a conclusão do processamento.                                                 | O processamento deve ser concluído corretamente.                                                                                      |
| 09 | Verificar a mensagem apresentada ao final da execução.                                 | O sistema deve informar que o fechamento foi realizado/concluído com sucesso, conforme o comportamento da versão utilizada.           |
| 10 | Consultar novamente os dados do período fechado.                                       | O sistema deve apresentar o período como fechado/encerrado, conforme as regras do módulo.                                             |
| 11 | Consultar os ativos processados no período.                                            | Os ativos devem apresentar os valores e informações atualizados após o fechamento.                                                    |
| 12 | Validar os valores de depreciação e demais movimentações processadas.                  | Os valores devem estar de acordo com os cálculos e movimentações esperados para o período.                                            |
| 13 | Tentar realizar novamente o fechamento do mesmo período, quando aplicável.             | O sistema deve impedir ou tratar adequadamente uma nova tentativa de fechamento de um período já encerrado, conforme regra da rotina. |

## 7. Resultado Esperado

A rotina **ATFA470 – Fechamento Mensal do Ativo Fixo** deve executar o fechamento do período selecionado com sucesso, processando corretamente os ativos e suas respectivas movimentações.

Ao final do processamento:

* O período deve ser identificado como **fechado/encerrado**.
* Os cálculos relacionados aos ativos devem estar atualizados.
* Os valores de depreciação devem permanecer consistentes com os parâmetros e regras configurados.
* As movimentações do período devem ser processadas corretamente.
* O sistema não deve apresentar erros durante ou após o processamento.
* O sistema deve impedir ou tratar corretamente uma nova tentativa de fechamento do mesmo período, quando essa operação não for permitida.

## 8. Critério de Aprovação

O caso de teste será considerado **APROVADO** quando:

1. A rotina ATFA470 for acessada corretamente.
2. O período informado for processado sem erros.
3. O fechamento for concluído com sucesso.
4. Os dados dos ativos forem atualizados corretamente.
5. Os valores processados forem compatíveis com a massa de teste e regras de negócio.
6. O período não puder ser indevidamente fechado novamente.

**Status:** `A definir durante a execução`

**Evidências:** `A anexar durante a execução do teste`

**Responsável:** `A definir`

**Data de Execução:** `A definir`
