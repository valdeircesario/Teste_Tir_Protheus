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

from tir import Webapp
from utilis.md_reporter import TirReportAgent
DateSystem = datetime.today().strftime('%d/%m/%Y')

# .\venv\Scripts\python.exe -m pytest tests/Outros/test_GPEA020.py -s

#------------------------
# CADAASTRO DE DEPENDENTES
#------------------------

class GPEA020(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.Matricula = '000016'
        cls.filial = '01'
        cls.Nome = 'TESTE DE DEPENDENTE 01'
        cls.Sexo = 'M'
        cls.Tipo = '03'
        cls.Grau = 'F - Filho'
        cls.TipoDep = '2 - Ate 21 Anos'
        cls.CPF = '808.350.540-47'
        cls.dataref = "26012026"
        cls.DataNasc = (datetime.today()-timedelta(days=360)).strftime("%d/%m/%Y")
        cls.DataEntrega = (datetime.today()-timedelta(days=20)).strftime("%d/%m/%Y")
        configfile = getcwd() + '\\config.json'
        # 1. Instância base do TIR
        webapp_base = Webapp(configfile)
        
        # 2. Encapsula com o Agente de Relatório
        cls.oHelper = TirReportAgent(
            tir_instance=webapp_base,
            cod_modulo="07",
            nome_modulo="Gestão de Pessoal",
            ct_nome="test_GPEA020",
            descricao="Inclusão e Visualização  de dependente"
        )
        cls.oHelper.Setup('SIGAMDI',"10012026", '99', cls.filial, '07')
        
        cls.oHelper.SetLateralMenu("Atualizações > Funcionários > Dependentes")
        cls.oHelper.SetButton('Confirmar')
        
    

    def test_Cadastro_de_dependentes(self):

        try:
            sleep(5)
            if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
                self.oHelper.SetButton('Fechar')
       
            sleep(2)
            if self.oHelper.IfExists("Moedas"):
                self.oHelper.CheckResult('Dolar', '0,0000')
                self.oHelper.SetButton('Confirmar')
        
                
            #----------------------------------
            # INCLUIR DEPENDENTES AO FUNCIONARIO
            #----------------------------------
            
            self.oHelper.WaitShow("Dependentes")
            self.oHelper.Screenshot("Dependente/001")   
            self.oHelper.SearchBrowse(self.Matricula, column="Matricula*")
            sleep(1)
            self.oHelper.Screenshot("Dependente/002")

            print('---------------------Incluir')   
            self.oHelper.SetButton("Manutenção") 
            self.oHelper.WaitShow("Funcionários - MANUTENÇÃO") 
            self.oHelper.Screenshot("Dependente/003")  
            self.oHelper.SetValue("Nome",         self.Nome,        grid=True, grid_number=1, check_value=False)
            self.oHelper.SetValue("Data Nasc.",   self.DataNasc,    grid=True, grid_number=1, check_value=False)
            self.oHelper.SetValue("Tp Dep.eSoci", self.Tipo,        grid=True, grid_number=1, check_value=False)
            self.oHelper.SetValue("Sexo",          self.Sexo,       grid=True, grid_number=1, check_value=False)
            self.oHelper.SetValue("Tp Dep.eSoci", self.Tipo,        grid=True, grid_number=1, check_value=False)
            self.oHelper.SetValue("Grau Parent.",   self.Grau,      grid=True, grid_number=1, check_value=False)
            self.oHelper.SetValue("Tipo Dep.IR",   self.TipoDep,    grid=True, grid_number=1, check_value=False)
            self.oHelper.SetValue("Tipo Dep. SF", "2",              grid=True, grid_number=1, check_value=False)
            self.oHelper.SetValue("Local Nasc.",   "BRASILIA",      grid=True, grid_number=1, check_value=False)
            self.oHelper.SetValue("Cartorio",      "DE REGISTRO",   grid=True, grid_number=1, check_value=False)
            self.oHelper.SetValue("No.Reg.Cart.",    "123",         grid=True, grid_number=1, check_value=False)
            self.oHelper.SetValue("No.Livro",      "130",           grid=True, grid_number=1, check_value=False)
            self.oHelper.SetValue("No.Folha",      "11",            grid=True, grid_number=1, check_value=False)
            self.oHelper.SetValue("Dt.Entrega",    self.dataref,    grid=True, grid_number=1, check_value=False)
            self.oHelper.SetValue("CPF",           self.CPF,        grid=True, grid_number=1, check_value=False)       
            self.oHelper.LoadGrid()
            self.oHelper.Screenshot("Dependente/004")
            self.oHelper.SetButton("Confirmar")  
            self.oHelper.WaitShow("Registro alterado com sucesso.")
            self.oHelper.Screenshot("Dependente/005")
            self.oHelper.SetButton("Fechar")         
            self.oHelper.WaitShow("Dependentes")

            #--------------------
            # VISUALIZAR
            #--------------------

            print('--------------------Visualizar')
            self.oHelper.SetButton("Visualizar")        
            self.oHelper.WaitShow("Funcionários - VISUALIZAR")
            self.oHelper.CheckResult('Matricula',self.Matricula)
            self.oHelper.Screenshot("Dependente/006")
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Dependentes")

        except Exception as e:
            self.oHelper.registrar_erro(e)
            raise e
        finally:
            self.oHelper.salvar_relatorio()
        
        print("/")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_inserção_de_dependentes")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA020('test_Cadastro_de_dependentes'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
