from tir import Webapp
from pytest import mark
import unittest
from os import getcwd
from datetime import datetime, timedelta
from time import sleep
from selenium.webdriver.common.by import By

DateSystem = datetime.today().strftime('%d/%m/%Y')

#  .\venv\Scripts\python.exe -m pytest tests/Outros/test_PXGPEM89.py -s

# OBSERVAÇÃO:
# O ACORDO COLETIVO S SEMPRE ACORDADO PARA O MES, 09 DE CADA ANO, SEMPRE QUE EXECUTAR ESSE TESTE PROCURAR USAR O PERIODO DO ACORDO 
# SEMPRE OS PERIODOS DOS MESES: 11,12,01,02,03,04,05,06,07,08. E USAR O ACESSO AO CALCULO COM A DATA DO PERIODO EM ABERTO.
class PXGPEM89(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.filial = '02DF0001'
        cls.matricula = '208201'
        cls.processo = '00001'
        cls.periodo = '012026'# PERIODO  QUE FOI CRIADO O ACORDO COLETIVO 
        cls.nome = 'MARCELO CORREA'
        
        cls.dataref = (datetime.today()-timedelta(days=30)).strftime("%d/%m/%Y")# AJUSTAR DATA PARA PERIODO EM ABERTO 
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', cls.dataref, '02', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Miscelanea > Cálculos > Integrações")
        cls.oHelper.SetButton('Confirmar')
        
        if cls.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            cls.oHelper.SetButton('Fechar')

        if cls.oHelper.IfExists("Moedas"):
            cls.oHelper.CheckResult('Dolar', '0,0000')
            cls.oHelper.SetButton('Confirmar')
        

    def test_reajuste_salarial_dissidio_acordo_coletivo(self):
        
        #-----------------------------------
        # GARANTE A INTEGRAÇÃO DOS ROTEIROS
        #-----------------------------------
     
        self.oHelper.SetValue("Processo ?", self.processo, check_value=False) 
        self.oHelper.Screenshot("PXGPEM89/Dissidio_integração_01")  
        self.oHelper.SetButton('Outras Ações','Inverter Seleção')
        self.oHelper.Screenshot("PXGPEM89/Dissidio_integração_02")
        
        self.oHelper.SetButton('Integrar')
        
        if self.oHelper.IfExists("Integrações Com a Folha de Pagamento"):
            self.oHelper.Screenshot("PXGPEM89/Dissidio_integração_03")
            self.oHelper.SetButton('Executar')
            self.oHelper.WaitProcessing("Processando")
            self.oHelper.SetButton('Ok')
            self.oHelper.Screenshot("PXGPEM89/Dissidio_integração_04")
            self.oHelper.WaitProcessing("Processando")
            self.oHelper.SetButton('Ok')
            self.oHelper.WaitProcessing("Processando")
            self.oHelper.SetButton('x')
            self.oHelper.WaitProcessing("Processando")
            self.oHelper.Screenshot("PXGPEM89/Dissidio_integração_05")
            self.oHelper.SetButton('x')
        
        self.oHelper.Screenshot("PXGPEM89/Dissidio_integração_06")    
        if self.oHelper.IfExists("ATENÇÃO"):
            self.oHelper.CheckHelp(text="ATENÇÃO", button="Fechar")
            self.oHelper.SetButton('x')
            self.oHelper.WaitProcessing("Processando")
            self.oHelper.Screenshot("PXGPEM89/Dissidio_integração_05")
            self.oHelper.SetButton('x')
            
        #--------------------------------------------------------------------
        # FAZ O LANÇAMENTO DE REAJUSTE SALARIAL PELO DISSÍDIO/ACORDO COLETIVO
        #--------------------------------------------------------------------
        
        self.oHelper.SetLateralMenu("Atualizações > Especificos > Dissid.Retroativo Poupex")
        self.oHelper.SetButton('Confirmar')
        self.oHelper.WaitShow('Calculo Acordo Coletivo')
        
        #-------------------------
        #DESINTEGRAR
        #-------------------------
        self.oHelper.Screenshot("PXGPEM89/Dissidio_integração_07")
        self.oHelper.SetButton('Outras Ações','Integração')
        self.oHelper.SetValue("Matrícula De ?", self.matricula, check_value=False)  
        self.oHelper.SetValue("Matrícula Até ?", self.matricula, check_value=False) 
        self.oHelper.SetValue("Tipo ?", 'Desintegrar', check_value=False)
        self.oHelper.Screenshot("PXGPEM89/Dissidio_integração_08")  
        self.oHelper.SetButton('OK')
        
        #------------------------
        # GERAR O ACORDO COLETIVO
        #-----------------------
        
        self.oHelper.SetButton('Outras Ações','Gerar')
        self.oHelper.Screenshot("PXGPEM89/Dissidio_integração_09")
        
        self.oHelper.SetValue("Mês/Ano Acordo: ?", self.periodo, check_value=False)  
        self.oHelper.SetValue("Matrícula De ?", self.matricula, check_value=False)  
        self.oHelper.SetValue("Matrícula Até ?", self.matricula, check_value=False)  
        self.oHelper.SetValue("% Reajuste ?", '1000', check_value=False)
        self.oHelper.Screenshot("PXGPEM89/Dissidio_integração_10")
        self.oHelper.SetButton('OK')
        
        if self.oHelper.IfExists("Os dados do acordo coletivo foram gerados com sucesso!"):
            self.oHelper.Screenshot("PXGPEM89/Dissidio_integração_11")
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
                
        #----------------------------------------------------
        # FAZER INTEGRAÇÃO DO ACORDO PARA CALCULO FOLHA
        #----------------------------------------------------
        self.oHelper.SetButton('Outras Ações','Integração')  
        self.oHelper.SetValue("Matrícula De ?", self.matricula, check_value=False)  
        self.oHelper.SetValue("Matrícula Até ?", self.matricula, check_value=False) 
        self.oHelper.SetValue("Tipo ?", 'Integrar', check_value=False)
        self.oHelper.SetButton('OK')
        sleep(5)
        
        #---------------------------------------------
        # MANUTENÇÃO
        #---------------------------------------------
        
        self.oHelper.SearchBrowse(self.filial + self.matricula + self.nome, key="Filial+Matricula+Nome")
        self.oHelper.Screenshot("PXGPEM89/Dissidio_integração_12")
        
        self.oHelper.SetButton('Manutenção')
        self.oHelper.WaitShow('Funcionários - MANUTENÇÃO')
        self.oHelper.Screenshot("PXGPEM89/Dissidio_integração_13")
        self.oHelper.SetButton('Fechar') 
        
        
        
        
        
        #--------------------------------------------
        # FAZER CALCULO FOLHA
        #---------------------------------------------
        self.oHelper.SetLateralMenu("Atualizações > Lançamentos > Por Funcionário")
        self.oHelper.SetButton('Confirmar')
        self.oHelper.WaitShow('Lançamentos por Período')
        self.oHelper.Screenshot("PXGPEM89/Dissidio_integração_14")
 
        self.oHelper.SearchBrowse(self.filial + self.matricula + self.nome, key="Filial+Matricula+Nome")
        self.oHelper.Screenshot("PXGPEM89/Dissidio_integração_15")
        self.oHelper.SetButton('Alterar')
        self.oHelper.WaitShow('Lançamentos por Funcionário')
        self.oHelper.Screenshot("PXGPEM89/Dissidio_integração_16")
        
        self.oHelper.SetButton('Outras Ações','Calcular Lançamento')
        self.oHelper.Screenshot("PXGPEM89/Dissidio_integração_17") 
        self.oHelper.WaitProcessing("Processando")
        self.oHelper.Screenshot("PXGPEM89/Dissidio_integração_18") 
        self.oHelper.SetButton('OK')
        
        self.oHelper.SetButton('Outras Ações','Consultar Cálculo')
        self.oHelper.Screenshot("PXGPEM89/Dissidio_integração_19")
        self.oHelper.SetButton('Cancelar')
        self.oHelper.Screenshot("PXGPEM89/Dissidio_integração_20") 
        self.oHelper.SetButton('Cancelar')
        
        #---------------------------------------------
        # CANCELAR A INTEGRAÇÃO DO ACORDO COLETIVO
        #---------------------------------------------
        self.oHelper.SetLateralMenu("Atualizações > Especificos > Dissid.Retroativo Poupex")
        self.oHelper.SetButton('Confirmar')
        self.oHelper.WaitShow('Calculo Acordo Coletivo')
        
        #-------------------------
        # DESINTEGRAR
        #-------------------------
        self.oHelper.SetButton('Outras Ações','Integração')
        self.oHelper.SetValue("Matrícula De ?", self.matricula, check_value=False)  
        self.oHelper.SetValue("Matrícula Até ?", self.matricula, check_value=False) 
        self.oHelper.SetValue("Tipo ?", 'Desintegrar', check_value=False)
        self.oHelper.SetButton('OK')
          
        self.oHelper.AssertTrue()
        
        print("------------------------------------------------")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_reajuste_salarial_dissidio_acordo_coletivo")
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
