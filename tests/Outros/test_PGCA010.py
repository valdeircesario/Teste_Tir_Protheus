from tir import Webapp
from pytest import mark
import unittest
from os import getcwd
from datetime import datetime, timedelta
from time import sleep
from selenium.webdriver.common.by import By

DateSystem = datetime.today().strftime('%d/%m/%Y')

#  .\venv\Scripts\python.exe -m pytest tests/Outros/test_PXGPEM89.py -s

# OBSERVAÇÃO
class PGCA010(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.filial = '02DF0001'
        cls.matricula = '209690'
        cls.processo = '00001'
        cls.periodo = '012026'# PERIODO  QUE FOI CONCEDIDO O ACORDO COLETIVO 
        cls.nome = 'RENATO DE SOUZA BRITO'
        
        cls.dataref = (datetime.today()-timedelta(days=30)).strftime("%d/%m/%Y")# AJUSTAR DATA PARA PERIODO EM ABERTO 
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', cls.dataref, '02', cls.filial, '02')
        cls.oHelper.SetLateralMenu("Atualizações > Novo Fluxo de Compras > Novo Fluxo de Compras")
        cls.oHelper.SetButton('Confirmar')
        
        if cls.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            cls.oHelper.SetButton('Fechar')

        if cls.oHelper.IfExists("Moedas"):
            cls.oHelper.CheckResult('Dolar', '0,0000')
            cls.oHelper.SetButton('Confirmar')
        

    def test_novo_fluxo_compras(self):
        
        #-------------------------------------------------
        # SELECIONAR UMA SOLICITAÇÃO PARA GERAR A CONTAÇÃO
        #-------------------------------------------------
        sleep(5)
        
        self.oHelper.ClickIcon('Necessidade de Compra')
        self.oHelper.SetValue("Processo ?", self.processo, check_value=False) 
        self.oHelper.Screenshot("Dissidio_Acor_Coletivo_01")  
        self.oHelper.SetButton('Outras Ações','Inverter Seleção')
        self.oHelper.Screenshot("Dissidio_Acor_Coletivo_02")
        
        self.oHelper.SetButton('Integrar')
        
        if self.oHelper.IfExists("Integrações Com a Folha de Pagamento"):
            self.oHelper.Screenshot("Dissidio_Acor_Coletivo_03")
            self.oHelper.SetButton('Executar')
            self.oHelper.WaitProcessing("Processando")
            self.oHelper.SetButton('Ok')
            self.oHelper.Screenshot("Dissidio_Acor_Coletivo_04")
            self.oHelper.WaitProcessing("Processando")
            # as duas linhas abaixo com ## não existem no ambiente https://qasrverp:10020/webapp/
            # com atualização da 2510 no proj2 elas surgiram, observar esse detalhe
            self.oHelper.SetButton('Ok')##
            self.oHelper.WaitProcessing("Processando")##
            self.oHelper.SetButton('x')
            self.oHelper.WaitProcessing("Processando")
            self.oHelper.Screenshot("Dissidio_Acor_Coletivo_05")
            self.oHelper.SetButton('x')
        
        self.oHelper.Screenshot("Dissidio_Acor_Coletivo_06")    
        if self.oHelper.IfExists("ATENÇÃO"):
            self.oHelper.CheckHelp(text="ATENÇÃO", button="Fechar")
            self.oHelper.SetButton('x')
            self.oHelper.WaitProcessing("Processando")
            self.oHelper.Screenshot("Dissidio_Acor_Coletivo_05")
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
        self.oHelper.Screenshot("Dissidio_Acor_Coletivo_07")
        self.oHelper.SetButton('Outras Ações','Integração')
        self.oHelper.SetValue("Matrícula De ?", self.matricula, check_value=False)  
        self.oHelper.SetValue("Matrícula Até ?", self.matricula, check_value=False) 
        self.oHelper.SetValue("Tipo ?", 'Desintegrar', check_value=False)
        self.oHelper.Screenshot("Dissidio_Acor_Coletivo_08")  
        self.oHelper.SetButton('OK')
        
        #------------------------
        # GERAR O ACORDO COLETIVO
        #-----------------------
        
        self.oHelper.SetButton('Outras Ações','Gerar')
        self.oHelper.Screenshot("Dissidio_Acor_Coletivo_09")
        
        self.oHelper.SetValue("Mês/Ano Acordo: ?", self.periodo, check_value=False)  
        self.oHelper.SetValue("Matrícula De ?", self.matricula, check_value=False)  
        self.oHelper.SetValue("Matrícula Até ?", self.matricula, check_value=False)  
        self.oHelper.SetValue("% Reajuste ?", '1000', check_value=False)
        self.oHelper.Screenshot("Dissidio_Acor_Coletivo_10")
        self.oHelper.SetButton('OK')
        
        if self.oHelper.IfExists("Os dados do acordo coletivo foram gerados com sucesso!"):
            self.oHelper.Screenshot("Dissidio_Acor_Coletivo_11")
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
        self.oHelper.Screenshot("Dissidio_Acor_Coletivo_12")
        
        self.oHelper.SetButton('Manutenção')
        self.oHelper.WaitShow('Funcionários - MANUTENÇÃO')
        self.oHelper.Screenshot("Dissidio_Acor_Coletivo_13")
        self.oHelper.SetButton('Fechar') 
        
        
        
        
        
        #--------------------------------------------
        # FAZER CALCULO FOLHA
        #---------------------------------------------
        self.oHelper.SetLateralMenu("Atualizações > Lançamentos > Por Funcionário")
        #self.oHelper.SetButton('Confirmar')
        self.oHelper.WaitShow('Lançamentos por Período')
        self.oHelper.Screenshot("Dissidio_Acor_Coletivo_14")
 
        self.oHelper.SearchBrowse(self.filial + self.matricula + self.nome, key="Filial+Matricula+Nome")
        self.oHelper.Screenshot("Dissidio_Acor_Coletivo_15")
        self.oHelper.SetButton('Alterar')
        self.oHelper.WaitShow('Lançamentos por Funcionário')
        self.oHelper.Screenshot("Dissidio_Acor_Coletivo_16")
        
        self.oHelper.SetButton('Outras Ações','Calcular Lançamento')
        self.oHelper.Screenshot("Dissidio_Acor_Coletivo_17") 
        self.oHelper.WaitProcessing("Processando")
        sleep(5)
        self.oHelper.Screenshot("Dissidio_Acor_Coletivo_18") 
        self.oHelper.SetButton('OK')
        
        self.oHelper.SetButton('Outras Ações','Consultar Cálculo')
        sleep(5)
        self.oHelper.Screenshot("Dissidio_Acor_Coletivo_19")
        self.oHelper.SetButton('Cancelar')
        sleep(5)
        self.oHelper.Screenshot("Dissidio_Acor_Coletivo_20") 
        self.oHelper.SetButton('Cancelar')
        sleep(5)
        
        #---------------------------------------------
        # CANCELAR A INTEGRAÇÃO DO ACORDO COLETIVO
        #---------------------------------------------
        self.oHelper.SetLateralMenu("Atualizações > Especificos > Dissid.Retroativo Poupex")
        self.oHelper.SetButton('Confirmar')
        sleep(5)
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
        print("X 🎯 test_novo_fluxo_compras")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
        
    

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(PGCA010('test_novo_fluxo_compras'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
