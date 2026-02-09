# gestão disciplinar  Atualizações > Controle Disciplinar > Gestão Disciplinarfrom tir.technologies.core.base import By

#python -m pytest tests/Outros/test_GPEA643.py -v -s

from tir import Webapp
from pytest import mark
import unittest
from time import sleep
from os import getcwd
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')

# .\venv\Scripts\python.exe -m pytest tests/Outros/test_GPEM020_VTR.py -s

#------------------------
# CALCULO DE ROTEIRO VTR
#------------------------

class GPEM020_VTR(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.filial = '02DF0001'
        self.Matricula = '222557'
        self.Nome = 'VANDERLI CESARIO DA SILVA'
        self.Roteiro = "VTR"
        self.Processo = '00001'
        self.Verba = '620'
        
        
        
        self.dataref = (datetime.today()-timedelta(days=15)).strftime("%d/%m/%Y") # AJUSTAR DATA PARA PERIODO EM ABERTO ss
        self.Processo = '00001'
        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', self.dataref, '02', self.filial, '07')
        
        #self.oHelper.SetLateralMenu("Miscelanea > Cálculos (13)> Por Roteiros")
        #self.oHelper.SetLateralMenu("Miscelanea > Cálculos > Integrações")
        self.oHelper.SetLateralMenu("Atualizações > Lançamentos > Por Funcionário ")
        
       
    def test_teste(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
            
        #-----------------------------------
        # GARANTE O CANCELAMENTO DA INTEGRAÇÃO
        
        """ self.oHelper.SetValue('Processo','00001')

        self.oHelper.Screenshot("Cancela_integração_01")
        self.oHelper.SetButton("Outras Ações","Apenas Integrados")
        sleep(3)
        self.oHelper.Screenshot("Cancela_integração_02")
        
        self.oHelper.SetButton('Cancelar Integração')
        
        if self.oHelper.IfExists("Integrações Com a Folha de Pagamento"):
            self.oHelper.SetButton('Executar')
            self.oHelper.Screenshot("Cancela_integração_03")
            sleep(90)
            self.oHelper.Screenshot("Cancela_integração_04")
            sleep(90)
            self.oHelper.Screenshot("Cancela_integração_05")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
        
        self.oHelper.Screenshot("Cancela_integração_06")

        self.oHelper.CheckHelp(text="Nenhum roteiro selecionado.", button="Fechar")
        sleep(1) """
        
        #----------------------------------------------
        # CALCULO POR ROTEIRO DO VTR
        #---------------------------------
        
        
        #self.oHelper.SetLateralMenu("Miscelanea > Cálculos (13)> Por Roteiros")
        
        """ self.oHelper.WaitShow("Processo de Calculo")
        self.oHelper.WaitShow("Este programa realiza processos de calculos")
        self.oHelper.Screenshot("roteiroVTR_01.png")
        
        self.oHelper.SetButton("Parametros")
        sleep(5)
        self.oHelper.SetValue("Processo ?",self.Processo,           check_value=False)
        self.oHelper.SetValue("Roteiro ?",self.Roteiro,             check_value=False)
        sleep(0.5)
        self.oHelper.Screenshot("roteiroVTR_02.png")
        
        self.oHelper.SetButton("OK")
        sleep(5)
        
        
        if self.oHelper.IfExists("Parametros"):
            sleep(1)
            self.oHelper.Screenshot("roteiroVTR_03.png")
            self.oHelper.SetButton("OK")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()


        self.oHelper.SetButton("Filtro Rapido")
        self.oHelper.SetValue("Campos:","Matricula")
        self.oHelper.SetValue("Expressäo:","222557")
        self.oHelper.Screenshot("roteiroVTR_03.png")
        self.oHelper.SetButton("Adiciona")
        sleep(1)
        self.oHelper.SetButton("OK")
        sleep(1)


        self.oHelper.SetButton("Calcular")
        self.oHelper.Screenshot("roteiroVTR_04.png")
        
        
        if self.oHelper.IfExists("Confirma configuracäo dos parametros?"):
            self.oHelper.Screenshot("roteiroVTR_05.png")
            self.oHelper.SetButton("Sim")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        if self.oHelper.IfExists("Nenhum filtro foi selecionado! Processar toda a tabela?"):
            self.oHelper.Screenshot("roteiroVTR_06.png")
            self.oHelper.SetButton("Sim")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        sleep(30) 
        
        self.oHelper.Screenshot("roteiroVTR_07.png")
        sleep(30)
        self.oHelper.Screenshot("roteiroVTR_08.png")
        sleep(30)
        
        self.oHelper.WaitShow("Log de Ocorrencias no Processo de Calculo") 
        
        if self.oHelper.IfExists("Log de Ocorrencias no Processo de Calculo"):
            self.oHelper.ClickLabel("Em Disco")
            self.oHelper.Screenshot("roteiroVTR_09.png")
            self.oHelper.SetButton("OK")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        sleep(25)
        self.oHelper.Screenshot("roteiroVTR_10.png")
    
        self.oHelper.SetButton("Sair")
        sleep(10) """
        
        #----------------------------------------------
        # GARANTE A INTEGRAÇÃO DO SISTEMA PARA CALCULAR FOLHA
        #-------------------------------------------------------
        
        #self.oHelper.SetLateralMenu("Miscelanea > Cálculos > Integrações") 
        
        """ self.oHelper.Screenshot("integração_01")
        
        sleep(2)
        self.oHelper.SetValue("Processo","00001")
        sleep(1)
        self.oHelper.SetButton("Outras Ações","Inverter Seleção")
        sleep(3)
        self.oHelper.SetButton('Integrar')
        
        
        
        if self.oHelper.IfExists("Integrações Com a Folha de Pagamento"):
            self.oHelper.Screenshot("ntegração_02")
            self.oHelper.SetButton('Executar') 
            self.oHelper.SetButton('Ok')
            sleep(100)
            self.oHelper.Screenshot('ntegração_03')
            sleep(100)
            self.oHelper.Screenshot('ntegração_04')
            sleep(100)
        else:
            self.oHelper.AssertTrue()
            
        self.oHelper.Screenshot('ntegração_05')

        sleep(20)
        self.oHelper.SetButton('x')
        self.oHelper.AssertTrue() """
        
        
        #-------------------------------------------
        # CALCULAR FOLHA PARA VALIDAR A INCLUSÃO DO VTR
        #--------------------------------------------
        
        
        self.oHelper.SetLateralMenu("Atualizações > Lançamentos > Por Funcionário ")
        sleep(10)
        self.oHelper.Screenshot("VTR/Calcular_folha_01")
        
        self.oHelper.SearchBrowse(self.filial + self.Matricula + self.Nome, key="Filial+matricula+Nome")
        sleep(1)
        self.oHelper.Screenshot("Calculo_folha_vtr_02")
        self.oHelper.SetButton("Alterar")
        sleep(1)
        self.oHelper.WaitShow("Lançamentos por Funcionário")
        self.oHelper.ScrollGrid(column="Cod Verba", match_value = self.Verba,         grid_number=1)
        self.oHelper.Screenshot("Calculo_folha_vtr_03")
        self.oHelper.LoadGrid()
        self.oHelper.SetKey("F6")
        sleep(30)
        self.oHelper.Screenshot("Calculo_folha_vtr_04")
        self.oHelper.SetButton('OK')
        sleep(5)
        self.oHelper.SetKey("F7")
        sleep(5)
        self.oHelper.ScrollGrid(column="Codigo Verba", match_value = self.Verba,         grid_number=1)
        self.oHelper.Screenshot("Calculo_folha_vtr_05")
        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Confirmar')
        sleep(5)
        self.oHelper.SetButton('Salvar')
        sleep(1)
        self.oHelper.AssertTrue()
        
        
        
        
        
        
        
        
       
        

        self.oHelper.AssertTrue()
        print("------------------------------------------------")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_teste")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEM020_VTR('test_teste'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
