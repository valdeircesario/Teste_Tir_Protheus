import unittest
import sys
import logging
from time import sleep
from os import getcwd, path
from datetime import datetime, timedelta

from selenium.webdriver.common.by import By
from tir import Webapp


# ======================================================
# CONFIGURAÇÃO DE LOG
# ======================================================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Ajuste de path (mantém compatível com TIR)
sys.path.insert(0, path.abspath(path.join(path.dirname(__file__), '../../')))


class GPEA133(unittest.TestCase):
    """
    Teste de geração de relatório e navegação de páginas
    utilizando TIR (TOTVS Interface Robot)
    """

    # ==================================================
    # SETUP
    # ==================================================
    @classmethod
    def setUpClass(cls):
        cls.filial = '02DF0001'
        cls.dataref = (datetime.today() - timedelta(days=5)).strftime("%d/%m/%Y")

        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)

        logging.info("Iniciando setup do teste")

        cls.oHelper.Setup('SIGAMDI', cls.dataref, '02', cls.filial, '07')
        cls.oHelper.SetLateralMenu(
            "Relatorios > Lançamentos > Por Periodo Vertical"
        )
        cls.oHelper.SetButton('Confirmar')

        # Tratativas padrão de ambiente
        if cls.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            cls.oHelper.SetButton('Fechar')

        if cls.oHelper.IfExists("Moedas"):
            cls.oHelper.SetButton('Confirmar')

        logging.info("Setup finalizado com sucesso")

    # ==================================================
    # TESTE
    # ==================================================
    def test_geracao_relatorio_verba(self):
        """
        Gera relatório e navega para a próxima página
        """

        logging.info("Iniciando execução do teste")

        # Evidência inicial
        self.oHelper.Screenshot("Relatorio_verba_01")

        # Geração do relatório
        self.oHelper.SetButton('Imprimir')
        sleep(8)  # aguarda renderização do relatório

        self.oHelper.Screenshot("Relatorio_verba_02")

        # ==================================================
        # CLIQUE NA PRÓXIMA PÁGINA (CSS SELECTOR)
        # ==================================================
        self.oHelper.ClickByLocator(
            selector='button[title="Próxima pagina"]',
            locator=By.CSS_SELECTOR
        )

        logging.info("Clique na próxima página realizado")

        sleep(3)
        self.oHelper.Screenshot("Relatorio_verba_03")

        # Validação final
        self.oHelper.AssertTrue()
        logging.info("Teste executado com sucesso")

    # ==================================================
    # TEARDOWN
    # ==================================================
    @classmethod
    def tearDownClass(cls):
        logging.info("Encerrando teste")
        cls.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main(verbosity=2)