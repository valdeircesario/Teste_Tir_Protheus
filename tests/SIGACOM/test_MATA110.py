from tir import Webapp
from os import getcwd
import unittest
from datetime import datetime
from time import sleep
DateSystem = datetime.today().strftime('%d/%m/%Y')

#------------------------------------------
#-- Teste MATA110  solicitação de compras
#------------------------------------------

class MATA110(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       
        cls.Produto = '000000000000002'
        cls.Quantidade = '11'
        cls.Observacao = "TESTE DE SOLICITAÇÃO DE COMPRAS"
        cls.filial = '01'
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '02')
        cls.oHelper.SetLateralMenu("Atualizações > Solicitações > Solicitação de Compras")

    def test_de_incluir_solicitação_de_conpras(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        #-------------------------
        # Inclusão de solicitação de compras
        #-------------------------

        self.oHelper.WaitShow("Solicitaçäo de Compras") 
        self.oHelper.SetButton("Incluir")
        sleep(1)
        self.oHelper.WaitShow("Solicitaçäo de Compras - INCLUIR")

        self.oHelper.SetValue("Produto", self.Produto, grid=True, grid_number=1, check_value=False)
        self.oHelper.SetValue("Quantidade", self.Quantidade, grid=True, grid_number=1, check_value=False)
        self.oHelper.SetValue("Observacao", self.Observacao, grid=True, grid_number=1, check_value=False)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")
        sleep(1)
        self.oHelper.SetButton("Cancelar")
        sleep(1)
        self.oHelper.WaitShow("Solicitaçäo de Compras")

        #-------------------
        # VISUALIZAR
        #-------------------
        

        self.oHelper.SetButton("Visualizar")
        sleep(0.5)
        self.oHelper.WaitShow("Solicitaçäo de Compras")
        self.oHelper.Screenshot("Solicitação_Compra01.png")
        sleep(0.5)
        self.oHelper.SetButton("Confirmar")
        sleep(0.5)
        self.oHelper.WaitShow("Solicitaçäo de Compras")


        self.oHelper.AssertTrue()
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_incluir_solicitação_de_compras")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MATA110('test_de_incluir_solicitação_de_compras'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)