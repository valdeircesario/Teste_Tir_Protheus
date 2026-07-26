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
#---------------------------------------------------------------


class GPEA133(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
                                                                        
        cls.filial = '01'
        cls.Matricula = 'XXXXX'
        cls.Nome = 'TAIS SILVEIRA GOMES'
        cls.Verba = '620'        
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '07')
                
        
        cls.oHelper.SetLateralMenu("Atualizações > Beneficios > Vt / Vr / Va > Atualização")    
        cls.oHelper.SetButton('Confirmar') 

        

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
        self.oHelper.Screenshot("Incluindo_VTR_02")        
        self.oHelper.SetButton('Manutenção')
        sleep(2)
        
        print('-----------------------Incluir')
        self.oHelper.WaitShow("Ao Deletar um registro a rotina verifica se existem dados vinculados àquele Benefício")
        self.oHelper.Screenshot("Incluindo_VTR_03")
        self.oHelper.SetButton('OK')
        self.oHelper.WaitShow('Funcionários - MANUTENÇÃO')
        self.oHelper.SetKey("ENTER",wait_change=False)
        self.oHelper.SetKey("ENTER",wait_change=False)
        
        self.oHelper.Screenshot("Incluindo_VTR_04")
        
        self.oHelper.SetButton('Confirmar')
        
        self.oHelper.IfExists("Registro alterado com sucesso")
        self.oHelper.Screenshot("Incluindo_VTR_05")
        self.oHelper.SetButton('Fechar')     
        self.oHelper.WaitShow('Atualização Vales')
        

        print('--------------------Visualizar')
        self.oHelper.SetButton("Visualizar")        
        self.oHelper.WaitShow('Funcionários - VISUALIZAR')
        self.oHelper.Screenshot("Incluindo_VTR_06")
        self.oHelper.SetButton('Fechar')    
        self.oHelper.WaitShow("Atualização Vales")
        
        
        #------------------------
        # CALCULAR ROTEIRO VTR
        #-----------------------
        print('------------------Calcular Folha')
        self.oHelper.SetLateralMenu("Atualizações > Lançamentos > Por Funcionário ") 
        self.oHelper.WaitShow("Lançamentos por Período")
        self.oHelper.Screenshot("Calculo_vtr_01.png") 
        
        #------------------------------------
        # PESQUISAR O FUNCIONARIO PARA O CALCULO
        #------------------------------------ 
        
        
        self.oHelper.SearchBrowse(self.filial + self.Matricula + self.Nome, key="Filial+matricula+Nome")
        self.oHelper.Screenshot("Calculo_vtr_06.png")
        self.oHelper.ScrollGrid(column="Matricula", match_value = self.Matricula)
        self.oHelper.Screenshot("Calculo_vtr_07.png")
        
        #-----------------------
        # CALCULAR FOLHA CTRL+F9
        #-----------------------

        sc = SeleniumCommands(self.oHelper._Webapp__webapp.driver)
        sc.send_key('body',Keys.CONTROL+Keys.F9)
        
   
        self.oHelper.WaitShow("Deseja processar o contracheques do funcionario(a):")
        self.oHelper.Screenshot("Calculo_vtr_08.png")
        self.oHelper.SetButton('Sim')

        self.oHelper.WaitProcessing('Calculando')      
        self.oHelper.Screenshot("Calculo_vtr_10.png")
        self.oHelper.SetButton('x')
        
        #---------------------
        # CONSULTAR CALCULO 
        #---------------------
        print('------------------------------Conferir Calculo')
        self.oHelper.SetButton('Alterar')   
        self.oHelper.WaitShow("Lançamentos por Funcionário")        
        self.oHelper.Screenshot("Calculo_vtr_12.png")
        self.oHelper.SetKey("F7",wait_change=False)
        self.oHelper.ScrollGrid(column="Codigo Verba", match_value= self.Verba)
        self.oHelper.Screenshot("Calculo_vtr_13.png")
        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Confirmar') 
        self.oHelper.SetButton("Salvar")
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
