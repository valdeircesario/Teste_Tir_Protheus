# CT01_GPEA020 – Inclusão e Visualização de Dependente

## 1. Nome do Caso de Teste

**CT01_GPEA020 – Inclusão e Visualização de Dependente**

## 2. Nome da Rotina

**GPEA020 – Dependentes**

## 3. Caminho da Rotina

**Protheus → SIGAGPE → Atualizações → Funcionários → Dependentes**

## 4. Objetivo

Validar o cadastro de dependente para um funcionário existente, verificando a localização do funcionário pela matrícula, o preenchimento das informações do dependente, a gravação do registro e a posterior visualização dos dados cadastrados.

O teste também valida a apresentação da mensagem de confirmação da alteração e o acesso à tela de visualização do funcionário.

## 5. Passo a Passo

### 5.1 Acesso à rotina e localização do funcionário

| Nº | Ação                                                                                                       | Resultado Esperado                                                |
| -: | ---------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
|  1 | Acessar o ambiente Protheus e realizar a configuração inicial do módulo **SIGAGPE**.                       | O ambiente é carregado corretamente.                              |
|  2 | Acessar **Atualizações → Funcionários → Dependentes**.                                                     | A tela **Dependentes** é apresentada corretamente.                |
|  3 | Caso seja apresentada a mensagem **"Este ambiente utiliza base de Homologação."**, selecionar **Fechar**.  | A mensagem é encerrada e o fluxo continua normalmente.            |
|  4 | Caso seja apresentada a tela **Moedas**, validar o valor de **Dolar = 0,0000** e selecionar **Confirmar**. | A tela é confirmada e o fluxo prossegue.                          |
|  5 | Aguardar a apresentação da tela **Dependentes**.                                                           | A tela é carregada corretamente.                                  |
|  6 | Pesquisar o funcionário pela matrícula **000016**.                                                         | O funcionário correspondente à matrícula **000016** é localizado. |
|  7 | Registrar evidência da localização do funcionário.                                                         | A matrícula pesquisada fica registrada como evidência do teste.   |

### 5.2 Inclusão do dependente

| Nº | Ação                                                              | Resultado Esperado                                                            |
| -: | ----------------------------------------------------------------- | ----------------------------------------------------------------------------- |
|  8 | Selecionar **Manutenção**.                                        | A tela **Funcionários - MANUTENÇÃO** é apresentada.                           |
|  9 | Informar o nome do dependente como **TESTE DE DEPENDENTE 01**.    | O nome é preenchido corretamente.                                             |
| 10 | Informar a **Data Nasc.** conforme o valor definido para o teste. | A data de nascimento é preenchida corretamente.                               |
| 11 | Informar **Tp Dep.eSoci = 03**.                                   | O tipo de dependente é preenchido corretamente.                               |
| 12 | Informar **Sexo = M**.                                            | O sexo é preenchido corretamente.                                             |
| 13 | Informar **Grau Parent. = F - Filho**.                            | O grau de parentesco é preenchido corretamente.                               |
| 14 | Informar **Tipo Dep.IR = 2 - Até 21 Anos**.                       | O tipo de dependente para IR é preenchido corretamente.                       |
| 15 | Informar **Tipo Dep. SF = 2**.                                    | O tipo de dependente para salário-família é preenchido corretamente.          |
| 16 | Informar **Local Nasc. = BRASILIA**.                              | O local de nascimento é preenchido corretamente.                              |
| 17 | Informar **Cartorio = DE REGISTRO**.                              | O cartório é preenchido corretamente.                                         |
| 18 | Informar **No.Reg.Cart. = 123**.                                  | O número do registro do cartório é preenchido corretamente.                   |
| 19 | Informar **No.Livro = 130**.                                      | O número do livro é preenchido corretamente.                                  |
| 20 | Informar **No.Folha = 11**.                                       | O número da folha é preenchido corretamente.                                  |
| 21 | Informar **Dt.Entrega** conforme o valor definido para o teste.   | A data de entrega é preenchida corretamente.                                  |
| 22 | Informar o CPF **808.350.540-47**.                                | O CPF é preenchido corretamente.                                              |
| 23 | Confirmar os dados preenchidos na grade.                          | Os dados do dependente são carregados e permanecem disponíveis para gravação. |
| 24 | Registrar evidência dos dados informados.                         | Os dados preenchidos ficam registrados como evidência.                        |
| 25 | Selecionar **Confirmar**.                                         | O sistema processa a alteração do cadastro.                                   |
| 26 | Aguardar a mensagem **"Registro alterado com sucesso."**.         | A mensagem de sucesso é apresentada, indicando que o cadastro foi gravado.    |
| 27 | Selecionar **Fechar**.                                            | A mensagem é encerrada e o sistema retorna para a tela **Dependentes**.       |

