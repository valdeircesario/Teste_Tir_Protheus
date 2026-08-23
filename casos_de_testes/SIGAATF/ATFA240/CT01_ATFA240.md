# CT01_ATFA240 – Classificação de Compras / Aquisição de Imobilizado

## 1. Nome do Caso de Teste

**CT02_ATFA240 – Classificação de Compras / Aquisição de Imobilizado**

## 2. Nome da Rotina

**ATFA240 – Classificação de Compras / Aquisição de Imobilizado**

## 3. Caminho da Rotina

**Protheus → SIGAATF – Ativo Fixo → Atualizações → Classificação de Compras / Aquisição de Imobilizado**

> **Observação:** O caminho e a nomenclatura dos menus podem variar conforme a versão do Protheus, configuração do menu e customizações existentes no ambiente.

## 4. Objetivo

Validar o processo de **Classificação de Compras / Aquisição de Imobilizado**, garantindo que uma aquisição de bem seja corretamente classificada e incorporada ao **Ativo Fixo**, respeitando as informações fiscais, contábeis e patrimoniais configuradas no sistema.

O teste deve verificar se os dados da aquisição são apresentados corretamente, se a classificação pode ser realizada e se o bem é posteriormente registrado de forma consistente no módulo de Ativo Fixo.

## 5. Pré-condições

* Usuário com permissão de acesso à rotina **ATFA240**.
* Ambiente Protheus disponível e conectado ao banco de dados.
* Módulo **SIGAATF – Ativo Fixo** configurado.
* Cadastro de fornecedores disponível.
* Cadastro de produtos/bens ou informações necessárias para aquisição disponível.
* Contas contábeis e classes de ativos devidamente configuradas.
* Existência de uma compra/aquisição elegível para classificação como imobilizado.
* Parâmetros fiscais e contábeis necessários configurados.
* Massa de teste previamente definida.

## 6. Passo a Passo

| Nº | Ação                                                                                                                                                 | Resultado Esperado                                                                                                                                |
| -: | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| 01 | Acessar o ambiente **Protheus** com um usuário autorizado.                                                                                           | O sistema deve permitir o acesso ao ambiente.                                                                                                     |
| 02 | Acessar o módulo **SIGAATF – Ativo Fixo**.                                                                                                           | O módulo Ativo Fixo deve ser apresentado corretamente.                                                                                            |
| 03 | Acessar o menu **Atualizações**.                                                                                                                     | O sistema deve apresentar as opções disponíveis para o módulo.                                                                                    |
| 04 | Selecionar a rotina **ATFA240 – Classificação de Compras / Aquisição de Imobilizado**.                                                               | A rotina deve ser aberta corretamente.                                                                                                            |
| 05 | Consultar os documentos/aquisições disponíveis para classificação.                                                                                   | O sistema deve apresentar as aquisições disponíveis conforme os filtros e regras configurados.                                                    |
| 06 | Selecionar uma aquisição que será classificada como imobilizado.                                                                                     | A aquisição selecionada deve ser apresentada com suas respectivas informações.                                                                    |
| 07 | Conferir os dados da aquisição, como fornecedor, documento, data, produto, quantidade e valor.                                                       | Os dados apresentados devem corresponder à aquisição registrada no sistema.                                                                       |
| 08 | Selecionar/classificar o item como **Imobilizado**.                                                                                                  | O sistema deve permitir a classificação conforme as permissões e regras de negócio.                                                               |
| 09 | Informar os dados necessários para a classificação do ativo, como classe, conta contábil, centro de custo, localização e demais campos obrigatórios. | O sistema deve aceitar os dados válidos e validar os campos obrigatórios.                                                                         |
| 10 | Confirmar a classificação/aquisição do imobilizado.                                                                                                  | O sistema deve validar os dados informados e concluir o processamento sem erros.                                                                  |
| 11 | Consultar o ativo gerado após a classificação.                                                                                                       | O ativo deve estar disponível no cadastro de Ativo Fixo com os dados correspondentes à aquisição.                                                 |
| 12 | Conferir o valor de aquisição do ativo.                                                                                                              | O valor registrado no ativo deve estar de acordo com o valor da aquisição e com as regras configuradas.                                           |
| 13 | Conferir a classificação contábil e patrimonial do ativo.                                                                                            | O ativo deve estar associado corretamente à classe, conta contábil e demais informações informadas.                                               |
| 14 | Consultar a origem/movimentação do ativo.                                                                                                            | O sistema deve permitir identificar a aquisição que originou o ativo, quando essa rastreabilidade estiver disponível na configuração do ambiente. |
| 15 | Tentar classificar novamente a mesma aquisição, quando aplicável.                                                                                    | O sistema deve impedir duplicidade ou apresentar tratamento adequado conforme as regras da rotina.                                                |

## 7. Resultado Esperado

A rotina **ATFA240 – Classificação de Compras / Aquisição de Imobilizado** deve permitir que uma aquisição elegível seja corretamente classificada e incorporada ao Ativo Fixo.

Ao final do processo:

* A aquisição deve ser localizada corretamente na rotina.
* Os dados do documento de compra devem ser apresentados de forma consistente.
* O sistema deve permitir a classificação como imobilizado quando os critérios forem atendidos.
* Os campos obrigatórios devem ser validados corretamente.
* O ativo deve ser criado/registrado conforme a configuração do ambiente.
* O valor de aquisição deve ser registrado corretamente.
* A classificação contábil e patrimonial deve estar de acordo com os dados informados.
* A origem da aquisição deve permanecer rastreável quando essa funcionalidade estiver disponível.
* O sistema não deve permitir a geração indevida de ativos duplicados.
* Nenhum erro inesperado deve ocorrer durante o processamento.

## 8. Critério de Aprovação

O caso de teste será considerado **APROVADO** quando:

1. A rotina ATFA240 for acessada corretamente.
2. A aquisição de teste for localizada.
3. Os dados da aquisição forem apresentados corretamente.
4. A classificação como imobilizado for realizada com sucesso.
5. O ativo for criado/registrado corretamente.
6. Os valores e informações contábeis/patrimoniais estiverem consistentes.
7. Não ocorrer duplicidade ou inconsistência no cadastro do ativo.

**Status:** `A definir durante a execução`

**Evidências:** `A anexar durante a execução do teste`

**Responsável:** `A definir`

**Data de Execução:** `A definir`
