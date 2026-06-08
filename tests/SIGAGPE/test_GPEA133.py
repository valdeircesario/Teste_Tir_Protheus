import sys, os
sys.path.insert(0, os.path.join(os.getcwd()))
from selenium.webdriver.common.keys import Keys
from tools.Selenium_commands import SeleniumCommands
from tir.technologies.core.base import By
from tir import Webapp
from pytest import mark
import unittest
from time import sleep
from os import getcwd
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')

#----------------------------------------------------------------
# LANÇAMENTO DE VALE TRANSPORTE E CALCULO NA FOLHA E VALIDAÇÃO
#----------------------------------------------------------------

# OBSERVAÇÃO >>> DEVE EXECUTAR ESSE TESTE SEMPRE COM UM FUNCIONARIO QUE NÃO POSSUA VTR NA FOLHA.

# ESTE TESTE TEM POR OBJETIVO FAZER UM LANÇAMENTO DE VTR PARA UM FUNCIONARIO, 


class GPEA133(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
                                                                        
        cls.filial = '02DF0001'
        cls.Matricula = '210168'
        cls.Nome = 'TAIS SIMOES SEIDLER'
        cls.Verba = '620'
        cls.dataref = (datetime.today()-timedelta(days=5)).strftime("%d/%m/%Y")
        
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', cls.dataref, '02', cls.filial, '07')
                
        
        cls.oHelper.SetLateralMenu("Atualizações > Beneficios > Vt / Vr / Va > Atualização")
         
        #cls.oHelper.SetButton('Confirmar') -- observar essas linha, em meu ambiete de trabalho, o browser não visualiza a tela de trocar modulos.

        

    def test_lancamento_vale_transporte_e_claculo_folha(self):

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
            
            
            
        #----------------------------------------------------------------
        # FAZ O LANÇAMENTO DO VTR PARA UM FUNCIONARIO, QUE NÃO POSSUA VTR
        #-----------------------------------------------------------------
    
        self.oHelper.WaitShow("Atualização Vales")
        self.oHelper.Screenshot("Incluindo_VTR_01") 
        
        #------------------------------------
        # PESQUISAR O FUNCIONARIO PARA O CALCULO
        #------------------------------------ 
        self.oHelper.SearchBrowse(self.filial + self.Matricula + self.Nome, key="Filial+matricula+Nome")
        sleep(0.5)
        self.oHelper.Screenshot("Incluindo_VTR_02")
        sleep(1)
        
        self.oHelper.SetButton('Manutenção')
        sleep(2)
        
        
        if self.oHelper.IfExists("Ao Deletar um registro a rotina verifica se existem dados vinculados àquele Benefício"):
            self.oHelper.Screenshot("Incluindo_VTR_03")
            self.oHelper.SetButton('OK')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        sleep(2)
        self.oHelper.WaitShow('Funcionários - MANUTENÇÃO')
        sleep(2)
        self.oHelper.SetKey("ENTER")
        sleep(2)
        self.oHelper.SetKey("ENTER")
        sleep(1)     
        
        self.oHelper.Screenshot("Incluindo_VTR_04")
        
        self.oHelper.SetButton('Confirmar')
        
        if self.oHelper.IfExists("Registro alterado com sucesso"):
            self.oHelper.Screenshot("Incluindo_VTR_05")
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        self.oHelper.WaitShow('Atualização Vales')
        sleep(1)
        
        self.oHelper.SetButton("Visualizar")
        sleep(1)
        
        self.oHelper.WaitShow('Funcionários - VISUALIZAR')
        self.oHelper.Screenshot("Incluindo_VTR_06")
        self.oHelper.SetButton('Fechar')    
        self.oHelper.WaitShow("Atualização Vales")
        sleep(10)  
        
        
        #------------------------
        # CALCULAR ROTEIRO VTR
        #-----------------------
        
        self.oHelper.SetLateralMenu("Atualizações > Lançamentos > Por Funcionário ")
        
        self.oHelper.WaitShow("Lançamentos por Período")
        self.oHelper.Screenshot("Calculo_vtr_01.png") 
        
        #------------------------------------
        # PESQUISAR O FUNCIONARIO PARA O CALCULO
        #------------------------------------ 
        
        
        self.oHelper.SearchBrowse(self.filial + self.Matricula + self.Nome, key="Filial+matricula+Nome")
        sleep(0.5)
        self.oHelper.Screenshot("Calculo_vtr_06.png")
        sleep(1) 
        self.oHelper.ScrollGrid(column="Matricula", match_value = self.Matricula, grid_number=1)
        sleep(1)
        self.oHelper.Screenshot("Calculo_vtr_07.png")
        
        #-----------------------
        # CALCULAR FOLHA CTRL+F9
        #-----------------------

        sc = SeleniumCommands(self.oHelper._Webapp__webapp.driver)
        sc.send_key('body',Keys.CONTROL+Keys.F9)
        
   
        if self.oHelper.IfExists("Deseja processar o contracheques do funcionario(a):"):
            self.oHelper.Screenshot("Calculo_vtr_08.png")
            self.oHelper.SetButton('Sim')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        self.oHelper.Screenshot("Calculo_vtr_10.png")
        sleep(70)
        self.oHelper.Screenshot("Calculo_vtr_11.png")
        sleep(70) 
        self.oHelper.SetButton('x')
        sleep(2)
        
        #---------------------
        # CONSULTAR CALCULO 
        #---------------------
        
        self.oHelper.SetButton('Alterar')   
        sleep(5) 
        self.oHelper.WaitShow("Lançamentos por Funcionário")        
        self.oHelper.Screenshot("Calculo_vtr_12.png")
        sleep(5) 
        self.oHelper.SetKey("F7")
        sleep(1)
        self.oHelper.ScrollGrid(column="Codigo Verba", match_value= self.Verba,          grid_number=1)
        self.oHelper.Screenshot("Calculo_vtr_13.png")
        self.oHelper.LoadGrid()
        sleep(1)
        self.oHelper.SetButton('Confirmar') 
        sleep(0.5) 
        self.oHelper.SetButton("Salvar")
        sleep(2)
        self.oHelper.WaitShow("Lançamentos por Período")
        self.oHelper.AssertTrue()
       
     
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_lancamento_vale_transporte_e_calculo_folha")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
        
            

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA133('test_lancamento_vale_transporte_e_claculo_folha'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
