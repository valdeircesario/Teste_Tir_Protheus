            
from tir import Webapp
from pytest import mark
import unittest
from os import getcwd
from datetime import datetime, timedelta
from time import sleep
from selenium.webdriver.common.by import By

DateSystem = datetime.today().strftime('%d/%m/%Y')


# OBSEVAÇÃO:  ANTES DE RODAR O TESTE, DEVE FAZER A INTERGRAÇÃO DOS ROTEIROS . Miscelanea > Cálculos > Integrações


#  .\venv\Scripts\python.exe -m pytest .\TESTS\Outros\test_fechamento_periodo_FHE.py -s

class FECHAMENTO_PERIODO_FHE(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.filial = '01DF0001'
        self.periodofercham = '202601'# PERIODO QUE DESEJA FECHAMENTO
        
        #------------------------------------------------------------
        # AJUSTAR SEMPRE ESSA DATA PARA O MES SEGUINTE DO FECHAMENTO. AQUI FAZ O LANÇAMENTO DOS ROTEIROS DO MES SEGUINTE
        self.periodo = '202602'# PERIODO SEGUINTE DO FECHAMENTO
        self.datapag = '28022026'# ALTERAR DATA DE PAGAMENTO SEMPRE PARA O ULTIMO DIA DO MES
        
        self.dataref = (datetime.today()-timedelta(days=30)).strftime("%d/%m/%Y")# AJUSTAR DATA PARA PERIODO EM ABERTO 
    
        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', self.dataref, '01', self.filial, '07')
        #self.oHelper.SetLateralMenu("Atualizações > Definições Cálculo > Períodos")
        self.oHelper.SetLateralMenu("Miscelanea > Fechamentos > Período")
        self.oHelper.SetButton('Confirmar')
        

    def test_fechamento_periodo_FHE(self):

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
            
        #--------------------------------------
        # CADASTRO DOS ROTEIRO PARA O MES POSTERIOR
        #--------------------------------------  
        self.oHelper.Screenshot("Fechammento_periodo_FHE_01")       
        self.oHelper.InputByLocator(selector='COMP4586', locator=By.ID, value='Filtar')   
        self.oHelper.SetButton("Criar Filtro")
        self.oHelper.SetValue("Campo","Cód. Período",check_value=False)
        self.oHelper.SetValue("Expressão",self.periodo,check_value=False)
        self.oHelper.SetButton("Adicionar")
        self.oHelper.SetButton("Salvar")
        filtro_texto = f"Cód. Período Igual a '{self.periodo}'"  
        self.oHelper.ClickCheckBox(filtro_texto,1)
        self.oHelper.SetButton("Aplicar filtros selecionados")
        sleep(2)
        self.oHelper.Screenshot("Fechammento_periodo_FHE_02")
        self.oHelper.SetButton("Alterar") 
        self.oHelper.WaitShow('Cadastro de Períodos - ALTERAR')
        self.oHelper.Screenshot("Fechammento_periodo_FHE_03")
        
        self.oHelper.SetKey("DOWN",                                       grid=True)
        self.oHelper.SetValue("Roteiro Calc","FOL", grid=True, grid_number=1)
        self.oHelper.SetValue("Data Pagto", self.datapag, grid=True, grid_number=1)
        self.oHelper.LoadGrid()  
        self.oHelper.SetKey("DOWN",                                       grid=True)   
        self.oHelper.SetValue("Roteiro Calc","RES", grid=True, grid_number=1)                   
        self.oHelper.SetValue("Data Pagto", self.datapag, grid=True, grid_number=1)
        self.oHelper.LoadGrid() 
        self.oHelper.SetKey("DOWN",                                       grid=True)
        
        self.oHelper.Screenshot("Fechammento_periodo_FHE_04")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton('x')
        
        print("✅ LANÇAMENTOS DOS ROTEIROS DO MES SEGUINTE, FINALIZADO COM SUCESSO")
        print("------------------------------------------------")
        
        #--------------------------------------
        # FECHAMENTO DO PERIODO DESEJADO
        #-------------------------------------- 
        
        sleep(5)
        #self.oHelper.SetLateralMenu("Miscelanea > Fechamentos > Período")
        print("🎯 FECHEAMENTO DO PERIODO DESEJADO, 00004")
        print("------------------------------------------------")
        self.oHelper.Program("GPEM120")
        self.oHelper.SetButton("Confirmar")
        sleep(5)
        
        if self.oHelper.IfExists("Deseja desativar o grid?"):
            self.oHelper.SetButton('Não')
        sleep(5)    
        #----------------------------------------
        # FECHAMENTO DOS AUTONOMOS PROCESSO 00004, PRIMEIRO
        #---------------------------------------- 
        
        self.oHelper.Screenshot("Fechammento_periodo_FHE_05")
        self.oHelper.SetValue('Processo','00004',check_value=False)
        self.oHelper.SetValue('Cod. Periodo',self.periodofercham,check_value=False)
        self.oHelper.SetValue('Roteiro Calc','AUT',check_value=False)        
        self.oHelper.ClickBox("Roteiro", "AUT",grid_number=1) 
        self.oHelper.Screenshot("Fechammento_periodo_FHE_06")
        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.Screenshot("Fechammento_periodo_FHE_07")
        
        if self.oHelper.IfExists("Log de Ocorrencias no Fechamento de Periodo"):
            self.oHelper.ClickLabel("Em Disco")
            self.oHelper.Screenshot("Fechammento_periodo_FHE_08")
            self.oHelper.SetButton("OK")
            self.oHelper.WaitProcessing("Processando")
            self.oHelper.Screenshot("Fechammento_periodo_FHE_09")
            self.oHelper.SetButton("Sair")  
            
            
        print("✅ FECHAMENTO DO PROCESSO 00004 FINALIZADO COM SUCESSO")
        print("------------------------------------------------") 
        
      
        #----------------------------------------
        # FECHAMENTO DOS AUTONOMOS PROCESSO 00003, SEGUNDO
        #----------------------------------------
        
        
        print("🎯 FECHEAMENTO DO PERIODO DESEJADO, 00003")
        print("------------------------------------------------")
        #self.oHelper.SetLateralMenu("Miscelanea > Fechamentos > Período")
        self.oHelper.Program("GPEM120")
        self.oHelper.SetButton("Confirmar")
        sleep(5)
        
        if self.oHelper.IfExists("Deseja desativar o grid?"):
            self.oHelper.SetButton('Não')
        sleep(5)
        self.oHelper.SetValue('Processo','00003',check_value=False)
        self.oHelper.SetValue('Cod. Periodo',self.periodofercham,check_value=False)
        self.oHelper.SetValue('Roteiro Calc','AUT',check_value=False)        
        self.oHelper.ClickBox("Roteiro", "AUT",grid_number=1)
        self.oHelper.Screenshot("Fechammento_periodo_FHE_10")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.Screenshot("Fechammento_periodo_FHE_11")
        
        if self.oHelper.IfExists("Log de Ocorrencias no Fechamento de Periodo"):
            self.oHelper.ClickLabel("Em Disco")
            self.oHelper.Screenshot("Fechammento_periodo_FHE_12")
            self.oHelper.SetButton("OK")
            self.oHelper.WaitProcessing("Processando")
            self.oHelper.Screenshot("Fechammento_periodo_FHE_13")   
            self.oHelper.SetButton("Sair")  
            
            
        print("✅ FECHAMENTO DO PROCESSO 00003 FINALIZADO COM SUCESSO")
        print("------------------------------------------------")
        
        
        #----------------------------------------
        # FECHAMENTO DO PROCESSO 00001, TERCEIRO
        #---------------------------------------- 
        
        #self.oHelper.SetLateralMenu("Miscelanea > Fechamentos > Período")
        print("🎯 FECHEAMENTO DO PERIODO DESEJADO, 00001")
        print("------------------------------------------------")
        self.oHelper.Program("GPEM120")
        self.oHelper.SetButton("Confirmar")
        sleep(5)
        if self.oHelper.IfExists("Deseja desativar o grid?"):
            self.oHelper.SetButton('Não')
        sleep(5)
        self.oHelper.SetValue('Processo','00001',check_value=False)
        self.oHelper.SetValue('Cod. Periodo',self.periodofercham,check_value=False)
        self.oHelper.ClickBox("Roteiro", "FER",grid_number=1)
        self.oHelper.ClickBox("Roteiro", "RES",grid_number=1)
        self.oHelper.Screenshot("Fechammento_periodo_FHE_14")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.Screenshot("Fechammento_periodo_FHE_15") 
        sleep(10)
        
        if self.oHelper.IfExists("Log de Ocorrencias no Fechamento de Periodo"):
            self.oHelper.ClickLabel("Em Disco")
            self.oHelper.Screenshot("Fechammento_periodo_FHE_16")
            self.oHelper.SetButton("OK")
            self.oHelper.WaitProcessing("Processando")
            self.oHelper.Screenshot("Fechammento_periodo_FHE_17")
            self.oHelper.SetButton("Sair")  
                 
        print("✅ FECHAMENTO DO PROCESSO 00001 FINALIZADO COM SUCESSO")
        print("------------------------------------------------")
        
        #----------------------------------------
        # FECHAMENTO DO PROCESSO 00001, FOLHA E SEMPRE O ULTIMO
        #---------------------------------------- 
        
        print("🎯 FECHAMENTO DO PROCESSO 00001, (FOL) SEMPRE ESSE PROCESSO SER O ULTIMO FECHAMENTO ") 
        print("------------------------------------------------")
        #self.oHelper.SetLateralMenu("Miscelanea > Fechamentos > Período")
        self.oHelper.Program("GPEM120")
        self.oHelper.SetButton("Confirmar")
        sleep(5)
        if self.oHelper.IfExists("Deseja desativar o grid?"):
            self.oHelper.SetButton('Não')
        sleep(5)
        self.oHelper.SetValue('Processo','00001',check_value=False)
        self.oHelper.SetValue('Cod. Periodo',self.periodofercham,check_value=False)
        self.oHelper.ClickBox("Roteiro", "FOL",grid_number=1)
        self.oHelper.Screenshot("Fechammento_periodo_FHE_18")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.Screenshot("Fechammento_periodo_FHE_19") 
        sleep(15)
        
        if self.oHelper.IfExists("Log de Ocorrencias no Fechamento de Periodo"):
            self.oHelper.ClickLabel("Em Disco")
            self.oHelper.Screenshot("Fechammento_periodo_FHE_20")
            self.oHelper.SetButton("OK")
            self.oHelper.WaitProcessing("Processando")
            self.oHelper.Screenshot("Fechammento_periodo_FHE_21")
            self.oHelper.SetButton("Sair")  
                 
        print("✅ FECHAMENTO DO PROCESSO 00001 FOLHA FINALIZADO COM SUCESSO")     
        self.oHelper.AssertTrue()
       
        print("------------------------------------------------")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_fechamento_periodo_FHE")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
          

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(FECHAMENTO_PERIODO_FHE('test_fechamento_periodo_FHE'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
