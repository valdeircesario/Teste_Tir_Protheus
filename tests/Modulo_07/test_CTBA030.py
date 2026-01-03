from tir import Webapp
from os import getcwd
import unittest
from datetime import datetime
from time import sleep
DateSystem = datetime.today().strftime('%d/%m/%Y')

 # # python -m pytest tests/Modulo_02/test_CTBA030.py -v -s --html=reports/report_CTBA030.html --self-contained-html

#------------------------------------------
#-- Teste CTBA030 - Cadastro de Centro de Custos
#------------------------------------------


class CTBA030(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       
        cls.CentroCusto = '011'# SEMPRE USAR 3 DIGITOS
        cls.Descricao = 'GEREM'# SEMPRE RENOMEAR
        cls.filial = '01'
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros > Centro de Custos")

    def test_de_incluir_Centro_de_Custo(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        self.oHelper.WaitShow("Cadastro C Custo")
        
        self.oHelper.SetButton("Incluir")
        sleep(1)
        self.oHelper.WaitShow("Cadastro C Custo - INCLUIR")
        self.oHelper.SetValue("CTT_CUSTO", self.CentroCusto)
        self.oHelper.SetValue("CTT_DESC01", self.Descricao)
        self.oHelper.Screenshot("CentroCusto.png")
        self.oHelper.SetKey("TAB") 

        self.oHelper.SetButton("Salvar")
        sleep(1)
        self.oHelper.SetButton("Cancelar")
        self.oHelper.WaitShow("Cadastro C Custo")
        self.oHelper.Screenshot("CentroCusto01.png")

        self.oHelper.SetButton("Visualizar")

        #-------------------------
        # Visualização da inclusão
        #-------------------------

        self.oHelper.WaitShow("Centro de Custo - VISUALIZAR")
        self.oHelper.CheckResult("CTT_CUSTO", self.CentroCusto)
        self.oHelper.CheckResult("CTT_DESC01", self.Descricao)
        self.oHelper.Screenshot("CentroCusto02.png")
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Cadastro C Custo")
        self.oHelper.Screenshot("CentroCusto03.png")

        self.oHelper.AssertTrue()
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_incluir_Centro_de_Custo")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CTBA030('test_de_incluir_Centro_de_Custo'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)