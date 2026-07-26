from tir import Webapp
from pytest import mark
import unittest
import os
from os import getcwd
from datetime import date
from datetime import datetime, timedelta
from time import sleep

from utilis.click_pageview import click_pageview_visible_button


# TRANSFERENCIA FUNCIONÁRIO PARA OUTRO DEPARTAMENTO

class GPEA180(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.filial = '01'
        cls.mat = '12345' 
        cls.DP_destino = '000000883'  
        cls.dataref = (datetime.today()-timedelta(days=5)).strftime("%d/%m/%Y")# AJUSTAR DATA PARA PERIODO EM ABERTO 
    
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', cls.dataref, '99', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Atualizações > Funcionários > Transferências")
        

    def test_transferencia_funcionario_de_departamento(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        
        print('----------------------Pesquisa de funcionario')   
        self.oHelper.WaitShow("Transferências")
        self.oHelper.Screenshot("transferencia_02_01.png")
        self.oHelper.SetButton("Pesquisar")
        self.oHelper.SetButton("Parâmetros")
        self.oHelper.SetValue("Filial", self.filial)
        self.oHelper.SetValue("Matricula", self.mat)
        self.oHelper.SetButton("Ok")
        self.oHelper.Screenshot("transferencia_02_02.png")

        print('--------------------------Transferir')
        self.oHelper.SetButton('Outras Ações', 'Transferir')    
        self.oHelper.WaitShow('Transferências - TRANSFERIR')
        self.oHelper.ClickBox("Matricula", self.mat,   grid_number=1)
        self.oHelper.Screenshot("transferencia_02_03.png")
        self.oHelper.SetButton('Confirmar')
        
        self.oHelper.WaitShow('Transferências - TRANSFERIR')
        self.oHelper.Screenshot("transferencia_02_04.png")
        
        self.oHelper.SetValue("RA_DEPTO", self.DP_destino, grid=True, grid_number=2)
        self.oHelper.LoadGrid()
        self.oHelper.Screenshot("transferencia_02_05.png")
        self.oHelper.SetButton('Confirmar')

        print('--------------------------Confirmar Transferencia')  
        self.oHelper.IfExists("Confirma a Transferência ? ")
        self.oHelper.Screenshot("transferencia_02_06.png")
        self.oHelper.SetButton('Sim')    
        sleep(3) 
        
        if self.oHelper.IfExists("O funcionário é responsavel por um departamento, deseja desassociá-lo?"):
            self.oHelper.Screenshot("AD_GLPI_06.1.png")
            self.oHelper.SetButton('Sim')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        sleep(3)    
        if self.oHelper.IfExists("Deseja enviar e-mail dessa Transferência?"):
            self.oHelper.Screenshot("transferencia_02_07.png")
            self.oHelper.SetButton('Sim')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            sleep(0.5)     
        print('--------------------------Conferindo os Logs')
        self.oHelper.WaitShow("Log de Ocorrencias - Gestão de Pessoal - Versao 12")
        self.oHelper.ClickLabel("Em Disco")
        self.oHelper.Screenshot("transferencia_02_11.png")
        self.oHelper.SetButton("OK")     
        sleep(10)
        click_pageview_visible_button(self.oHelper, "Ampliar (+)")
        self(2)
        click_pageview_visible_button(self.oHelper, "Ampliar (+)")
        self(2)
        click_pageview_visible_button(self.oHelper, "Ampliar (+)")
        self(2)
        self.oHelper.Screenshot("transferencia_02_12.png")
        self.oHelper.SetButton("Sair")
        sleep(5)
        self.oHelper.SetButton("Cancelar")
        self.oHelper.WaitShow("Transferências")
        self.oHelper.AssertTrue()
        
        print("------------------------------------------------")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_transferencia_funcionario_de_departamento")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
    

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA180('test_transferencia_funcionario_de_departamento'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
