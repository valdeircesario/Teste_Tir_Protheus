import sys, os
sys.path.insert(0, os.path.join(os.getcwd()))
from selenium.webdriver.common.keys import Keys
from tools.Selenium_commands import SeleniumCommands
from pytest import mark
import unittest
from time import sleep
from os import getcwd
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')

#----------------------------------------------------------------
# CALCULO FOLHA POR FUNCIONARIO COM PARAMETRO CTRL+F9
#----------------------------------------------------------------

class GPEA580_CTRL_F9(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from tir.technologies.core.base import By
        from tir import Webapp
                                                                        
        cls.filial = '02DF0001'
        cls.Matricula = '227884'
        cls.dataref = (datetime.today()-timedelta(days=30)).strftime("%d/%m/%Y")
        
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', cls.dataref, '02', cls.filial, '02')
        
        cls.oHelper.SetLateralMenu("Atualizações > Novo Fluxo de Compras > Novo Fluxo de Compras")
        cls.oHelper.SetButton('Confirmar') #-- observar essas linha, em meu ambiete de trabalho, o browser não visualiza a tela de trocar modulos.

        

    def test_Calculo_folha_CTRL_F9(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
            
        
        driver = self.oHelper._Webapp__webapp.drive 
        
        WebDriverWait(driver, 30).until( # type: ignore
        EC.presence_of_element_located((By.TAG_NAME, "body"))) # type: ignore
        driver.switch_to.default_content()
        driver.switch_to.frame(0)
        sc = SeleniumCommands(driver)
        sc.click_by_class_contains("po-icon-home")

        
         
        
        
        sc = SeleniumCommands(self.oHelper._Webapp__webapp.driver,wait_time=10)

        sc.click_by_class_contains("po-icon-home")

    
       
     
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_Calculo_folha_CTRL_F9")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
        
            

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA580_CTRL_F9('test_Calculo_folha_CTRL_F9'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
