import sys

from tir import Webapp
from os import getcwd, path
import unittest
from datetime import datetime
from time import sleep

# Garante a importação dos módulos da pasta utilis
PROJECT_ROOT = path.abspath(path.join(path.dirname(__file__), '..', '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tir import Webapp
from utilis.md_reporter import TirReportAgent

DateSystem = datetime.today().strftime('%d/%m/%Y')

#------------------------------------------
#-- Teste MATA020 - Cadastro de fornecedores
#------------------------------------------

class MATA020(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       
        cls.Codigo = '000005'
        cls.Loja = '01'
        cls.RazaoSocial = 'BANCO BR LTDA'
        cls.Fantasia = 'BB BRASILIA'
        cls.FantasiaEdt = 'BANCO BR ALTERADO'
        cls.Endereco = 'JARDIM OLIVEIRA DE BARROS, 0823'
        cls.Bairro = 'CENTRO'
        cls.Cidade = 'BRASILIA'
        cls.UF = 'DF'
        cls.Nunicipio = '00108'
        cls.CEP = '72802625'
        cls.Tipo = 'J - Juridico'# F - Fisico  J - Juridica X - Outros
        cls.CNPJ = '20658673000140' #59.462.902/0001-92
        cls.Telefone = '84080130'
        cls.Email = 'brasilialtda@teste.com'
        cls.Banco = '01'
        cls.Natureza = '001'
        cls.CondPagto = '001'
        cls.FormPgto = '03'
        cls.filial = '01'
        configfile = getcwd() + '\\config.json'
        # 1. Instância base do TIR
        webapp_base = Webapp(configfile)
                
        # 2. Encapsula com o Agente de Relatório
        cls.oHelper = TirReportAgent(
            tir_instance=webapp_base,
            cod_modulo="02",
            nome_modulo="Compras",
            ct_nome="test_MATA020",
            descricao="Inclusão e Visualização de Fornecedor"
        )
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '02')
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros > Fornecedores")
        cls.oHelper.SetButton('Confirmar')

    def test_de_incluir_fornecedor(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        try:

            self.oHelper.WaitShow("Fornecedores")
            self.oHelper.Screenshot("Fornecedor02/001")

            #-------------------------
            # Inclusão de fornecedor
            #-------------------------
            print('-------------------------Incluir')
            self.oHelper.SetButton("Incluir")
            self.oHelper.WaitShow("Fornecedores - Incluir")
            self.oHelper.Screenshot("Fornecedor02/002")
            self.oHelper.SetValue("A2_COD", self.Codigo,        check_value = False)
            self.oHelper.SetValue("A2_LOJA", self.Loja,         check_value = False)
            self.oHelper.SetValue("A2_NOME", self.RazaoSocial,  check_value = False)
            self.oHelper.SetValue("A2_NREDUZ", self.Fantasia,   check_value = False)
            self.oHelper.SetValue("A2_END", self.Endereco,      check_value = False)
            self.oHelper.SetValue("A2_BAIRRO", self.Bairro,     check_value = False)
            self.oHelper.SetValue("A2_EST", self.UF,            check_value = False)
            self.oHelper.SetValue("A2_COD_MUN", self.Nunicipio, check_value = False)
            self.oHelper.SetValue("A2_CEP", self.CEP,           check_value = False)
            self.oHelper.SetValue("Tipo", self.Tipo,            check_value = False)
            self.oHelper.SetValue("A2_CGC", self.CNPJ,          check_value = False)
            self.oHelper.SetValue("A2_TEL", self.Telefone,      check_value = False)
            self.oHelper.SetValue("A2_EMAIL", self.Email,       check_value = False)
            self.oHelper.Screenshot("Fornecedor02/003")

            #-------------------------
            # Aba de dados adm.
            #-------------------------
            print('-------------------------Adm/Fin')
            self.oHelper.ClickFolder("adm/Fin.")
            self.oHelper.Screenshot("Fornecedor02/004")
            self.oHelper.SetValue("A2_BANCO", self.Banco,       check_value = False)
            self.oHelper.SetValue("A2_NATUREZ", self.Natureza,  check_value = False)
            self.oHelper.SetValue("A2_COND", self.CondPagto,    check_value = False)
            self.oHelper.SetValue("A2_FORMPAG", self.FormPgto,  check_value = False)
            self.oHelper.Screenshot("Fornecedor02/005")

            self.oHelper.ClickFolder("Cadastrais")
            sleep(0.5)
            self.oHelper.Screenshot("Fornecedor02/006")

            #-------------------------
            # Confirma a inclusão   
            #-------------------------

            self.oHelper.SetButton("Confirmar")        
            self.oHelper.WaitShow("Registro inserido com sucesso.")
            self.oHelper.Screenshot("Fornecedor02/007")
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Fornecedores")
            self.oHelper.Screenshot("Fornecedor02/008")
            
            #-------------------------
            # Visualização da inclusão
            #-------------------------
            print('-------------------------Visualizar')
            self.oHelper.SetButton("Visualizar")
            self.oHelper.WaitShow("Fornecedores - Visualizar")
            self.oHelper.CheckResult("A2_NOME", self.RazaoSocial)
            self.oHelper.CheckResult("A2_CGC", self.CNPJ)
            self.oHelper.CheckResult("A2_TEL", self.Telefone)
            self.oHelper.CheckResult("A2_EMAIL", self.Email)
            self.oHelper.Screenshot("Fornecedor02/009")

            #-------------------------
            # Aba de dados adm.
            #-------------------------

            self.oHelper.ClickFolder("adm/Fin.")
            self.oHelper.CheckResult("A2_BANCO", self.Banco)
            self.oHelper.CheckResult("A2_NATUREZ", self.Natureza)
            self.oHelper.CheckResult("A2_COND", self.CondPagto)
            self.oHelper.CheckResult("A2_FORMPAG", self.FormPgto)
            self.oHelper.Screenshot("Fornecedor02/010")
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Fornecedores")

            #---------------------
            #  alterar
            #---------------------

            print('-------------------------Alterar')
            self.oHelper.SetButton("Alterar")
            self.oHelper.WaitShow("Fornecedores - Alterar")
            self.oHelper.SetValue("A2_NREDUZ",self.FantasiaEdt, check_value= False)
            self.oHelper.Screenshot("Fornecedor02/011")
            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Fornecedores")
            self.oHelper.Screenshot("Fornecedor02/012")

            self.oHelper.AssertTrue()
        except Exception as e:
            self.oHelper.registrar_erro(e)
            raise e
        finally:
            self.oHelper.salvar_relatorio()

        print('------------------------------------')    
        print("🎯 test_de_incluir_fornecedor")
        print("✅ Teste finalizado com sucesso")
        print('------------------------------------')

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MATA020('test_de_incluir_fornecedor'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)