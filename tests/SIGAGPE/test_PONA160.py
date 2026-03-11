# troca de turno de trabalho do funcionario  atualizações > Ponto Eletronico > Turnos de Trabalho



from tir.technologies.core.base import By
from tir import Webapp
from pytest import mark
import unittest
from time import sleep
from os import getcwd
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')

# .\venv\Scripts\python.exe -m pytest tests/Outros/test_CSAA100.py -s


#------------------------
# TESTE DE INCLUSÃO DE TURNO DE TRABALHO
#------------------------

class PONA160(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.filial = '01'
        self.Turno = '03'
        self.Descricao = 'MEIO PERIODO'
        self.DescricaoEdit = 'MEIO PERIODO EDITADO'
        

        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', DateSystem, '99', self.filial, '07')
        
        self.oHelper.SetLateralMenu("Atualizações > Ponto Eletrônico > Turnos de Trabalho")
        
    

    def test_de_inclusão_de_turno_de_trabalho(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()

        if self.oHelper.IfExists("Confirma a exclusäo do Turno?"):
            self.oHelper.SetButton('Sim')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        #----------------------------------------
        # TESTE DE INCLUIR NOVO TURNO DE TRABALHO
        #----------------------------------------
        self.oHelper.WaitShow("Turnos de Trabalho")
        self.oHelper.Screenshot("TURNO_TRABALHO/turno_trabalho_01")
        self.oHelper.SetButton("Incluir")
        sleep(1)
        self.oHelper.WaitShow("Turnos de Trabalho - INCLUIR")
        self.oHelper.Screenshot("TURNO_TRABALHO/turno_trabalho_02")
        self.oHelper.SetValue('R6_TURNO',self.Turno)
        self.oHelper.SetValue('R6_DESC',self.Descricao)
        self.oHelper.ClickFolder("Informacoes Ponto")
        self.oHelper.SetValue('Tp Jornada','09 - Demais tipos de jornada')
        self.oHelper.SetValue('Desc.Tp.Jorn','TESTE')
        self.oHelper.Screenshot("TURNO_TRABALHO/turno_trabalho_03")
        self.oHelper.ClickFolder("Gerais")
        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.WaitShow('Turnos de Trabalho')
        self.oHelper.Screenshot("TURNO_TRABALHO/turno_trabalho_04")
        #-----------------------------
        # VISUALIZAR TURNO DE TRABALHO
        #----------------------------

        self.oHelper.SetButton('Visualizar')
        self.oHelper.WaitShow("Turnos de Trabalho - VISUALIZAR")
        self.oHelper.CheckResult('R6_TURNO','03')
        self.oHelper.CheckResult('R6_DESC','MEIO PERIODO')
        self.oHelper.Screenshot("TURNO_TRABALHO/turno_trabalho_05")
        self.oHelper.SetButton('Cancelar')
        self.oHelper.WaitShow('Turnos de Trabalho')
        #-----------------------------
        # ALTERAR TURNO DE TRABALHO
        #----------------------------
        self.oHelper.SetButton('Alterar')
        self.oHelper.WaitShow('Turnos de Trabalho - ALTERAR')
        self.oHelper.SetValue('R6_DESC',self.DescricaoEdit)
        self.oHelper.Screenshot("TURNO_TRABALHO/turno_trabalho_06")
        self.oHelper.SetButton('Salvar')
        self.oHelper.WaitShow('Turnos de Trabalho')
        self.oHelper.Screenshot("TURNO_TRABALHO/turno_trabalho_07")

        #-----------------------------
        # EXCLUIR TURNO DE TRABALHO
        #----------------------------
        self.oHelper.SetButton('Outras Ações','Excluir')


        self.oHelper.WaitShow("Confirma a exclusäo do Turno?")
        self.oHelper.Screenshot("TURNO_TRABALHO/turno_trabalho_08")
        self.oHelper.SetButton('Sim')
            
        self.oHelper.WaitShow("Deseja gerar Log?")
        self.oHelper.Screenshot("TURNO_TRABALHO/turno_trabalho_09")
        self.oHelper.SetButton('Não')
        sleep(1)
        self.oHelper.SetButton('Confirmar')
        sleep(1)
        self.oHelper.Screenshot("TURNO_TRABALHO/turno_trabalho_10")

        self.oHelper.WaitShow('Turnos de Trabalho')
        self.oHelper.Screenshot("TURNO_TRABALHO/turno_trabalho_11")

        self.oHelper.AssertTrue()
            
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
