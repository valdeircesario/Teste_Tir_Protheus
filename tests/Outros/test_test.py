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





class GPEA133(unittest.TestCase):
    
    # SETUP
    # ==================================================
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


    # ==================================================
    # TESTE
    # ==================================================
    def test_geracao_relatorio_verba(self):
        


        # Evidência inicial
        

        
        #self.oHelper.SetButton('Imprimir')
        sleep(8)
        
        
        

    # Clica no ícone do carrinho
        sc = SeleniumCommands(self.oHelper._Webapp__webapp.driver)
        sc.click_by_xpath("//*[contains(@class, 'po-icon-cart')]")
    

    
   
    @classmethod
    def tearDownClass(cls):
        logging.info("Encerrando teste")
        cls.oHelper_Poui.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA133('test_geracao_relatorio_verba'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)