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
#-- Teste GPEA370 - Cadastro de Cargos
#------------------------------------------


class GPEA370(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       
        cls.Cargo = '0007'
        cls.Descrição = 'SUPERVISOR DE EQUIPE 01'
        cls.DescriçãoEdt = 'SUPERVISOR DE EQUIPE EDITADO'
        cls.CentroCusto = '003'
        cls.filial = '01'
        cls.Depatamento = '000000006'
        configfile = getcwd() + '\\config.json'
        # 1. Instância base do TIR
        webapp_base = Webapp(configfile)
                
        # 2. Encapsula com o Agente de Relatório
        cls.oHelper = TirReportAgent(
            tir_instance=webapp_base,
            cod_modulo="07",
            nome_modulo="Gestão de Pessoal",
            ct_nome="test_GPEA370",
            descricao="Inclusão, Visualização e Alteração de Cargos"
        )
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros > Cargos")
        cls.oHelper.SetButton('Confirmar')

    def test_de_incluir_Cagos(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        try:

            self.oHelper.WaitShow("Cargo")
            self.oHelper.Screenshot("Cargo/001")

            #----------------------------
            # Inclusão
            #---------------------------

            print('--------------------------Incluir')
            self.oHelper.SetButton("Incluir")
            self.oHelper.WaitShow("Cargo - INCLUIR")
            self.oHelper.Screenshot("Cargo/002")
            self.oHelper.SetValue("Q3_CARGO", self.Cargo,           check_value=False)
            self.oHelper.SetValue("Q3_DESCSUM", self.Descrição,     check_value=False)
            self.oHelper.SetValue("Q3_CC", self.CentroCusto,        check_value=False)
            self.oHelper.SetValue("Q3_DEPTO", self.Depatamento,     check_value=False)
            self.oHelper.Screenshot("Cargo/003")
            print('--------------------------------Confirmação')
            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Registro inserido com sucesso.")
            self.oHelper.Screenshot("Cargo/004")
            self.oHelper.SetButton("Fechar") 
            self.oHelper.WaitShow("Cargo")
            self.oHelper.Screenshot("Cargo/005")

            #-------------------------
            # Visualização da inclusão
            #-------------------------
            print('--------------------------Visualizar')
            self.oHelper.SetButton("Visualizar")
            self.oHelper.WaitShow("Cargo - VISUALIZAR")
            self.oHelper.Screenshot("Cargo/006")
            self.oHelper.CheckResult("Q3_CARGO", self.Cargo)
            self.oHelper.CheckResult("Q3_DESCSUM", self.Descrição)
            self.oHelper.CheckResult("Q3_CC", self.CentroCusto)
            self.oHelper.CheckResult("Q3_DEPTO", self.Depatamento)
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Cargo")

            #-------------------------
            # Visualização da inclusão
            #-------------------------
            print('--------------------------Alteração')
            self.oHelper.SetButton("Alterar")
            self.oHelper.WaitShow("Cargo - ALTERAR")
            self.oHelper.Screenshot("Cargo/007")
            self.oHelper.CheckResult("Q3_CARGO", self.Cargo)
            self.oHelper.SetValue("Q3_DESCSUM", self.DescriçãoEdt,        check_value=False)
            self.oHelper.CheckResult("Q3_CC", self.CentroCusto)
            self.oHelper.CheckResult("Q3_DEPTO", self.Depatamento)
            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Registro alterado com sucesso.")
            self.oHelper.Screenshot("Cargo/008")
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Cargo")
            self.oHelper.Screenshot("Cargo/008")


            self.oHelper.AssertTrue()

        except Exception as e:
            self.oHelper.registrar_erro(e)
            raise e
        finally:
            self.oHelper.salvar_relatorio()

        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_incluir_Cagos")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")



    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA370('test_de_incluir_Cagos'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)