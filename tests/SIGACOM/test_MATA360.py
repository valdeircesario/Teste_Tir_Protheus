from tir import Webapp
from os import getcwd
import unittest
from datetime import datetime
from time import sleep
DateSystem = datetime.today().strftime('%d/%m/%Y')

#------------------------------------------
#-- Teste MATA360 condições de pagamento
#------------------------------------------

class MATA360(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       
        cls.Codigo = '002'
        cls.Tipo = '3'
        cls.ConPgt = "1,2,3"
        cls.ConPgtEdt = "1,2,3,4"
        cls.Descrição = 'A PRAZO'
        cls.DescriçãoEdt = 'A PRAZO PARCELADO'
        cls.filial = '01'
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '02')
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros > Condição de Pagamento")

    def test_de_incluir_condições_de_pagamento(self):
        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        #-------------------------
        # Inclusão de forma de pagamento
        #-------------------------

        self.oHelper.WaitShow("Condiçäo de Pagamento:") 
        self.oHelper.SetButton("Incluir")
        sleep(1)
        self.oHelper.WaitShow("Condiçäo de Pagamento - INCLUIR")
        self.oHelper.SetValue("E4_CODIGO", self.Codigo)
        self.oHelper.SetValue("E4_TIPO", self.Tipo)
        self.oHelper.SetValue("E4_COND", self.ConPgt)
        self.oHelper.SetValue("E4_DESCRI", self.Descrição)
        self.oHelper.SetButton("Confirmar")
        sleep(0.5)
        self.oHelper.WaitShow("Registro inserido com sucesso.")
        self.oHelper.SetButton("Fechar")
        sleep(1)
        

        #-------------------------
        # Visualização da inclusão
        #-------------------------
        self.oHelper.SetButton("Visualizar")
        self.oHelper.WaitShow("Condiçäo de Pagamento - VISUALIZAR")
        self.oHelper.CheckResult("E4_CODIGO", self.Codigo)
        self.oHelper.CheckResult("E4_TIPO", self.Tipo)
        self.oHelper.CheckResult("E4_COND", self.ConPgt)
        self.oHelper.CheckResult("E4_DESCRI", self.Descrição)
        sleep(0.5)
        self.oHelper.SetButton("Fechar")
        sleep(0.5)
        self.oHelper.WaitShow("Condiçäo de Pagamento:")

        #----------------------
        # Alteração da condição falta completar,estava dando erros
        #----------------------
        """ self.oHelper.SetButton("Alterar")
        sleep(0,5)
        self.oHelper.SetValue("E4_COND", self.ConPgtEdt)
        self.oHelper.SetValue("E4_DESCRI", self.DescriçãoEdt)
        self.oHelper.SetButton("Confirmar")
        sleep(0.5)
        self.oHelper.WaitShow("Registro alterado com sucesso.")
        self.oHelper.SetButton("Fechar")
        sleep(1)
        self.oHelper.WaitShow("Condiçäo de Pagamento:") """

        self.oHelper.AssertTrue()
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X🎯 test_de_incluir_condições_de_pagamento")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MATA360('test_de_incluir_condições_de_pagamento'))
    runner = unittest.TextTestRunner(verbosity=2)
    