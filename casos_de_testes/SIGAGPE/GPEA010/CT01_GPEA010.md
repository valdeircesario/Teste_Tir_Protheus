# CT01_GPEA010 – Inclusão de Novo Funcionário

## 1. Nome do Caso de Teste

**CT10_GPEA010 – Inclusão de Novo Funcionário**

## 2. Nome da Rotina

**GPEA010 – Cadastro de Funcionários**

## 3. Caminho da Rotina

**Protheus → SIGAGPE → Atualizações → Funcionários → Funcionários**

## 4. Objetivo

Validar a **inclusão de um novo funcionário** na rotina **GPEA010**, garantindo que o cadastro seja realizado corretamente com os dados informados e que o funcionário seja disponibilizado para consulta após a gravação.

## 5. Passo a Passo

### CREATE – Inclusão de Funcionário

| Nº | Ação                                                                  | Resultado Esperado                                                        |
| -: | --------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| 01 | Acessar a rotina **GPEA010 – Cadastro de Funcionários**.              | A rotina deve ser apresentada corretamente.                               |
| 02 | Selecionar a opção **Incluir**.                                       | O sistema deve abrir a tela para cadastro de um novo funcionário.         |
| 03 | Preencher os campos obrigatórios do funcionário.                      | O sistema deve aceitar os dados válidos informados.                       |
| 04 | Preencher os demais dados necessários para o cadastro do funcionário. | O sistema deve permitir o preenchimento das informações.                  |
| 05 | Conferir os dados informados antes da gravação.                       | Os dados preenchidos devem ser apresentados corretamente.                 |
| 06 | Confirmar a inclusão do funcionário.                                  | O sistema deve validar os dados e gravar o cadastro sem apresentar erros. |
| 07 | Registrar a identificação do funcionário criado.                      | O sistema deve disponibilizar a identificação do funcionário cadastrado.  |

## 6. Validação de Campos Obrigatórios

| Nº | Ação                                                 | Resultado Esperado                                                                             |
| -: | ---------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| 08 | Iniciar a inclusão de um novo funcionário.           | A tela de inclusão deve ser apresentada.                                                       |
| 09 | Deixar um campo obrigatório sem preenchimento.       | O sistema deve identificar a ausência da informação.                                           |
| 10 | Tentar confirmar a inclusão do funcionário.          | O sistema deve impedir a gravação e apresentar uma mensagem de validação.                      |
| 11 | Preencher o campo obrigatório e confirmar novamente. | O sistema deve permitir a continuidade da inclusão, desde que os demais dados estejam válidos. |

## 7. Validação da Persistência dos Dados

| Nº | Ação                                                                       | Resultado Esperado                                                       |
| -: | -------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| 12 | Após a inclusão, sair da tela de cadastro do funcionário.                  | O sistema deve retornar à tela anterior sem apresentar erros.            |
| 13 | Pesquisar o funcionário utilizando sua identificação.                      | O funcionário deve ser localizado corretamente.                          |
| 14 | Abrir o cadastro do funcionário incluído.                                  | O sistema deve apresentar os dados cadastrados.                          |
| 15 | Conferir os dados apresentados com os dados informados durante a inclusão. | As informações devem permanecer consistentes e sem alterações indevidas. |

## 8. Resultado Esperado

A rotina **GPEA010 – Cadastro de Funcionários** deve permitir realizar corretamente a **inclusão de um novo funcionário**.

O sistema deve:

* Permitir a inclusão de funcionários com dados válidos.
* Validar os campos obrigatórios antes da gravação.
* Permitir o preenchimento das informações necessárias para o cadastro.
* Gravar corretamente o funcionário.
* Disponibilizar a identificação do funcionário cadastrado.
* Permitir localizar o funcionário após sua inclusão.
* Apresentar corretamente os dados cadastrados durante a consulta.
* Manter a integridade e consistência dos dados após a gravação.

## 9. Critério de Aprovação

O caso de teste será considerado **APROVADO** quando um **novo funcionário for incluído corretamente e posteriormente localizado e visualizado no sistema**, apresentando os mesmos dados informados durante o cadastro, sem erros ou inconsistências.

**Status:** `A definir durante a execução`

**Evidências:** `A anexar durante a execução`

**Responsável:** `A definir`

**Data de Execução:** `A definir`
