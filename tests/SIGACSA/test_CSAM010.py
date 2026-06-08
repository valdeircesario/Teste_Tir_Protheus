from tir import Webapp
from pytest import mark
import unittest
from os import getcwd
from datetime import datetime, timedelta
from time import sleep
from selenium.webdriver.common.by import By

DateSystem = datetime.today().strftime('%d/%m/%Y')

# python -m pytest tests/Outros/test_CSAM010.py -v -s --html=reports/report_CSAM010.html --self-contained-html

#

class CSAM010(unittest.TestCase):	
    @classmethod
    def setUpClass(cls):
        cls.filial = '01'
        cls.tabelaSalarial = '002'
        cls.tipoAumento = '003'
        
        cls.dataref = (datetime.today()-timedelta(days=10)).strftime("%d/%m/%Y")# AJUSTAR DATA PARA PERIODO EM ABERTO 
    
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', cls.dataref, '99', cls.filial, '40')
        cls.oHelper.SetLateralMenu("Miscelanea > Reajuste > Salário Por Tabela")
        cls.oHelper.SetButton('Confirmar')
        

    def test_reajuste_salarial_por_tabela(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')
            

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')
        
        sleep(5)
        self.oHelper.WaitShow("Este programa atualiza o salario dos funcionarios conforme a Tabela Salarial.")      
        self.oHelper.Screenshot("reajuste_salarial_01")
        self.oHelper.SetButton("Param.") 
        self.oHelper.WaitShow("Parametros")
        self.oHelper.Screenshot("reajuste_salarial_02")   
        self.oHelper.SetValue('Tabela Salarial ?',self.tabelaSalarial,check_value=False)  
        self.oHelper.SetValue('Tipo de Aumento ?',self.tipoAumento,check_value=False) 
        self.oHelper.SetValue('Data do Aumento ?',self.dataref,check_value=False)
        self.oHelper.Screenshot("reajuste_salarial_03")
        self.oHelper.SetValue('Atual.Sal.Dissidio ?',"Sim",check_value=False)
        self.oHelper.SetValue('Classe salarial De ?',"001",check_value=False)
        self.oHelper.SetValue('Classe salarial Ate ?',"011",check_value=False)
        self.oHelper.SetValue('Data tabela salarial ?',self.dataref,check_value=False)
        self.oHelper.Screenshot("reajuste_salarial_04")
        self.oHelper.SetButton("OK")
        sleep(5)
        self.oHelper.SetButton("OK")
        
        if self.oHelper.IfExists("Confirma configuraçäo dos parâmetros?"):
            self.oHelper.Screenshot("reajuste_salarial_05")
            self.oHelper.SetButton('Sim')
        sleep(15)    
        if self.oHelper.IfExists("LOG DE OCORRENCIAS - Cargos e Salários  - Versao 12"):
            self.oHelper.ClickLabel("Em Disco")
            self.oHelper.Screenshot("reajuste_salarial_06")
            self.oHelper.SetButton("OK")
            sleep(25)
            self.oHelper.Screenshot("reajuste_salarial_07")
            self.oHelper.SetButton("Sair") 
                
        
        sleep(0.5)
        self.oHelper.Screenshot("reajuste_salarial_08")
        self.oHelper.WaitShow("Histórico Salarial")
        self.oHelper.Screenshot("reajuste_salarial_09")
        sleep(10)
        self.oHelper.WaitProcessing("Histórico Salarial")
        sleep(2)
        
        self.oHelper.SetLateralMenu("Miscelanea > Reajuste > Salário Por Tabela")
        self.oHelper.SetButton('Confirmar')
        sleep(1)
        self.oHelper.WaitShow("Este programa atualiza o salario dos funcionarios conforme a Tabela Salarial.")       
        self.oHelper.Screenshot("reajuste_salarial_10")
        
        self.oHelper.AssertTrue()
        
        print("------------------------------------------------")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_reajuste_salarial_por_tabela")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
        
    

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CSAM010('test_reajuste_salarial_por_tabela'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
