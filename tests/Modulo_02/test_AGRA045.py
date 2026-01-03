from tir import Webapp
from os import getcwd
import unittest
from datetime import datetime
from time import sleep
DateSystem = datetime.today().strftime('%d/%m/%Y')


# python -m pytest tests/Modulo_02/test_AGRA045.py -v -s --html=reports/report_AGRA045.html --self-contained-html
#------------------------------------------
#-- Teste AGRA045 - Cadastro de local de estoque
#------------------------------------------




class AGRA045(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       
        cls.Codigo = '03'
        cls.Descrição = 'EXTERNO'
        cls.filial = '01'
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '02')
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros > Locais de Estoque")

    def test_de_incluir_local_de_estoque(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        #-------------------------
        # Inclusão de local de estoque
        #-------------------------
        
        self.oHelper.SetButton("Incluir")
        sleep(1)
        self.oHelper.WaitShow("Locais de Estoque - INCLUIR")
        self.oHelper.SetValue("NNR_CODIGO", self.Codigo)
        self.oHelper.SetValue("NNR_DESCRI", self.Descrição)

        self.oHelper.SetButton("Confirmar")
        sleep(0.5)


       
        self.oHelper.WaitShow("Registro inserido com sucesso.")
        self.oHelper.SetButton("Fechar")
        sleep(1)
        

        #-------------------------
        # Visualização da inclusão
        #-------------------------
        self.oHelper.SetButton("Outras Ações","Visualizar")
        self.oHelper.WaitShow("Locais de Estoque - VISUALIZAR")
        self.oHelper.CheckResult("NNR_CODIGO", self.Codigo)
        self.oHelper.CheckResult("NNR_DESCRI", self.Descrição)
        sleep(0.5)
        self.oHelper.SetButton("Fechar")
        sleep(0.5)

        self.oHelper.AssertTrue()
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_incluir_local_de_estoque")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(AGRA045('test_de_incluir_local_de_estoque'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)