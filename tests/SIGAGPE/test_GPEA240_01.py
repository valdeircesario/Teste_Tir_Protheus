from tir.technologies.core.base import By
from tir import Webapp
from pytest import mark
import unittest
from time import sleep
from os import getcwd
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')


#------------------------
# LANÇAMENTO DE AUSENCIAS MATERNIDADE 120 DIAS
#------------------------

class GPEA240_01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.filial = '01'
        cls.Matricula = '00124'
        cls.CodigoAusen ='007'
        cls.dataref = (datetime.today()-timedelta(days=0)).strftime("%d/%m/%Y")
        cls.dataIncio = (datetime.today()-timedelta(days=0)).strftime("%d/%m/%Y")
        cls.dataFim = (datetime.today()+timedelta(days=119)).strftime("%d/%m/%Y")
        

        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', cls.dataref, '02', cls.filial, '07')
        
        cls.oHelper.SetLateralMenu("Atualizações > Lançamentos > Ausências")
        cls.oHelper.SetButton('Confirmar')
        
       
    def test_Cadastro_de_ausencia_maternidade_120_dias(self):

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
            self.oHelper.Screenshot("GPEA240_01_1")
            self.oHelper.SetButton('OK')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        sleep(1)
        self.oHelper.WaitShow("Cadastro de Ausencias")
        self.oHelper.Screenshot("ausencia_01_1")  
        self.oHelper.SearchBrowse(self.filial + self.Matricula , key="Filial+Matricula+Nome")
        self.oHelper.Screenshot("ausencia_01_2")
        
        #-------------------
        # INCLUIR AUSENCIA
        #-------------------
        
        print('--------------------------Incluir')
        self.oHelper.SetButton('Manutenção')
        self.oHelper.WaitShow("Cadastro de Ausencias - MANUTENÇÃO")
        self.oHelper.Screenshot("ausencia_01_3") 
         
        self.oHelper.ScrollGrid(column="Sequência", match_value= "018",                 grid_number=1)
        self.oHelper.SetKey("DOWN",                                                     grid=True)
        self.oHelper.SetValue('Cód. Ausenc',  self.CodigoAusen,                         grid= True, check_value=False)
        self.oHelper.SetValue('Data Afast',  self.dataref,                              grid= True, check_value=False)
        self.oHelper.SetValue('Fim Afast',  self.dataFim,                               grid= True, check_value=False)
        self.oHelper.SetValue('Inf. Compl.', "TESTE AUT LICENÇA MATERNIDADE 120 DIAS",  grid= True, check_value=False)
        self.oHelper.LoadGrid()
        self.oHelper.Screenshot("ausencia_01_4")
        self.oHelper.SetButton("Confirmar")
        sleep(1)

        print('--------------------------Confirmação')
        if self.oHelper.IfExists("Atenção"):
            self.oHelper.WaitShow('Sequência 002: Atenção, o prazo do envio deste evento é : 25/01/2020')
            self.oHelper.Screenshot("ausencia_01_5")
            self.oHelper.SetButton('OK')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
            
        self.oHelper.WaitShow('Registro enviado para o TAF com sucesso!')
        self.oHelper.Screenshot("ausencia_01_6")
        self.oHelper.SetButton('OK')     
        self.oHelper.IfExists("Registro alterado com sucesso.")
        self.oHelper.Screenshot("ausencia_01_8")
        self.oHelper.SetButton('Fechar')     
        self.oHelper.WaitShow("Cadastro de Ausencias")

        #-------------------
        # VISUALIZAR AUSENCIA
        #-------------------
    
        print('--------------------------Visualizar')
        self.oHelper.SetButton("Visualizar")
        self.oHelper.WaitShow("Cadastro de Ausencias - VISUALIZAR")
        self.oHelper.ScrollGrid(column="Fim Afast", match_value= self.dataFim,          grid_number=1)
        self.oHelper.Screenshot("ausencia_01_9") 
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Cadastro de Ausencias")
        
        #------------------------
        # EXCLUIR AUSENCIA
        #------------------------
        print('--------------------------Excluir')
        self.oHelper.SetButton("Manutenção")
        self.oHelper.ScrollGrid(column="Fim Afast", match_value= self.dataFim,          grid_number=1)
        self.oHelper.SetKey("DELETE", grid=True, grid_number=1)
        self.oHelper.Screenshot("ausencia_01_10")
        self.oHelper.SetButton("Confirmar")
        print('--------------------------Confirmação')
        sleep(1)
        
        if self.oHelper.IfExists("Atenção"):
            self.oHelper.Screenshot("ausencia_01_11")
            self.oHelper.SetButton('OK')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        sleep(1)
            
        self.oHelper.IfExists("Atenção!")
        self.oHelper.WaitShow('Registro enviado para o TAF com sucesso!')
        self.oHelper.Screenshot("ausencia_01_12")
        self.oHelper.SetButton('OK')
               
        self.oHelper.IfExists("Registro alterado com sucesso.")
        self.oHelper.Screenshot("ausencia_01_14")
        self.oHelper.SetButton('Fechar')
            
        self.oHelper.WaitShow("Cadastro de Ausencias")
        self.oHelper.Screenshot("ausencia_01_15")
          

        self.oHelper.AssertTrue()
        
        print("/")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_Cadastro_de_ausencia_maternidade_120_dias")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA240_01('test_Cadastro_de_ausencia_maternidade_120_dias'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
