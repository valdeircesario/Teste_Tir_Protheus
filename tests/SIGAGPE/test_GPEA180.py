from tir import Webapp
from pytest import mark
import unittest
import os
from os import getcwd,path
from datetime import date
from datetime import datetime, timedelta
from time import sleep

import sys
# Garante a importação dos módulos da pasta utilis
PROJECT_ROOT = path.abspath(path.join(path.dirname(__file__), '..', '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
from time import sleep

from tir import Webapp
from utilis.md_reporter import TirReportAgent

from utilis.click_pageview import click_pageview_visible_button
DateSystem = datetime.today().strftime('%d/%m/%Y')


# TRANSFERENCIA FUNCIONÁRIO ENTRE CENTRO DE CUSTO DIFERENTE

class GPEA180(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.filial = "01"
        cls.mat = "000014"
        cls.CC_destino = "009"
        cls.DP_destino = "000000006" 
        cls.Periodo = "25012026"
    
        configfile = getcwd() + '\\config.json'
            # 1. Instância base do TIR
        webapp_base = Webapp(configfile)
        # 2. Encapsula com o Agente de Relatório
        cls.oHelper = TirReportAgent(
            tir_instance=webapp_base,
            cod_modulo="07",
            nome_modulo="Gestão de Pessoal",
            ct_nome="test_GPEA180",
            descricao="Transferencia de funcionario departamento"
        )
        cls.oHelper.Setup('SIGAMDI',cls.Periodo, '99', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Atualizações > Funcionários > Transferências")
        cls.oHelper.SetButton('Confirmar')
        

    def test_transferencia_funcionario(self):
        sleep(5)
        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')
     
        sleep(2)
        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')
       


        try:
            
            #--------------------------
            # Tranferencia
            #----------------------------------
            
            print('----------------------Pesquisando funcionario')  
            self.oHelper.WaitShow("Transferências")
            self.oHelper.Screenshot("Transferencia/001")
            self.oHelper.SetButton("Pesquisar")
            self.oHelper.SetButton("Parâmetros")
            self.oHelper.SetValue("Matricula", self.mat)
            self.oHelper.SetButton("Ok")
            self.oHelper.Screenshot("Transferencia/002")
            self.oHelper.SetButton('Outras Ações', 'Transferir')

            self.oHelper.WaitShow('Haverá transferência de Matricula?')
            self.oHelper.ClickLabel("Sim")
            self.oHelper.ClickLabel("Não")
            self.oHelper.Screenshot("Transferencia/003")
            self.oHelper.SetButton("Ok")
        

            print('----------------------------Tranferindo')
            self.oHelper.WaitShow('Transferências - TRANSFERIR')

            self.oHelper.SetValue('Data de Referencia :','28012026')
            self.oHelper.Screenshot("Transferencia/004")
            self.oHelper.ClickBox("Matricula", self.mat,   grid_number=1)
            self.oHelper.Screenshot("Transferencia/005")
            self.oHelper.SetButton('Confirmar')
            
            self.oHelper.WaitShow('Transferências - TRANSFERIR')
            self.oHelper.Screenshot("Transferencia/006")
            
            self.oHelper.SetValue("Centro Custo", self.CC_destino,      grid=True, grid_number=2)
            self.oHelper.SetValue("RA_DEPTO", self.DP_destino,          grid=True, grid_number=2)
            self.oHelper.LoadGrid()
            self.oHelper.Screenshot("Transferencia/007")
            self.oHelper.SetButton('Confirmar')

            sleep(2)
            if self.oHelper.IfExists("Departamento possui centro de custo diferente do centro de custos do funcionário"):
                self.oHelper.Screenshot("Transferencia/008")
                self.oHelper.SetButton('Fechar')

            sleep(2)
            if self.oHelper.IfExists("Departamento possui centro de custo diferente do centro de custos do funcionário"):
                self.oHelper.SetButton('Fechar')

            print('-----------------Confirmando transferencia')
            self.oHelper.WaitShow("Confirma a Transferência ?")
            self.oHelper.Screenshot("Transferencia/009")
            self.oHelper.SetButton('Sim')
                

                
            print('--------------------------Conferindo os logs')
            self.oHelper.WaitShow("Log de Ocorrencias - Gestão de Pessoal - Versao 12")
            self.oHelper.ClickLabel("Via Spool")
            self.oHelper.ClickLabel("Em Disco")
            self.oHelper.Screenshot("Transferencia/010")
            self.oHelper.SetButton("OK")
            self.oHelper.Screenshot("tranferencias_01_09.png")
            sleep(8)

            self.oHelper.Screenshot("Transferencia/011")
            self.oHelper.SetButton("Sair")
            sleep(5)
            self.oHelper.SetButton("Cancelar")
            self.oHelper.WaitShow("Transferências")

            self.oHelper.AssertTrue()
        except Exception as e:
            self.oHelper.registrar_erro(e)
            raise e
        finally:
            self.oHelper.salvar_relatorio()
        
        print("------------------------------------------------")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_transferencia_funcionario")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
    

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA180('test_transferencia_funcionario'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
