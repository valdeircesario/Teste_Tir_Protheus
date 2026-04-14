from tir.technologies.core.base import By
from tir import Webapp
from pytest import mark
import unittest
from time import sleep
from os import getcwd
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')

#  .\venv\Scripts\python.exe -m pytest .\TESTS\SIGAGPE\ETAPA04\GPEM040\test_GPEM040_01.py

#------------------------
# RECISÃO COMPLEMENTAR
#------------------------

class GPEM040_01(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.filial = '02DF0001'
        self.Matricula = '202394'
        self.Nome = 'ELMAR DIAS DE ABREU'
        self.data ='09/10/2020'
        self.Periodo = '202603'
        self.dataref = (datetime.today()-timedelta(days=10)).strftime("%d/%m/%Y")


        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', self.dataref, '02', self.filial, '07')
        self.oHelper.SetLateralMenu("Miscelanea > Cálculos (13)> Rescisão")
        #self.oHelper.SetButton('Confirmar')

    def test_Rescisao_Complementar(self):

        sleep(5)

        if self.oHelper.IfExists("Reforma Tributária"):
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()

        sleep(5)

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()

        self.oHelper.WaitShow("Funcionários")
    
        
        self.oHelper.Screenshot("GPEM040_01.png")
        
        self.oHelper.SearchBrowse(self.filial + self.Matricula + self.Nome, key="Filial+Matricula+Nome")
        sleep(1)       

        """ self.oHelper.SetButton('Incluir')
        self.oHelper.SearchBrowse(self.filial)
        self.oHelper.Screenshot("GPEM040_03.png")
        self.oHelper.SetButton("OK")
        sleep(1)
        
        if self.oHelper.IfExists("Foi criada a opção Retificação, que irá retificar os eventos S-2299/S-2399 do eSocial"):
            self.oHelper.SetButton("OK")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        sleep(2)
            
        self.oHelper.SetButton('Salvar')
        
            
        sleep(2)
        
         
        self.oHelper.WaitShow("Rescisões - INCLUIR")
        self.oHelper.Screenshot("GPEM040_04.png")
        
        
        
        sleep(3)
        self.oHelper.SetValue("RG_DATAHOM",self.dataref)
        self.oHelper.SetValue("RG_DTGERAR",self.dataref)
        
        self.oHelper.SetKey("F7")
        
        sleep(2)
         
        
        
        self.oHelper.WaitShow('Lançamentos por Funcionário')
        
        #self.oHelper.SetValue("CPERIODO",self.Periodo,  grid=True, grid_number=1)
        self.oHelper.SetValue("Cod Verba",'850',        grid=True, grid_number=1, check_value=False)
        self.oHelper.SetValue("Valor",'199',            grid=True, grid_number=1, check_value=False)
        
        self.oHelper.LoadGrid()
        self.oHelper.Screenshot("GPEM040_05.png")
        sleep(0.5)  
        
        self.oHelper.SetButton("Salvar")
        self.oHelper.Screenshot("GPEM040_05.png")
        sleep(0.5)
        self.oHelper.SetKey('F6')
        
        self.oHelper.CheckHelp(text="ATENÇÃO", button="Sim")
        
        self.oHelper.WaitProcessing("Processando")
        
        self.oHelper.ScrollGrid(column="Codigo Verba", match_value= "850",                 grid_number=1)
        self.oHelper.LoadGrid()
        
        self.oHelper.SetButton('Confirmar')
        
        if self.oHelper.IfExists("Registro inserido com sucesso"):
            self.oHelper.SetButton("Fechar")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue() """
            
        """ self.oHelper.SetButton("Visualizar")
        self.oHelper.WaitShow('Rescisões - VISUALIZAR')
        self.oHelper.Screenshot("GPEM040_04.png")
        self.oHelper.SetButton("Fechar")
        
        sleep(2)
        
        self.oHelper.SetButton("Outras Ações","Excluir")
        
        self.oHelper.WaitShow('Tem certeza que deseja excluir o item abaixo?')
        
        self.oHelper.SetButton('Confirmar') """
        
        sleep(3)
        
        
        # Clica na primeira linha da grid para selecionar o registro
        self.oHelper.ScrollGrid(column="Dt. Homologa", match_value = self.dataref, grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Outras Ações","Excluir")
        
        self.oHelper.Screenshot("GPEM040_05.png")
        sleep(0.5)

        self.oHelper.SetKey("F6")
        self.oHelper.Screenshot("GPEM040_06.png")
        sleep(2)

        if self.oHelper.IfExists("Atenção"):
            self.oHelper.Screenshot("GPEM040_07.png")
            self.oHelper.SetButton("Sim")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()

        self.oHelper.Screenshot("GPEM040_08.png")
        sleep(6)

        if self.oHelper.IfExists("Log de Ocorrencias no Processo de Calculo"):
            self.oHelper.ClickCheckBox("Em Disco")
            self.oHelper.Screenshot("GPEM040_09.png")
            self.oHelper.SetButton("OK")
            sleep(1)
            self.oHelper.Screenshot("GPEM040_10.png")
            self.oHelper.SetButton("Sair")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            sleep(5)
        self.oHelper.Screenshot("GPEM040_10.png")
        sleep(2)

        self.oHelper.WaitShow("Rescisões - INCLUIR")
        sleep(1)
        self.oHelper.SetButton("Confirmar")

        self.oHelper.WaitShow("Funcionários")

        self.oHelper.Screenshot("GPEM040_11.png")

        self.oHelper.AssertTrue()

        print("/")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_Rescisao_Complementar")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEM040_01('test_Rescisao_Complementar'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
