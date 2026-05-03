from pytest import mark
import unittest
from time import sleep
from os import getcwd
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')
from tir.technologies.core.base import By
from tir import Webapp

class CTBA211_02(unittest.TestCase):
    @classmethod
    def setUpClass(self):
                                                                        
       
        self.filial = '02DF0001'
        self.dataref = (datetime.today()-timedelta(days=5)).strftime("%d/%m/%Y") 
        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', self.dataref, '02', self.filial, '07')
                
        
        self.oHelper.SetLateralMenu("Miscelanea > Cálculos > Integrações")
        
    def test_integração_do_sistema_com_todos_os_roteiros(self):

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
            
            
            
        #-------------------------------------------------------------
        # VALIDAR INTEGRAÇÃO DO SISTEMA DA FOLHA COM TODOS OS ROTEIROS
        #-------------------------------------------------------------
        sleep(5)
        
        self.oHelper.SetValue("Processo","00001")

        self.oHelper.Screenshot("Integração_01")
        self.oHelper.SetButton("Outras Ações","Inverter Seleção")
        sleep(3)
        self.oHelper.Screenshot("Integração_02")
        
        self.oHelper.SetButton("Integrar")
        
        if self.oHelper.IfExists("Integrações Com a Folha de Pagamento"):
            self.oHelper.SetButton("Executar")
            self.oHelper.Screenshot("Integração_03")
            self.oHelper.SetButton('OK')
            sleep(130)
            self.oHelper.Screenshot("Integração_04")
            sleep(130)
            self.oHelper.Screenshot("Integração_05")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
        
        self.oHelper.Screenshot("Integração_06")

        if self.oHelper.IfExists("Nenhum roteiro selecionado."):
            self.oHelper.Screenshot("Integração_07")
            self.oHelper.CheckHelp(text="Nenhum roteiro selecionado.", button="Fechar")
        sleep(1)
        self.oHelper.SetButton("x")
        self.oHelper.AssertTrue()
        print("")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 integrar o sistema da foha com todos os roteiros")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
        
            

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CTBA211_02('test_integração_do_sistema_com_todos_os_roteiros'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)