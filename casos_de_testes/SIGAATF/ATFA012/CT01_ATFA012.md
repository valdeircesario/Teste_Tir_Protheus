# CT01_ATFA012 – Cadastro de Ativos

## 1. Nome do Caso de Teste

**CT03_ATFA012 – Cadastro de Ativos**

## 2. Nome da Rotina

**ATFA012 – Cadastro de Ativos**

## 3. Caminho da Rotina

**Protheus → SIGAATF – Ativo Fixo → Atualizações → Ativos → Cadastro de Ativos**

> **Observação:** O caminho e a nomenclatura dos menus podem variar conforme a versão do Protheus, configuração do menu e customizações existentes no ambiente.

## 4. Objetivo

Validar o processo de **Cadastro de Ativos**, garantindo que um novo ativo possa ser incluído corretamente no módulo **Ativo Fixo**, com suas respectivas informações patrimoniais, contábeis e administrativas.

O teste deve verificar o preenchimento dos campos obrigatórios, validação dos dados informados, gravação do cadastro e posterior consulta do ativo cadastrado.

## 5. Pré-condições

* Usuário com permissão de acesso à rotina **ATFA012**.
* Ambiente Protheus disponível e conectado ao banco de dados.
* Módulo **SIGAATF – Ativo Fixo** configurado.
* Classes de ativos previamente cadastradas.
* Contas contábeis necessárias configuradas.
* Centros de custo disponíveis, quando aplicável.
* Locais de ativos cadastrados, quando aplicável.
* Parâmetros do módulo devidamente configurados.
* Massa de teste definida para o novo ativo.

## 6. Dados para Teste

| Campo              | Exemplo                                  |
| ------------------ | ---------------------------------------- |
| Descrição do Ativo | Notebook Dell Latitude                   |
| Classe do Ativo    | Equipamentos de Informática              |
| Data de Aquisição  | 01/08/2026                               |
| Valor de Aquisição | R$ 5.000,00                              |
| Quantidade         | 1                                        |
| Centro de Custo    | Administrativo                           |
| Localização        | Escritório                               |
| Conta Contábil     | Conforme configuração do ambiente        |
| Vida Útil          | Conforme configuração da classe do ativo |

> Os valores acima são exemplos e devem ser substituídos pelos dados definidos para a massa de teste do ambiente.

## 7. Passo a Passo

| Nº | Ação                                                                                          | Resultado Esperado                                                                                                        |
| -: | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| 01 | Acessar o ambiente **Protheus** com um usuário autorizado.                                    | O sistema deve permitir o acesso ao ambiente.                                                                             |
| 02 | Acessar o módulo **SIGAATF – Ativo Fixo**.                                                    | O módulo Ativo Fixo deve ser apresentado corretamente.                                                                    |
| 03 | Acessar o menu **Atualizações → Ativos**.                                                     | O sistema deve apresentar as opções relacionadas ao cadastro de ativos.                                                   |
| 04 | Selecionar a rotina **ATFA012 – Cadastro de Ativos**.                                         | A tela de cadastro de ativos deve ser apresentada corretamente.                                                           |
| 05 | Selecionar a opção **Incluir/Novo**.                                                          | O sistema deve disponibilizar os campos para inclusão de um novo ativo.                                                   |
| 06 | Informar a descrição do ativo.                                                                | O sistema deve aceitar a descrição informada.                                                                             |
| 07 | Informar a classe do ativo.                                                                   | O sistema deve validar a classe informada e apresentar as informações relacionadas à configuração da classe.              |
| 08 | Informar a data de aquisição.                                                                 | O sistema deve aceitar uma data válida conforme as regras do módulo.                                                      |
| 09 | Informar o valor de aquisição do ativo.                                                       | O sistema deve aceitar e validar o valor informado.                                                                       |
| 10 | Informar quantidade e demais informações obrigatórias.                                        | O sistema deve validar os campos obrigatórios.                                                                            |
| 11 | Informar centro de custo, localização e demais informações administrativas, quando aplicável. | O sistema deve aceitar os dados válidos e realizar as respectivas validações.                                             |
| 12 | Conferir os dados contábeis e patrimoniais apresentados pelo sistema.                         | As informações devem estar de acordo com a classe e parâmetros configurados.                                              |
| 13 | Confirmar a inclusão do ativo.                                                                | O sistema deve validar os dados e gravar o novo ativo sem apresentar erros.                                               |
| 14 | Registrar o código/identificador gerado para o ativo.                                         | O sistema deve disponibilizar um identificador único para o ativo cadastrado.                                             |
| 15 | Pesquisar o ativo recém-cadastrado.                                                           | O ativo deve ser localizado corretamente na consulta.                                                                     |
| 16 | Abrir o cadastro do ativo e conferir os dados gravados.                                       | Todas as informações devem permanecer de acordo com os dados informados durante a inclusão.                               |
| 17 | Validar o valor de aquisição, classe, data e demais informações patrimoniais.                 | Os dados devem estar consistentes com a massa de teste.                                                                   |
| 18 | Verificar se o ativo está disponível para as demais operações do módulo, conforme seu status. | O ativo deve estar corretamente registrado e disponível para utilização nas rotinas subsequentes permitidas pelo sistema. |

