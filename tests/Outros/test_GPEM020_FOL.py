from tir.technologies.core.base import By
from tir import Webapp
from pytest import mark
import unittest
from time import sleep
from os import getcwd
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')

# .\venv\Scripts\python.exe -m pytest tests/Outros/test_GPEM020_FOL.py -s

#------------------------
# CALCULO DE ROTEIRO FOL
#------------------------

class GPEM020_FOL(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.filial = '02DF0001'
        self.Roteiro = 'FOL'
        self.dataref = (datetime.today()-timedelta(days=5)).strftime("%d/%m/%Y")
        self.Processo = '00001'
        

        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', self.dataref, '02', self.filial, '07')
        
        self.oHelper.SetLateralMenu("Miscelanea > Cálculos (13)> Por Roteiros")
        
       
    def test_Calculo_Roteiro_FOL(self):

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
        self.oHelper.Screenshot("RoteiroFOL_01.png")
        
        self.oHelper.SetButton("Parametros")
        sleep(5)
        self.oHelper.SetValue("Processo ?",self.Processo,           check_value=False)
        self.oHelper.SetValue("Roteiro ?",self.Roteiro,             check_value=False)
        sleep(0.5)
        self.oHelper.Screenshot("RoteiroFOL_02.png")
        
        self.oHelper.SetButton("OK")
        sleep(5)
        
        
        if self.oHelper.IfExists("Parametros"):
            sleep(1)
            self.oHelper.Screenshot("RoteiroFOL_03.png")
            self.oHelper.SetButton("OK")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
        
        self.oHelper.SetButton("Calcular")
        self.oHelper.Screenshot("RoteiroFOL_04.png")
        
        
        if self.oHelper.IfExists("Confirma configuracäo dos parametros?"):
            self.oHelper.Screenshot("RoteiroFOL_05.png")
            self.oHelper.SetButton("Sim")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        if self.oHelper.IfExists("Nenhum filtro foi selecionado! Processar toda a tabela?"):
            self.oHelper.Screenshot("RoteiroFOL_06.png")
            self.oHelper.SetButton("Sim")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        sleep(300) 
        
        self.oHelper.Screenshot("RoteiroFOL_07.png")
        sleep(300)
        self.oHelper.Screenshot("RoteiroFOL_08.png")
        sleep(300)
        
        self.oHelper.WaitShow("Log de Ocorrencias no Processo de Calculo") 
        
        if self.oHelper.IfExists("Log de Ocorrencias no Processo de Calculo"):
            self.oHelper.ClickLabel("Em Disco")
            self.oHelper.Screenshot("RoteiroFOL_09.png")
            self.oHelper.SetButton("OK")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        sleep(45)
        self.oHelper.Screenshot("RoteiroFOL_10.png")
    
        self.oHelper.SetButton("Sair")
        sleep(10)

        self.oHelper.AssertTrue()
        print("------------------------------------------------")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_Calculo_Roteiro_FOL")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEM020_FOL('test_Calculo_Roteiro_FOL'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
