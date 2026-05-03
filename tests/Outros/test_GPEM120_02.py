            
from tir import Webapp
from pytest import mark
import unittest
from os import getcwd
from datetime import datetime, timedelta
from time import sleep
from selenium.webdriver.common.by import By

DateSystem = datetime.today().strftime('%d/%m/%Y')


# OBSEVAÇÃO:  ANTES DE RODAR O TESTE, DEVE FAZER A INTERGRAÇÃO DOS ROTEIROS . Miscelanea > Cálculos > Integrações


#  .\venv\Scripts\python.exe -m pytest .\TESTS\Outros\test_GPEM120_02.py -s

class GPEM120_FHE(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.filial = '01DF0001'
        self.periodofercham = '202603'# PERIODO QUE DESEJA FECHAMENTO
        
        #------------------------------------------------------------
        # AJUSTAR SEMPRE ESSA DATA PARA O MES SEGUINTE DO FECHAMENTO. AQUI FAZ O LANÇAMENTO DOS ROTEIROS DO MES SEGUINTE
        self.periodo = '202604'# PERIODO SEGUINTE DO FECHAMENTO
        self.datapag = '30042026'# ALTERAR DATA DE PAGAMENTO SEMPRE PARA O ULTIMO DIA DO MES
        
        self.dataref = (datetime.today()-timedelta(days=30)).strftime("%d/%m/%Y")# AJUSTAR DATA PARA PERIODO EM ABERTO 
    
        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', self.dataref, '01', self.filial, '07')
        self.oHelper.SetLateralMenu("Atualizações > Definições Cálculo > Períodos")
        #self.oHelper.SetLateralMenu("Miscelanea > Fechamentos > Período")
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
        self.oHelper.Screenshot("fechamento_periodo_01")       
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
        self.oHelper.Screenshot("fechamento_periodo_02")
        self.oHelper.SetButton("Alterar") 
        self.oHelper.WaitShow('Cadastro de Períodos - ALTERAR')
        self.oHelper.Screenshot("fechamento_periodo_03")
        
        self.oHelper.SetKey("DOWN",                                       grid=True)
        self.oHelper.SetValue("Roteiro Calc","FOL", grid=True, grid_number=1)
        self.oHelper.SetValue("Data Pagto", self.datapag, grid=True, grid_number=1)
        self.oHelper.LoadGrid()  
        self.oHelper.SetKey("DOWN",                                       grid=True)   
        self.oHelper.SetValue("Roteiro Calc","RES", grid=True, grid_number=1)                   
        self.oHelper.SetValue("Data Pagto", self.datapag, grid=True, grid_number=1)
        self.oHelper.LoadGrid() 
        self.oHelper.SetKey("DOWN",                                       grid=True)
        self.oHelper.SetValue("Roteiro Calc","PLA", grid=True, grid_number=1)                   
        self.oHelper.SetValue("Data Pagto", self.datapag, grid=True, grid_number=1)
        self.oHelper.LoadGrid() 
        self.oHelper.SetKey("DOWN",                                       grid=True)
        
        self.oHelper.Screenshot("fechamento_periodo_04")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton('x')
        
        print("✅ LANÇAMENTOS DOS ROTEIROS DO MES SEGUINTE, FINALIZADO COM SUCESSO")
        print("------------------------------------------------")
        
        #--------------------------------------
        # FECHAMENTO DO PERIODO DESEJADO
        #-------------------------------------- 
        
        sleep(5)
        print("🎯 FECHEAMENTO DO PERIODO DESEJADO, 00004")
        print("------------------------------------------------")
        #self.oHelper.SetLateralMenu("Miscelanea > Fechamentos > Período")
        self.oHelper.Program("GPEM120")
        self.oHelper.SetButton("Confirmar")
        sleep(5)
        
        if self.oHelper.IfExists("Deseja desativar o grid?"):
            self.oHelper.SetButton('Não')
        sleep(5)    
        #----------------------------------------
        # FECHAMENTO DOS AUTONOMOS PROCESSO 00004, PRIMEIRO
        #---------------------------------------- 
        
        self.oHelper.Screenshot("fechamento_periodo_05")
        self.oHelper.SetValue('Processo','00004',check_value=False)
        self.oHelper.SetValue('Cod. Periodo',self.periodofercham,check_value=False)
        self.oHelper.SetValue('Roteiro Calc','AUT',check_value=False)        
        self.oHelper.ClickBox("Roteiro", "AUT",grid_number=1) 
        self.oHelper.Screenshot("fechamento_periodo_06")
        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.Screenshot("fechamento_periodo_07")
        
        if self.oHelper.IfExists("Log de Ocorrencias no Fechamento de Periodo"):
            self.oHelper.ClickLabel("Em Disco")
            self.oHelper.Screenshot("fechamento_periodo_08")
            self.oHelper.SetButton("OK")
            self.oHelper.WaitProcessing("Processando")
            self.oHelper.Screenshot("fechamento_periodo_09")
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
        self.oHelper.Screenshot("fechamento_periodo_10")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.Screenshot("fechamento_periodo_11")
        
        if self.oHelper.IfExists("Log de Ocorrencias no Fechamento de Periodo"):
            self.oHelper.ClickLabel("Em Disco")
            self.oHelper.Screenshot("fechamento_periodo_12")
            self.oHelper.SetButton("OK")
            self.oHelper.WaitProcessing("Processando")
            self.oHelper.Screenshot("fechamento_periodo_13")   
            self.oHelper.SetButton("Sair")  
            
            
        print("✅ FECHAMENTO DO PROCESSO 00003 FINALIZADO COM SUCESSO")
        print("------------------------------------------------")
        
        
        #----------------------------------------
        # FECHAMENTO DO PROCESSO 00001, TERCEIRO
        #---------------------------------------- 
        
        print("🎯 FECHEAMENTO DO PERIODO DESEJADO, 00001")
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
        self.oHelper.ClickBox("Roteiro", "FER",grid_number=1)
        self.oHelper.ClickBox("Roteiro", "RES",grid_number=1)
        self.oHelper.ClickBox("Roteiro", "PLA",grid_number=1)
        self.oHelper.Screenshot("fechamento_periodo_14")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.Screenshot("fechamento_periodo_15") 
        sleep(10)
        
        if self.oHelper.IfExists("Log de Ocorrencias no Fechamento de Periodo"):
            self.oHelper.ClickLabel("Em Disco")
            self.oHelper.Screenshot("fechamento_periodo_16")
            self.oHelper.SetButton("OK")
            self.oHelper.WaitProcessing("Processando")
            self.oHelper.Screenshot("fechamento_periodo_17")
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
        self.oHelper.Screenshot("fechamento_periodo_18")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.Screenshot("fechamento_periodo_19") 
        sleep(15)
        
        if self.oHelper.IfExists("Log de Ocorrencias no Fechamento de Periodo"):
            self.oHelper.ClickLabel("Em Disco")
            self.oHelper.Screenshot("fechamento_periodo_20")
            self.oHelper.SetButton("OK")
            self.oHelper.WaitProcessing("Processando")
            self.oHelper.Screenshot("fechamento_periodo_21")
            self.oHelper.SetButton("Sair")  
                 
        print("✅ FECHAMENTO DO PROCESSO 00001 FOLHA FINALIZADO COM SUCESSO")     
        self.oHelper.AssertTrue()
       
        print("------------------------------------------------")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_fechamento_periodo")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
          

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEM120_FHE('test_fechamento_periodo_FHE'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
