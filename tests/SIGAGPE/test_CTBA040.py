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
    def setUpClass(self):
        self.filial = '02DF0001'
        self.Codigo = '111001'
        self.Descricao = 'TESTE ITEM CONTABIL'
        self.DescricaoEdit = 'TESTE ITEM CONTABIL ALTERADO'
        
        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', DateSystem, '02', self.filial, '07')
        
        self.oHelper.SetLateralMenu("Atualizações > Cadastros (23) > Item Contábil")
        
       
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
        self.oHelper.SetButton("Incluir")
        sleep(0.5)  
        self.oHelper.WaitShow("Cadastro Item Conta - INCLUIR")
        self.oHelper.Screenshot("CTBA040_02.png")
        self.oHelper.SetValue("CTD_ITEM",           self.Codigo)
        self.oHelper.SetValue("CTD_DESC01",         self.Descricao)
        sleep(0.5)
        self.oHelper.Screenshot("CTBA040_03.png")   
        self.oHelper.SetButton("Salvar")
        sleep(5)
        self.oHelper.SetButton("Cancelar")
        sleep(0.5)
        self.oHelper.WaitShow("Cadastro Item Conta")
        self.oHelper.Screenshot("CTBA040_04.png")
        
        
        #------------------------------
        # VISUALIZAR ITEM CONTABIL
        #----------------------------
        
        self.oHelper.SetButton("Visualizar")
        sleep(0.5)
        self.oHelper.WaitShow('Cadastro Item Conta - VISUALIZAR')
        self.oHelper.Screenshot("CTBA040_05.png")
        
        self.oHelper.CheckResult("CTD_ITEM",    self.Codigo)
        self.oHelper.CheckResult("CTD_DESC01",  self.Descricao)
        self.oHelper.SetButton("Confirmar")
        
        #----------------------
        # EDITAR ITEM CONTABIL
        #-----------------------
        
        self.oHelper.SetButton("Alterar")
        sleep(0.5)
        self.oHelper.WaitShow("Cadastro Item Conta - ALTERAR")
        self.oHelper.Screenshot("CTBA040_06.png")
        self.oHelper.SetValue("CTD_DESC01",self.DescricaoEdit)
        self.oHelper.Screenshot("CTBA040_07.png")
        self.oHelper.SetButton("Salvar")
        sleep(5)
        self.oHelper.Screenshot("CTBA040_08.png")
        
        #-------------------------
        # BLOQUEAR ITEM CONTABIL
        #-------------------------
        
        self.oHelper.SetButton("Alterar")
        sleep(0.5)
        self.oHelper.WaitShow("Cadastro Item Conta - ALTERAR")
        self.oHelper.Screenshot("CTBA040_09.png")
        self.oHelper.SetValue("CTD_BLOQ","1 - Bloqueado")
        self.oHelper.Screenshot("CTBA040_10.png")
        self.oHelper.SetButton("Salvar")
        sleep(5)
        self.oHelper.Screenshot("CTBA040_11.png")
        
        #-----------------------
        # EXCLUIR ITEM CONTABIL
        #-----------------------
        
        self.oHelper.SetButton("Outras Ações","Excluir")
        sleep(0.5)
        self.oHelper.WaitShow("Cadastro Item Conta - EXCLUIR")
        self.oHelper.Screenshot("CTBA040_12.png")
        self.oHelper.SetButton("Confirmar")
        sleep(0.5)
        self.oHelper.Screenshot("CTBA040_13.png")
     
        self.oHelper.AssertTrue()
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_cadastro_de_item_contabil_CRUD")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CTBA040('test_cadastro_de_item_contabil_CRUD'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
