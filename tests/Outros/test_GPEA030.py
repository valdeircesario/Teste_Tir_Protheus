from tir import Webapp
from os import getcwd
import unittest
from datetime import datetime
from time import sleep
DateSystem = datetime.today().strftime('%d/%m/%Y')

 # # python -m pytest tests/Outros/test_GPEA030.py -v -s --html=reports/report_GPEA030.html --self-contained-html

#---------------------------
# CADASTROS DE FUNÇÕES CRUD
#---------------------------


class GPEA030(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.filial = '02DF0001'
        cls.Codigo = '1119'
        cls.FuncaoAd = 'FUNÇÃO TESTE'
        cls.CBO = '0111'
        cls.FuncaoAdEdt = 'FUNÇÃO TESTE EDITADO'
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', DateSystem, '02', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros > Funções")

    def test_de_Cadastro_de_função_CRUD(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        self.oHelper.WaitShow("Cadastro de Funções")
        self.oHelper.Screenshot('GPEA030_01')
        
        self.oHelper.SetButton("Incluir")
        sleep(1)
        self.oHelper.WaitShow("Funções - INCLUIR")
        self.oHelper.Screenshot('GPEA030_02')
        self.oHelper.SetValue("RJ_FUNCAO", self.Codigo)
        self.oHelper.SetValue("RJ_XDESC", self.FuncaoAd)
        self.oHelper.SetValue("RJ_CODCBO", self.CBO)
        self.oHelper.SetKey("TAB") 

        self.oHelper.SetButton("Confirmar")

        if self.oHelper.IfExists("Registro inserido com sucesso."):
            self.oHelper.Screenshot('GPEA030_03')
            self.oHelper.SetButton("Fechar")
            self.oHelper.AssertTrue()
            
        
        self.oHelper.WaitShow("Cadastro de Funções")
        self.oHelper.Screenshot('GPEA030_04')

        #-------------------------
        # VISUALISAR INCLUSÃO
        #-------------------------
        self.oHelper.SetButton("Visualizar")
        self.oHelper.WaitShow("Funções - VISUALIZAR")
        self.oHelper.Screenshot('GPEA030_05')
        self.oHelper.CheckResult("RJ_FUNCAO", self.Codigo)
        self.oHelper.CheckResult("RJ_XDESC", self.FuncaoAd)
        self.oHelper.CheckResult("RJ_CODCBO", self.CBO)
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Cadastro de Funções")
        
        #-------------------------
        # ALTERAR FUNÇÃO
        #-------------------------
        self.oHelper.SetButton("Alterar")

        self.oHelper.WaitShow("Funções - ALTERAR")
        self.oHelper.Screenshot('GPEA030_06')
        self.oHelper.SetValue("RJ_XDESC", self.FuncaoAdEdt)
        self.oHelper.Screenshot('GPEA030_07')
        
        self.oHelper.SetButton("Confirmar")

        if self.oHelper.IfExists("Registro alterado com sucesso."):
            self.oHelper.Screenshot('GPEA030_08')
            self.oHelper.SetButton("Fechar")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
          
        self.oHelper.WaitShow("Cadastro de Funções")
        self.oHelper.Screenshot('GPEA030_09')
        
        #--------------------------
        # EXCLUIR FUNÇÃO
        #--------------------------
        
        self.oHelper.SetButton("Outras Ações","Excluir")
        sleep(1)
        self.oHelper.Screenshot('GPEA030_10')
        self.oHelper.WaitShow("Tem certeza que deseja excluir o item abaixo?")
        self.oHelper.SetButton("Confirmar")
        sleep(2)
        if self.oHelper.IfExists("Registro excluído com sucesso."):
            self.oHelper.Screenshot('GPEA030_11')
            self.oHelper.SetButton("Fechar")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        sleep(1)
        self.oHelper.Screenshot('GPEA030_12')
          
        self.oHelper.WaitShow("Cadastro de Funções")

        self.oHelper.AssertTrue()
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_Cadastro_de_função_CRUD")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")



    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA030('test_de_Cadastro_de_função_CRUD'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)