from tir.technologies.core.base import By
from tir import Webapp
from pytest import mark
import unittest
from time import sleep
from os import getcwd
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')

# .\venv\Scripts\python.exe -m pytest tests/test_Spool.py -s

#------------------------
# CONFERENCIA DE LOG NO SPOOL
#------------------------

class SPOOL(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.filial = '02DF0001'
        self.Log = 'VTR'
        self.dataref = (datetime.today()-timedelta(days=90)).strftime("%d/%m/%Y")
        self.Processo = '00001'
        

        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', self.dataref, '02', self.filial, '07')
        
        self.oHelper.SetLateralMenu("Miscelanea > Spool")
        
    

    def test_Conferir_Log_No_Spool(self):

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
            
        #----------------
        # PROCURA O LOG NO SPOOL
        #----------------
            
            
        self.oHelper.SetValue("Localizar",self.Log,check_value=False)
        sleep(0.2)
        self.oHelper.SetKey("ENTER")
        sleep(0.2)
        if self.oHelper.IfExists("Log de Ocorrencias no Processo de Calculo"):
            self.oHelper.Screenshot("roteiroVTR.png")
            self.oHelper.SetButton("Sair")
            
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(SPOOL('test_Conferir_Log_No_Spool'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
