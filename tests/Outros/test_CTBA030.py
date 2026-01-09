from tir.technologies.core.base import By
from tir import Webapp
from pytest import mark
import unittest
from time import sleep
from os import getcwd
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')

# cd Testes-Protheus; & .\venv\Scripts\Activate.ps1; pytest TESTS/SIGAGPE/CTBA030/test_CTBA030.py

#------------------------
# CADASTRO CENTRO DE CUSTO 
#------------------------

class CTBA030(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.filial = '02DF0001'
        self.CentroCustoEdit = '00088888'
        self.DescricaoEdit = 'TESTE ALTERADO'
        self.CentroCusto = '00099999'
        self.custoAD = 'TESTE AUTOMATIZADO 01'
        self.custoADEdit = 'TESTE AUTOMATIZADO 01 EDITADO'
        self.Decricao = 'DESCRICAO TESTE AUTOMATIZADO 01'
        self.supervisor = '000000677'
        
        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', DateSystem, '02', self.filial, '07')
        
        self.oHelper.SetLateralMenu("Atualizações > Cadastros (23) > Centro de Custos")
        
       
    def test_cadastro_Centro_de_Custo(self):

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
              
        self.oHelper.WaitShow("Cadastro UTA")
        self.oHelper.Screenshot("CTBA030_01.png")
        self.oHelper.SetButton("Incluir")
        sleep(0.5)  
        self.oHelper.WaitShow("Cadastro UTA - INCLUIR")
        self.oHelper.Screenshot("CTBA030_02.png")
        self.oHelper.SetValue("CTT_CUSTO",      self.CentroCusto,       check_value=False)
        self.oHelper.SetKey("TAB")
        self.oHelper.SetValue("CTT_XDESC",      self.custoAD,           check_value=False)
        self.oHelper.SetKey("TAB")
        self.oHelper.SetValue("CTT_DESC01",     self.Decricao,          check_value=False)
        self.oHelper.SetKey("TAB")
        self.oHelper.SetValue("CTT_NORMAL",'0 - Nenhum',                check_value=False)
        self.oHelper.SetKey("TAB")
        sleep(0.5)
        
        self.oHelper.SetButton("Salvar")
        sleep(5)  
        if self.oHelper.IfExists("Atenção!"):
            self.oHelper.Screenshot("CTBA030_03.png")
            self.oHelper.SetButton("OK")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
        
        
        self.oHelper.SetButton("Cancelar")
        self.oHelper.Screenshot("CTBA030_04.png")
        sleep(2)
        self.oHelper.WaitShow("Cadastro UTA")
        self.oHelper.Screenshot("CTBA030_05.png")
        self.oHelper.SetButton("Visualizar")
        sleep(0.5)
        
        #-------------------------
        # VISUALIZAR CENTRO DE CUSTO
        #-------------------------
        
        self.oHelper.WaitShow("Centro de Custo - VISUALIZAR")
        self.oHelper.Screenshot("CTBA030_06.png")
        self.oHelper.CheckResult("CTT_CUSTO",self.CentroCusto)
        self.oHelper.CheckResult("CTT_XDESC",self.custoAD)
        self.oHelper.CheckResult("CTT_DESC01",self.Decricao)
        self.oHelper.SetButton("Fechar")
        sleep(2)
        self.oHelper.WaitShow("Cadastro UTA")
        #-------------------------
        # EDITAR CENTRO DE CUSTO
        #-------------------------
        
        self.oHelper.SetButton("Alterar")
        sleep(0.5)
        self.oHelper.WaitShow("Cadastro UTA - INCLUIR")
        self.oHelper.SetValue("CTT_XDESC",self.custoADEdit,     check_value=False)
        self.oHelper.SetKey("TAB")
        self.oHelper.SetValue("CTT_DESC01",self.DescricaoEdit,  check_value=False)
        self.oHelper.SetKey("TAB")
        self.oHelper.Screenshot("CTBA030_07.png")
        self.oHelper.SetButton("Salvar")
        sleep(5)
        self.oHelper.Screenshot("CTBA030_08.png")
        
        #------------------------
        # EXCLUIR CENTRO DE CUSTO
        #------------------------
        
        self.oHelper.SetButton("Outras Ações","Excluir")
        sleep(0.5)
        self.oHelper.Screenshot("CTBA030_09.png")
        self.oHelper.SetButton("Confirmar")
        
        if self.oHelper.IfExists("Atenção!"):
            self.oHelper.Screenshot("CTBA030_10.png")#SIGAGPE
            self.oHelper.SetButton("OK")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
     
        self.oHelper.AssertTrue()
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_CRUD_de_centro_custo")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CTBA030('test_cadastro_Centro_de_Custo'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
