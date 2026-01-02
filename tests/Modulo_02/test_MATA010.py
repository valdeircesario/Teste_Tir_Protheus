from tir import Webapp
from os import getcwd
import unittest
from datetime import datetime
from time import sleep
DateSystem = datetime.today().strftime('%d/%m/%Y')

#.\venv\Scripts\python.exe -m pytest tests/Modulo_02/test_MATA010.py -v -s --html=report_MATA010.html --self-contained-html
#------------------------------------------
#-- Teste MATA010 - Cadastro de produtos
#------------------------------------------




class MATA010(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       
        cls.Codigo = '000000000000003'
        cls.Descrição = 'IMPRESSORA 3D'
        cls.Tipo = 'ME'
        cls.Unidade = 'PC'
        cls.Armazem = '01'
        cls.Grupo = '0003'
        cls.Preco = '99,00'
        cls.NomeCientifico = 'IMPRESSORA 3D NOME CIENTIFICO'
        cls.filial = '01'
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '02')
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros > Produtos")

    def test_de_incluir_produtos(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        self.oHelper.WaitShow("Atualizacao de Produtos:")

        #-------------------------
        # Inclusão de produto
        #-------------------------
        
        self.oHelper.SetButton("Incluir")
        sleep(1)
        self.oHelper.WaitShow("Atualizacao de Produtos - Incluir")
        self.oHelper.SetValue("B1_COD", self.Codigo)
        self.oHelper.SetValue("B1_DESC", self.Descrição)
        self.oHelper.SetValue("B1_TIPO", self.Tipo)
        self.oHelper.SetValue("B1_UM", self.Unidade)
        self.oHelper.SetValue("B1_LOCPAD", self.Armazem)
        self.oHelper.SetValue("B1_GRUPO", self.Grupo)
        self.oHelper.SetValue("B1_UPRC", self.Preco)
        self.oHelper.SetValue("B5_CEME", self.NomeCientifico)

        self.oHelper.SetButton("Confirmar")
        sleep(0.5)


       
        self.oHelper.WaitShow("Registro inserido com sucesso.")
        self.oHelper.SetButton("Fechar")
        sleep(1)
        self.oHelper.WaitShow("Atualizacao de Produtos:")
        

        #-------------------------
        # Visualização da inclusão
        #-------------------------
        self.oHelper.SetButton("Visualizar")
        self.oHelper.WaitShow("Atualizacao de Produtos - Visualizar")
        self.oHelper.CheckResult("B1_DESC", self.Descrição)
        self.oHelper.CheckResult("B1_GRUPO", self.Grupo)
        self.oHelper.CheckResult("B5_CEME", self.NomeCientifico)
        self.oHelper.CheckResult("B1_UPRC", self.Preco)
        self.oHelper.CheckResult("B1_LOCPAD", self.Armazem)
        self.oHelper.CheckResult("B1_TIPO", self.Tipo)
        self.oHelper.CheckResult("B1_UM", self.Unidade)
        self.oHelper.SetButton("Fechar")

        sleep(0.5)

        self.oHelper.WaitShow("Atualizacao de Produtos:")

        self.oHelper.AssertTrue()
        print("🎯 test_de_incluir_produtos")
        print("✅ Teste finalizado com sucesso")

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MATA010('test_de_incluir_produtos'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)