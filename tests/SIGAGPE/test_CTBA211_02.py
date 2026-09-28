import sys

from pytest import mark
import unittest
from time import sleep
from os import getcwd,path
from datetime import datetime, timedelta

# Garante a importação dos módulos da pasta utilis
PROJECT_ROOT = path.abspath(path.join(path.dirname(__file__), '..', '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
from time import sleep

from tir import Webapp
from utilis.md_reporter import TirReportAgent
DateSystem = datetime.today().strftime('%d/%m/%Y')
from tir.technologies.core.base import By
from tir import Webapp

class CTBA211_02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
                                                                        
       
        cls.filial = '01'
        cls.dataref = "20012026" 
        configfile = getcwd() + '\\config.json'
        # 1. Instância base do TIR
        webapp_base = Webapp(configfile)
                
        # 2. Encapsula com o Agente de Relatório
        cls.oHelper = TirReportAgent(
            tir_instance=webapp_base,
            cod_modulo="07",
            nome_modulo="Gestão de Pessoal",
            ct_nome="test_CTBA211_02",
            descricao="Integração de todos os roteiros da folha"
        )
        cls.oHelper.Setup('SIGAMDI', cls.dataref, '99', cls.filial, '07') 
        cls.oHelper.SetLateralMenu("Miscelanea > Cálculos > Integrações")
        cls.oHelper.SetButton("Confirmar")
        
    def test_integração_do_sistema_com_todos_os_roteiros(self):


        try:
            sleep(5)
            if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
                self.oHelper.SetButton('Fechar')
              
            sleep(2)
            if self.oHelper.IfExists("Moedas"):
                self.oHelper.CheckResult('Dolar', '0,0000')
                self.oHelper.SetButton('Confirmar')
                
            #-------------------------------------------------------------
            # VALIDAR INTEGRAÇÃO DO SISTEMA DA FOLHA COM TODOS OS ROTEIROS
            #-------------------------------------------------------------

            self.oHelper.WaitShow('Integrações com a Folha de Pagamento') 
            self.oHelper.SetValue("Processo","00001")
            self.oHelper.Screenshot("Integração/001")
            self.oHelper.SetButton("Outras Ações","Inverter Seleção")
            sleep(2)
            self.oHelper.Screenshot("Integração/002")   
            self.oHelper.SetButton("Integrar")
            sleep(2)

            if self.oHelper.IfExists("Nenhum roteiro selecionado."):
                self.oHelper.Screenshot("Integração/003")
                self.oHelper.CheckHelp(text="Nenhum roteiro selecionado.", button="Fechar")
            
            if self.oHelper.IfExists("Integrações Com a Folha de Pagamento"):
                self.oHelper.Screenshot("Integração/004")
                self.oHelper.SetButton("Executar")

            sleep(2)
            if self.oHelper.IfExists("Log de Ocorrências nos Identificadores de Cálculo"):
                self.oHelper.SetButton("OK")
                sleep(3)
                self.oHelper.Screenshot("Integração/005")
                self.oHelper.SetButton("Sair")

            sleep(2)
            if self.oHelper.IfExists("Log de Ocorrências nos Identificadores de Cálculo"):
                self.oHelper.SetButton("OK")
                sleep(3)
                self.oHelper.Screenshot("Integração/006")
                self.oHelper.SetButton("Sair")

            sleep(2)
            if self.oHelper.IfExists("Log de Ocorrências nos Identificadores de Cálculo"):
                self.oHelper.SetButton("OK")
                sleep(3)
                self.oHelper.Screenshot("Integração/007")
                self.oHelper.SetButton("Sair")

            sleep(2)
            if self.oHelper.IfExists("Log de Ocorrências nos Identificadores de Cálculo"):
                self.oHelper.SetButton("OK")
                sleep(3)
                self.oHelper.Screenshot("Integração/008")
                self.oHelper.SetButton("Sair")

            #self.oHelper.WaitProcessing('Aguarde Processando..')

            
            self.oHelper.Screenshot("Integração/009")
            sleep(1)
            self.oHelper.SetButton("x")
            sleep(5)
            self.oHelper.AssertTrue()

        except Exception as e:
            self.oHelper.registrar_erro(e)
            raise e
        finally:
            self.oHelper.salvar_relatorio()
    
        print("")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 integrar o sistema da foha com todos os roteiros")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
        
            

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CTBA211_02('test_integração_do_sistema_com_todos_os_roteiros'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)