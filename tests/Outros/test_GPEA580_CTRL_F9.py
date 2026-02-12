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
    def setUpClass(self):
        from tir.technologies.core.base import By
        from tir import Webapp
                                                                        
        self.filial = '02DF0001'
        self.Matricula = '227884'
        self.dataref = (datetime.today()-timedelta(days=5)).strftime("%d/%m/%Y")
        
        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', self.dataref, '02', self.filial, '07')
        
        self.oHelper.SetLateralMenu("Atualizações > Lançamentos > Por Funcionário ")
        #self.oHelper.SetButton('Confirmar') -- observar essas linha, em meu ambiete de trabalho, o browser não visualiza a tela de trocar modulos.

        

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
            
            
        self.oHelper.WaitShow("Lançamentos por Período")
        self.oHelper.Screenshot("ctrlF9_01.png") 
        
        #------------------------------------
        # PESQUISAR O FUNCIONARIO PARA O CALCULO
        #------------------------------------ 
        self.oHelper.SearchBrowse(self.filial + self.Matricula, key="Filial+matricula+Nome")
        sleep(0.5)
        self.oHelper.Screenshot("ctrlF9_06.png")
        sleep(1) 
        self.oHelper.ScrollGrid(column="Matricula", match_value = self.Matricula, grid_number=1)
        sleep
        self.oHelper.Screenshot("ctrlF9_07.png")
        
        #-----------------------
        # CALCULAR FOLHA CTRL+F9
        #-----------------------
        
       

        sc = SeleniumCommands(self.oHelper._Webapp__webapp.driver)
        sc.send_key('body',Keys.CONTROL+Keys.F9)
        
   
        if self.oHelper.IfExists("Deseja processar o contracheques do funcionario(a):"):
            self.oHelper.Screenshot("ctrlF9_08.png")
            self.oHelper.SetButton('Sim')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        self.oHelper.Screenshot("ctrlF9_10.png")
        sleep(90)
        self.oHelper.Screenshot("ctrlF9_11.png")
        sleep(90) 
        self.oHelper.SetButton('x')
        sleep(2)
        
        #---------------------
        # CONSULTAR CALCULO 
        #---------------------
        
        self.oHelper.SetButton('Alterar')   
        sleep(5) 
        self.oHelper.WaitShow("Lançamentos por Funcionário")        
        self.oHelper.Screenshot("ctrlF9_12.png")
        sleep(5) 
        self.oHelper.SetKey("F7")
        sleep(1)
        self.oHelper.ScrollGrid(column="Codigo Verba", match_value= "120",          grid_number=1)
        self.oHelper.Screenshot("ctrlF9_13.png")
        self.oHelper.LoadGrid()
        sleep(1)
        self.oHelper.SetButton('Confirmar') 
        sleep(0.5) 
        self.oHelper.SetButton("Salvar")
        sleep(2)
        self.oHelper.WaitShow("Lançamentos por Período")
        self.oHelper.AssertTrue()
       
     
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
