import pyautogui
import unittest


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



from tir import Poui
import unittest
import sys
import logging
from time import sleep
from os import getcwd, path
from datetime import datetime, timedelta
from pytest import mark
import unittest
from time import sleep
from os import getcwd
# Ajuste de path (mantém compatível com TIR)
sys.path.insert(0, path.abspath(path.join(path.dirname(__file__), '../../')))

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tools.Selenium_commands import SeleniumCommands

from tir import Webapp





class test_test(unittest.TestCase):

    @classmethod
    def setup_class(cls):

        global driver
        driver = webdriver.Firefox()


        cls.filial = '01'
class GPEA133(unittest.TestCase):
    
    # SETUP
    @classmethod
    def setUpClass(cls):
        
        
        cls.oHelper_Poui = Poui()
        cls.filial = '02DF0001'
        cls.dataref = (datetime.today() - timedelta(days=5)).strftime("%d/%m/%Y")

        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)


        cls.oHelper.Setup('SIGAMDI', cls.dataref, '02', cls.filial, '02')
        cls.oHelper.SetLateralMenu("Atualizações > Novo Fluxo de Compras > Novo Fluxo de Compras")
        cls.oHelper.SetButton('Confirmar')

        # Tratativas padrão de ambiente
        if cls.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            cls.oHelper.SetButton('Fechar')

        if cls.oHelper.IfExists("Moedas"):
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


   

    # ==================================================
    # TESTE
    # ==================================================
    def test_geracao_relatorio_verba(self):
        


        # Evidência inicial
        

        
        #self.oHelper.SetButton('Imprimir')
        sleep(8)
        
        
        

    
    
    
        sc = SeleniumCommands(self.oHelper._Webapp__webapp.driver)
        sc.click_by_class_contains('po-icon-cart')
    

    
    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()

   
    @classmethod
    def tearDownClass(cls):
        logging.info("Encerrando teste")
        cls.oHelper_Poui.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(test_test('test_test'))
    suite.addTest(GPEA133('test_geracao_relatorio_verba'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)