from tir import Webapp
from pytest import mark
import unittest
from os import getcwd
from datetime import datetime, timedelta
from time import sleep
from selenium.webdriver.common.by import By

DateSystem = datetime.today().strftime('%d/%m/%Y')

class GPER102(unittest.TestCase):# 	GPER102
    @classmethod
    def setUpClass(self):
        self.filial = '02DF0001'
        self.matricula = '227902'
        self.situacao = ' ADFT*'
        self.periodo = '202601'
        
        self.dataref = (datetime.today()-timedelta(days=5)).strftime("%d/%m/%Y")# AJUSTAR DATA PARA PERIODO EM ABERTO 
    
        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', self.dataref, '02', self.filial, '07')
        self.oHelper.SetLateralMenu("Relatorios > Lançamentos > Por Periodo Vertical")
        self.oHelper.SetButton('Confirmar')
        

    def test_geracao_relatorio_verba(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            #self.oHelper.SetButton('Confirmar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        self.oHelper.Screenshot("Relatorio_verba_01")    
            
        self.oHelper.SetButton("Outras Ações",'Parâmetros')
        self.oHelper.Screenshot("Relatorio_verba_02") 
        
        self.oHelper.SetValue("Filial ?", self.filial, check_value=False)
        
        self.oHelper.SetValue("Matrícula ?", self.matricula, check_value=False)
        
        self.oHelper.SetValue("Situações ?", self.situacao, check_value=False)
         
        self.oHelper.SetButton('Confirmar')
        
        self.oHelper.SetValue("Categorias ?", 'M*****************', check_value=False)
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetKey('TAB')
        
        
        self.oHelper.SetValue("Período ?", self.periodo)
        self.oHelper.Screenshot("Relatorio_verba_03")    
        self.oHelper.SetValue("Todas as Verbas ?", 'Sim', check_value=False)
        self.oHelper.SetButton('Confirmar')  
        self.oHelper.SetValue("Salário do Cadastro ?", 'Não', check_value=False) 
        self.oHelper.SetValue("Lista Total Empresa ?", 'Sim', check_value=False) 
        self.oHelper.SetValue("Imprimir Bases ?", 'Não', check_value=False) 
        self.oHelper.SetButton('OK')
        self.oHelper.Screenshot("Relatorio_verba_04")
        self.oHelper.SetButton('Imprimir')   
        sleep(8)
        self.oHelper.Screenshot("Relatorio_verba_04")
        
        
        
        self.oHelper.SetButton('Sair')
        sleep(5)
        self.oHelper.AssertTrue()
        
        print("------------------------------------------------")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_geracao_relatorio_verba")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
        
    

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPER102('test_geracao_relatorio_verba'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
