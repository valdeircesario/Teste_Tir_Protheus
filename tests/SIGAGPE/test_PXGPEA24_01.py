from tir.technologies.core.base import By
from tir import Webapp
from pytest import mark
import unittest
from time import sleep
from os import getcwd
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')

# .\venv\Scripts\python.exe -m pytest .\TESTS\SIGAGPE\PXGPEA24\test_PXGPEA24_01.py

#---------------------------------
# LANÇAMENTO AVULSO NA FOLHA CRUD
#--------------------------------

class PXGPEA24_01(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.filial = '02DF0001'
        self.Matricula = '228419'
        self.Nome = 'MURILO AUGUSTO DA SILVA'
        self.dataref = (datetime.today()-timedelta(days=0)).strftime("%d/%m/%Y")
        self.dataVenv = (datetime.today()-timedelta(days= 0)).strftime("%d/%m/%Y")
        self.Verba = '773'
        self.VerbaEdit = '771'
        self.Valor = '180'
        
        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', self.dataref, '02', self.filial, '07')
        
        self.oHelper.SetLateralMenu("Atualizações > Lançamentos > Lancamentos Avulso")
        
    

    def test_Lançamento_Avulso_crud(self):

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
            
        self.oHelper.WaitShow("Lançamentos Avulsos")
        self.oHelper.Screenshot("PXGPEA24_01_01.png")
        
        self.oHelper.SearchBrowse(self.filial + self.Matricula + self.Nome, key="Filial+matricula+Nome")
        sleep(10)
        self.oHelper.Screenshot("PXGPEA24_01_02.png")
        
        self.oHelper.WaitShow("Lançamentos Avulsos")
        
        #------------------------
        # INCLUIR LANÇAMENTO
        #------------------------
        
        self.oHelper.SetButton("Manutenção")
        sleep(5)
        self.oHelper.Screenshot("PXGPEA24_01_03.png")
        self.oHelper.WaitShow("Funcionários - MANUTENÇÃO")  
      
        self.oHelper.ScrollGrid(column="Sequencia", match_value= "0012",     grid_number=1)
        self.oHelper.SetKey("DOWN",                                          grid=True)
        self.oHelper.SetValue('Verba',  self.Verba,                          grid= True, check_value=False)
        self.oHelper.SetValue('Valor',  self.Valor,                          grid=True,  check_value=False)
        self.oHelper.SetValue('Dt. Venc.', self.dataVenv,                    grid=True,  check_value=False)
        self.oHelper.SetValue('Observacao', "TESTE AUTOMATIZADO",            grid=True,  check_value=False)
        self.oHelper.SetValue('Roteiro', "FOL",                              grid=True,  check_value=False)
        self.oHelper.LoadGrid()
        self.oHelper.Screenshot("PXGPEA24_01_04.png")
        self.oHelper.SetButton("Confirmar")
        
        if self.oHelper.IfExists("Registro alterado com sucesso"):
            self.oHelper.Screenshot("PXGPEA24_01_05.png")
            self.oHelper.SetButton("Fechar")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
             
        self.oHelper.WaitShow("Lançamentos Avulsos")
        
        #------------------------
        # VISUALIZAR O LANÇAMENTO
        #------------------------
        
        self.oHelper.SetButton("Visualizar")  
        self.oHelper.Screenshot("PXGPEA24_01_06.png") 
        self.oHelper.WaitShow("Funcionários - VISUALIZAR")
        
        self.oHelper.ScrollGrid(column="Verba", match_value= self.Verba,          grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.Screenshot("PXGPEA24_01_07.png")   
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Lançamentos Avulsos")
        sleep(3)
        
        #------------------------
        # EDITAR O LANÇAMENTO
        #------------------------
        
        self.oHelper.SetButton("Manutenção")
        sleep(5)
        self.oHelper.WaitShow("Funcionários - MANUTENÇÃO")  
      
        self.oHelper.ScrollGrid(column="Verba", match_value= self.Verba,          grid_number=1)
        self.oHelper.SetValue('Verba',              self.VerbaEdit,               grid= True,    grid_number=1, check_value=False)
        self.oHelper.SetValue('Valor',              self.Valor,                   grid=True,     grid_number=1, check_value=False)
        self.oHelper.SetValue('Dt. Venc.',          self.dataVenv,                grid=True,     grid_number=1, check_value=False)
        self.oHelper.SetValue('Observacao', "TESTE AUT EDITADO",                  grid=True,     grid_number=1, check_value=False)
        self.oHelper.SetValue('Roteiro', "FOL",                                   grid=True,     grid_number=1, check_value=False)
        self.oHelper.LoadGrid()
        self.oHelper.Screenshot("PXGPEA24_01_08.png") 
        self.oHelper.SetButton("Confirmar")
        
        if self.oHelper.IfExists("Registro alterado com sucesso"):
            self.oHelper.Screenshot("PXGPEA24_01_09.png") 
            self.oHelper.SetButton("Fechar")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
        self.oHelper.WaitShow("Lançamentos Avulsos")
        sleep(3)
        
        #------------------------
        # EXCLUIR O LANÇAMENTO
        #------------------------
        
        self.oHelper.SetButton("Manutenção")
        sleep(5)
        self.oHelper.WaitShow("Funcionários - MANUTENÇÃO")  
      
        self.oHelper.ScrollGrid(column="Verba", match_value= self.VerbaEdit,          grid_number=1)
        self.oHelper.SetKey("DELETE", grid=True, grid_number=1)
        self.oHelper.LoadGrid() 
        self.oHelper.Screenshot("PXGPEA24_01_10.png")                                  
        self.oHelper.SetButton("Confirmar")
        
        if self.oHelper.IfExists("Registro alterado com sucesso"):
            self.oHelper.Screenshot("PXGPEA24_01_11.png") 
            self.oHelper.SetButton("Fechar")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
        self.oHelper.WaitShow("Lançamentos Avulsos")
        sleep(3)
        
        #------------------------
        # VERIFICA EXCLUSÃO DO LANÇAMENTO
        #------------------------
        
        self.oHelper.SetButton("Manutenção")
        sleep(5)
        self.oHelper.WaitShow("Funcionários - MANUTENÇÃO")
        self.oHelper.Screenshot("PXGPEA24_01_12.png")     
        self.oHelper.AssertTrue()
        
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_lançamento_avulso_crud")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(PXGPEA24_01('test_Lançamento_Avulso_crud'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
