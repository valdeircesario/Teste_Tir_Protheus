from pytest import mark
import unittest
from time import sleep
from os import getcwd
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')



#----------------------------------------------------------------
# LANÇAMENTO AVULSO PARA FUNCIONARIO, CALCULAR / LANÇAR /CALCULAR
#----------------------------------------------------------------

class GPEA580_CTRL_F9(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        from tir.technologies.core.base import By
        from tir import Webapp
                                                                        
        self.filial = '02DF0001'
        self.Matricula = '228419'
        self.Nome = 'MURILO AUGUSTO DA SILVA'
        self.dataref = (datetime.today()-timedelta(days=15)).strftime("%d/%m/%Y")
        
        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', self.dataref, '02', self.filial, '07')
        
        self.oHelper.SetLateralMenu("Atualizações > Lançamentos > Por Funcionário ")
        

    def test_Calculo_folha_CTRL_F9(self):

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
        self.oHelper.Screenshot("ctrlF9_01.png")  
        self.oHelper.SearchBrowse(self.filial + self.Matricula, key="Filial+matricula+Nome")
        sleep(0.5)
        self.oHelper.Screenshot("ctrlF9_06.png")
        sleep(1)
         
        #------------------
        # CALCULAR FOLHA CTRL+F9
        #------------------
        # ERRO AO PASSARR O CTRL F9 O BROWSER NAO ESTA RECONHECENDO O COMANDO
        self.oHelper.SetKey(key="CTRL", additional_key="F9")
        
        if self.oHelper.IfExists("Deseja processar o contracheques do funcionario(a):"):
            self.oHelper.Screenshot("ctrlF9_08.png")
            self.oHelper.SetButton('Sim')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        self.oHelper.Screenshot("ctrlF9_10.png.png")
        
        self.oHelper.SetButton("Sim")  
        
        sleep(30)
        self.oHelper.Screenshot("ctrlF9_11.png.png")
        sleep(20) 
        self.oHelper.SetButton("OK")
        
        #---------------------
        # CONSULTAR CALCULO 
        #---------------------
        
        self.oHelper.SetButton('Alterar')   
        sleep(5)
        
        self.oHelper.WaitShow("Lançamentos por Funcionário")  
            
        self.oHelper.Screenshot("ctrlF9_12.png")
        sleep(5)
        
        self.oHelper.SetKey("F7")
        sleep(1)
        self.oHelper.ScrollGrid(column="Codigo Verba", match_value= "120",          grid_number=1)
        self.oHelper.Screenshot("ctrlF9_13.png")
        self.oHelper.LoadGrid()
        sleep(1)
        self.oHelper.SetButton('Confirmar') 
        sleep(0.5)
        
        self.oHelper.SetButton("Salvar")
        sleep(2)
        
        self.oHelper.AssertTrue()
       
     
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_Calculo_folha_CTRL_F9")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
        
            

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA580_CTRL_F9('test_Calculo_folha_CTRL_F9'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
