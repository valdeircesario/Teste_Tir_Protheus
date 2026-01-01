from tir import Webapp
from os import getcwd
import unittest
from datetime import datetime
from time import sleep

 # .\venv\Scripts\python.exe -m pytest tests/Pessoal/test_GPEA030.py -v -s --html=report_GPEA030.html --self-contained-html

DateSystem = datetime.today().strftime('%d/%m/%Y')

class GPEA030(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       
        cls.Funcao = '00014'
        cls.Descrição = 'AUDITOR INTERN0'
        cls.filial = '01'
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros > Funções")

    def test_Ponto_fixo_caso_de_uso(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        self.oHelper.WaitShow("Cadastro de Funções")
        
        self.oHelper.SetButton("Incluir")
        sleep(1)
        self.oHelper.WaitShow("Funções - INCLUIR")
        self.oHelper.SetValue("RJ_FUNCAO", self.Funcao)
        self.oHelper.SetValue("RJ_DESC", self.Descrição)
        self.oHelper.SetKey("TAB") 

        self.oHelper.SetButton("Confirmar")

        if self.oHelper.IfExists("Registro inserido com sucesso."):
            self.oHelper.SetButton("Fechar")
            self.oHelper.AssertTrue()
            
        
        self.oHelper.WaitShow("Cadastro de Funções")

        self.oHelper.SetButton("Visualizar")

        #-------------------------
        # Visualização da inclusão
        #-------------------------

        self.oHelper.WaitShow("Funções - VISUALIZAR")
        self.oHelper.CheckResult("RJ_FUNCAO", self.Funcao)
        self.oHelper.CheckResult("RJ_DESC", self.Descrição)
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Cadastro de Funções")




        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA030('test_de_incluir_Funções'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)