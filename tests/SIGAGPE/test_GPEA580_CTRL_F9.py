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
                                                                        
        cls.filial = '01'
        cls.Matricula = '00123'
        cls.dataref = (datetime.today()-timedelta(days=30)).strftime("%d/%m/%Y")
        
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', cls.dataref, '02', cls.filial, '07')
        
        cls.oHelper.SetLateralMenu("Atualizações > Lançamentos > Por Funcionário ")
        cls.oHelper.SetButton('Confirmar')

        

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
        print('--------------------------Pesquisar funcionario')
        self.oHelper.SearchBrowse(self.filial + self.Matricula, key="Filial+matricula+Nome")
        self.oHelper.Screenshot("ctrlF9_02.png")
        self.oHelper.ScrollGrid(column="Matricula", match_value = self.Matricula, grid_number=1)
        self.oHelper.Screenshot("ctrlF9_03.png")
        
        #-----------------------
        # CALCULAR FOLHA CTRL+F9
        #-----------------------
        print('--------------------------calcular com ctrl+f9')
        sc = SeleniumCommands(self.oHelper._Webapp__webapp.driver)
        sc.send_key('body',Keys.CONTROL+Keys.F9)
        
   
        self.oHelper.WaitShow("Deseja processar o contracheques do funcionario(a):")
        self.oHelper.Screenshot("ctrlF9_04.png")
        self.oHelper.SetButton('Sim')
            
        self.oHelper.Screenshot("ctrlF9_05.png")
        self.oHelper.WaitProcessing('Processando')
        self.oHelper.Screenshot("ctrlF9_06.png")
        self.oHelper.SetButton('x')
        sleep(2)
        
        #---------------------
        # CONSULTAR CALCULO 
        #---------------------
        print('--------------------------Consultar calculo')
        self.oHelper.SetButton('Alterar')   
        self.oHelper.WaitShow("Lançamentos por Funcionário")        
        self.oHelper.Screenshot("ctrlF9_07.png")
        self.oHelper.SetKey("F7",wait_change=False)
        self.oHelper.ScrollGrid(column="Codigo Verba", match_value= "120")
        self.oHelper.Screenshot("ctrlF9_08.png")
        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Confirmar') 
        self.oHelper.SetButton("Salvar")
        self.oHelper.WaitShow("Lançamentos por Período")
        self.oHelper.AssertTrue()
       
     
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_Calculo_folha_CTRL_F9")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
        
            

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA580_CTRL_F9('test_Calculo_folha_CTRL_F9'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
