from tir import Webapp
from os import getcwd
import unittest
from datetime import datetime, timedelta
from time import sleep

DateSystem = datetime.today().strftime('%d/%m/%Y')

class GPEA080(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.filial = '02DF0001'
        cls.descricao = "09:05 AS 15:05 - INTERVALO 13:20 AS 13:35"
        cls.descricaoEdit = "09:05 AS 15:05 - INTERVALO 13:15 AS 13:30"
        cls.descricaoTipJorn = "TESTE"
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI',DateSystem , '02', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Atualizações > Ponto Eletrônico > Turnos de Trabalho")

    def test_CRUD_turno_de_trabalho(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')
        else:
            self.oHelper.AssertTrue()

        
        self.oHelper.WaitShow("Turnos de Trabalho") 
        self.oHelper.Screenshot("Turno_Trabalho_01")
        
        #-------------------------------
        # CRUD TURNO DE TRABALHO
        #--------------------------------
        
        self.oHelper.SetButton("Incluir")
        self.oHelper.WaitShow("Turnos de Trabalho - INCLUIR")
        self.oHelper.Screenshot("Turno_Trabalho_02")
        
        self.oHelper.SetValue('R6_DESC', self.descricao) 
        self.oHelper.ClickFolder('Informacoes Ponto')
        self.oHelper.Screenshot("Turno_Trabalho_03") 
        self.oHelper.SetValue('R6_DTPJOR',self.descricaoTipJorn)
        self.oHelper.SetValue('Tipo Jornada','9 - Demais tipos de jornada')
        self.oHelper.Screenshot("Turno_Trabalho_04") 
        self.oHelper.ClickFolder('Gerais')
        
        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.WaitShow("Turnos de Trabalho") 
        self.oHelper.Screenshot("Turno_Trabalho_05")
        
        #--------------------------
        # VISUALIZAR
        #--------------------------
        
        self.oHelper.SetButton('Visualizar')
        self.oHelper.WaitShow("Turnos de Trabalho - VISUALIZA")   
        self.oHelper.CheckResult('R6_DESC', self.descricao)
        self.oHelper.Screenshot("Turno_Trabalho_06")
        self.oHelper.ClickFolder('Informacoes Ponto')
        self.oHelper.CheckResult('R6_DTPJOR',self.descricaoTipJorn)
        self.oHelper.CheckResult('Tipo Jornada','9 - Demais tipos de jornada')
        self.oHelper.Screenshot("Turno_Trabalho_07")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Turnos de Trabalho")
        #------------------
        # ALTERAR
        #--------------------
        
        self.oHelper.SetButton("Alterar")
        
        self.oHelper.WaitShow("Turnos de Trabalho - ALTERAR")
        self.oHelper.Screenshot("Turno_Trabalho_08")   
        self.oHelper.SetValue('R6_DESC', self.descricaoEdit)
        self.oHelper.Screenshot("Turno_Trabalho_09")    
        self.oHelper.SetButton('Salvar')
        self.oHelper.WaitShow("Turnos de Trabalho")
        self.oHelper.Screenshot("Turno_Trabalho_10") 
        
        
        #------------------
        # EXCLUIR
        #--------------------
        
        
        self.oHelper.SetButton('Outras Ações','Excluir')
        
        if self.oHelper.IfExists('Confirma a exclusäo do Turno?'):
            self.oHelper.Screenshot("Turno_Trabalho_11") 
            self.oHelper.SetButton('Sim')
        else:
            self.oHelper.Screenshot("erro_mensagem_exclusao") 
            self.oHelper.AssertTrue()
            
        if self.oHelper.IfExists('Deseja gerar Log?'):
            self.oHelper.Screenshot("Turno_Trabalho_13") 
            self.oHelper.SetButton('Não')
        else:
            self.oHelper.Screenshot("erro_mensagem_log") 
            self.oHelper.AssertTrue()
         
        
        self.oHelper.WaitShow("Turnos de Trabalho - EXCLUIR")
        self.oHelper.Screenshot("Turno_Trabalho_14") 
        self.oHelper.SetButton('Confirmar')
        self.oHelper.Screenshot("Turno_Trabalho_15")
        
        self.oHelper.AssertTrue()
        print("")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test CRUD turno de trabalho")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA080('test_CRUD_turno_de_trabalho'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)