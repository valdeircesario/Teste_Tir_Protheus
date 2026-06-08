import pyautogui
import unittest
import logging
from time import sleep
from os import getcwd, path
from datetime import datetime, timedelta
from os import getcwd
from tir import Webapp



class GPEA133(unittest.TestCase):
    
    # SETUP
    @classmethod
    def setUpClass(cls):
        
        
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
        pyautogui.click(28,282)# nescessidade de compras
        sleep(1)
        sleep(1)
        self.oHelper.Screenshot("compras_001")
        pyautogui.click(312,440)# botão de busca
        sleep(1)
        pyautogui.write('000000000002605', interval=0.1)
        sleep(1)
        pyautogui.press('enter')
        sleep(1)
        self.oHelper.Screenshot("compras_003")
        pyautogui.click(90,626)#selecionar linha
        sleep(5)
        pyautogui.click(36,325)# cotações
        sleep(2)
        self.oHelper.Screenshot("compras_004")
        sleep(2)
        pyautogui.click(28,356)# sair
        sleep(2)
        self.oHelper.Screenshot("compras_006")
        pyautogui.click(1385,681)# confirmar
        sleep(1)
        self.oHelper.Screenshot("compras_007")


   

    
        
        
        
    @classmethod
    def tearDownClass(cls):
        logging.info("Encerrando teste")
        cls.oHelper_Poui.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA133('test_test'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)