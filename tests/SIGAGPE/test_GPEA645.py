from tir import Webapp
from os import getcwd
import unittest
from datetime import datetime
from time import sleep
DateSystem = datetime.today().strftime('%d/%m/%Y')

 # # python -m pytest tests/SIGAGPE/test_GPEA645.py -v -s --html=reports/report_GPEA645.html --self-contained-html

#------------------------------------------
#-- CADASTRO DE DISCIPLINA
#------------------------------------------


class GPEA645(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       
        cls.Descricao = 'TESTE DE DISCIPLINA'
        cls.DescricaoEdit = 'ABANDONO AO POSTO'
        cls.filial = '01'
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Atualizações > Controle Disciplinar > Disciplina")

    def test_de_incluir_cadastro_de_disciplina(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        self.oHelper.WaitShow("Cadastro de Disciplinas")
        self.oHelper.Screenshot("Disciplina/001")
        
        self.oHelper.SetButton("Incluir")
        sleep(1)
        self.oHelper.WaitShow("Tipo de Disciplina - INCLUIR")
        self.oHelper.Screenshot("Disciplina/002")
        self.oHelper.SetValue("TIQ_DESCR", self.Descricao)
        self.oHelper.Screenshot("Disciplina/003")
        self.oHelper.SetKey("TAB") 

        self.oHelper.SetButton("Confirmar")
        sleep(1)

        if self.oHelper.IfExists("Registro inserido com sucesso."):
            self.oHelper.Screenshot("Disciplina/004")
            self.oHelper.SetButton("Fechar")
        else:
            self.oHelper.AssertTrue()

        self.oHelper.WaitShow("Cadastro de Disciplinas")
        self.oHelper.Screenshot("Disciplina/005")


        #-------------------------
        # Visualização da inclusão
        #-------------------------
        self.oHelper.SetButton("Visualizar")

        self.oHelper.WaitShow("Tipo de Disciplina - VISUALIZAR")
        self.oHelper.Screenshot("Disciplina/006")
        self.oHelper.CheckResult("TIQ_DESCR", self.Descricao)
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Cadastro de Disciplinas")

        #-------------------------
        # Edição do registro
        #-------------------------
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow("Tipo de Disciplina - ALTERAR")
        self.oHelper.Screenshot("Disciplina/007")
        self.oHelper.SetValue("TIQ_DESCR", self.DescricaoEdit)
        self.oHelper.Screenshot("Disciplina/008") 

        self.oHelper.AssertTrue()
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_incluir_cadastro_de_disciplina")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA645('test_de_incluir_cadastro_de_disciplina'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)