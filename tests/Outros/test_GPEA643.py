# gestão disciplinar  Atualizações > Controle Disciplinar > Gestão Disciplinarfrom tir.technologies.core.base import By

#python -m pytest tests/Outros/test_GPEA643.py -v -s

from tir import Webapp
from pytest import mark
import unittest
from time import sleep
from os import getcwd
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')

# .\venv\Scripts\python.exe -m pytest tests/Outros/test_GPEM020_VTR.py -s

#------------------------
# CALCULO DE ROTEIRO VTR
#------------------------

class GPEM020_VTR(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.filial = '01'
        self.Matricula = '000016'
        self.dataref = (datetime.today()-timedelta(days=5)).strftime("%d/%m/%Y") # AJUSTAR DATA PARA PERIODO EM ABERTO
        self.Processo = '00001'
        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', self.dataref, '99', self.filial, '07')
        
        self.oHelper.SetLateralMenu("Atualizações > Funcionários > Funcionários")
        
       
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



        #self.oHelper.SearchBrowse(self.Matricula, column="Matricula")

        #self.oHelper.ClickCheckBox("Search",1)
        self.oHelper.ClickImage("▼")

        self.oHelper.SetButton("|")
        self.oHelper.ClickFolder("Coluna")
        sleep(50)

            
        
        self.oHelper.WaitShow("Processo de Calculo")
        self.oHelper.WaitShow("Este programa realiza processos de calculos")
        self.oHelper.Screenshot("roteiroVTR_01.png")
        
        self.oHelper.SetButton("Parametros")
        sleep(5)
        

        self.oHelper.AssertTrue()
        print("------------------------------------------------")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_Calculo_Roteiro_VTR")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEM020_VTR('test_Calculo_Roteiro_VTR'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
