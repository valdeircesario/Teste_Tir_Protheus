# Padrao dos testes

## Estrutura comum

A maioria dos arquivos segue `unittest.TestCase`:

```python
class ROTINA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup(...)
        cls.oHelper.SetLateralMenu("...")

    def test_cenario(self):
        try:
            self.oHelper.WaitShow("...")
            self.oHelper.SetButton("Incluir")
            self.oHelper.SetValue("CAMPO", valor, check_value=False)
            self.oHelper.CheckResult("CAMPO", valor)
            self.oHelper.AssertTrue()
        finally:
            ...

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()
```

## Responsabilidades

- `setUpClass`: massa fixa ou dinamica, configuracao, login e navegacao inicial.
- `test_*`: fluxo funcional completo, geralmente CRUD ou consulta.
- `WaitShow`: sincronizacao com a tela ou mensagem.
- `SetValue`: preenchimento e alteracao.
- `CheckResult`: conferencia de dados apresentados.
- `AssertTrue`: conclusao da validacao TIR.
- `Screenshot`: evidencia de etapas relevantes.
- `tearDownClass`: encerramento do navegador.

## Tratamento de excecao

Nos testes que usam `TirReportAgent`, o fluxo normalmente registra a excecao, relanca o erro para o executor marcar o teste como falho e salva o relatorio em `finally`.

## Massa de dados

A massa esta declarada dentro dos proprios testes: codigos, descricoes, datas, filiais, campos de cadastro, CPFs e valores. Nao existe atualmente uma camada unica de fixtures ou factory de dados.

## Convencoes observadas

Os nomes de arquivos seguem `test_<rotina>.py`, com sufixos para variacoes do cenario. A organizacao e funcional, mas ha testes legados ou experimentais em `tests/Outros` e alguns nomes de classe/metodo variam entre arquivos.
