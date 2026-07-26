from tir.technologies.core.base import By
from tir import Webapp
from pytest import mark
import unittest
from time import sleep
from os import getcwd
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')


#------------------------
# LANÇAMENTO DE AUSENCIAS LUTO
#------------------------

class GPEA240_02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.filial = '01'
        cls.Matricula = '00132'
        cls.CodigoAusen ='025'
        cls.dataref = (datetime.today()-timedelta(days=0)).strftime("%d/%m/%Y")
        cls.dataIncio = (datetime.today()-timedelta(days=0)).strftime("%d/%m/%Y")
        cls.dataFim = (datetime.today()+timedelta(days=1)).strftime("%d/%m/%Y")
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', cls.dataref, '99', cls.filial, '07')
        
        cls.oHelper.SetLateralMenu("Atualizações > Lançamentos > Ausências")
        cls.oHelper.SetButton('Confirmar')
        
       
    def test_Cadastro_de_ausencia_LUTO(self):

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
            
        if self.oHelper.IfExists("Cadastro de Ausencias"):
            self.oHelper.Screenshot("GPEA240_02")
            self.oHelper.SetButton('OK')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        sleep(1)
        print('--------------------------Pesquisar funcionario')
        self.oHelper.WaitShow("Cadastro de Ausencias")
        self.oHelper.Screenshot("ausencia_02_01")  
        self.oHelper.SearchBrowse(self.filial + self.Matricula , key="Filial+Matricula+Nome")
        self.oHelper.Screenshot("ausencia_02_02")
        
        #-------------------
        # INCLUIR AUSENCIA
        #-------------------
        print('--------------------------Incluir')
        self.oHelper.SetButton('Manutenção')
        self.oHelper.WaitShow("Cadastro de Ausencias - MANUTENÇÃO")
        self.oHelper.Screenshot("ausencia_02_03") 
         
        self.oHelper.ScrollGrid(column="Sequência", match_value= "018",                 grid_number=1)
        self.oHelper.SetKey("DOWN",                                                     grid=True,  wait_change=False)
        self.oHelper.SetValue('Cód. Ausenc',  self.CodigoAusen,                         grid= True, check_value=False)
        self.oHelper.SetValue('Data Afast',  self.dataref,                              grid= True, check_value=False)
        self.oHelper.SetValue('Fim Afast',  self.dataFim,                               grid= True, check_value=False)
        self.oHelper.SetValue('Inf. Compl.', "TESTE  AUSENCIA LUTO",  grid= True, check_value=False)
        self.oHelper.LoadGrid()
        self.oHelper.Screenshot("ausencia_02_04")
        self.oHelper.SetButton("Confirmar")
        print('--------------------------Confirmação')
        sleep(1)
        
        if self.oHelper.IfExists("Atenção"):
            self.oHelper.WaitShow('Sequência 002: Atenção, o prazo do envio deste evento é : 25/01/2020')
            self.oHelper.Screenshot("ausencia_02_05")
            self.oHelper.SetButton('OK')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
    
        self.oHelper.IfExists("Registro alterado com sucesso.")
        self.oHelper.Screenshot("ausencia_02_06")
        self.oHelper.SetButton('Fechar')      
        self.oHelper.WaitShow("Cadastro de Ausencias")

        #-------------------
        # VISUALIZAR AUSENCIA
        #-------------------
        print('--------------------------Visualizar')
        self.oHelper.SetButton("Visualizar")
        self.oHelper.WaitShow("Cadastro de Ausencias - VISUALIZAR")
        self.oHelper.ScrollGrid(column="Fim Afast", match_value= self.dataFim,          grid_number=1)
        self.oHelper.Screenshot("ausencia_02_07") 
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Cadastro de Ausencias")
        
        #------------------------
        # EXCLUIR AUSENCIA
        #------------------------
        print('--------------------------Excluir')
        self.oHelper.SetButton("Manutenção")
        self.oHelper.ScrollGrid(column="Fim Afast", match_value= self.dataFim,          grid_number=1)
        self.oHelper.SetKey("DELETE", grid=True, wait_change=False)
        self.oHelper.Screenshot("ausencia_02_08")
        self.oHelper.SetButton("Confirmar")
        print('--------------------------Confirmação')
        sleep(1)
        
        if self.oHelper.IfExists("Atenção"):
            self.oHelper.Screenshot("ausencia_02_09")
            self.oHelper.SetButton('OK')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
            
        self.oHelper.IfExists("Registro alterado com sucesso.")
        self.oHelper.Screenshot("ausencia_02_10")
        self.oHelper.SetButton('Fechar')    
        self.oHelper.WaitShow("Cadastro de Ausencias")
        self.oHelper.Screenshot("ausencia_02_11")
          

        self.oHelper.AssertTrue()
        
        print("/")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_Cadastro_de_ausencia_LUTO")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA240_02('test_Cadastro_de_ausencia_LUTO'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
