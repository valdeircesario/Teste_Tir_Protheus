from tir import Webapp
from pytest import mark
import unittest
import os
from os import getcwd
from datetime import date
from datetime import datetime, timedelta
from time import sleep

import sys
from os import path
sys.path.append(path.abspath(path.join(path.dirname(__file__), '..', '..')))

from utilis.click_pageview import click_pageview_visible_button
DateSystem = datetime.today().strftime('%d/%m/%Y')


# TRANSFERENCIA FUNCIONÁRIO ENTRE CENTRO DE CUSTO DIFERENTE

class GPEA180(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.filial = '01'
        cls.mat = '00000' 
        cls.CC_destino = '021'
        cls.DP_destino = '254' 
        cls.Periodo_Para = (datetime.today()+timedelta(days=-0)).strftime("%Y%m")# AJUSTAR DADA PARA PERIODO EM ABERTO
    
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI',DateSystem, '99', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Atualizações > Funcionários > Transferências")
        

    def test_transferencia_funcionario_entre_centro_de_custo_diferenteUTA(self):

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
            
        #--------------------------
        # Tranferencia
        #----------------------------------
        
        print('----------------------Pesquisando funcionario')  
        self.oHelper.WaitShow("Transferências")
        self.oHelper.Screenshot("tranferencias_01_01.png")
        self.oHelper.SetButton("Pesquisar")
        self.oHelper.SetButton("Parâmetros")
        self.oHelper.SetValue("Filial", self.filial)
        self.oHelper.SetValue("Matricula", self.mat)
        self.oHelper.SetButton("Ok")
        self.oHelper.Screenshot("tranferencias_01_02.png")
        self.oHelper.SetButton('Outras Ações', 'Transferir')

        print('----------------------------Tranferindo')
        self.oHelper.WaitShow('Transferências - TRANSFERIR')
        self.oHelper.ClickBox("Matricula", self.mat,   grid_number=1)
        self.oHelper.Screenshot("tranferencias_01_03.png")
        self.oHelper.SetButton('Confirmar')
        
        self.oHelper.WaitShow('Transferências - TRANSFERIR')
        self.oHelper.Screenshot("tranferencias_01_04.png")
        
        self.oHelper.SetValue("RA_CC", self.CC_destino,    grid=True, grid_number=2)
        self.oHelper.SetValue("RA_DEPTO", self.DP_destino, grid=True, grid_number=2)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Confirmar')

        print('-----------------Confirmando transferencia')
        self.oHelper.WaitShow("Confirma a Transferência ? ")
        self.oHelper.Screenshot("tranferencias_01_05.png")
        self.oHelper.SetButton('Sim')
               
        self.oHelper.WaitShow("Deseja enviar e-mail dessa Transferência?")
        self.oHelper.Screenshot("tranferencias_01_06.png")
        self.oHelper.SetButton('Sim')
             
        print('--------------------------Conferindo os logs')
        self.oHelper.WaitShow("Log de Ocorrencias - Gestão de Pessoal - Versao 12")
        self.oHelper.ClickLabel("Em Disco")
        self.oHelper.Screenshot("tranferencias_01_08.png")
        self.oHelper.SetButton("OK")
        self.oHelper.Screenshot("tranferencias_01_09.png")
        self.oHelper.SetButton("Sair")
        sleep(10)
        click_pageview_visible_button(self.oHelper, "Ampliar (+)")
        self(2)
        click_pageview_visible_button(self.oHelper, "Ampliar (+)")
        self(2)
        click_pageview_visible_button(self.oHelper, "Ampliar (+)")
        self(2)
        self.oHelper.Screenshot("GPEA180_12.png")
        self.oHelper.SetButton("Sair")
        sleep(5)
        self.oHelper.SetButton("Cancelar")
        self.oHelper.WaitShow("Transferências")
        self.oHelper.AssertTrue()
        
        print("------------------------------------------------")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_transferencia_funcionario_entre_centro_de_custo_diferenteUTA")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
    

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA180('test_test_transferencia_funcionario_entre_centro_de_custo_diferenteUTA'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
