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
from time import sleep

from tir import Webapp
from utilis.md_reporter import TirReportAgent
DateSystem = datetime.today().strftime('%d/%m/%Y')

## python -m pytest tests/Modulo_02/test_CSAA100.py -v -s --html=reports/report_CSAA100.html --self-contained-html

#------------------------------------------
#-- Teste CSAA100 - Cadastro de Departamentos
#------------------------------------------




class CSAA100(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       
        cls.Descrição = 'GESTÃO CONTAIL 5'
        cls.DescriçãoEdt = 'GESTÃO CONTAIL EDIÇÃO'
        cls.CentroCusto = '003'
        cls.DepartamentoSuper = '000000003'
        cls.Responsavel = '000012'
        cls.filial = '01'
        configfile = getcwd() + '\\config.json'
        # 1. Instância base do TIR
        webapp_base = Webapp(configfile)
                                
        # 2. Encapsula com o Agente de Relatório
        cls.oHelper = TirReportAgent(
            tir_instance=webapp_base,
            cod_modulo="07",
            nome_modulo="Gestão de Pessoal",
            ct_nome="test_CTBA060",
            descricao="Inclusão, Visualização, Edição e Exclusão de Departamento"
        )
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros > Departamentos")
        cls.oHelper.SetButton('Confirmar')

    def test_de_incluir_departamento(self):

        try:

            if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
                self.oHelper.SetButton('Fechar')

            if self.oHelper.IfExists("Moedas"):
                self.oHelper.CheckResult('Dolar', '0,0000')
                self.oHelper.SetButton('Confirmar')

            
            self.oHelper.WaitShow("Departamento")
            self.oHelper.Screenshot("Departamento/001")


            print('--------------------Incluir')  
            self.oHelper.SetButton("Incluir")
            self.oHelper.WaitShow("Departamento - INCLUIR")
            self.oHelper.Screenshot("Departamento/002")
            self.oHelper.SetValue("QB_DESCRIC", self.Descrição,         check_value=False)
            self.oHelper.SetValue("QB_CC", self.CentroCusto,            check_value=False)
            self.oHelper.SetValue("QB_DEPSUP", self.DepartamentoSuper,  check_value=False)
            self.oHelper.SetValue("QB_MATRESP", self.Responsavel,       check_value=False)
            self.oHelper.Screenshot("Departamento/003")
            self.oHelper.SetButton("Salvar")
            self.oHelper.SetButton("Cancelar")
            self.oHelper.WaitShow("Departamento")
            self.oHelper.Screenshot("Departamento/004")

            #-------------------------
            # Visualização da inclusão
            #-------------------------
            print('--------------------Visualizar')
            self.oHelper.SetButton("Visualizar")
            self.oHelper.WaitShow("Departamento - VISUALIZAR")
            self.oHelper.Screenshot("Departamento/005")
            self.oHelper.CheckResult("QB_DESCRIC", self.Descrição)
            self.oHelper.CheckResult("QB_CC", self.CentroCusto)
            self.oHelper.CheckResult("QB_DEPSUP", self.DepartamentoSuper)
            self.oHelper.CheckResult("QB_MATRESP", self.Responsavel)
            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Departamento")

            #-------------------------
            # Editar a inclusão
            #-------------------------
            print('--------------------Visualizar')
            self.oHelper.SetButton("Alterar")
            self.oHelper.WaitShow("Departamento - ALTERAR")
            self.oHelper.Screenshot("Departamento/006")
            self.oHelper.SetValue("QB_DESCRIC", self.DescriçãoEdt,         check_value=False)
            self.oHelper.CheckResult("QB_CC", self.CentroCusto)
            self.oHelper.CheckResult("QB_DEPSUP", self.DepartamentoSuper)
            self.oHelper.CheckResult("QB_MATRESP", self.Responsavel)
            self.oHelper.Screenshot("Departamento/007")
            self.oHelper.SetButton("Salvar")
            self.oHelper.WaitShow("Departamento")
            self.oHelper.Screenshot("Departamento/008")

            #-------------------------
            # Exclusão
            #-------------------------
            print('--------------------Visualizar')
            self.oHelper.SetButton("Outras Ações","Excluir")
            self.oHelper.WaitShow("Departamento - EXCLUIR")
            self.oHelper.Screenshot("Departamento/009")
            self.oHelper.CheckResult("QB_DESCRIC", self.DescriçãoEdt)
            self.oHelper.CheckResult("QB_CC", self.CentroCusto)
            self.oHelper.CheckResult("QB_DEPSUP", self.DepartamentoSuper)
            self.oHelper.CheckResult("QB_MATRESP", self.Responsavel)
            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Confirma a exclusäo?")
            self.oHelper.Screenshot("Departamento/010")
            self.oHelper.SetButton("Sim")
            self.oHelper.WaitShow("Deseja gerar Log?")
            self.oHelper.Screenshot("Departamento/011")
            self.oHelper.SetButton("Não")
            self.oHelper.WaitShow("Departamento")
            self.oHelper.Screenshot("Departamento/012")
        

            self.oHelper.AssertTrue()
        except Exception as e:
            self.oHelper.registrar_erro(e)
            raise e
        finally:
            self.oHelper.salvar_relatorio()

        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_incluir_departamento")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CSAA100('test_de_incluir_departamento'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)