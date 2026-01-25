from tir import Webapp
from os import getcwd
import unittest
from datetime import datetime
from time import sleep
DateSystem = datetime.today().strftime('%d/%m/%Y')

 # # python -m pytest tests/Modulo_07/test_GPEA340.py -v -s --html=reports/report_GPEA340.html --self-contained-html

#------------------------------------------
#-- Teste GPEA340 - Cadastro de Sindicato
#------------------------------------------


class GPEA340(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       
        cls.Codigo = '04'
        cls.Descrição = 'UNIÃO GERAL DOS TRABALHADORES'
        cls.DescriçãoEdit = 'UNIÃO GERAL DOS TRABALHADORES UGT'
        cls.Cnpj = '01450256000163'
        cls.Endereco ='AVENIDA BRASIL'
        cls.Numero ="21"
        cls.filial = '01'
        cls.Complemento = 'CENTRO'
        cls.Bairro = 'PALISTA'
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros > Sindicatos")

    def test_de_Cadastro_sindicato_e_edição(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        self.oHelper.WaitShow("Cadastro de Sindicatos")
        self.oHelper.Screenshot('GPEA030_01')
        
        self.oHelper.SetButton("Incluir")
        sleep(1)
        self.oHelper.WaitShow("Sindicatos - INCLUIR")
        self.oHelper.Screenshot('GPEA030_02')
        self.oHelper.SetValue("RCE_CODIGO", self.Codigo)
        self.oHelper.SetValue("RCE_DESCRI", self.Descrição)
        self.oHelper.SetValue("RCE_CGC", self.Cnpj)
        self.oHelper.SetValue("RCE_ENTSIN", '5487')
        self.oHelper.SetValue("RCE_ENDER", self.Endereco)
        self.oHelper.SetValue("RCE_NUMER", self.Numero)
        self.oHelper.SetValue("RCE_COMPLE", self.Complemento)
        self.oHelper.SetValue("RCE_BAIRRO", self.Bairro)
        self.oHelper.SetValue("RCE_CEP", '72800000')
        self.oHelper.SetValue("RCE_UF", 'DF')
        self.oHelper.Screenshot('GPEA030_03')
        self.oHelper.SetValue("RCE_CODMUN", '00108')
        self.oHelper.SetValue("RCE_DDD", '61')
        self.oHelper.SetValue("RCE_FONE", '994875124')
        self.oHelper.SetValue("RCE_EMAIL", 'TESTESINDICATO01@GMAIL.COM')
        self.oHelper.SetKey("TAB") 
        self.oHelper.Screenshot('GPEA030_04')

        self.oHelper.SetButton("Confirmar")

        if self.oHelper.IfExists("Atenção"):
            self.oHelper.Screenshot('GPEA030_05')
            self.oHelper.SetButton("Sim")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
        
        if self.oHelper.IfExists("Registro inserido com sucesso."):
            self.oHelper.Screenshot('GPEA030_06')
            self.oHelper.SetButton("Fechar")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()

        sleep(1)
            
        
        self.oHelper.WaitShow("Cadastro de Sindicatos")
        self.oHelper.Screenshot('GPEA030_06')

        self.oHelper.SetButton("Visualizar")
        sleep(1)
        
        #-------------------------
        # Visualização da inclusão
        #-------------------------

        self.oHelper.WaitShow("Sindicatos - VISUALIZAR")
        self.oHelper.Screenshot('GPEA030_07')
        self.oHelper.CheckResult("RCE_CODIGO", self.Codigo)
        self.oHelper.CheckResult("RCE_DESCRI", self.Descrição)
        self.oHelper.CheckResult("RCE_CGC", self.Cnpj)
        self.oHelper.CheckResult("RCE_ENTSIN", '5487')
        self.oHelper.CheckResult("RCE_ENDER", self.Endereco)
        self.oHelper.CheckResult("RCE_NUMER", self.Numero)
        self.oHelper.CheckResult("RCE_COMPLE", self.Complemento)
        self.oHelper.CheckResult("RCE_CEP", '72800000')
        self.oHelper.CheckResult("RCE_UF", 'DF')
        self.oHelper.CheckResult("RCE_CODMUN", '00108')
        self.oHelper.CheckResult("RCE_DDD", '61')
        self.oHelper.Screenshot('GPEA030_08')
        self.oHelper.SetButton("Fechar")
        sleep(1)
        self.oHelper.WaitShow("Cadastro de Sindicatos")

        #-------------------
        # EDITAR SINDICATO
        #-------------------

        self.oHelper.SetButton("Alterar")
        sleep(1)
        self.oHelper.WaitShow("Sindicatos - ALTERAR")
        self.oHelper.Screenshot('GPEA030_09')
        self.oHelper.SetValue("RCE_DESCRI", self.DescriçãoEdit)
        self.oHelper.SetKey("TAB") 
        self.oHelper.Screenshot('GPEA030_10')
        self.oHelper.SetButton("Confirmar")
        sleep(1)

        if self.oHelper.IfExists("Atenção"):
            self.oHelper.Screenshot('GPEA030_11')
            self.oHelper.SetButton("Sim")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
        
        if self.oHelper.IfExists("Registro alterado com sucesso."):
            self.oHelper.Screenshot('GPEA030_12')
            self.oHelper.SetButton("Fechar")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()

        sleep(1)

    
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_Cadastro_sindicato_e_edição")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")



    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA340('test_de_Cadastro_sindicato_e_edição'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)