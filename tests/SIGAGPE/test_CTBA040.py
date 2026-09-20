from datetime import datetime
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
DateSystem = datetime.today().strftime('%d/%m/%Y')


#------------------------
# CADASTRO ITEM CONTABIL
#------------------------

class CTBA040(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.filial = '01'
        cls.Codigo = '1110014'
        cls.Descricao = 'TESTE ITEM CONTABIL 01'
        cls.DescricaoEdit = 'TESTE ITEM CONTABIL ALTERADO'
        
        configfile = getcwd() + '\\config.json'
        # 1. Instância base do TIR
        webapp_base = Webapp(configfile)
                
        # 2. Encapsula com o Agente de Relatório
        cls.oHelper = TirReportAgent(
            tir_instance=webapp_base,
            cod_modulo="07",
            nome_modulo="Gestão de Pessoal",
            ct_nome="test_CTBA040",
            descricao="Inclusão, Visualização, Alteração  e exclusão de Item Contabil"
        )
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros (23) > Item Contábil")
        cls.oHelper.SetButton('Confirmar')
        
       
    def test_cadastro_de_item_contabil_CRUD(self):
        sleep(5)
        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')
          
        sleep(2)
        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')
         
        try:     
            self.oHelper.WaitShow("Cadastro Item Conta")
            self.oHelper.Screenshot("Item_Contabil/001")

            #-------------------------
            # Incluir Item Contabil
            #-------------------------


            self.oHelper.SetButton("Incluir")

            print('------------------------Incluir')
            self.oHelper.WaitShow("Cadastro Item Conta - INCLUIR")
            self.oHelper.Screenshot("Item_Contabil/002")
            self.oHelper.SetValue("CTD_ITEM",           self.Codigo,    check_value=False)
            self.oHelper.SetValue("CTD_DESC01",         self.Descricao, check_value=False)
            self.oHelper.Screenshot("Item_Contabil/003")   
            self.oHelper.SetButton("Salvar")
            self.oHelper.SetButton("Cancelar")
            self.oHelper.WaitShow("Cadastro Item Conta")
            self.oHelper.Screenshot("Item_Contabil/004")
            
            
            #------------------------------
            # VISUALIZAR ITEM CONTABIL
            #----------------------------

            print('--------------------Visualizar')
            self.oHelper.SetButton("Visualizar")
            self.oHelper.WaitShow('Cadastro Item Conta - VISUALIZAR')
            self.oHelper.CheckResult("CTD_ITEM",    self.Codigo)
            self.oHelper.CheckResult("CTD_DESC01",  self.Descricao)
            self.oHelper.Screenshot("Item_Contabil/005")
            self.oHelper.SetButton("Confirmar")
            
            #----------------------
            # EDITAR ITEM CONTABIL
            #-----------------------

            print('------------------------Alterar')
            self.oHelper.SetButton("Alterar")
            self.oHelper.WaitShow("Cadastro Item Conta - ALTERAR")
            self.oHelper.SetValue("CTD_DESC01",self.DescricaoEdit,      check_value=False)
            self.oHelper.Screenshot("Item_Contabil/006")
            self.oHelper.SetButton("Salvar")
            
            #-------------------------
            # BLOQUEAR ITEM CONTABIL
            #-------------------------

            print('--------------------Bloquear item')
            self.oHelper.SetButton("Alterar")
            self.oHelper.WaitShow("Cadastro Item Conta - ALTERAR")
            self.oHelper.Screenshot("Item_Contabil/008")
            self.oHelper.SetValue("CTD_BLOQ","1 - Bloqueado",           check_value=False)
            self.oHelper.SetButton("Salvar")
            self.oHelper.Screenshot("Item_Contabil/009")
            
            #-----------------------
            # EXCLUIR ITEM CONTABIL
            #-----------------------

            print('--------------------Excluir')
            self.oHelper.SetButton("Outras Ações","Excluir")
            self.oHelper.WaitShow("Cadastro Item Conta - EXCLUIR")
            self.oHelper.Screenshot("Item_Contabil/010")
            self.oHelper.SetButton("Confirmar")
            self.oHelper.Screenshot("Item_Contabil/011")
        
            self.oHelper.AssertTrue()

        except Exception as e:
            self.oHelper.registrar_erro(e)
            raise e
        finally:
            self.oHelper.salvar_relatorio()

        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_cadastro_de_item_contabil_CRUD")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CTBA040('test_cadastro_de_item_contabil_CRUD'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
