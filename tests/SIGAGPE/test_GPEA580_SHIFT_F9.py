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

#---------------------------------------------------
# CALCULO  DE TODA A FOLHA COM PARAMETRO SHIFT+F9
#----------------------------------------------------

# ESSE PROCESSO E DEMORADO REQUER ACOMPANHAMENTO DO USUARIO PARA ACOMPANHAR O TIME MALT

class GPEA580_SHIFT_F9(unittest.TestCase):
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

        

    def test_Calculo_folha_SHIFT_F9(self):

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
        self.oHelper.Screenshot("SHIFT+F9_01.png") 
        
        #-----------------------
        # CALCULAR FOLHA SHIFT+F9
        #-----------------------
        
        sc = SeleniumCommands(self.oHelper._Webapp__webapp.driver)
        sc.send_key('body',Keys.SHIFT+Keys.F9)
        
   
        if self.oHelper.IfExists("Deseja processar toda a Folha?"):
            self.oHelper.Screenshot("SHIFT+F9_02.png")
            self.oHelper.SetButton('Sim')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
            
        self.oHelper.WaitHide("Processando")
        self.oHelper.WaitShow("Calculando")
        self.oHelper.Screenshot("SHIFT+F9_03.png")
        sleep(90)
        self.oHelper.Screenshot("SHIFT+F9_04.png")
        self.oHelper.SetButton('x')
        
        #---------------------
        # CONSULTAR CALCULO 
        #---------------------
        
        #------------------------------------
        # PESQUISAR O FUNCIONARIO PARA O CALCULO
        #------------------------------------ 
        self.oHelper.WaitShow("Lançamentos por Período")
        self.oHelper.SearchBrowse(self.filial + self.Matricula, key="Filial+matricula+Nome")
        self.oHelper.Screenshot("SHIFT+F9_05.png")
        self.oHelper.ScrollGrid(column="Matricula", match_value = self.Matricula, grid_number=1)
        self.oHelper.Screenshot("SHIFT+F9_06.png")
        self.oHelper.SetButton('Alterar')   
        self.oHelper.WaitShow("Lançamentos por Funcionário")        
        self.oHelper.Screenshot("SHIFT+F9_07.png")
        sc = SeleniumCommands(self.oHelper._Webapp__webapp.driver)
        sc.send_key('body',Keys.F7)
        self.oHelper.ScrollGrid(column="Codigo Verba", match_value= "120",          grid_number=1)
        self.oHelper.Screenshot("SHIFT+F9_08.png")
        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Confirmar') 
        self.oHelper.SetButton("Salvar")
        self.oHelper.WaitShow("Lançamentos por Período")
        self.oHelper.AssertTrue()
       
     
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_Calculo_folha_SHIFT_F9")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
        
            

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA580_SHIFT_F9('test_Calculo_folha_SHIFT_F9'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