### 5.3 Visualização do cadastro

| Nº | Ação                                 | Resultado Esperado                                                           |
| -: | ------------------------------------ | ---------------------------------------------------------------------------- |
| 28 | Selecionar **Visualizar**.           | A tela **Funcionários - VISUALIZAR** é apresentada.                          |
| 29 | Validar a matrícula apresentada.     | A matrícula exibida corresponde à matrícula **000016**.                      |
| 30 | Registrar evidência da visualização. | A tela de visualização fica registrada como evidência do teste.              |
| 31 | Selecionar **Fechar**.               | A tela de visualização é encerrada e o sistema retorna para **Dependentes**. |

## 6. Validações

### 6.1 Validação do funcionário

* A rotina deve permitir localizar o funcionário pela matrícula **000016**.
* O funcionário localizado deve ser disponibilizado para manutenção dos dependentes.

### 6.2 Validação do dependente

Devem ser preenchidas as informações utilizadas pela automação:

| Campo        | Valor                  |
| ------------ | ---------------------- |
| Nome         | TESTE DE DEPENDENTE 01 |
| Sexo         | M                      |
| Tp Dep.eSoci | 03                     |
| Grau Parent. | F - Filho              |
| Tipo Dep.IR  | 2 - Até 21 Anos        |
| Tipo Dep. SF | 2                      |
| Local Nasc.  | BRASILIA               |
| Cartorio     | DE REGISTRO            |
| No.Reg.Cart. | 123                    |
| No.Livro     | 130                    |
| No.Folha     | 11                     |
| CPF          | 808.350.540-47         |

A **Data Nasc.** e a **Dt.Entrega** devem ser consideradas conforme as datas geradas/utilizadas pelo teste automatizado.

### 6.3 Validação da gravação

* O sistema deve permitir confirmar o cadastro.
* A mensagem **"Registro alterado com sucesso."** deve ser apresentada.
* Após o fechamento da mensagem, o sistema deve retornar para a tela **Dependentes**.

### 6.4 Validação da visualização

* A opção **Visualizar** deve abrir a tela **Funcionários - VISUALIZAR**.
* A matrícula apresentada deve ser **000016**.
* A tela deve ser encerrada corretamente através de **Fechar**.

## 7. Evidências

As seguintes evidências devem ser registradas durante a execução:

* **Dependente/001** – Tela inicial da rotina **Dependentes**.
* **Dependente/002** – Funcionário localizado pela matrícula.
* **Dependente/003** – Tela **Funcionários - MANUTENÇÃO**.
* **Dependente/004** – Dados do dependente preenchidos.
* **Dependente/005** – Mensagem **"Registro alterado com sucesso."**.
* **Dependente/006** – Tela **Funcionários - VISUALIZAR**.

## 8. Resultado Esperado

A rotina **GPEA020 – Dependentes** deve permitir localizar o funcionário pela matrícula **000016**, acessar a manutenção e cadastrar o dependente com os dados informados.

Após a confirmação, o sistema deve apresentar a mensagem:

> **"Registro alterado com sucesso."**

O cadastro deve permanecer disponível na rotina e permitir a abertura da tela **Funcionários - VISUALIZAR**, apresentando a matrícula **000016**.

Todo o fluxo deve ser concluído sem erros impeditivos, travamentos ou encerramento inesperado da rotina.

## 9. Critério de Aprovação

O caso de teste será considerado **APROVADO** quando:

* A rotina **Dependentes** for acessada corretamente;
* O funcionário de matrícula **000016** for localizado;
* A tela de manutenção for apresentada;
* Os dados do dependente forem preenchidos corretamente;
* O cadastro for confirmado com sucesso;
* A mensagem **"Registro alterado com sucesso."** for apresentada;
* A tela de visualização for acessada corretamente;
* A matrícula **000016** for apresentada na visualização;
* O fluxo puder ser encerrado normalmente;
* Todas as evidências previstas forem registradas.

**Status:** ⬜ Aprovado / ⬜ Reprovado


