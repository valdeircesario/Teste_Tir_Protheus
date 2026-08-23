from tir.technologies.core.base import By
from tir import Webapp
from pytest import mark
import unittest
from time import sleep
from os import getcwd
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')

#  .\venv\Scripts\python.exe -m pytest .\TESTS\SIGAGPE\GPEA320\test_GPEA320.py 

#------------------------
# CALCULO E RESCISÃO
#------------------------

class GPEA320(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.filial = '01'
        self.Matricula = '00XXX'
        self.TipoRes ='02'
        self.dataref = (datetime.today()-timedelta(days=5)).strftime("%d/%m/%Y")
        

        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', self.dataref, '99', self.filial, '07')
        
        self.oHelper.SetLateralMenu("Miscelanea > Cálculos (13)> Rescisão")
        
       
    def test_Calculo_Rescisão(self):

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
            
        
        self.oHelper.WaitShow("Funcionários")
        self.oHelper.Screenshot("GPEA320_01.png")
        self.oHelper.SetButton("Filtrar")
        sleep(0.2)
        self.oHelper.WaitShow("Gerenciador de Filtros")
        self.oHelper.ClickCheckBox("Situacao Normal",1)
        self.oHelper.Screenshot("GPEA320_02.png")
        self.oHelper.SetButton("Aplicar filtros selecionados")
        sleep(1) 
        self.oHelper.SearchBrowse(self.filial + self.Matricula + self.Nome, key="Filial+Matricula+Nome")
        sleep(1)
        
        self.oHelper.SetButton('Incluir')
        self.oHelper.SearchBrowse(self.filial)
        self.oHelper.Screenshot("GPEA320_03.png")
        self.oHelper.SetButton("OK")
        sleep(1)
        
        
        
        self.oHelper.WaitShow("Rescisões - INCLUIR")
        self.oHelper.Screenshot("GPEA320_04.png")
        
        self.oHelper.SetValue("RG_TIPORES",self.TipoRes,       check_value=False)
        self.oHelper.SetValue("RG_DATAHOM",self.dataref,         check_value=False)
        self.oHelper.SetValue("RG_DTGERAR",self.dataref,         check_value=False)
        self.oHelper.SetValue("RG_DTAVISO",self.dataref,         check_value=False)
        self.oHelper.SetKey("TAB")
        self.oHelper.Screenshot("GPEA320_05.png")
        sleep(0.5)
        
        self.oHelper.SetKey("F6")
        self.oHelper.Screenshot("GPEA320_06.png")
        sleep(2)
        
        
        if self.oHelper.IfExists("Atenção"):
            self.oHelper.Screenshot("GPEA320_07.png")
            self.oHelper.SetButton("Sim")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        self.oHelper.Screenshot("GPEA320_08.png")
        sleep(6)
        
        if self.oHelper.IfExists("Log de Ocorrencias no Processo de Calculo"):
            self.oHelper.SetButton("Em Disco")
            self.oHelper.Screenshot("GPEA320_09.png")
            self.oHelper.SetButton("Cancelar")
            sleep(1)
            self.oHelper.Screenshot("GPEA320_10.png")
            self.oHelper.SetButton("Sair")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            sleep(5)
        sleep(2)
        
        self.oHelper.WaitShow("Rescisões - INCLUIR")
        sleep(1)
        self.oHelper.SetButton("Confirmar")
        
        self.oHelper.WaitShow("Funcionários")
        
        self.oHelper.Screenshot("GPEA320_11.png")

        self.oHelper.AssertTrue()
        
        print("/")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_Calculo_de_Rescisão")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA320('test_Calculo_Recissão'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
