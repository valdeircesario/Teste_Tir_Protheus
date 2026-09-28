# troca de turno de trabalho do funcionario  atualizações > Ponto Eletronico > Turnos de Trabalho



import sys

from tir.technologies.core.base import By
from tir import Webapp
from pytest import mark
import unittest
from time import sleep
from os import getcwd,path
from datetime import datetime, timedelta

# Garante a importação dos módulos da pasta utilis
PROJECT_ROOT = path.abspath(path.join(path.dirname(__file__), '..', '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
from time import sleep

from tir import Webapp
from utilis.md_reporter import TirReportAgent
DateSystem = datetime.today().strftime('%d/%m/%Y')


#------------------------
# TESTE DE INCLUSÃO DE TURNO DE TRABALHO
#------------------------

class PONA160(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.filial = '01'
        cls.Turno = '03'
        cls.Descricao = 'MEIO PERIODO'
        cls.DescricaoEdit = 'MEIO PERIODO EDITADO'
        configfile = getcwd() + '\\config.json'
        # 1. Instância base do TIR
        webapp_base = Webapp(configfile)
                
        # 2. Encapsula com o Agente de Relatório
        cls.oHelper = TirReportAgent(
            tir_instance=webapp_base,
            cod_modulo="07",
            nome_modulo="Gestão de Pessoal",
            ct_nome="test_PONA160",
            descricao="Incluir, Visualizar,Alterar e Excluir um Turno de Trabalho"
        )
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '07') 
        cls.oHelper.SetLateralMenu("Atualizações > Ponto Eletrônico > Turnos de Trabalho")
        cls.oHelper.SetButton('Confirmar')
        

    def test_de_inclusão_de_turno_de_trabalho(self):

        try:
            sleep(5)
            if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
                self.oHelper.SetButton('Fechar')
            
            sleep(2)
            if self.oHelper.IfExists("Confirma a exclusäo do Turno?"):
                self.oHelper.SetButton('Sim')
                
            #----------------------------------------
            # TESTE DE INCLUIR NOVO TURNO DE TRABALHO
            #----------------------------------------

            self.oHelper.WaitShow("Turnos de Trabalho")
            self.oHelper.Screenshot("TURNO_TRABALHO/001")
            self.oHelper.SetButton("Incluir")

            print('----------------------------Incluir')
            self.oHelper.WaitShow("Turnos de Trabalho - INCLUIR")
            self.oHelper.Screenshot("TURNO_TRABALHO/002")
            self.oHelper.SetValue('R6_TURNO',self.Turno,            check_value=False)
            self.oHelper.SetValue('R6_DESC',self.Descricao,         check_value=False)
            self.oHelper.ClickFolder("Informacoes Ponto")
            self.oHelper.SetValue('Tp Jornada','09',                check_value=False)
            self.oHelper.SetValue('Desc.Tp.Jorn','TESTE',           check_value=False)
            self.oHelper.Screenshot("TURNO_TRABALHO/003")
            self.oHelper.ClickFolder("Gerais")
            self.oHelper.SetButton('Salvar')
            self.oHelper.SetButton('Cancelar')
            self.oHelper.WaitShow('Turnos de Trabalho')
            self.oHelper.Screenshot("TURNO_TRABALHO/004")

            #-----------------------------
            # VISUALIZAR TURNO DE TRABALHO
            #----------------------------

            print('--------------------------Visualizar')
            self.oHelper.SetButton('Visualizar')
            self.oHelper.WaitShow("Turnos de Trabalho - VISUALIZAR")
            self.oHelper.CheckResult('R6_TURNO','03')
            self.oHelper.CheckResult('R6_DESC','MEIO PERIODO')
            self.oHelper.Screenshot("TURNO_TRABALHO/005")
            self.oHelper.SetButton('Cancelar')
            self.oHelper.WaitShow('Turnos de Trabalho')

            #-----------------------------
            # ALTERAR TURNO DE TRABALHO
            #----------------------------

            print('------------------------Alterar')
            self.oHelper.SetButton('Alterar')
            self.oHelper.WaitShow('Turnos de Trabalho - ALTERAR')
            self.oHelper.SetValue('R6_DESC',self.DescricaoEdit,         check_value=False)
            self.oHelper.Screenshot("TURNO_TRABALHO/006")
            self.oHelper.SetButton('Salvar')
            self.oHelper.WaitShow('Turnos de Trabalho')
            self.oHelper.Screenshot("TURNO_TRABALHO/007")

            #-----------------------------
            # EXCLUIR TURNO DE TRABALHO
            #----------------------------

            print('---------------------------Excluir')
            self.oHelper.SetButton('Outras Ações','Excluir')
            self.oHelper.WaitShow("Confirma a exclusäo do Turno?")
            self.oHelper.Screenshot("TURNO_TRABALHO/008")
            self.oHelper.SetButton('Sim')    
            self.oHelper.WaitShow("Deseja gerar Log?")
            self.oHelper.Screenshot("TURNO_TRABALHO/009")
            self.oHelper.SetButton('Não')
            self.oHelper.SetButton('Confirmar')
            self.oHelper.WaitShow('Turnos de Trabalho')
            self.oHelper.Screenshot("TURNO_TRABALHO/010")

            self.oHelper.AssertTrue()
        except Exception as e:
            self.oHelper.registrar_erro(e)
            raise e
        finally:
            self.oHelper.salvar_relatorio()
            
        print("------------------------------------------------")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_inclusão_de_turno_de_trabalho")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                   
        
          
            

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(PONA160('test_de_inclusão_de_turno_de_trabalho'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
