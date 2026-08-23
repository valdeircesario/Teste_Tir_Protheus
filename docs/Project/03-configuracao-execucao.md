# Configuracao e execucao

## Preparacao

O script `setup.ps1` verifica o Python, atualiza `pip` e `virtualenv`, cria `venv` e instala `tir_framework`.

```powershell
.\setup.ps1
.\venv\Scripts\Activate.ps1
```

No VS Code, o interpretador esperado e `venv/Scripts/python.exe`.

## Configuracao

`config.template.json` documenta os parametros principais do TIR:

- URL do ambiente.
- Navegador.
- idioma.
- usuario e senha.
- release, build e biblioteca.
- timeout.
- modo headless.
- logs, cobertura e instalacao automatica de driver.

`config.json` e local e deve conter os valores reais do ambiente. Credenciais nao devem ser versionadas ou copiadas para documentacao.

## Execucao recomendada

```powershell
python -m pytest tests/SIGACOM/test_MATA010.py -v -s
python -m pytest tests/SIGAGPE -v -s
python -m pytest tests/test_fluxo_necessidade_compra_poui.py -v -s
```

Para HTML com pytest, os testes existentes usam o padrao `--html=reports/nome.html --self-contained-html`.

## Ciclo de vida

1. O teste carrega o `config.json`.
2. `setUpClass` cria o helper e prepara login, data, filial e modulo.
3. O fluxo trata modais iniciais e navega ate a rotina.
4. O metodo `test_*` executa a operacao funcional.
5. `tearDownClass` chama `TearDown` para encerrar a sessao.

A execucao real requer ambiente Protheus disponivel; a simples analise dos arquivos nao valida a aplicacao remota.
