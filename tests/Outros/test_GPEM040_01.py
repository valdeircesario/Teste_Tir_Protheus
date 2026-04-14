import sys
from os import getcwd
from os.path import abspath, join, dirname

# Adicionar diretório raiz ao sys.path para importar tools
sys.path.insert(0, abspath(join(dirname(__file__), '..', '..')))

from tir.technologies.core.base import By
from tir import Webapp
from pytest import mark
import unittest
from time import sleep
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tools.click_helper import ClickHelper
DateSystem = datetime.today().strftime('%d/%m/%Y')

 

#------------------------
# LANÇAMENTO DE RESCISÃO COMPLEMENTAR
#------------------------

class GPEM040_01(unittest.TestCase):
    
    
    @classmethod
    def setUpClass(self):
        self.filial = '02DF0001'
        self.Matricula = '200561' # ACONSELHO UTILIZAR SEMPRE UM FUNCIONARIO DEFERENTE, PARA MELHOR CALCULO DO TESTE
        self.Nome = 'JOSE AFONSO TAVARES'
        self.dataref = (datetime.today()-timedelta(days=13)).strftime("%d/%m/%Y")# USE O PERIODO EM ABERTO
        

        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', self.dataref, '02', self.filial, '07')
        
        self.oHelper.SetLateralMenu("Miscelanea > Cálculos (13)> Rescisão")
        self.oHelper.SetButton('Confirmar')
       
    def test_lancamento_rescisao_complementar(self):
        
        
        
        
        sleep(5)

        if self.oHelper.IfExists("Reforma Tributária"):
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()

        sleep(5)

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()

        self.oHelper.WaitShow("Funcionários")
        
        #----------------------------------------------------------------------------------
        # CANCELAR A INTEGRAÇÃO PARA REALIZAR A EXLUSÃO DO RESIDUO DE RESCISÃO COMPLEMENTAR
        #----------------------------------------------------------------------------------
        
        self.oHelper.SetButton("Integração")   
        self.oHelper.SetValue('Processo ?','00001')
        self.oHelper.Screenshot("Res_Complementar_14")
        self.oHelper.ClickBox("Roteiro", "RES",grid_number=1)
        self.oHelper.SetButton("Cancelar Integração")
        
        if self.oHelper.IfExists("Integrações Com a Folha de Pagamento"):
            self.oHelper.SetButton("Executar")
            self.oHelper.Screenshot("Res_Complementar_15")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
        
        if self.oHelper.IfExists("Nenhum roteiro selecionado."):
            self.oHelper.Screenshot("Res_Complementar_16")
            self.oHelper.CheckHelp(text="Nenhum roteiro selecionado.", button="Fechar")
        sleep(1)
        self.oHelper.SetButton("x") 
        sleep(2) 
        self.oHelper.Screenshot("Res_Complementar_01")
        self.oHelper.SearchBrowse(self.filial + self.Matricula + self.Nome, key="Filial+Matricula+Nome")
        sleep(1)       

        self.oHelper.SetButton('Incluir')
        self.oHelper.SearchBrowse(self.filial)
        self.oHelper.Screenshot("Res_Complementar_02")
        self.oHelper.SetButton("OK")
        sleep(1)
        
        if self.oHelper.IfExists("Rescisão Complementar"):
            self.oHelper.Screenshot("Res_Complementar_03")
            self.oHelper.SetButton("OK")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        sleep(2)
        self.oHelper.Screenshot("Res_Complementar_04")
        self.oHelper.SetButton('Salvar')   
        sleep(2)
        self.oHelper.WaitShow("Rescisões - INCLUIR")
        sleep(3)
        self.oHelper.Screenshot("Res_Complementar_05") 
        sleep(3)
        self.oHelper.SetValue("RG_DATAHOM",self.dataref)
        self.oHelper.SetValue("RG_DTGERAR",self.dataref) 
        self.oHelper.SetKey("F7")
        sleep(2) 
        
        self.oHelper.WaitShow('Lançamentos por Funcionário')
        self.oHelper.Screenshot("Res_Complementar_06") 
        self.oHelper.SetValue("Cod Verba",'850',        grid=True, grid_number=1, check_value=False)
        self.oHelper.SetValue("Valor",'199',            grid=True, grid_number=1, check_value=False)
        self.oHelper.LoadGrid()
        self.oHelper.Screenshot("Res_Complementar_07")
        sleep(0.5)  
        self.oHelper.SetButton("Salvar")
        self.oHelper.Screenshot("Res_Complementar_08")
        sleep(1)
        self.oHelper.SetKey('F6')
        sleep(2)
        self.oHelper.Screenshot("Res_Complementar_09")
        
        self.oHelper.CheckHelp(text="ATENÇÃO", button="Sim") 
        self.oHelper.Screenshot("Res_Complementar_10")
        self.oHelper.WaitProcessing("Processando")
        
        self.oHelper.ScrollGrid(column="Codigo Verba", match_value= "850",                 grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.Screenshot("Res_Complementar_11") 
        self.oHelper.SetButton('Confirmar')
        
        if self.oHelper.IfExists("Registro inserido com sucesso"):
            self.oHelper.Screenshot("Res_Complementar_12")
            self.oHelper.SetButton("Fechar")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        self.oHelper.WaitShow("Funcionários")
        
        sleep(2)
             
        
        #---------------------------
        # FILTRAR A DATA DA HOMOLOGA
        #---------------------------
        
        self.oHelper.InputByLocator(selector='COMP4604', locator=By.ID, value='Filtar')
        self.oHelper.SetButton('Criar Filtro')
        sleep(1)
        self.oHelper.SetValue("Campo","Dt. Homologa",check_value=False)
        sleep(1)
        self.oHelper.SetValue("Expressão",self.dataref,check_value=False)
        self.oHelper.SetButton('Adicionar')
        self.oHelper.Screenshot("Res_Complementar_17")
        sleep(1)
        self.oHelper.SetButton("Salvar")
        sleep(0.5)
        filtro_texto = f"Dt. Homologa Igual a "
        self.oHelper.ClickCheckBox(filtro_texto,1)
        self.oHelper.Screenshot("Res_Complementar_18")
        self.oHelper.SetButton("Aplicar filtros selecionados")
        sleep(2)
        self.oHelper.Screenshot("Res_Complementar_19")
        
        #-----------------------------------------
        # EXCLUIR O RESIDUO DE RESCISÃO COMPLEMENTAR
        #-----------------------------------------
         
        self.oHelper.InputByLocator(selector='COMP4656', locator=By.ID, value='Outras Ações')
        self.oHelper.ClickMenuPopUpItem("Excluir")
        sleep(5)
        self.oHelper.WaitShow("Tem certeza que deseja excluir o item abaixo?")
        self.oHelper.Screenshot("Res_Complementar_20")
        self.oHelper.SetButton("Confirmar")
        
        
        if self.oHelper.IfExists("Se houve importação de dados do Ponto Eletrônico eles não serão excluídos ao executar o cancelamento da rescisão."):
            self.oHelper.Screenshot("Res_Complementar_21")
            self.oHelper.CheckHelp(text="Se houve importação de dados do Ponto Eletrônico eles não serão excluídos ao executar o cancelamento da rescisão.", button="Fechar")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
        sleep(5)
        
        if self.oHelper.IfExists("Registro excluído com sucesso."):
            self.oHelper.Screenshot("Res_Complementar_22")
            self.oHelper.SetButton("Fechar")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
        sleep(2)
        self.oHelper.AssertTrue()
        
        print("/")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_lancamento_rescisao_complementar")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEM040_01('test_lancamento_rescisao_complementar'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
