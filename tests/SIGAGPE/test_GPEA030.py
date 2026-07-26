from tir import Webapp
from os import getcwd
import unittest
from datetime import datetime
from time import sleep
DateSystem = datetime.today().strftime('%d/%m/%Y')

 # # python -m pytest tests/SIGAGPE/test_GPEA030.py -v -s --html=reports/report_GPEA030.html --self-contained-html

#------------------------------------------
#-- Teste GPEA030 - Cadastro de Funções
#------------------------------------------


class GPEA030(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       
        cls.Funcao = '00016'
        cls.Descrição = 'TESTE DE FUNCAO'
        cls.DescricaoEdit = 'ASSITEMTE SENIOR '
        cls.Cargo = '0005'
        cls.filial = '01'
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros > Funções")

    def test_de_incluir_Funções(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        #-----------------------
        # Incluir Função
        #-----------------------

        print('-----------------------Incluir')
        self.oHelper.WaitShow("Cadastro de Funções")
        self.oHelper.Screenshot("Funcao/001") 
        self.oHelper.SetButton("Incluir")
        self.oHelper.WaitShow("Funções - INCLUIR")
        self.oHelper.Screenshot("Funcao/002")
        self.oHelper.SetValue("RJ_FUNCAO", self.Funcao,     check_value=False)
        self.oHelper.SetValue("RJ_DESC", self.Descrição,    check_value=False)
        self.oHelper.SetValue("RJ_CODCBO", "1234",          check_value=False)
        self.oHelper.SetValue("RJ_CARGO", self.Cargo,       check_value=False)
        self.oHelper.SetValue("RJ_ADDATA", DateSystem,      check_value=False)
        self.oHelper.SetKey("TAB",                          wait_change=False)
        self.oHelper.Screenshot("Funcao/003") 
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Registro inserido com sucesso.")
        self.oHelper.Screenshot("Funcao/004")
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Cadastro de Funções")
        self.oHelper.Screenshot("Funcao/005")

        

        #-------------------------
        # Visualização da inclusão
        #-------------------------
        print('--------------------Visualizar')
        self.oHelper.SetButton("Visualizar")
        self.oHelper.WaitShow("Funções - VISUALIZAR")
        self.oHelper.Screenshot("Funcao/006")
        self.oHelper.CheckResult("RJ_FUNCAO", self.Funcao)
        self.oHelper.CheckResult("RJ_DESC", self.Descrição)
        self.oHelper.CheckResult("RJ_CARGO", self.Cargo)
        self.oHelper.SetButton("Fechar")
        self.oHelper.Screenshot("Funcao/007")
        self.oHelper.WaitShow("Cadastro de Funções")

        #-------------------------
        # Edição do registro
        #-------------------------
        print('----------------------Alterar')
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow("Funções - ALTERAR")
        self.oHelper.Screenshot("Funcao/008")
        self.oHelper.SetValue("RJ_DESC", self.DescricaoEdit,check_value=False)
        self.oHelper.Screenshot("Funcao/009")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Registro alterado com sucesso.")
        self.oHelper.Screenshot("Funcao/010")
        self.oHelper.SetButton("Fechar")       
        self.oHelper.WaitShow("Cadastro de Funções")
        self.oHelper.Screenshot("Funcao/011")

        self.oHelper.AssertTrue()
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_incluir_Funções")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")



    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA030('test_de_incluir_Funções'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)