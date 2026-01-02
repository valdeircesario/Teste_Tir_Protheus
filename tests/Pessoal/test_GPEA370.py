from tir import Webapp
from os import getcwd
import unittest
from datetime import datetime
from time import sleep
DateSystem = datetime.today().strftime('%d/%m/%Y')

# .\venv\Scripts\python.exe -m pytest tests/Pessoal/test_GPEA370.py -v -s --html=report_GPEA370.html --self-contained-html
#------------------------------------------
#-- Teste GPEA370 - Cadastro de Cargos
#------------------------------------------


class GPEA370(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       
        cls.Cargo = '0005'
        cls.Descrição = 'SUPERVISOR DE EQUIPE'
        cls.CentroCusto = '003'
        cls.filial = '01'
        cls.Depatamento = '000000006'
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros > Cargos")

    def test_de_incluir_Cagos(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        self.oHelper.WaitShow("Cargo")
        
        self.oHelper.SetButton("Incluir")
        sleep(1)
        self.oHelper.WaitShow("Cargo - INCLUIR")
        self.oHelper.SetValue("Q3_CARGO", self.Cargo)
        self.oHelper.SetKey("TAB") 
        self.oHelper.SetValue("Q3_DESCSUM", self.Descrição)
        self.oHelper.SetKey("TAB")
        self.oHelper.SetValue("Q3_CC", self.CentroCusto)
        self.oHelper.SetKey("TAB") 
        self.oHelper.SetValue("Q3_DEPTO", self.Depatamento)
        self.oHelper.SetKey("TAB") 

        self.oHelper.SetButton("Confirmar")

        if self.oHelper.IfExists("Registro inserido com sucesso."):
            self.oHelper.SetButton("Fechar")
            self.oHelper.AssertTrue()
            
        
        self.oHelper.WaitShow("Cargo")
        sleep(1)

        #-------------------------
        # Visualização da inclusão
        #-------------------------

        self.oHelper.SetButton("Visualizar")

        self.oHelper.WaitShow("Cargo - VISUALIZAR")
        self.oHelper.CheckResult("Q3_CARGO", self.Cargo)
        self.oHelper.CheckResult("Q3_DESCSUM", self.Descrição)
        self.oHelper.CheckResult("Q3_CC", self.CentroCusto)
        self.oHelper.CheckResult("Q3_DEPTO", self.Depatamento)
        self.oHelper.SetButton("Fechar")
        sleep(1)


        self.oHelper.WaitShow("Cargo")

        self.oHelper.AssertTrue()
        print("🎯 test_de_incluir_Cagos")
        print("✅ Teste finalizado com sucesso")

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA370('test_de_incluir_Cagos'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)