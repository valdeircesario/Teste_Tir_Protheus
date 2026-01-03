from tir import Webapp
from os import getcwd
import unittest
from datetime import datetime
from time import sleep
DateSystem = datetime.today().strftime('%d/%m/%Y')

#python -m pytest tests/Modulo_02/test_MATA020.py -v -s --html=reports/report_MATA020.html --self-contained-html
#------------------------------------------
#-- Teste MATA020 - Cadastro de fornecedores
#------------------------------------------

class MATA020(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       
        cls.Codigo = '000003'
        cls.Loja = '01'
        cls.RazaoSocial = 'PERNANBUCANAS LTDA'
        cls.Fantasia = 'PERMANBUC'
        cls.FantasiaEdt = 'PERNANBUCANAS'
        cls.Endereco = 'JARDIM OLIVEIRA DE BARROS, 0823'
        cls.Bairro = 'CENTRO'
        cls.Cidade = 'BRASILIA'
        cls.UF = 'DF'
        cls.Nunicipio = '00108'
        cls.CEP = '72802625'
        cls.Tipo = 'J - Juridico'# F - Fisico  J - Juridica X - Outros
        cls.CNPJ = '43.075.034/0001-58' #,80.727.782/0001-02,20.658.673/0001-40,59.462.902/0001-92
        cls.Telefone = '84080130'
        cls.Email = 'pernanbucanasltda@teste.com'
        cls.Banco = '01'
        cls.Natureza = '001'
        cls.CondPagto = '001'
        cls.FormPgto = '03'
        cls.filial = '01'
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '02')
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros > Fornecedores")

    def test_de_incluir_fornecedor(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        self.oHelper.WaitShow("Fornecedores")

        #-------------------------
        # Inclusão de fornecedor
        #-------------------------
        
        self.oHelper.SetButton("Incluir")
        sleep(1)
        self.oHelper.WaitShow("Fornecedores - Incluir")

        self.oHelper.SetValue("A2_COD", self.Codigo)
        self.oHelper.SetValue("A2_LOJA", self.Loja)
        self.oHelper.SetValue("A2_NOME", self.RazaoSocial)
        self.oHelper.SetValue("A2_NREDUZ", self.Fantasia)
        self.oHelper.SetValue("A2_END", self.Endereco)
        self.oHelper.SetValue("A2_BAIRRO", self.Bairro)
        self.oHelper.SetValue("A2_EST", self.UF)
        self.oHelper.SetValue("A2_COD_MUN", self.Nunicipio)
        self.oHelper.SetValue("A2_CEP", self.CEP)
        self.oHelper.SetValue("Tipo", self.Tipo)
        self.oHelper.SetValue("A2_CGC", self.CNPJ, check_value = False)
        self.oHelper.SetValue("A2_TEL", self.Telefone)
        self.oHelper.SetValue("A2_EMAIL", self.Email)
        self.oHelper.SetKey("TAB")

        #-------------------------
        # Aba de dados adm.
        #-------------------------

        self.oHelper.ClickFolder("adm/Fin.")

        self.oHelper.SetValue("A2_BANCO", self.Banco)
        self.oHelper.SetValue("A2_NATUREZ", self.Natureza)
        self.oHelper.SetValue("A2_COND", self.CondPagto)
        self.oHelper.SetValue("A2_FORMPAG", self.FormPgto)
        self.oHelper.SetKey("TAB")

        self.oHelper.ClickFolder("Cadastrais")
        sleep(0.5)

        #-------------------------
        # Confirma a inclusão   
        #-------------------------

        self.oHelper.SetButton("Confirmar")
        sleep(0.5)
       
        self.oHelper.WaitShow("Registro inserido com sucesso.")
        self.oHelper.SetButton("Fechar")
        sleep(0.5)


        self.oHelper.WaitShow("Fornecedores")
        
        #-------------------------
        # Visualização da inclusão
        #-------------------------
        self.oHelper.SetButton("Visualizar")
        sleep(1)
        self.oHelper.WaitShow("Fornecedores - Visualizar")
        self.oHelper.CheckResult("A2_NOME", self.RazaoSocial)
        self.oHelper.CheckResult("A2_CGC", self.CNPJ)
        self.oHelper.CheckResult("A2_TEL", self.Telefone)
        self.oHelper.CheckResult("A2_EMAIL", self.Email)

        #-------------------------
        # Aba de dados adm.
        #-------------------------

        self.oHelper.ClickFolder("adm/Fin.")
        self.oHelper.CheckResult("A2_BANCO", self.Banco)
        self.oHelper.CheckResult("A2_NATUREZ", self.Natureza)
        self.oHelper.CheckResult("A2_COND", self.CondPagto)
        self.oHelper.CheckResult("A2_FORMPAG", self.FormPgto)

        self.oHelper.SetButton("Fechar")
        sleep(1)

        self.oHelper.WaitShow("Fornecedores")

        #---------------------
        # conferindo alteração
        #---------------------

        self.oHelper.SetButton("Alterar")
        sleep(1)

        self.oHelper.WaitShow("Fornecedores - Alterar")
        self.oHelper.SetValue("A2_NREDUZ",self.FantasiaEdt,check_value= False)

        self.oHelper.SetButton("Confirmar")

        self.oHelper.WaitShow("Fornecedores")

        self.oHelper.AssertTrue()
        print("🎯 test_de_incluir_fornecedor")
        print("✅ Teste finalizado com sucesso")

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MATA020('test_de_incluir_fornecedor'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)