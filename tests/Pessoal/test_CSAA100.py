from tir import Webapp
from os import getcwd
import unittest
from datetime import datetime
from time import sleep

 #.\venv\Scripts\Activate.ps1; python -m pytest tests/Pessoal/test_CSAA100.py -q -rP

DateSystem = datetime.today().strftime('%d/%m/%Y')

class CSAA100(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       
        cls.Descrição = 'FMCRO'
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
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.WaitShow("Departamento")

        
        self.assertTrue(True, "Teste finalizado com sucesso")

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CSAA100('test_de_incluir_departamento'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)