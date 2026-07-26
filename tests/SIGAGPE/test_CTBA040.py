from tir.technologies.core.base import By
from tir import Webapp
from pytest import mark
import unittest
from time import sleep
from os import getcwd
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')

# cd Testes-Protheus; & .\venv\Scripts\Activate.ps1; pytest TESTS/SIGAGPE/CTBA040/test_CTBA030.py

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
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '07')
        
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros (23) > Item Contábil")
        
       
    def test_cadastro_de_item_contabil_CRUD(self):

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
              
        self.oHelper.WaitShow("Cadastro Item Conta")
        self.oHelper.Screenshot("CTBA040_01.png")

        #-------------------------
        # Incluir Item Contabil
        #-------------------------


        self.oHelper.SetButton("Incluir")

        print('------------------------Incluir')
        self.oHelper.WaitShow("Cadastro Item Conta - INCLUIR")
        self.oHelper.Screenshot("CTBA040_02.png")
        self.oHelper.SetValue("CTD_ITEM",           self.Codigo,    check_value=False)
        self.oHelper.SetValue("CTD_DESC01",         self.Descricao, check_value=False)
        self.oHelper.Screenshot("CTBA040_03.png")   
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.WaitShow("Cadastro Item Conta")
        self.oHelper.Screenshot("CTBA040_04.png")
        
        
        #------------------------------
        # VISUALIZAR ITEM CONTABIL
        #----------------------------
        print('--------------------Visualizar')
        self.oHelper.SetButton("Visualizar")
        self.oHelper.WaitShow('Cadastro Item Conta - VISUALIZAR')
        self.oHelper.Screenshot("CTBA040_05.png")  
        self.oHelper.CheckResult("CTD_ITEM",    self.Codigo)
        self.oHelper.CheckResult("CTD_DESC01",  self.Descricao)
        self.oHelper.SetButton("Confirmar")
        
        #----------------------
        # EDITAR ITEM CONTABIL
        #-----------------------
        print('------------------------Alterar')
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow("Cadastro Item Conta - ALTERAR")
        self.oHelper.Screenshot("CTBA040_06.png")
        self.oHelper.SetValue("CTD_DESC01",self.DescricaoEdit,      check_value=False)
        self.oHelper.Screenshot("CTBA040_07.png")
        self.oHelper.SetButton("Salvar")
        self.oHelper.Screenshot("CTBA040_08.png")
        
        #-------------------------
        # BLOQUEAR ITEM CONTABIL
        #-------------------------
        print('--------------------Bloquear item')
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow("Cadastro Item Conta - ALTERAR")
        self.oHelper.Screenshot("CTBA040_09.png")
        self.oHelper.SetValue("CTD_BLOQ","1 - Bloqueado",           check_value=False)
        self.oHelper.Screenshot("CTBA040_10.png")
        self.oHelper.SetButton("Salvar")
        self.oHelper.Screenshot("CTBA040_11.png")
        
        #-----------------------
        # EXCLUIR ITEM CONTABIL
        #-----------------------

        print('--------------------Excluir')
        self.oHelper.SetButton("Outras Ações","Excluir")
        self.oHelper.WaitShow("Cadastro Item Conta - EXCLUIR")
        self.oHelper.Screenshot("CTBA040_12.png")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.Screenshot("CTBA040_13.png")
     
        self.oHelper.AssertTrue()
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
