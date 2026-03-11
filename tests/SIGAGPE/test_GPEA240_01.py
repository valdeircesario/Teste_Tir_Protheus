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
    def setUpClass(self):
        self.filial = '02DF0001'
        self.Matricula = '227950'
        self.Nome = 'ANALINE SOUSA PAULINO E SILVA' 
        self.CodigoAusen ='007'
        self.dataref = (datetime.today()-timedelta(days=0)).strftime("%d/%m/%Y")
        self.dataIncio = (datetime.today()-timedelta(days=0)).strftime("%d/%m/%Y")
        self.dataFim = (datetime.today()+timedelta(days=119)).strftime("%d/%m/%Y")
        

        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', self.dataref, '02', self.filial, '07')
        
        self.oHelper.SetLateralMenu("Atualizações > Lançamentos > Ausências")
        
       
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
        self.oHelper.Screenshot("GPEA240_01_1")  
        self.oHelper.SearchBrowse(self.filial + self.Matricula + self.Nome, key="Filial+Matricula+Nome")
        sleep(1)
        self.oHelper.Screenshot("GPEA240_01_2")
        
        #-------------------
        # INCLUIR AUSENCIA
        #-------------------
        
        self.oHelper.SetButton('Manutenção')
        sleep(2)
        self.oHelper.WaitShow("Cadastro de Ausencias - MANUTENÇÃO")
        self.oHelper.Screenshot("GPEA240_01_3") 
         
        self.oHelper.ScrollGrid(column="Sequência", match_value= "018",                 grid_number=1)
        self.oHelper.SetKey("DOWN",                                                     grid=True)
        self.oHelper.SetValue('Cód. Ausenc',  self.CodigoAusen,                         grid= True, check_value=False)
        self.oHelper.SetValue('Data Afast',  self.dataref,                              grid= True, check_value=False)
        self.oHelper.SetValue('Fim Afast',  self.dataFim,                               grid= True, check_value=False)
        self.oHelper.SetValue('Inf. Compl.', "TESTE AUT LICENÇA MATERNIDADE 120 DIAS",  grid= True, check_value=False)
        self.oHelper.LoadGrid()
        self.oHelper.Screenshot("GPEA240_01_4")
        self.oHelper.SetButton("Confirmar")
        sleep(1)
        
        if self.oHelper.IfExists("Atenção"):
            self.oHelper.WaitShow('Sequência 002: Atenção, o prazo do envio deste evento é : 25/01/2020')
            self.oHelper.Screenshot("GPEA240_01_5")
            self.oHelper.SetButton('OK')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        sleep(1)
            
        if self.oHelper.IfExists("Atenção!"):
            self.oHelper.WaitShow('Registro enviado para o TAF com sucesso!')
            self.oHelper.Screenshot("GPEA240_01_6")
            self.oHelper.SetButton('OK')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        if self.oHelper.IfExists("Retorno - Ifractal"):
            self.oHelper.Screenshot("GPEA240_01_7")
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        if self.oHelper.IfExists("Registro alterado com sucesso."):
            self.oHelper.Screenshot("GPEA240_01_8")
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        self.oHelper.WaitShow("Cadastro de Ausencias")
        self.oHelper.SetButton("Visualizar")
        sleep(0.5)
        #-------------------
        # VISUALIZAR AUSENCIA
        #-------------------
        
        self.oHelper.WaitShow("Cadastro de Ausencias - VISUALIZAR")
        self.oHelper.ScrollGrid(column="Fim Afast", match_value= self.dataFim,          grid_number=1)
        self.oHelper.Screenshot("GPEA240_01_9") 
        self.oHelper.SetButton("Fechar")
        sleep(0.5)
        self.oHelper.WaitShow("Cadastro de Ausencias")
        
        #------------------------
        # EXCLUIR AUSENCIA
        #------------------------
        
        self.oHelper.SetButton("Manutenção")
        sleep(1)
        self.oHelper.ScrollGrid(column="Fim Afast", match_value= self.dataFim,          grid_number=1)
        self.oHelper.SetKey("DELETE", grid=True, grid_number=1)
        self.oHelper.Screenshot("GPEA240_01_10")
        self.oHelper.SetButton("Confirmar")
        sleep(1)
        
        if self.oHelper.IfExists("Atenção"):
            self.oHelper.Screenshot("GPEA240_01_11")
            self.oHelper.SetButton('OK')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        sleep(1)
            
        if self.oHelper.IfExists("Atenção!"):
            self.oHelper.WaitShow('Registro enviado para o TAF com sucesso!')
            self.oHelper.Screenshot("GPEA240_01_12")
            self.oHelper.SetButton('OK')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        if self.oHelper.IfExists("Retorno - Ifractal"):
            self.oHelper.Screenshot("GPEA240_01_13")
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        if self.oHelper.IfExists("Registro alterado com sucesso."):
            self.oHelper.Screenshot("GPEA240_01_14")
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        self.oHelper.WaitShow("Cadastro de Ausencias")
        self.oHelper.Screenshot("GPEA240_01_15")
          

        self.oHelper.AssertTrue()
        
        print("/")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_Cadastro_de_ausencia_maternidade_120_dias")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA240_01('test_Cadastro_de_ausencia_maternidade_120_dias'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
