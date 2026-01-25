from tir import Webapp
from pytest import mark
import unittest
import os
from os import getcwd
from datetime import date
from datetime import datetime, timedelta
from time import sleep

# cd Testes-Protheus; & .\venv\Scripts\Activate.ps1; pytest TESTS/SIGAGPE/GPEA180/test_GPEA180_01.py

# TRANSFERENCIA FUNCIONÁRIO PARA OUTRO DEPARTAMENTO

class GPEA180_02(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.filial = '02DF0001'
        self.mat = '225955' # O TESTE DEVE SEMPRE PROCURAR UM FUNCIONARIO DO CENTRO DE CUSTOS 000000677 PARA MELHOR RESULTADO
        self.DP_destino = '000000868' # USE SEMPRE UM DOS DEPATAMENTOS AQUI  >  DP_destino = 000000866,000000868,000000869,000000870,000000876,000000877,000000879,000000880,000000881,000000882,000000883,000000884,000000885,000000886,000000894
        self.dataref = (datetime.today()-timedelta(days=0)).strftime("%d/%m/%Y")# AJUSTAR DATA PARA PERIODO EM ABERTO
        self.Periodo_Para = (datetime.today()+timedelta(days=-0)).strftime("%Y%m")
    
        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', self.dataref, '02', self.filial, '07')
        self.oHelper.SetLateralMenu("Atualizações > Funcionários > Transferências")
        

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
            
        if self.oHelper.IfExists("Departamento possui centro de custo diferente do centro de custos do funcionário"):
            self.oHelper.SetButton('Fechar')
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
        
            self.oHelper.AssertTrue()
            
        self.oHelper.WaitShow("Transferências")
        self.oHelper.Screenshot("GPEA180_01.png")
        self.oHelper.SetButton("Pesquisar")
        self.oHelper.SetButton("Parâmetros")
        self.oHelper.SetValue("Filial", self.filial)
        self.oHelper.SetValue("Matricula", self.mat)
        self.oHelper.SetButton("Ok")
        self.oHelper.Screenshot("GPEA180_02.png")
        self.oHelper.SetButton('Outras Ações', 'Transferir')
        sleep(0.8)
        
        self.oHelper.WaitShow('Transferências - TRANSFERIR')
        self.oHelper.ClickBox("Matricula", self.mat,   grid_number=1)
        self.oHelper.Screenshot("GPEA180_03.png")
        self.oHelper.SetButton('Confirmar')
        
        self.oHelper.WaitShow('Transferências - TRANSFERIR')
        self.oHelper.Screenshot("GPEA180_04.png")
        
        self.oHelper.SetValue("RA_DEPTO", self.DP_destino, grid=True, grid_number=2)
        self.oHelper.LoadGrid()
        self.oHelper.Screenshot("GPEA180_05.png")
        self.oHelper.SetButton('Confirmar')
          
        if self.oHelper.IfExists("Confirma a Transferência ? "):
            self.oHelper.Screenshot("GPEA180_06.png")
            self.oHelper.SetButton('Sim')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        sleep(0.5)    
        if self.oHelper.IfExists("Deseja enviar e-mail dessa Transferência?"):
            self.oHelper.Screenshot("GPEA180_07.png")
            self.oHelper.SetButton('Sim')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            sleep(0.5)     
            
        if self.oHelper.IfExists("Deseja inserir a Data da Portaria?"):
            self.oHelper.Screenshot("GPEA180_08.png")
            self.oHelper.SetButton('Sim')
            self.oHelper.SetValue("Data da Portaria", self.dataref)
            self.oHelper.Screenshot("GPEA180_09.png")
            self.oHelper.SetButton('Confirmar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        sleep(0.9)
        self.oHelper.Screenshot("GPEA180_10.png")  
        self.oHelper.SetButton('fechar')
        
        sleep(0.5)
        self.oHelper.WaitShow("Log de Ocorrencias - Gestão de Pessoal - Versao 12")
        if self.oHelper.IfExists("Log de Ocorrencias - Gestão de Pessoal - Versao 12"):
            self.oHelper.ClickLabel("Em Disco")
            self.oHelper.Screenshot("GPEA180_11.png")
            self.oHelper.SetButton("OK")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
        sleep(25)
        self.oHelper.Screenshot("GPEA180_12.png")
        self.oHelper.SetButton("Sair")
        sleep(10)
        self.oHelper.SetButton("Cancelar")
        sleep(10)
        self.oHelper.AssertTrue()
        
        print("------------------------------------------------")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_transferencia_funcionario_de_departamento")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
    

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA180_02('test_transferencia_funcionario_de_departamento'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
