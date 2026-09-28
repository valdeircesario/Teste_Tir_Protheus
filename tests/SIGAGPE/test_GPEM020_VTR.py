import sys

from tir.technologies.core.base import By
from tir import Webapp
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


#------------------------
# CALCULO DE ROTEIRO VTR
#------------------------

class GPEM020_VTR(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.filial = '01'
        cls.Roteiro = 'VTR'
        cls.Processo = '00001'
        configfile = getcwd() + '\\config.json'
        # 1. Instância base do TIR
        webapp_base = Webapp(configfile)
                
        # 2. Encapsula com o Agente de Relatório
        cls.oHelper = TirReportAgent(
            tir_instance=webapp_base,
            cod_modulo="07",
            nome_modulo="Gestão de Pessoal",
            ct_nome="test_GPEA020_VTR",
            descricao="calcular Roteiro VTR"
        )
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '07')
        
        cls.oHelper.SetLateralMenu("Miscelanea > Cálculos > Por Roteiros")
        cls.oHelper.SetButton('Confirmar')
        
       
    def test_Calculo_Roteiro_VTR(self):
        try:
            sleep(5)
            if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
                self.oHelper.SetButton('Fechar')
        
            sleep(2)
            if self.oHelper.IfExists("Moedas"):
                self.oHelper.CheckResult('Dolar', '0,0000')
                self.oHelper.SetButton('Confirmar')
        
                
            
            self.oHelper.WaitShow("Processo de Calculo")
            self.oHelper.WaitShow("Este programa realiza processos de calculos")
            self.oHelper.Screenshot("RoteiroVTR/001")
            
            self.oHelper.SetButton("Parametros")
            sleep(1)
            self.oHelper.SetValue("Processo ?",self.Processo,           check_value=False)
            self.oHelper.SetValue("Roteiro ?",self.Roteiro,             check_value=False)
            sleep(0.5)
            self.oHelper.Screenshot("RoteiroVTR/002")  
            self.oHelper.SetButton("OK")    
            self.oHelper.WaitShow("Parametros")
            self.oHelper.Screenshot("RoteiroVTR/003")
            self.oHelper.SetButton("OK")
                  
            self.oHelper.SetButton("Calcular")
            self.oHelper.Screenshot("RoteiroVTR/004")
              
            self.oHelper.WaitShow("Confirma configuracäo dos parametros?")
            self.oHelper.Screenshot("RoteiroVTR/005")
            self.oHelper.SetButton("Sim")
            
            self.oHelper.WaitShow("Log de Ocorrencias no Processo de Calculo")  
            #self.oHelper.ClickLabel("Em Disco")
            self.oHelper.Screenshot("RoteiroVTR/006")
            self.oHelper.SetButton("OK")   
            sleep(6)
            self.oHelper.Screenshot("RoteiroVTR/007")
            sleep(5)
            self.oHelper.SetButton("Sair")
            sleep(5)
            self.oHelper.AssertTrue()

        except Exception as e:
            self.oHelper.registrar_erro(e)
            raise e
        finally:
            self.oHelper.salvar_relatorio()
        
        print("------------------------------------------------")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_Calculo_Roteiro_VTR")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEM020_VTR('test_Calculo_Roteiro_VTR'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
