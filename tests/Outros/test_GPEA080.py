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
        self.oHelper.Screenshot("AD_01.png")
        
        #-------------------------------
        # CRUD TURNO DE TRABALHO
        #--------------------------------
        
        self.oHelper.SetButton("Incluir")
        
        self.oHelper.SetValue('R6_DESC', self.descricao)
        
        self.oHelper.ClickFolder('Informacoes Ponto')
        
        self.oHelper.SetValue('R6_DTPJOR',self.descricaoTipJorn)
        self.oHelper.SetValue('Tipo Jornada','9 - Demais tipos de jornada')
        
        self.oHelper.ClickFolder('Gerais')
        
        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Cancelar')
        
        #--------------------------
        # VISUALIZAR
        #--------------------------
        
        self.oHelper.SetButton('Visualizar')
        
        self.oHelper.CheckResult('R6_DESC', self.descricao)
        
        
        self.oHelper.SetButton("Confirmar")
        #------------------
        # ALTERAR
        #--------------------
        
        self.oHelper.SetButton("Alterar")
        
        self.oHelper.SetValue('R6_DESC', self.descricaoEdit)  
        
        self.oHelper.SetButton('Salvar') 
        
        
        #------------------
        # EXCLUIR
        #--------------------
        
        
        self.oHelper.SetButton('Outras Ações','Excluir')
        
        self.oHelper.WaitShow('Confirma a exclusäo do Turno?')
        
        self.oHelper.SetButton('Sim')
        
        self.oHelper.WaitShow("Deseja gerar Log?")
        self.oHelper.SetButton('Não')
        
        self.oHelper.SetButton('Confirmar')
        
        self.oHelper.AssertTrue()
        

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA080('test_CRUD_turno_de_trabalho'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)