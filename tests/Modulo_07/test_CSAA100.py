from tir import Webapp
from os import getcwd
import unittest
from datetime import datetime
from time import sleep
DateSystem = datetime.today().strftime('%d/%m/%Y')

#.\venv\Scripts\python.exe -m pytest tests/Modulo_07/test_CSAA100.py -v -s --html=report_CSAA100.html --self-contained-html
#------------------------------------------
#-- Teste CSAA100 - Cadastro de Departamentos
#------------------------------------------




class CSAA100(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       
        cls.Descrição = 'GESTÃO DE PESSOAS'
        cls.CentroCusto = '003'
        cls.DepartamentoSuper = '000000002'
        cls.Responsavel = '000012'
        cls.filial = '01'
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros > Departamentos")

    def test_de_incluir_departamento(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        self.oHelper.WaitShow("Departamento")
        
        self.oHelper.SetButton("Incluir")
        sleep(1)
        self.oHelper.WaitShow("Departamento - INCLUIR")
        self.oHelper.SetValue("QB_DESCRIC", self.Descrição)
        self.oHelper.SetValue("QB_CC", self.CentroCusto)
        self.oHelper.SetValue("QB_DEPSUP", self.DepartamentoSuper)
        self.oHelper.SetValue("QB_MATRESP", self.Responsavel)

        self.oHelper.SetButton("Salvar")
        sleep(1)
        self.oHelper.SetButton("Cancelar")
        sleep(1)
        self.oHelper.WaitShow("Departamento")

        #-------------------------
        # Visualização da inclusão
        #-------------------------
        self.oHelper.SetButton("Visualizar")
        self.oHelper.WaitShow("Departamento - VISUALIZAR")
        self.oHelper.CheckResult("QB_DESCRIC", self.Descrição)
        self.oHelper.CheckResult("QB_CC", self.CentroCusto)
        self.oHelper.CheckResult("QB_DEPSUP", self.DepartamentoSuper)
        self.oHelper.CheckResult("QB_MATRESP", self.Responsavel)

        self.oHelper.SetButton("Confirmar")
        sleep(1)

        self.oHelper.WaitShow("Departamento")

        self.oHelper.AssertTrue()
        print("🎯 test_de_incluir_departamento")
        print("✅ Teste finalizado com sucesso")

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CSAA100('test_de_incluir_departamento'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)