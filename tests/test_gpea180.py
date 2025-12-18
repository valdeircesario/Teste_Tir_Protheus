from tir import Webapp
from pytest import mark
import unittest
import os
from os import getcwd
from datetime import date
from datetime import datetime, timedelta
from time import sleep

# cd c:\Users\97137227104\Desktop\cloneTirProthus\tir\tests; C:\Users\97137227104\Desktop\cloneTirProthus\.venv\Scripts\python.exe test_gpea180.py 

# TRANSFERENCIA FUNCIONÁRIO

class GPEA180(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.filial = '02CE0043'
        self.mat = '218843' #sempre usar matricula diferentes, 21998X,226919,220546,228253,210176,21032X
        self.CC_destino = '000000677'  # Aconsenhavel usar centro de custo que tenha vaga  Proxima 000000040, '000000653,000000040,000000005,000000470, 000000103,000000043,000000270,000000646, 000000083,000000677,000000040
        self.DP_destino = '000000877'  # Aconsenhavel usar departamento que tenha vaga   Proxima " 000000192, 000000261 , 000000193,000000006,000000470,000000787, 000000845, 000000626, 000000795, 000000530,000000877,000000192
        self.Fl_destino = '02AM0042'
        self.dataref = (datetime.today()-timedelta(days=80)).strftime("%d/%m/%Y")
        self.Periodo_Para = (datetime.today()+timedelta(days=-80)).strftime("%Y%m")
        self.Nro_Pagto_Para = '01'
        

        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', self.dataref, '02', self.filial, '07')
        self.oHelper.SetLateralMenu("Atualizações > Funcionários > Transferências")
        

    def test_transferencia(self):

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
        self.oHelper.SetButton("Pesquisar")
        self.oHelper.SetButton("Parâmetros")
        self.oHelper.SetValue("Filial", self.filial)
        self.oHelper.SetValue("Matricula", self.mat)
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton('Outras Ações', 'Transferir')
        sleep(0.8)
        
        self.oHelper.WaitShow('Transferências - TRANSFERIR')
        self.oHelper.ClickBox("Matricula", self.mat,   grid_number=1)
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetValue("RA_FILIAL", self.Fl_destino, grid=True, grid_number=2)
        self.oHelper.SetValue("RA_CC", self.CC_destino,    grid=True, grid_number=2)
        self.oHelper.SetValue("RA_DEPTO", self.DP_destino, grid=True, grid_number=2)
        self.oHelper.SetValue("RA_PROCES", "00001",    grid=True, grid_number=2)
        self.oHelper.SetValue("RA_ITEM", "0001",       grid=True, grid_number=2)
        self.oHelper.SetValue("RA_CLVL", "0001.1",       grid=True, grid_number=2)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton('Confirmar')
        
        if self.oHelper.IfExists("Departamento possui centro de custo diferente do centro de custos do funcionário"):
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
        
            self.oHelper.AssertTrue()
            
        if self.oHelper.IfExists("Departamento possui centro de custo diferente do centro de custos do funcionário"):
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
        
            self.oHelper.AssertTrue()
        
        
        
        self.oHelper.WaitShow("Confirma a Transferência ?")
        self.oHelper.SetButton('Sim')
        
        
        if self.oHelper.IfExists("Transferências - TRANSFERIR"):
            self.oHelper.SetValue("Periodo Para",self.Periodo_Para,grid=True, grid_number=1)
            self.oHelper.SetValue("Nro. Pagto Para", self.Nro_Pagto_Para,grid=True, grid_number=1)
            self.oHelper.LoadGrid()
            self.oHelper.SetButton('Confirmar')
            
            self.oHelper.AssertTrue()
        else:
        
            self.oHelper.AssertTrue()
            
            
        #self.oHelper.WaitShow("Não existe vaga disponivel para esse departamento!")
            
        if self.oHelper.IfExists("Não existe vaga disponivel para esse departamento!"):
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
        
            self.oHelper.AssertTrue()
        
        if self.oHelper.IfExists("Não existe vaga disponivel para esse departamento!"):
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
        
            self.oHelper.AssertTrue()
        
            
        
        #self.oHelper.WaitShow("Help: ATENÇÃO")
        
        if self.oHelper.IfExists("Help: ATENÇÃO"):
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
        
            self.oHelper.AssertTrue()
            
        self.oHelper.WaitShow("Help: ATENÇÃO")     
        
        if self.oHelper.IfExists("Help: ATENÇÃO"):
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
        
            self.oHelper.AssertTrue()
            self.oHelper.SetButton('Fechar')
        
    
        if self.oHelper.IfExists("Deseja enviar e-mail dessa Transferência?"):
            self.oHelper.SetButton('Sim')
            self.oHelper.AssertTrue()
        else:
        
            self.oHelper.AssertTrue()
        
        if self.oHelper.IfExists("Deseja inserir a Data da Portaria?"):
            self.oHelper.SetButton('Sim')
            self.oHelper.SetValue("Data da Portaria", self.dataref)
            self.oHelper.SetButton('Confirmar')
            self.oHelper.AssertTrue()
        else:
        
            self.oHelper.AssertTrue()
            
        
        self.oHelper.SetButton('fechar')
        
        
        self.oHelper.WaitShow("Log de Ocorrencias - Gestão de Pessoal - Versao 12")
        self.oHelper.SetButton('Cancelar')
        
        self.oHelper.WaitShow("Deseja cancelar a geraçäo do LOG?")
        self.oHelper.SetButton('Sim')
        
        self.oHelper.SetButton('Cancelar')
        
        
        self.oHelper.SetButton('Visualizar')
        self.oHelper.WaitShow('Transferências - Visualizar')
        self.oHelper.SetButton('Confirmar')
        
        self.oHelper.WaitShow("Transferências")
        self.oHelper.SetButton("Outras Ações", "Informar Data da Portaria")
        self.oHelper.WaitShow("Manutenção portarias - Edição")
        self.oHelper.SetValue("Data da Portaria", self.dataref)
        self.oHelper.SetButton('Confirmar')
        self.oHelper.LoadGrid()

        self.oHelper.AssertTrue()
        
    

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA180('test_transferencia'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
