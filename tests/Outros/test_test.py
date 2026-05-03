import pyautogui
import unittest


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



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


class test_test(unittest.TestCase):

    @classmethod
    def setup_class(cls):

        global driver
        driver = webdriver.Firefox()


        cls.filial = '01'
        cls.dataref = (datetime.today() - timedelta(days=5)).strftime("%d/%m/%Y")

        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)

        logging.info("Iniciando setup do teste")

        cls.oHelper.Setup('SIGAMDI', cls.dataref, '99', cls.filial, '02')
        cls.oHelper.SetLateralMenu("Atualizações > Novo Fluxo de Compras > Novo Fluxo de Compras")
        cls.oHelper.SetButton('Confirmar')

        if cls.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            cls.oHelper.SetButton('Fechar')

        if cls.oHelper.IfExists("Moedas"):
            cls.oHelper.CheckResult('Dolar', '0,0000')
            cls.oHelper.SetButton('Confirmar')

    



    def test_test(self):
        sleep(5)
        self.oHelper.Screenshot("compras_001")
        sleep(3)
        pyautogui.click(30,261)# nescessidade de compras
        sleep(1)
        sleep(1)
        self.oHelper.Screenshot("compras_001")
        pyautogui.click(337,435)# botão de busca
        sleep(1)
        pyautogui.write('000000000000003', interval=0.1)
        sleep(1)
        pyautogui.press('enter')
        sleep(1)
        self.oHelper.Screenshot("compras_003")
        pyautogui.click(104,644)#selecionar linha
        sleep(5)
        pyautogui.click(28,315)# cotações
        sleep(2)
        self.oHelper.Screenshot("compras_004")
        pyautogui.click(32,354)# historico de copras
        sleep(2)
        self.oHelper.Screenshot("compras_005")
        pyautogui.click(34,395)# sair
        sleep(2)
        self.oHelper.Screenshot("compras_006")
        pyautogui.click(1143,592)# confirmar
        sleep(1)
        self.oHelper.Screenshot("compras_007")


   

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
    def tearDownClass(self):
        self.oHelper.TearDown()



if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(test_test('test_test'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)