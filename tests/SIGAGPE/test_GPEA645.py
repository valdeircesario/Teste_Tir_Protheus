import sys

from tir import Webapp
from os import getcwd,path
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
        # 1. Instância base do TIR
        webapp_base = Webapp(configfile)
                
        # 2. Encapsula com o Agente de Relatório
        cls.oHelper = TirReportAgent(
            tir_instance=webapp_base,
            cod_modulo="07",
            nome_modulo="Gestão de Pessoal",
            ct_nome="test_GPEA645",
            descricao="Inclusão, Visualizar, Alterar e Excluir uma Disciplina"
        )
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Atualizações > Controle Disciplinar > Disciplina")
        cls.oHelper.SetButton('Confirmar')

    def test_de_incluir_cadastro_de_disciplina(self):



        try:
            if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
                self.oHelper.SetButton('Fechar')

            if self.oHelper.IfExists("Moedas"):
                self.oHelper.CheckResult('Dolar', '0,0000')
                self.oHelper.SetButton('Confirmar')

            self.oHelper.WaitShow("Cadastro de Disciplinas")
            self.oHelper.Screenshot("Disciplina/001")

            #----------
            # Inclusão
            #----------

            print('-----------------------------Incluir')
            self.oHelper.SetButton("Incluir")
            self.oHelper.WaitShow("Tipo de Disciplina - INCLUIR")
            self.oHelper.Screenshot("Disciplina/002")
            self.oHelper.SetValue("TIQ_TIPO", "1 - Punicao",            check_value=False)
            self.oHelper.SetValue("TIQ_DESCR", self.Descricao,          check_value=False)
            codigo = self.oHelper.GetValue('Codigo')
            self.oHelper.Screenshot("Disciplina/003")
            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Registro inserido com sucesso.")
            self.oHelper.Screenshot("Disciplina/004")
            self.oHelper.SetButton("Fechar")     
            self.oHelper.WaitShow("Cadastro de Disciplinas")
            self.oHelper.Screenshot("Disciplina/005")

            #-------------------------
            # Visualização da inclusão
            #-------------------------

            print('-----------------------------Visualizar')
            self.oHelper.SetButton("Visualizar")
            self.oHelper.WaitShow("Tipo de Disciplina - VISUALIZAR")
            self.oHelper.CheckResult("TIQ_TIPO", "1 - Punicao")
            self.oHelper.CheckResult('Codigo',codigo)
            self.oHelper.CheckResult("TIQ_DESCR", self.Descricao)
            self.oHelper.Screenshot("Disciplina/006")
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Cadastro de Disciplinas")

            #-------------------------
            # Edição do registro
            #-------------------------

            print('-----------------------------Alterar')
            self.oHelper.SetButton("Alterar")
            self.oHelper.WaitShow("Tipo de Disciplina - ALTERAR")
            self.oHelper.CheckResult("TIQ_TIPO", "1 - Punicao")
            self.oHelper.CheckResult('Codigo',codigo)
            self.oHelper.SetValue("TIQ_DESCR", self.DescricaoEdit,      check_value=False)
            self.oHelper.Screenshot("Disciplina/007")
            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Registro alterado com sucesso.")
            self.oHelper.Screenshot("Disciplina/008")
            self.oHelper.SetButton("Fechar")     
            self.oHelper.WaitShow("Cadastro de Disciplinas")
            self.oHelper.Screenshot("Disciplina/009")

            #-------------------------
            # Excluir registro
            #-------------------------
    
            print('-----------------------------Excluir')    
            self.oHelper.SetButton("Outras Ações","Excluir")
            self.oHelper.WaitShow("Tem certeza que deseja excluir o item abaixo?")
            self.oHelper.WaitShow("Esta operação não poderá ser desfeita após a confirmação da exclusão")
            self.oHelper.CheckResult("TIQ_TIPO", "1 - Punicao")
            self.oHelper.CheckResult('Codigo',codigo)
            self.oHelper.Screenshot("Disciplina/010")
            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Registro excluído com sucesso.")
            self.oHelper.Screenshot("Disciplina/011")
            self.oHelper.SetButton("Fechar")     
            self.oHelper.WaitShow("Cadastro de Disciplinas")


            #-------------------------
            # Confirmar Exclusão do Registro
            #-------------------------
        
            self.oHelper.SearchBrowse(codigo, column="Codigo*")
            self.oHelper.Screenshot("Disciplina/012")       
            self.oHelper.AssertTrue()

        except Exception as e:
            self.oHelper.registrar_erro(e)
            raise e
        finally:
            self.oHelper.salvar_relatorio()
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