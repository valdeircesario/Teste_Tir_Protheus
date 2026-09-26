import sys, os
sys.path.insert(0, os.path.join(os.getcwd()))
from selenium.webdriver.common.keys import Keys
from tools.Selenium_commands import SeleniumCommands
from pytest import mark
import unittest
from time import sleep
from os import getcwd,path

# Garante a importação dos módulos da pasta utilis
PROJECT_ROOT = path.abspath(path.join(path.dirname(__file__), '..', '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
from time import sleep

from tir import Webapp
from utilis.md_reporter import TirReportAgent
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')

#----------------------------------------------------------------
# CALCULO FOLHA POR FUNCIONARIO 
#----------------------------------------------------------------

class GPEA580_Calcular_Folha(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from tir.technologies.core.base import By
        from tir import Webapp
                                                                        
        cls.filial = '01'
        cls.Matricula = '000007'
        cls.dataref = "29012026"# DATA DEVE SER A DATA DO ERIODO EM ABERTO
        
        configfile = getcwd() + '\\config.json'
        # 1. Instância base do TIR
        webapp_base = Webapp(configfile)
                
        # 2. Encapsula com o Agente de Relatório
        cls.oHelper = TirReportAgent(
            tir_instance=webapp_base,
            cod_modulo="07",
            nome_modulo="Gestão de Pessoal",
            ct_nome="test_GPEA580_01",
            descricao="calcular folha do funcionario"
        )
        cls.oHelper.Setup('SIGAMDI', cls.dataref, '99', cls.filial, '07')
        
        cls.oHelper.SetLateralMenu("Atualizações > Lançamentos > Por Funcionário ")
        cls.oHelper.SetButton('Confirmar')

        

    def test__Calcular_Folha(self):

        try:
            sleep(5)
            if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
                self.oHelper.SetButton('Fechar')
        
            sleep(2)
            if self.oHelper.IfExists("Moedas"):
                self.oHelper.CheckResult('Dolar', '0,0000')
                self.oHelper.SetButton('Confirmar')
        
            
            
            self.oHelper.WaitShow("Lançamentos por Período")
            self.oHelper.Screenshot("Folha/001") 
            
            #------------------------------------
            # PESQUISAR O FUNCIONARIO PARA O CALCULO
            #------------------------------------ 
            print('--------------------------Pesquisar funcionario')
            self.oHelper.SearchBrowse(self.Matricula, column="Matricula*")
            self.oHelper.Screenshot("Folha/002") 
            
            #-----------------------
            # CALCULAR FOLHA CTRL+F9
            #-----------------------
            print('--------------------------calcular com ctrl+f9')
            sc = SeleniumCommands(self.oHelper._Webapp__webapp.driver)
            sc.send_key('body',Keys.CONTROL+Keys.F9)
            
    
            self.oHelper.WaitShow("Deseja processar o contracheques do funcionario(a):")
            self.oHelper.Screenshot("Folha/003") 
            self.oHelper.SetButton('Sim')
                
            self.oHelper.Screenshot("Folha/004") 
            self.oHelper.WaitProcessing('Processando')
            self.oHelper.Screenshot("Folha/005") 
            self.oHelper.SetButton('x')
            sleep(2)
            
            #---------------------
            # CONSULTAR CALCULO 
            #---------------------
            print('--------------------------Consultar calculo')
            self.oHelper.SetButton('Alterar')   
            self.oHelper.WaitShow("Lançamentos por Funcionário")        
            self.oHelper.Screenshot("Folha/006") 
            self.oHelper.SetKey("F7",wait_change=False)
            self.oHelper.ScrollGrid(column="Codigo Verba", match_value= "120")
            self.oHelper.Screenshot("Folha/007") 
            self.oHelper.LoadGrid()
            self.oHelper.SetButton('Confirmar') 
            self.oHelper.SetButton("Salvar")
            self.oHelper.WaitShow("Lançamentos por Período")
            self.oHelper.AssertTrue()


        except Exception as e:
            self.oHelper.registrar_erro(e)
            raise e
        finally:
            self.oHelper.salvar_relatorio()
       
     
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test__Calcular_Folha")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
        
            

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA580_Calcular_Folha('test__Calcular_Folha'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
