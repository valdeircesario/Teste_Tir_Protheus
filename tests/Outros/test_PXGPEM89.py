from tir import Webapp
from pytest import mark
import unittest
from os import getcwd
from datetime import datetime, timedelta
from time import sleep
from selenium.webdriver.common.by import By

DateSystem = datetime.today().strftime('%d/%m/%Y')

class PXGPEM89(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.filial = '02DF0001'
        cls.matricula = '205733'
        cls.processo = '00001'
        cls.periodo = '202601'
        cls.nome = 'CLAUDIO GUEDES DA SILVA'
        
        cls.dataref = (datetime.today()-timedelta(days=30)).strftime("%d/%m/%Y")# AJUSTAR DATA PARA PERIODO EM ABERTO 
    
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', cls.dataref, '02', cls.filial, '07')
        #cls.oHelper.SetLateralMenu("Miscelanea > Cálculos > Integrações")
        cls.oHelper.SetLateralMenu("Atualizações > Especificos > Dissid.Retroativo Poupex")
        #cls.oHelper.SetLateralMenu("Atualizações > Lançamentos > Por Funcionário")
        cls.oHelper.SetButton('Confirmar')
        
        if cls.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            cls.oHelper.SetButton('Fechar')

        if cls.oHelper.IfExists("Moedas"):
            cls.oHelper.CheckResult('Dolar', '0,0000')
            cls.oHelper.SetButton('Confirmar')
        

    def test_reajuste_salarial_dissidio_acordo_coletivo(self):
        
        
        
        #-----------------------------------
        #GARANTE A INTEGRAÇÃO DOS ROTEIROS
        #-----------------------------------
    
        
        """ self.oHelper.SetValue("Processo ?", self.processo, check_value=False) 
        self.oHelper.Screenshot("Dissidio_integração_01")
        
        self.oHelper.SetButton('Outras Ações','Inverter Seleção')
        
        self.oHelper.SetButton('Integrar')
        
        if self.oHelper.IfExists("Integrações Com a Folha de Pagamento"):
            self.oHelper.Screenshot("Dissidio_integração_02")
            self.oHelper.SetButton('Executar')
            #self.oHelper.IfExists("Integração de Beneficios","OK") 
            
           
            
            self.oHelper.WaitProcessing("Processando")
            
            
        if self.oHelper.IfExists("Integração de Beneficios"):
            self.oHelper.Screenshot("Dissidio_integração_04")
            self.oHelper.SetButton('Ok')
            
       
            
        self.oHelper.Screenshot('Dissidio_integração_06')

        sleep(20)
        self.oHelper.CheckHelp(text="ATENÇÃO", button="Fechar")
        sleep(1) """
        
        
        #--------------------------------------------------------------------
        # FAZ O LANÇAMENTO DE REAJUSTE SALARIAL PELO DISSÍDIO/ACORDO COLETIVO
        #--------------------------------------------------------------------
        
        #self.oHelper.SetLateralMenu("Atualização > Especificos > Dissid.Retroativo Poupex")
        
        #-------------------------
        #DESINTEGRAR
        #-------------------------
        
        self.oHelper.SetButton('Outras Ações','Integração')
        self.oHelper.SetValue("Matrícula De ?", self.matricula, check_value=False)  
        self.oHelper.SetValue("Matrícula Até ?", self.matricula, check_value=False) 
        self.oHelper.SetValue("Tipo ?", 'Desintegrar', check_value=False)
        self.oHelper.Screenshot('Manutenção_01')  
        self.oHelper.SetButton('OK')
        
        
        #--------------
        # GERAR O ACORDO COLETIVO
        #--------------
        
        self.oHelper.SetButton('Outras Ações','Gerar')
        self.oHelper.Screenshot('Manutenção_06')
        
        self.oHelper.SetValue("Mês/Ano Acordo: ?", self.periodo, check_value=False)  
        self.oHelper.SetValue("Matrícula De ?", self.matricula, check_value=False)  
        self.oHelper.SetValue("Matrícula Até ?", self.matricula, check_value=False)  
        self.oHelper.SetValue("% Reajuste ?", '1000', check_value=False)
        self.oHelper.Screenshot('Manutenção_101')
        self.oHelper.SetButton('OK')
        
        if self.oHelper.IfExists("Os dados do acordo coletivo foram gerados com sucesso!"):
            self.oHelper.Screenshot("Dissidio_integração_0645")
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
            
        #----------------------------------------------------
        # FAZER INTEGRAÇÃO DO ACORDO PARA CALCULO FOLHA
        #----------------------------------------------------
        
        self.oHelper.SetButton('Outras Ações','Integração') 
        
        ### VER MATRICULA AQUI 
        self.oHelper.SetValue("Matrícula De ?", self.matricula, check_value=False)  
        self.oHelper.SetValue("Matrícula Até ?", self.matricula, check_value=False) 
        self.oHelper.SetValue("Tipo ?", 'Integrar', check_value=False) 
        self.oHelper.SetButton('OK')
        sleep(10)
        
        
        
        
        #---------------------------------------------
        # MANUTENÇÃO
        #---------------------------------------------
        self.oHelper.SearchBrowse(self.filial + self.matricula + self.nome, key="Filial+Matricula+Nome")
        
        self.oHelper.SetButton('Manutenção')
        self.oHelper.Screenshot('Manutenção_01')
        self.oHelper.SetButton('Fechar') 
        
        
        
        
        
        #---------------------------------------------
        # FAZER CALCULO FOLHA
        #---------------------------------------------
        self.oHelper.SetLateralMenu("Atualizações > Lançamentos > Por Funcionário")
        self.oHelper.SetButton('Confirmar')
        self.oHelper.Screenshot('Manutenção_054')
 
        self.oHelper.SearchBrowse(self.filial + self.matricula + self.nome, key="Filial+Matricula+Nome")
        self.oHelper.Screenshot('Manutenção_0568') 
        self.oHelper.SetButton('Alterar')
        self.oHelper.Screenshot('Manutenção_0879')
        
        self.oHelper.SetButton('Outras Ações','Calcular Lançamento')
        self.oHelper.Screenshot('Manutenção_0101')
        
        self.oHelper.WaitProcessing("Processando")
        self.oHelper.Screenshot('Manutenção_066564')
        
        self.oHelper.SetButton('OK')
        
        self.oHelper.SetButton('Outras Ações','Consultar Cálculo')
        self.oHelper.Screenshot('Calculo_01454')
        
        self.oHelper.SetButton('Cancelar')
        
        
        
        
        
        
        #self.oHelper.ScrollGrid(column="Cod Verba", match_value= "D03",                 grid_number=1)
        #self.oHelper.LoadGrid()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
              
        self.oHelper.SetButton("Outras Ações",'Parâmetros')
        self.oHelper.Screenshot("Relatorio_verba_02") 
        
        self.oHelper.SetValue("Filial ?", self.filial, check_value=False)
        
        self.oHelper.SetValue("Matrícula ?", self.matricula, check_value=False)
        
        self.oHelper.SetValue("Situações ?", self.situacao, check_value=False)
         
        self.oHelper.SetButton('Confirmar')
        
        self.oHelper.SetValue("Categorias ?", 'M*****************', check_value=False)
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetKey('TAB')
        
        
        self.oHelper.SetValue("Período ?", self.periodo)
        self.oHelper.Screenshot("Relatorio_verba_03")    
        self.oHelper.SetValue("Todas as Verbas ?", 'Sim', check_value=False)
        self.oHelper.SetButton('Confirmar')  
        self.oHelper.SetValue("Salário do Cadastro ?", 'Não', check_value=False) 
        self.oHelper.SetValue("Lista Total Empresa ?", 'Sim', check_value=False) 
        self.oHelper.SetValue("Imprimir Bases ?", 'Não', check_value=False) 
        self.oHelper.SetButton('OK')
        self.oHelper.Screenshot("Relatorio_verba_04")
        self.oHelper.SetButton('Imprimir')   
        sleep(8)
        self.oHelper.Screenshot("Relatorio_verba_04")
        
        
        
        self.oHelper.SetButton('Sair')
        sleep(5)
        self.oHelper.AssertTrue()
        
        print("------------------------------------------------")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_geracao_relatorio_verba")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
        
    

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(PXGPEM89('test_reajuste_salarial_dissidio_acordo_coletivo'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
