import sys

from tir.technologies.core.base import By
from tir import Webapp
from pytest import mark
import unittest
from time import sleep
from os import getcwd,path
# Garante a importação dos módulos da pasta utilis
PROJECT_ROOT = path.abspath(path.join(path.dirname(__file__), '..', '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
from time import sleep

from tir import Webapp
from utilis.md_reporter import TirReportAgent
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')


#------------------------
# LANÇAMENTO DE AUSENCIAS 
#------------------------

class GPEA240_01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.filial = '01'
        cls.matricula = "000007"
        cls.nome = "FERNANDA RIBEIRO PASSOS"
        cls.CodigoAusen ='018'
        cls.dataref = "21012026"# deve ajusta para data periodo em aberto
        cls.dataIncio = "22012026" 
        cls.dataFim = "28012026"
        

        configfile = getcwd() + '\\config.json'
        # 1. Instância base do TIR
        webapp_base = Webapp(configfile)
                
        # 2. Encapsula com o Agente de Relatório
        cls.oHelper = TirReportAgent(
            tir_instance=webapp_base,
            cod_modulo="07",
            nome_modulo="Gestão de Pessoal",
            ct_nome="test_GPEA240_01",
            descricao="Inclusão , Visualização e Exclusão de uma Ausencia"
        )
        cls.oHelper.Setup('SIGAMDI', cls.dataref, '99', cls.filial, '07')  
        cls.oHelper.SetLateralMenu("Atualizações > Lançamentos > Ausências")
        cls.oHelper.SetButton('Confirmar')
        
       
    def test_Cadastro_de_ausencia(self):

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
            
        if self.oHelper.IfExists("Cadastro de Ausencias"):
            self.oHelper.Screenshot("Ausencia/001")
            self.oHelper.SetButton('OK')
      
        try:   
            sleep(1)
            self.oHelper.WaitShow("Cadastro de Ausencias")
            self.oHelper.Screenshot("Ausencia/002")  
            self.oHelper.SearchBrowse(self.matricula, column="Matricula*") # Pesquisa Matricula
            self.oHelper.Screenshot("Ausencia/003")
            
            #-------------------
            # INCLUIR AUSENCIA
            #-------------------
            
            print('--------------------------Incluir')
            self.oHelper.SetButton('Manutenção')
            self.oHelper.WaitShow("Cadastro de Ausencias - MANUTENÇÃO")
            self.oHelper.Screenshot("Ausencia/004") 

            nomeFun = self.oHelper.GetValue('Nome') 
            self.oHelper.SetValue('Cód. Ausenc',  self.CodigoAusen,     grid= True, check_value=False)
            self.oHelper.SetValue('Dt.Afastam.',  self.dataref,         grid= True, check_value=False)
            self.oHelper.SetValue('Dt.Fim Afas.',  self.dataFim,        grid= True, check_value=False)
            self.oHelper.SetValue('Inf. Compl.', "TESTE AUT LICENÇA",   grid= True, check_value=False)
            self.oHelper.LoadGrid()
            self.oHelper.Screenshot("Ausencia/005")
            self.oHelper.SetButton("Confirmar")
            sleep(1)

            print('--------------------------Confirmação')
            if self.oHelper.IfExists("Atenção"):
                self.oHelper.WaitShow('Sequência 002:')
                self.oHelper.SetButton('OK')
        
                
                
            self.oHelper.WaitShow('Registro alterado com sucesso.')
            self.oHelper.Screenshot("Ausencia/006")
            self.oHelper.SetButton('Fechar')     
            self.oHelper.WaitShow("Cadastro de Ausencias")
            self.oHelper.Screenshot("Ausencia/007")

            #-------------------
            # VISUALIZAR AUSENCIA
            #-------------------
        
            print('--------------------------Visualizar')
            self.oHelper.SetButton("Visualizar")
            self.oHelper.WaitShow("Cadastro de Ausencias - VISUALIZAR")
            self.oHelper.CheckResult('Nome',nomeFun)
            self.oHelper.ScrollGrid(column="Cód. Ausenc", match_value= self.CodigoAusen,          grid_number=1)
            self.oHelper.Screenshot("Ausencia/008") 
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Cadastro de Ausencias")
            
            #------------------------
            # EXCLUIR AUSENCIA
            #------------------------
            print('--------------------------Excluir')
            self.oHelper.SetButton("Manutenção")
            self.oHelper.CheckResult('Nome',nomeFun)
            self.oHelper.ScrollGrid(column="Cód. Ausenc", match_value= self.CodigoAusen,          grid_number=1)
            self.oHelper.SetKey("DELETE", grid=True, grid_number=1)
            self.oHelper.Screenshot("Ausencia/009")
            self.oHelper.SetButton("Confirmar")
            print('--------------------------Confirmação')
            sleep(1)
            
            if self.oHelper.IfExists("Atenção"):
                self.oHelper.SetButton('OK')
                        
                
            self.oHelper.IfExists("Registro alterado com sucesso.")
            self.oHelper.Screenshot("Ausencia/010")
            self.oHelper.SetButton('Fechar')
                
            self.oHelper.WaitShow("Cadastro de Ausencias")
            self.oHelper.Screenshot("Ausencia/011")
            self.oHelper.AssertTrue()

        except Exception as e:
            self.oHelper.registrar_erro(e)
            raise e
        finally:
            self.oHelper.salvar_relatorio()
        
        print("/")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_Cadastro_de_ausencia")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA240_01('test_Cadastro_de_ausencia'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
