import unittest
import logging
from datetime import datetime, timedelta
from os import getcwd
from tir import Webapp


class TestNecessidadeCompraPOUI(unittest.TestCase):

    # ==================================================
    # SETUP
    # ==================================================
    @classmethod
    def setUpClass(cls):
        print(">>> INICIO SETUP")

        cls.filial = "02DF0001"
        cls.data_ref = (datetime.today() - timedelta(days=1)).strftime("%d/%m/%Y")

        config_path = getcwd() + "\\config.json"
        cls.oHelper = Webapp(config_path)
        print(">>> ANTES DO SETUP")

        # ✅ Inicializa o Protheus
        cls.oHelper.Setup(
            "SIGAMDI",
            cls.data_ref,
            "02",
            cls.filial,
            "02"
        )
        print(">>> DEPOIS DO SETUP")

        # ✅ Tratativas padrão
        if cls.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            cls.oHelper.SetButton("Fechar")

        if cls.oHelper.IfExists("Moedas"):
            cls.oHelper.SetButton("Confirmar")

        # ✅ Navegação PO-UI (MENU)
        print(">>> ANTES DO MENU")
        cls.oHelper.SetLateralMenu(
            "Atualizações > Novo Fluxo de Compras > Novo Fluxo de Compras"
        )

        cls.oHelper.SetButton('Confirmar')
        print(">>> DEPOIS DO MENU")

    # ==================================================
    # TESTE
    # ==================================================
    def test_consultar_necessidade_compra(self):

        # Evidência inicial
        self.oHelper.Screenshot("Tela_Inicial_Necessidade_Compra")

        # ✅ Exemplo: clicar em botão PO-UI
        self.oHelper.SetButton("Pesquisar")
        

        # ✅ Exemplo: validar campo PO-UI
        self.oHelper.CheckResult(
            campo="Filial",
            user_value=self.filial,
            po_component="po-input"
        )

        # ✅ Exemplo: interação com tabela PO-UI
        self.oHelper.ClickTable(
            columns="Status",
            values="Aberto"
        )

        self.oHelper.Screenshot("Resultado_Pesquisa")

        # ✅ Exemplo: clicar ação da linha
        self.oHelper.ClickTable(
            columns="Status",
            values="Aberto",
            click_cell="Detalhar"
        )

        self.oHelper.WaitProcessing()
        self.oHelper.Screenshot("Detalhe_Necessidade")

        # ✅ Validação final
        self.oHelper.AssertTrue()

    # ==================================================
    # TEARDOWN
    # ==================================================
    @classmethod
    def tearDownClass(cls):
        logging.info("Encerrando teste PO-UI")
        cls.oHelper.Finish()


if __name__ == "__main__":
    unittest.main(verbosity=2)
