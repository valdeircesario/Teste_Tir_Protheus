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
#-- Teste GPEA340 - Cadastro de Sindicato
#------------------------------------------


class GPEA340(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       
        cls.Codigo = '09'
        cls.Descrição = 'TESTE 02 SINDICATO DOS TRABALHADORES'
        cls.DescriçãoEdit = 'SINDICATO DOS TRABALHADORES SDT'
        cls.Cnpj = '01450256000163'
        cls.Endereco ='AVENIDA BRASIL'
        cls.Numero ="21"
        cls.filial = '01'
        cls.Complemento = 'CENTRO'
        cls.Bairro = 'PALISTA'
        configfile = getcwd() + '\\config.json'

        # 1. Instância base do TIR
        webapp_base = Webapp(configfile)
                
        # 2. Encapsula com o Agente de Relatório
        cls.oHelper = TirReportAgent(
            tir_instance=webapp_base,
            cod_modulo="07",
            nome_modulo="Gestão de Pessoal",
            ct_nome="test_GPEA340",
            descricao="Inclusão, Visualização, Alteração e Exclusão de Sindicato"
        )
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros > Sindicatos")
        cls.oHelper.SetButton('Confirmar')

    def test_de_Cadastro_sindicato_e_edição(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')


        try:

            self.oHelper.WaitShow("Cadastro de Sindicatos")
            self.oHelper.Screenshot("Sindicato/001")


            #-------------------
            # Incluir
            #-------------------

            print('--------------------------Incluir')
            self.oHelper.SetButton("Incluir")
            self.oHelper.WaitShow("Sindicatos - INCLUIR")
            self.oHelper.Screenshot("Sindicato/002")
            self.oHelper.SetValue("RCE_CODIGO", self.Codigo,                    check_value=False)
            self.oHelper.SetValue("RCE_DESCRI", self.Descrição,                 check_value=False)
            self.oHelper.SetValue("RCE_CGC", self.Cnpj,                         check_value=False)
            self.oHelper.SetValue("RCE_ENTSIN", '5487',                         check_value=False)
            self.oHelper.SetValue("RCE_ENDER", self.Endereco,                   check_value=False)
            self.oHelper.SetValue("RCE_NUMER", self.Numero,                     check_value=False)
            self.oHelper.SetValue("RCE_COMPLE", self.Complemento,               check_value=False)
            self.oHelper.SetValue("RCE_BAIRRO", self.Bairro,                    check_value=False)
            self.oHelper.SetValue("RCE_CEP", '72800000',                        check_value=False)
            self.oHelper.SetValue("RCE_UF", 'DF',                               check_value=False)
            self.oHelper.Screenshot("Sindicato/003")
            self.oHelper.SetValue("RCE_CODMUN", '00108',                        check_value=False)
            self.oHelper.SetValue("RCE_DDD", '61',                              check_value=False)
            self.oHelper.SetValue("RCE_FONE", '994875124',                      check_value=False)
            self.oHelper.SetValue("RCE_EMAIL", 'TESTESINDICATO01@GMAIL.COM',    check_value=False)
            self.oHelper.SetKey("TAB") 
            self.oHelper.Screenshot("Sindicato/004")

            self.oHelper.SetButton("Confirmar")
            print('--------------------------Confirmação')

            self.oHelper.WaitShow("Atenção")
            self.oHelper.Screenshot("Sindicato/005")
            self.oHelper.SetButton("Sim")
                
            self.oHelper.WaitShow("Registro inserido com sucesso.")
            self.oHelper.Screenshot("Sindicato/006")
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Cadastro de Sindicatos")
            self.oHelper.Screenshot("Sindicato/007")
            
            #-------------------------
            # Visualização da inclusão
            #-------------------------

            print('--------------------------Visualizar')
            self.oHelper.SetButton("Visualizar")
            self.oHelper.WaitShow("Sindicatos - VISUALIZAR")
            self.oHelper.Screenshot("Sindicato/008")
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
            self.oHelper.Screenshot("Sindicato/009")
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Cadastro de Sindicatos")
            self.oHelper.Screenshot("Sindicato/010")

            #-------------------
            # EDITAR SINDICATO
            #-------------------

            print('--------------------------Alterar')
            self.oHelper.SetButton("Alterar")
            self.oHelper.WaitShow("Sindicatos - ALTERAR")
            self.oHelper.Screenshot("Sindicato/011")
            self.oHelper.SetValue("RCE_DESCRI", self.DescriçãoEdit,     check_value=False)
            self.oHelper.Screenshot("Sindicato/012")
            self.oHelper.SetButton("Confirmar")

            self.oHelper.WaitShow("Atenção")
            self.oHelper.Screenshot("Sindicato/013")
            self.oHelper.SetButton("Sim")
            
            self.oHelper.WaitShow("Registro alterado com sucesso.")
            self.oHelper.Screenshot("Sindicato/014")
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Cadastro de Sindicatos")


            #-------------------
            # EXCLUIR SINDICATO
            #-------------------

            print('--------------------------Excluir')
            self.oHelper.SetButton("Outras Ações","Excluir")
            self.oHelper.WaitShow("Tem certeza que deseja excluir o item abaixo?")
            self.oHelper.WaitShow("Esta operação não poderá ser desfeita após a confirmação da exclusão.")
            self.oHelper.CheckResult("RCE_CGC", self.Cnpj)
            self.oHelper.CheckResult("RCE_ENTSIN", '5487')
            self.oHelper.CheckResult("RCE_ENDER", self.Endereco)
            self.oHelper.CheckResult("RCE_NUMER", self.Numero)
            self.oHelper.CheckResult("RCE_COMPLE", self.Complemento)
            self.oHelper.Screenshot("Sindicato/015")
            self.oHelper.SetButton("Confirmar")

            self.oHelper.WaitShow("Atenção")
            self.oHelper.Screenshot("Sindicato/016")
            self.oHelper.SetButton("Sim")
            
            self.oHelper.WaitShow("Registro excluído com sucesso")
            self.oHelper.Screenshot("Sindicato/017")
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Cadastro de Sindicatos")
            self.oHelper.AssertTrue()

        except Exception as e:
            self.oHelper.registrar_erro(e)
            raise e
        finally:
            self.oHelper.salvar_relatorio()


    
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