## 8. Validação de Campos Obrigatórios

Realizar uma segunda inclusão deixando, individualmente, campos obrigatórios sem preenchimento.

### Resultado Esperado

O sistema deve:

* Identificar o campo obrigatório não preenchido.
* Impedir a gravação do cadastro enquanto houver informações obrigatórias ausentes.
* Apresentar mensagem orientando o usuário sobre a informação necessária.
* Permitir a correção do campo e a continuidade do cadastro.

## 9. Validação de Dados Inválidos

Realizar testes com dados inválidos ou incompatíveis, quando aplicável, como:

* Valor de aquisição igual a zero ou negativo.
* Data de aquisição inválida.
* Classe de ativo inexistente.
* Centro de custo inválido.
* Conta contábil incompatível.
* Campos obrigatórios em branco.

### Resultado Esperado

O sistema deve validar os dados informados e impedir a gravação de informações que não atendam às regras de negócio configuradas.

## 10. Resultado Esperado

A rotina **ATFA012 – Cadastro de Ativos** deve permitir o cadastro correto de um novo ativo no módulo **SIGAATF**, garantindo a integridade das informações patrimoniais e contábeis.

Ao final do processo:

* O ativo deve ser incluído com sucesso.
* Um identificador único deve ser gerado para o ativo.
* Os campos obrigatórios devem ser devidamente validados.
* Os dados informados devem ser gravados corretamente.
* A classe do ativo deve ser respeitada.
* O valor e a data de aquisição devem permanecer consistentes.
* As informações contábeis e patrimoniais devem estar de acordo com a configuração do ambiente.
* O ativo deve estar disponível para consulta após a inclusão.
* Dados inválidos ou obrigatórios não preenchidos não devem permitir a gravação.
* O sistema não deve permitir a criação indevida de registros inconsistentes ou duplicados.

## 11. Critério de Aprovação

O caso de teste será considerado **APROVADO** quando:

1. A rotina ATFA012 for acessada corretamente.
2. Um novo ativo puder ser incluído com dados válidos.
3. Os campos obrigatórios forem devidamente validados.
4. O cadastro for gravado com sucesso.
5. Um identificador único for gerado.
6. O ativo puder ser localizado posteriormente.
7. Os dados gravados forem iguais aos dados informados.
8. Dados inválidos forem corretamente rejeitados pelo sistema.

**Status:** `A definir durante a execução`

**Evidências:** `A anexar durante a execução do teste`

**Responsável:** `A definir`

**Data de Execução:** `A definir`
