from tir.technologies.core.base import By
from tir import Webapp
from pytest import mark
import unittest
from time import sleep
from os import getcwd
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')

#  .\venv\Scripts\python.exe -m pytest .\TESTS\SIGAGPE\PXGPEA24\test_PXGPEA24_02.py -s

#----------------------------------------------------------------
# LANÇAMENTO AVULSO PARA FUNCIONARIO, CALCULAR / LANÇAR /CALCULAR
#----------------------------------------------------------------

class PXGPEA24_02(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.filial = '02DF0001'
        self.Matricula = '228419'
        self.Nome = 'MURILO AUGUSTO DA SILVA'
        self.dataref = (datetime.today()-timedelta(days=0)).strftime("%d/%m/%Y")
        self.dataVenv = (datetime.today()-timedelta(days= 0)).strftime("%d/%m/%Y")
        self.Movimentacao = '1 - Titular'
        self.Movimentacaoedit = '3  - Ambos'
        self.ValorTitular = '256'
        self.ValorDependente = '128'
        self.Verba01 = '771'
        self.Verba02 = '773'
        self.Valor = '150'
        

        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', self.dataref, '02', self.filial, '07')
        
        self.oHelper.SetLateralMenu("Atualizações > Lançamentos > Por Funcionário ")
        

    def test_de_lançamento_avulso_para_funcionario(self):

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
            
        #------------------------------------
        # CALCULAR FOLHA ANTES DO LANÇAMENTO
        #------------------------------------
            
        self.oHelper.WaitShow("Lançamentos por Período")
        self.oHelper.Screenshot("PXGPEA24_02_01.png")  
        self.oHelper.SearchBrowse(self.filial + self.Matricula, key="Filial+matricula+Nome")
        sleep(0.3)
        self.oHelper.Screenshot("PXGPEA24_02_02.png")
        self.oHelper.SetButton("Alterar")
        sleep(5) 
        #------------------
        # CALCULAR FOLHA F6
        #------------------
        self.oHelper.SetKey("F6")
        self.oHelper.WaitShow("Processando")
        sleep(30)
        self.oHelper.Screenshot("PXGPEA24_02_03.png") 
        self.oHelper.SetButton("OK")
        
        #---------------------
        # CONSULTAR CALCULO F7
        #---------------------
        
        self.oHelper.SetKey("F7")
        sleep(5)
        
        self.oHelper.WaitShow("Lançamentos por Funcionário")  
            
        self.oHelper.Screenshot("PXGPEA24_02_04.png")
        
        self.oHelper.SetButton('Confirmar') 
        self.oHelper.SetButton("Salvar")
        sleep(2)
        
        #------------------------------------
        # FAZER LANÇAMENTO PARA O FUNCIONARIO
        #------------------------------------
    
        self.oHelper.SetLateralMenu("Atualizações > Lançamentos > Lancamentos Avulso")
        self.oHelper.WaitShow("Lançamentos Avulsos")
        self.oHelper.Screenshot("PXGPEA24_02_10.png")
        self.oHelper.SearchBrowse(self.filial + self.Matricula + self.Nome, key="Filial+matricula+Nome")
        sleep(5)
        self.oHelper.Screenshot("PXGPEA24_02_11.png")
        
        self.oHelper.WaitShow("Lançamentos Avulsos")
        self.oHelper.SetButton("Manutenção")
        sleep(5)
        self.oHelper.WaitShow("Funcionários - MANUTENÇÃO")
        self.oHelper.Screenshot("PXGPEA24_02_12.png")
        
        #---------------------
        # PREENCHEDO AS GRID
        #---------------------
                
        self.oHelper.ScrollGrid(column="Sequencia", match_value= "0012",          grid_number=1)
        self.oHelper.SetKey("DOWN",                                                   grid=True)
        self.oHelper.SetValue('Verba',  self.Verba02,                        grid= True, check_value=False)
        self.oHelper.SetValue('Valor',  self.Valor,                          grid=True, check_value=False)
        self.oHelper.SetValue('Dt. Venc.', self.dataVenv,                    grid=True, check_value=False)
        self.oHelper.SetValue('Observacao', "TESTE AUTOMATIZADO",            grid=True, check_value=False)
        self.oHelper.SetValue('Roteiro', "FOL",                              grid=True, check_value=False)
        self.oHelper.LoadGrid()
        self.oHelper.Screenshot("PXGPEA24_02_13.png")
        
        #----------------------------------------
        # PREECHENDO CRID 2 PARA POIS LANCAMENTOS
        #----------------------------------------
        
        self.oHelper.ScrollGrid(column="Verba", match_value= self.Verba02,          grid_number=1)
        self.oHelper.SetKey("DOWN",                                                   grid=True)
        self.oHelper.SetValue('Verba',  self.Verba01,                        grid= True, check_value=False)
        self.oHelper.SetValue('Valor',  self.Valor,                          grid=True, check_value=False)
        self.oHelper.SetValue('Dt. Venc.', self.dataVenv,                    grid=True, check_value=False)
        self.oHelper.SetValue('Observacao', "TESTE AUTOMATIZADO",            grid=True, check_value=False)
        self.oHelper.SetValue('Roteiro', "FOL",                              grid=True, check_value=False)
        self.oHelper.LoadGrid()
        self.oHelper.Screenshot("PXGPEA24_02_14.png")
        self.oHelper.SetButton("Confirmar")
        
        if self.oHelper.IfExists("Registro alterado com sucesso"):
            self.oHelper.Screenshot("PXGPEA24_02_15.png")
            self.oHelper.SetButton("Fechar")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
             
        self.oHelper.WaitShow("Lançamentos Avulsos")
        
        #------------------------
        # VISUALIZAR O LANÇAMENTO
        #------------------------
        
        self.oHelper.SetButton("Visualizar")  
        self.oHelper.Screenshot("PXGPEA24_02_16.png") 
        self.oHelper.WaitShow("Funcionários - VISUALIZAR")
        
        self.oHelper.ScrollGrid(column="Verba", match_value= self.Verba02,          grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.ScrollGrid(column="Verba", match_value= self.Verba01,          grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.Screenshot("PXGPEA24_02_17.png")  
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Lançamentos Avulsos")
        sleep(3)
        
        #--------------------------------
        # CALCULAR FOLHA APOS O LANÇAMENTO
        #--------------------------------
        
        self.oHelper.SetLateralMenu("Atualizações > Lançamentos > Por Funcionário ")
        
        self.oHelper.WaitShow("Lançamentos por Período")
        self.oHelper.Screenshot("PXGPEA24_02_18.png")  
        self.oHelper.SearchBrowse(self.filial + self.Matricula, key="Filial+matricula+Nome")
        sleep(0.3)   
        self.oHelper.SetButton("Alterar")
        sleep(5)
        self.oHelper.Screenshot("PXGPEA24_02_19.png")
        
        #------------------
        # CALCULAR FOLHA F6
        #------------------
        
        self.oHelper.SetKey("F6")
        self.oHelper.WaitShow("Processando")
        sleep(30)
        self.oHelper.Screenshot("PXGPEA24_02_20.png")   
        self.oHelper.SetButton("OK")
        
        #----------------------------------------
        # CONSULTAR CALCULO F7 & VALIDA AS VERBAS
        #----------------------------------------
        
        self.oHelper.SetKey("F7")
        sleep(5)
        
        self.oHelper.WaitShow("Lançamentos por Funcionário")
        self.oHelper.CheckResult("Codigo Verba",self.Verba01,   grid=True)
        self.oHelper.CheckResult("Codigo Verba",self.Verba02,   grid=True)
        self.oHelper.LoadGrid()
        self.oHelper.Screenshot("PXGPEA24_02_21.png")
        
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_lançamento_avulso_para_funcionario")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
        
            

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(PXGPEA24_02('test_Lançamento_Avulso'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
