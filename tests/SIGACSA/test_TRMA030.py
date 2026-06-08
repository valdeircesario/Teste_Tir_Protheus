from os import getcwd

from tir import Webapp
from pytest import mark
import unittest
from datetime import datetime, timedelta
from time import sleep


DateSystem = datetime.today().strftime('%d/%m/%Y')

# python -m pytest tests/SIGACSA/test_TRMA030.py -v -s --html=reports/report_TRMA030.html --self-contained-html

# TESTE DE CADASTRO DE GRUPOS DE TRABALHO

class TRMA030(unittest.TestCase):	
    @classmethod
    def setUpClass(cls):
        cls.filial = '01'
        cls.descricao = 'TESTE GRUPO'
        cls.descricaoEdt = 'TESTE GRUPO EDITADO'
        cls.competencia = '002' 
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '40')
        cls.oHelper.SetLateralMenu("Atualizações > Cadastro > Grupos")
        cls.oHelper.SetButton('Confirmar')
        

    def test_cadastro_de_grupos(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')
            

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')
        
        sleep(5)
        self.oHelper.WaitShow("Grupo")      
        self.oHelper.Screenshot("GRUPO_01")
        self.oHelper.SetButton("Incluir")
        sleep(2) 
        self.oHelper.WaitShow("Grupo - INCLUIR")
        self.oHelper.Screenshot("GRUPO_02")   
        self.oHelper.SetValue('Descricao',self.descricao,check_value=False)
        sleep(2)
        self.oHelper.SetValue("Competencia",'000002',        grid=True, grid_number=1, check_value=False)
        self.oHelper.LoadGrid()    
        self.oHelper.SetButton("Salvar")
        sleep(1) 
        self.oHelper.SetButton("Cancelar")
        sleep(1)    
        
        self.oHelper.Screenshot("GRUPO_06")
        
        #---------------
        # VISUALIZAR
        #----------------
        self.oHelper.SetButton("Visualizar")
        sleep(2)
        self.oHelper.WaitShow('Grupo - VISUALIZAR')
        self.oHelper.Screenshot("GRUPO_07")
        self.oHelper.SetButton("Cancelar")
        
        #-----------------
        #  ALTERAR
        #----------------- 
        self.oHelper.SetButton('Alterar')        
        sleep(0.5)
        self.oHelper.WaitShow('Grupo - ALTERAR')
        self.oHelper.SetValue('Descricao',self.descricaoEdt,check_value=False)
        self.oHelper.Screenshot("GRUPO_08")
        self.oHelper.SetButton('Salvar')
        self.oHelper.Screenshot("GRUPO_09")
        
        #-----------------
        # EXCLUIR
        #-----------------
        
        self.oHelper.SetButton('Outras Ações',"Excluir")
        
        
        
        self.oHelper.WaitShow("Grupo - EXCLUIR")
        self.oHelper.Screenshot("GRUPO_10")
        sleep(1)
        self.oHelper.SetButton('Confirmar')
        sleep(1)
        self.oHelper.Screenshot("GRUPO_11")
        
        
        self.oHelper.AssertTrue()
        
        print("------------------------------------------------")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_cadastro_de_grupos")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
        
    

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TRMA030('test_cadastro_de_grupos'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
