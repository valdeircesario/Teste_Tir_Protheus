from tir.technologies.core.base import By
from tir import Webapp
from pytest import mark
import unittest
from time import sleep
from os import getcwd
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')

# .\venv\Scripts\python.exe -m pytest tests/test_Roteiros.py -s

#------------------------
# CALCULO DE ROTEIROS VTR
#------------------------

class ROTEIRO(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.filial = '02DF0001'
        self.Roteiro = 'VTR'
        self.Log = 'VTR'
        self.dataref = (datetime.today()-timedelta(days=90)).strftime("%d/%m/%Y")
        self.Processo = '00001'
        

        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', self.dataref, '02', self.filial, '07')
        
        self.oHelper.SetLateralMenu("Miscelanea > Cálculos (13)> Por Roteiros")
        
       
    def test_Calculo_Roteiro_VTR(self):

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
            
        
        self.oHelper.WaitShow("Processo de Calculo")
        self.oHelper.WaitShow("Este programa realiza processos de calculos")
        
        self.oHelper.SetButton("Parametros")
        sleep(5)
        self.oHelper.SetValue("Processo ?",self.Processo,check_value=False)
        self.oHelper.SetValue("Roteiro ?",self.Roteiro,check_value=False)
        sleep(0.5)
        
        self.oHelper.SetButton("OK")
        sleep(5)
        
        
        if self.oHelper.IfExists("Parametros"):
            self.oHelper.SetButton("OK")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
        
        
        
        
        self.oHelper.SetButton("Calcular")
        
        
        if self.oHelper.IfExists("Confirma configuracäo dos parametros?"):
            self.oHelper.SetButton("Sim")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        if self.oHelper.IfExists("Nenhum filtro foi selecionado! Processar toda a tabela?"):
            self.oHelper.SetButton("Sim")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        sleep(2)  
        
        self.oHelper.WaitShow("Log de Ocorrencias no Processo de Calculo")

        
        
        if self.oHelper.IfExists("Log de Ocorrencias no Processo de Calculo"):
            self.oHelper.Screenshot("roteiroVTR.png")
            #self.oHelper.ClickCheckBox("Em Disco",double_click=True)
            self.oHelper.SetButton("OK")
            self.oHelper.AssertTrue()
        else:
            sleep(5)
        
        
    
        self.oHelper.SetButton("Sair")
        sleep(5)
        
        
        ##### VERIFICA NO SPOOL #####
        
        self.oHelper.SetLateralMenu("Miscelanea > Spool")
        
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

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ROTEIRO('test_Calculo_Roteiro_VTR'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
