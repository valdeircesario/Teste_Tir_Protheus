import unittest
from time import sleep
from os import getcwd, path
from datetime import datetime, timedelta
import sys
import logging

# Configuração do log
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Ajuste de path
sys.path.insert(0, path.abspath(path.join(path.dirname(__file__), '../../')))

from tir import Webapp
from tools.click_css import click_css


class GPEA133(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.filial = '01'
        cls.dataref = (datetime.today() - timedelta(days=5)).strftime("%d/%m/%Y")

        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)

        logging.info("Iniciando setup do teste")

        cls.oHelper.Setup('SIGAMDI', cls.dataref, '99', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Miscelanea > Cálculos > Rescisão")
        cls.oHelper.SetButton('Confirmar')

        if cls.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            cls.oHelper.SetButton('Fechar')

        if cls.oHelper.IfExists("Moedas"):
            cls.oHelper.CheckResult('Dolar', '0,0000')
            cls.oHelper.SetButton('Confirmar')

    def test_lancamento_vale_transporte_e_claculo_folha(self):

        logging.info("Executando fluxo principal do teste")

        self.oHelper.SetButton("Incluir")
        sleep(2)

        self.oHelper.SetButton("OK")

        click_css(
            self.oHelper,
            "wa-print-preview",
            'button[title="Próxima página"]'
        )
        click_css(
            self.oHelper,
            "wa-print-preview",
            'button[title="Próxima página"]'
        )
        click_css(
            self.oHelper,
            "wa-print-preview",
            'button[title="Próxima página"]'
        )
        click_css(
            self.oHelper,
            "wa-print-preview",
            'button[title="Próxima página"]'
        )
        click_css(
            self.oHelper,
            "wa-print-preview",
            'button[title="Próxima página"]'
        )
        click_css(
            self.oHelper,
            "wa-print-preview",
            'button[title="Ampliar (+)"]'
        )
        click_css(
            self.oHelper,
            "wa-print-preview",
            'button[title="Reduzir (-)"]'
        )

        #Ir para a página    Ir para a página :      Ampliar (+)    Reduzir (-)

        logging.info("Clique na próxima página realizado")

        self.oHelper.AssertTrue()

        logging.info("Teste finalizado com sucesso")

    @classmethod
    def tearDownClass(cls):
        logging.info("Encerrando teste")
        cls.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main(verbosity=2)