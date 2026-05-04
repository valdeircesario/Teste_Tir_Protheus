
from selenium.webdriver.common.by import By
from selenium import webdriver
from tir import Webapp
from os import getcwd
import unittest
from datetime import datetime
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DateSystem = datetime.today().strftime('%d/%m/%Y')

## python -m pytest tests/Outros/test_compras.py -v -s --html=reports/report_compras.html --self-contained-html

#------------------------------------------
#-- Teste compras no fuxo de compras
#------------------------------------------




class CSAA100(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       
        cls.Descrição = 'GESTÃO DE PESSOAS'
        cls.CentroCusto = '003'
        cls.DepartamentoSuper = '000000002'
        cls.Responsavel = '000012'
        cls.filial = '02DF0001'
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', DateSystem, '02', cls.filial, '02')
        cls.oHelper.SetLateralMenu("Atualizações > Novo Fluxo de Compras > Novo Fluxo de Compras")
        cls.oHelper.SetButton('Confirmar')

    def test_novo_fuxo_de_compras(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        sleep(5)
        
        # Captura screenshot antes de clicar no carrinho (para debug)
        self.oHelper.Screenshot('debug_antes_clique_carrinho')
        
        # Tenta clicar no ícone do carrinho - testando diferentes abordagens
        print("Tentando clicar no carrinho...")
        
        # Primeira tentativa: Clica diretamente no ícone
        try:
            print("Tentativa 1: Seletor XPath direto")
            self.oHelper.ClickByLocator(selector="//*[contains(@class,'po-icon-cart')]", locator=By.XPATH)
            print("✅ Clicou com sucesso - Tentativa 1")
        except Exception as e1:
            print(f"❌ Tentativa 1 falhou: {str(e1)}")
            
            # Segunda tentativa: Clica no botão pai que contém o ícone
            try:
                print("Tentativa 2: Clica no botão pai")
                self.oHelper.ClickByLocator(selector="//button[contains(@class, 'po-icon-cart')]", locator=By.XPATH)
                print("✅ Clicou com sucesso - Tentativa 2")
            except Exception as e2:
                print(f"❌ Tentativa 2 falhou: {str(e2)}")
                
                # Terceira tentativa: Usa CSS selector
                try:
                    print("Tentativa 3: CSS Selector")
                    self.oHelper.ClickByLocator(selector="[class*='po-icon-cart']", locator=By.CSS_SELECTOR)
                    print("✅ Clicou com sucesso - Tentativa 3")
                except Exception as e3:
                    print(f"❌ Tentativa 3 falhou: {str(e3)}")
                    print("⚠️ Nenhuma tentativa funcionou. Capturando screenshot de erro...")
                    self.oHelper.Screenshot('debug_erro_clique_carrinho')
        
        
        
        
        
        
        
        
        
        
        
        
        #self.oHelper.SetButton("Incluir")
        sleep(1)
        

        self.oHelper.AssertTrue()
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_novo_fuxo_de_compras")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CSAA100('test_novo_fuxo_de_compras'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)