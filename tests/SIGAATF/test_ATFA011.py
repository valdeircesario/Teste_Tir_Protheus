from os import getcwd, path
import sys
from tir import Webapp
from pytest import mark
import unittest
from datetime import datetime, timedelta
from time import sleep

# Garante a importação dos módulos da pasta utilis
PROJECT_ROOT = path.abspath(path.join(path.dirname(__file__), '..', '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tir import Webapp
from utilis.md_reporter import TirReportAgent

DateSystem = datetime.today().strftime('%d/%m/%Y')


# TESTE DE CADASTRO DE RATEIO

class ATFA011(unittest.TestCase):	
    @classmethod
    def setUpClass(cls):
        cls.filial = '01'
        configfile = getcwd() + '\\config.json'
        # 1. Instância base do TIR
        webapp_base = Webapp(configfile)
                
        # 2. Encapsula com o Agente de Relatório
        cls.oHelper = TirReportAgent(
            tir_instance=webapp_base,
            cod_modulo="01",
            nome_modulo="Ativo Fixo",
            ct_nome="test_ATFA011",
            descricao="Inclusão e Visualização Rateio"
        )
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '01')
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros > Rateio")
        cls.oHelper.SetButton('Confirmar')
        

    def test_cadastro_Rateio(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')
            

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        try:
        
            self.oHelper.WaitShow("Rateio de despesas de depreciacao do imobilizado") 
            
            
            #--------------
            # INCLUISÃO
            #-------------
            
                
            self.oHelper.Screenshot("Rateio/001")
            print('-----------------------------Incluir')
            self.oHelper.SetButton("Incluir")
            self.oHelper.WaitShow("Rateio de Despesas de Depreciacao-Incluir")
            codRateio = self.oHelper.GetValue('Cod. Rateio')
            print(f"Codigo do Rateio:{codRateio}")
            self.oHelper.Screenshot("Rateio/002") 
            self.oHelper.SetValue('Percentual',"100",   grid=True ,          check_value=False) 
            self.oHelper.SetValue('C.Custo',"001",      grid=True,           check_value=False)
            self.oHelper.SetValue('C Contabil',"01111", grid=True,           check_value=False)
            self.oHelper.SetValue('Item Conta',"123",   grid=True,           check_value=False)
            self.oHelper.SetValue('Classe Valor',"2123",grid=True,           check_value=False)
            self.oHelper.LoadGrid()
            self.oHelper.SetButton("Salvar")
            self.oHelper.WaitShow("Rateio de Despesas de Depreciacao-Incluir") 
            self.oHelper.SetButton("Cancelar")
            self.oHelper.WaitShow("Rateio de despesas de depreciacao do imobilizado")
      
     
              
            
            #-----------------------
            # VISUALIZAR INCLUSÃO 
            #------------------------
            
            print('---------------------------------Visualizar')
            self.oHelper.SetButton("Visualizar")
            self.oHelper.WaitShow("Rateio de Despesas de Depreciacao-Visualizar")
            self.oHelper.Screenshot("Rateio/007") 
            self.oHelper.CheckResult('Cod. Rateio',codRateio) 
            self.oHelper.CheckResult('C.Custo',"001",           grid=True)
            self.oHelper.CheckResult('C Contabil',"01111",      grid=True)
            self.oHelper.CheckResult('Item Conta',"123",        grid=True)
            self.oHelper.CheckResult('Classe Valor',"2123",     grid=True)
            self.oHelper.LoadGrid()
            self.oHelper.Screenshot("Rateio/008")    
            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Rateio de despesas de depreciacao do imobilizado")
            
            self.oHelper.AssertTrue()

        except Exception as e:
            self.oHelper.registrar_erro(e)
            raise e
        finally:
            self.oHelper.salvar_relatorio()
        
        print("------------------------------------------------")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_cadastro_Rateio")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
        
    

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ATFA011('test_cadastro_Rateio'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
