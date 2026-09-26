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

from utilis.click_pageview import click_pageview_button
DateSystem = datetime.today().strftime('%d/%m/%Y')

#------------------------
# CALCULO DE ROTEIRO FOL
#------------------------

class GPEM020_FOL(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.filial = '01'
        cls.Roteiro = 'FOL'
        cls.matricula = "00007"
        cls.dataref = (datetime.today()-timedelta(days=10)).strftime("%d/%m/%Y")
        cls.Processo = '00001'
        configfile = getcwd() + '\\config.json'
        # 1. Instância base do TIR
        webapp_base = Webapp(configfile)
                
        # 2. Encapsula com o Agente de Relatório
        cls.oHelper = TirReportAgent(
            tir_instance=webapp_base,
            cod_modulo="07",
            nome_modulo="Gestão de Pessoal",
            ct_nome="test_GPEA020_FOL",
            descricao="calcular Roteiro FOL"
        )
        cls.oHelper.Setup('SIGAMDI', cls.dataref, '99', cls.filial, '07')  
        cls.oHelper.SetLateralMenu("Miscelanea > Cálculos (13)> Por Roteiros")
        cls.oHelper.SetButton('Confirmar')
        
       
    def test_Calculo_Roteiro_FOL(self):

        try:
            sleep(5)
            if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
                self.oHelper.SetButton('Fechar')
            
            sleep(2)
            if self.oHelper.IfExists("Moedas"):
                self.oHelper.CheckResult('Dolar', '0,0000')
                self.oHelper.SetButton('Confirmar')

            sleep(2)           
            if self.oHelper.IfExists("Novidades do Produto"):
                self.oHelper.SetButton('Fechar')



            #-------------------
            # Processo Calculo  
            #-------------------
            # 
            #   
            print('-------------------------------Prametros')
            self.oHelper.WaitShow("Processo de Calculo")
            self.oHelper.WaitShow("Este programa realiza processos de calculos")
            self.oHelper.Screenshot("RoteiroFOL/001")
            
            self.oHelper.SetButton("Parametros")
            self.oHelper.Screenshot("RoteiroFOL/002")
            self.oHelper.SetValue("Processo ?",self.Processo,           check_value=False)
            self.oHelper.SetValue("Roteiro ?",self.Roteiro,             check_value=False)
            self.oHelper.Screenshot("RoteiroFOL/003")
            self.oHelper.SetButton("OK")

            # Filtar Matricula

            print('-----------------------------Filtar matricula')
            self.oHelper.SetButton('Filtro Rapido')
            self.oHelper.SetValue("Campos:","Matricula",               check_value=False)
            self.oHelper.SetValue("Expressäo:",self.matricula)
            self.oHelper.Screenshot("RoteiroFOL/004")
            self.oHelper.SetButton("OK")
            
            self.oHelper.Screenshot("RoteiroFOL/005")
            self.oHelper.SetButton("Calcular")
            self.oHelper.Screenshot("RoteiroFOL/006") 
            sleep(2)
            if self.oHelper.IfExists("Confirma configuracäo dos parametros?"):
                self.oHelper.Screenshot("RoteiroFOL/007")
                self.oHelper.SetButton("Sim")
        
                
            
            self.oHelper.WaitShow("Log de Ocorrencias no Processo de Calculo")
            #self.oHelper.ClickLabel("Em Disco")
            self.oHelper.Screenshot("RoteiroFOL/008")
            self.oHelper.SetButton("OK")
            
                
            sleep(5)
            #click_pageview_button(self.oHelper,"Ampliar (+)")

            sleep(5)
            #click_pageview_button(self.oHelper,"Ampliar (+)")



            self.oHelper.Screenshot("RoteiroFOL/009")
        
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
        print("X 🎯 test_de_Calculo_Roteiro_FOL")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEM020_FOL('test_Calculo_Roteiro_FOL'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
