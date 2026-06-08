from tir.technologies.core.base import By
from tir import Webapp
from pytest import mark
import unittest
from time import sleep
from os import getcwd
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')

# .\venv\Scripts\python.exe -m pytest tests/Outros/test_GPEA020_01.py -s
# #cd Testes-Protheus .\venv\Scripts\activate pytest TESTS/SIGAGPE/GPEA020/test_GPEA020.py

#------------------------
# EXCLUSÃO DE DEPENDENTES
#------------------------

class GPEA020(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.Matricula = '227900'
        cls.filial = '01'
        cls.DataNasc = (datetime.today()-timedelta(days=360)).strftime("%d/%m/%Y")
        cls.DataEntrega = (datetime.today()-timedelta(days=20)).strftime("%d/%m/%Y")  
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '07')
        
        cls.oHelper.SetLateralMenu("Atualizações > Funcionários > Dependentes")
        
  

    def test_Cadastro_de_dependentes(self):

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
            
        #----------------------------------
        # EXCLUSÃO DEPENDENTES AO FUNCIONARIO
        #----------------------------------
        
        self.oHelper.WaitShow("Dependentes")
        
        
        self.oHelper.SetButton("Outras Ações","Pesquisar")
        self.oHelper.SetButton("Parâmetro")
        self.oHelper.SetValue("Filial",self.filial)
        self.oHelper.SetValue("Matricula",self.Matricula)
        self.oHelper.SetButton("OK")
        sleep(0.5)
        
        
        self.oHelper.SetButton("Manutenção")
        
        self.oHelper.SearchBrowse(self.filial)
        sleep(0.3)
        self.oHelper.SetButton("OK")
         
        self.oHelper.WaitShow("Funcionários - MANUTENÇÃO")
        sleep(1)
        self.oHelper.SetKey("Delete")
        sleep(0.5)    
       
        self.oHelper.SetButton("Confirmar")
        
        
        sleep(1)
        if self.oHelper.IfExists("Atenção!"):
            self.oHelper.WaitShow("Registro enviado para o TAF com sucesso!")
            self.oHelper.Screenshot("dependente01.png")
            self.oHelper.SetButton("OK")
            
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        if self.oHelper.IfExists("Registro alterado com sucesso."):
            self.oHelper.Screenshot("dependente02.png")
            self.oHelper.SetButton("Fechar")
            
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        self.oHelper.WaitShow("Dependentes")
        self.oHelper.SetButton("Visualizar")
        sleep(0.5)
        
        self.oHelper.WaitShow("Funcionários - VISUALIZAR")
        self.oHelper.Screenshot("dependente03.png")
        self.oHelper.SetButton("Fechar")
        sleep(0.5)
        self.oHelper.WaitShow("Dependentes")
        
        print("/")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_exclusão_de_dependentes")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
        
            

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA020('test_Exclusão_de_dependentes'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
