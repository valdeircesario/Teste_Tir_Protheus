import sys
from os import path, getcwd
import unittest
from datetime import datetime

# Garante a importação dos módulos da pasta utilis
PROJECT_ROOT = path.abspath(path.join(path.dirname(__file__), '..', '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tir import Webapp
from utilis.md_reporter import TirReportAgent

DateSystem = datetime.today().strftime('%d/%m/%Y')


# ------------------------------------------
# -- Teste GPEA030 - Cadastro de Funções
# ------------------------------------------

class GPEA030(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.Funcao = '00071'
        cls.Descrição = 'TESTE 03 DE FUNCAO'
        cls.DescricaoEdit = 'ASSITEMTE SENIOR 01 '
        cls.Cargo = '0005'

        cls.filial = '01'
        configfile = path.join(getcwd(), 'config.json')
        
        # 1. Instância base do TIR
        webapp_base = Webapp(configfile)
        
        # 2. Encapsula com o Agente de Relatório
        cls.oHelper = TirReportAgent(
            tir_instance=webapp_base,
            cod_modulo="07",
            nome_modulo="Gestão de Pessoal",
            ct_nome="test_GPEA030",
            descricao="Inclusão, Visualização e Alteração de Funções"
        )
        
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros > Funções")
        cls.oHelper.SetButton('Confirmar')

    def test_de_incluir_Funções(self):
        try:
            if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
                self.oHelper.SetButton('Fechar')

            if self.oHelper.IfExists("Moedas"):
                self.oHelper.CheckResult('Dolar', '0,0000')
                self.oHelper.SetButton('Confirmar')

            # -----------------------
            # Incluir Função
            # -----------------------
            print('-----------------------Incluir')
            self.oHelper.WaitShow("Cadastro de Funções")
            self.oHelper.Screenshot("Funcao/001") 
            self.oHelper.SetButton("Incluir")
            self.oHelper.WaitShow("Funções - INCLUIR")
            self.oHelper.Screenshot("Funcao/002")
            self.oHelper.SetValue("RJ_FUNCAO", self.Funcao, check_value=False)
            self.oHelper.SetValue("RJ_DESC", self.Descrição, check_value=False)
            self.oHelper.SetValue("RJ_CODCBO", "1234", check_value=False)
            self.oHelper.SetValue("RJ_CARGO", self.Cargo, check_value=False)
            self.oHelper.SetValue("RJ_ADDATA", DateSystem, check_value=False)
            self.oHelper.SetKey("TAB", wait_change=False)
            self.oHelper.Screenshot("Funcao/003") 
            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Registro inserido com sucesso.")
            self.oHelper.Screenshot("Funcao/004")
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Cadastro de Funções")
            self.oHelper.Screenshot("Funcao/005")

            # -------------------------
            # Visualização da inclusão
            # -------------------------
            print('--------------------Visualizar')
            self.oHelper.SetButton("Visualizar")
            self.oHelper.WaitShow("Funções - VISUALIZAR")
            self.oHelper.Screenshot("Funcao/006")
            self.oHelper.CheckResult("RJ_FUNCAO", self.Funcao)
            self.oHelper.CheckResult("RJ_DESC", self.Descrição)
            self.oHelper.CheckResult("RJ_CARGO", self.Cargo)
            self.oHelper.SetButton("Fechar")
            self.oHelper.Screenshot("Funcao/007")
            self.oHelper.WaitShow("Cadastro de Funções")

            # -------------------------
            # Edição do registro
            # -------------------------
            print('----------------------Alterar')
            self.oHelper.SetButton("Alterar")
            self.oHelper.WaitShow("Funções - ALTERAR")
            self.oHelper.Screenshot("Funcao/008")
            self.oHelper.CheckResult("RJ_FUNCAO", self.Funcao)
            self.oHelper.SetValue("RJ_DESC", self.DescricaoEdit, check_value=False)
            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Registro alterado com sucesso.")
            self.oHelper.Screenshot("Funcao/009")
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Cadastro de Funções")

            self.oHelper.AssertTrue()
        except Exception as e:
            self.oHelper.registrar_erro(e)
            raise e
        finally:
            self.oHelper.salvar_relatorio()

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA030('test_de_incluir_Funções'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)