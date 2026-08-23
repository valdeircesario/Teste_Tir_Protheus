# CT01_MATA360 – Inclusão e Visualização de Condição de Pagamento

## 1. Nome do Caso de Teste

**CT08_MATA360 – Inclusão e Visualização de Condição de Pagamento**

## 2. Nome da Rotina

**MATA360 – Condições de Pagamento**

## 3. Caminho da Rotina

**Protheus → SIGACOM → Atualizações → Cadastros → Condição de Pagamento**

## 4. Objetivo

Validar a **inclusão e visualização de uma Condição de Pagamento** na rotina **MATA360**, garantindo que a condição seja cadastrada corretamente com os dados informados e posteriormente localizada e visualizada no sistema.

## 5. Passo a Passo

### CREATE – Inclusão de Condição de Pagamento

| Nº | Ação                                                                          | Resultado Esperado                                                           |
| -: | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| 01 | Acessar a rotina **MATA360 – Condições de Pagamento**.                        | A rotina deve ser apresentada corretamente.                                  |
| 02 | Selecionar a opção **Incluir**.                                               | O sistema deve abrir a tela para cadastro de uma nova Condição de Pagamento. |
| 03 | Preencher os campos obrigatórios da Condição de Pagamento.                    | O sistema deve aceitar os dados válidos informados.                          |
| 04 | Informar os demais dados necessários para configurar a Condição de Pagamento. | O sistema deve permitir o preenchimento das informações.                     |
| 05 | Confirmar a inclusão da Condição de Pagamento.                                | O sistema deve validar os dados e gravar o cadastro sem apresentar erros.    |
| 06 | Registrar a identificação da Condição de Pagamento criada.                    | O sistema deve disponibilizar a identificação da condição cadastrada.        |

### READ – Visualização da Condição de Pagamento

| Nº | Ação                                                                               | Resultado Esperado                                                           |
| -: | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| 07 | Acessar novamente a rotina **MATA360** e localizar a Condição de Pagamento criada. | A condição deve ser localizada corretamente.                                 |
| 08 | Abrir o cadastro da Condição de Pagamento.                                         | O sistema deve apresentar os dados cadastrados.                              |
| 09 | Conferir as informações apresentadas.                                              | Os dados devem corresponder às informações utilizadas durante a inclusão.    |
| 10 | Conferir a identificação da Condição de Pagamento.                                 | O sistema deve apresentar corretamente o código ou identificação cadastrada. |

## 6. Validação de Campos Obrigatórios

| Nº | Ação                                                  | Resultado Esperado                                                                             |
| -: | ----------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| 11 | Iniciar a inclusão de uma nova Condição de Pagamento. | A tela de inclusão deve ser apresentada.                                                       |
| 12 | Deixar um campo obrigatório sem preenchimento.        | O sistema deve identificar a ausência da informação.                                           |
| 13 | Tentar confirmar a inclusão.                          | O sistema deve impedir a gravação e apresentar uma mensagem de validação.                      |
| 14 | Preencher o campo obrigatório e confirmar novamente.  | O sistema deve permitir a continuidade da inclusão, desde que os demais dados estejam válidos. |

## 7. Validação da Persistência dos Dados

| Nº | Ação                                                                       | Resultado Esperado                                                       |
| -: | -------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| 15 | Após a inclusão, sair da tela da Condição de Pagamento.                    | O sistema deve retornar à tela anterior sem apresentar erros.            |
| 16 | Pesquisar novamente a Condição de Pagamento utilizando sua identificação.  | A condição deve ser localizada corretamente.                             |
| 17 | Abrir a condição localizada.                                               | O sistema deve apresentar os dados anteriormente cadastrados.            |
| 18 | Comparar os dados apresentados com os dados informados durante a inclusão. | As informações devem permanecer consistentes e sem alterações indevidas. |

## 8. Resultado Esperado

A rotina **MATA360 – Condições de Pagamento** deve permitir realizar corretamente a **inclusão e visualização de Condições de Pagamento**.

O sistema deve:

* Permitir a inclusão de uma Condição de Pagamento com dados válidos.
* Validar os campos obrigatórios antes da gravação.
* Permitir o preenchimento das informações necessárias para o cadastro.
* Gravar corretamente a Condição de Pagamento.
* Disponibilizar a identificação da condição cadastrada.
* Permitir localizar a condição após sua inclusão.
* Apresentar corretamente os dados cadastrados durante a visualização.
* Manter a integridade e consistência dos dados após a gravação.

## 9. Critério de Aprovação

O caso de teste será considerado **APROVADO** quando a **Condição de Pagamento for incluída e posteriormente localizada e visualizada corretamente**, apresentando os mesmos dados informados durante a inclusão, sem erros ou inconsistências.

**Status:** `A definir durante a execução`

**Evidências:** `A anexar durante a execução`

**Responsável:** `A definir`

**Data de Execução:** `A definir`
