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
#-- Teste AGRA045 - Cadastro de local de estoque
#------------------------------------------




class AGRA045(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       
        cls.Codigo = '06'
        cls.Descricao = 'EXTERNO'
        cls.DescricaoEdt = 'EXTERNO EDITADO'
        cls.filial = '01'
        configfile = getcwd() + '\\config.json'
        # 1. Instância base do TIR
        webapp_base = Webapp(configfile)
                
        # 2. Encapsula com o Agente de Relatório
        cls.oHelper = TirReportAgent(
            tir_instance=webapp_base,
            cod_modulo="02",
            nome_modulo="Compras",
            ct_nome="test_AGRA045",
            descricao="Inclusão, Visualização, Alteração  e exclusão de Local de Estoque"
        )
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '02')
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros > Locais de Estoque")
        cls.oHelper.SetButton('Confirmar')

    def test_de_incluir_local_de_estoque(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        #-------------------------
        # Inclusão de local de estoque
        #-------------------------
        try:

            print('------------------------Incluir')
            self.oHelper.Screenshot("LocalEstoque/001")
            self.oHelper.SetButton("Incluir")
            self.oHelper.WaitShow("Locais de Estoque - INCLUIR")
            self.oHelper.Screenshot("LocalEstoque/002")
            self.oHelper.SetValue("NNR_CODIGO", self.Codigo,        check_value=False)
            self.oHelper.SetValue("NNR_DESCRI", self.Descricao,     check_value=False)
            self.oHelper.Screenshot("LocalEstoque/002")
            self.oHelper.SetButton("Confirmar")      
            self.oHelper.WaitShow("Registro inserido com sucesso.")
            self.oHelper.Screenshot("LocalEstoque/003")
            self.oHelper.SetButton("Fechar")
            self.oHelper.Screenshot("LocalEstoque/004")
           
            #-------------------------
            # Visualização da inclusão
            #-------------------------
            print('----------------------------Visualizar')
            self.oHelper.SetButton("Outras Ações","Visualizar")
            self.oHelper.WaitShow("Locais de Estoque - VISUALIZAR")
            self.oHelper.Screenshot("LocalEstoque/005")
            self.oHelper.CheckResult("NNR_CODIGO", self.Codigo)
            self.oHelper.CheckResult("NNR_DESCRI", self.Descricao)
            self.oHelper.SetButton("Fechar")

            #-------------------------
            # Editar inclusão
            #-------------------------
            print('----------------------------Alterar')
            self.oHelper.SetButton("Alterar")
            self.oHelper.WaitShow("Locais de Estoque - ALTERAR")
            self.oHelper.Screenshot("LocalEstoque/006")
            self.oHelper.CheckResult("NNR_CODIGO", self.Codigo)
            self.oHelper.SetValue("NNR_DESCRI", self.DescricaoEdt,    check_value=False)
            self.oHelper.Screenshot("LocalEstoque/007")
            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Registro alterado com sucesso.")
            self.oHelper.Screenshot("LocalEstoque/008")
            self.oHelper.SetButton("Fechar")
            self.oHelper.Screenshot("LocalEstoque/009")


            #-------------------------
            # Exclusão
            #-------------------------
            print('------------------------Excluir')
            self.oHelper.SetButton("Outras Ações","Excluir")
            self.oHelper.WaitShow("Tem certeza que deseja excluir o item abaixo?")
            self.oHelper.CheckResult("NNR_CODIGO", self.Codigo)
            self.oHelper.CheckResult("NNR_DESCRI", self.DescricaoEdt)
            self.oHelper.Screenshot("LocalEstoque/010")
            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Registro excluído com sucesso.")
            self.oHelper.Screenshot("LocalEstoque/011")
            self.oHelper.SetButton("Fechar")

            self.oHelper.AssertTrue()
        except Exception as e:
            self.oHelper.registrar_erro(e)
            raise e
        finally:
            self.oHelper.salvar_relatorio()

        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_incluir_local_de_estoque")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(AGRA045('test_de_incluir_local_de_estoque'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)