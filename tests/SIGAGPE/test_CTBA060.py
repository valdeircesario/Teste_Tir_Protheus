from tir.technologies.core.base import By
from tir import Webapp
from pytest import mark
import unittest
from time import sleep
from os import getcwd
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')

# cd Testes-Protheus; & .\venv\Scripts\Activate.ps1; pytest TESTS/SIGAGPE/CTBA060/test_CTBA030.py

#------------------------
# CADASTRO Classe de valor
#------------------------

class CTBA060(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.filial = '01'
        cls.Codigo = '111001'
        cls.Descricao = 'TESTE CL VALOR'
        cls.DescricaoEdit = 'TESTE CL VALOR ALTERADO'
        cls.supervisor = '000000677'
        
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '07')
        
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros (23) > Classe de Valor")
        
       
    def test_cadastro_de_classe_valor_CRUD(self):

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

        #--------------------------
        # Incluir classe de valor
        #--------------------------
              
        self.oHelper.WaitShow("Cadastro Cod Cl Val")
        self.oHelper.Screenshot("CTBA060_01.png")

        print('----------------------Incluir')
        self.oHelper.SetButton("Incluir")
        self.oHelper.WaitShow("Cadastro Cod Cl Val - INCLUIR")
        self.oHelper.Screenshot("CTBA060_02.png")
        self.oHelper.SetValue("CTH_CLVL",           self.Codigo,    check_value=False)
        self.oHelper.SetValue("CTH_DESC01",         self.Descricao, check_value=False)
        self.oHelper.Screenshot("CTBA060_03.png")   
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.WaitShow("Cadastro Cod Cl Val")
        self.oHelper.Screenshot("CTBA060_04.png")
        
        
        #------------------------------
        # VISUALIZAR INCLUSÃO
        #----------------------------


        print('----------------------Visualizar')
        self.oHelper.SetButton("Visualizar")
        self.oHelper.WaitShow('Cadastro Cod Cl Val - VISUALIZAR')
        self.oHelper.Screenshot("CTBA060_05.png")   
        self.oHelper.CheckResult("CTH_CLVL",    self.Codigo)
        self.oHelper.CheckResult("CTH_DESC01",  self.Descricao)
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Cadastro Cod Cl Val")
        
        #----------------------
        # EDITAR CLASSE DE VALOR
        #-----------------------
        print('--------------------Alterar')
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow("Cadastro Cod Cl Val - ALTERAR")
        self.oHelper.Screenshot("CTBA060_06.png")
        self.oHelper.SetValue("CTH_DESC01",self.DescricaoEdit,      check_value=False)
        self.oHelper.Screenshot("CTBA060_07.png")
        self.oHelper.SetButton("Salvar")
        self.oHelper.Screenshot("CTBA060_08.png")
        self.oHelper.WaitShow("Cadastro Cod Cl Val")
        
        #-------------------------
        # BLOQUEAR CLASSE VALOR
        #-------------------------
        print('------------------------Bloquear')
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow("Cadastro Cod Cl Val - ALTERAR")
        self.oHelper.Screenshot("CTBA060_09.png")
        self.oHelper.SetValue("CTH_BLOQ","1 - Bloqueado")
        self.oHelper.Screenshot("CTBA060_10.png")
        self.oHelper.SetButton("Salvar")
        self.oHelper.Screenshot("CTBA060_11.png")
        self.oHelper.WaitShow("Cadastro Cod Cl Val")
        
        #-----------------------
        # EXCLUIR CLASSE DE VALOR
        #-----------------------

        print('--------------------Excluir')
        self.oHelper.SetButton("Outras Ações","Excluir")
        self.oHelper.WaitShow("Cadastro Cod Cl Val - EXCLUIR")
        self.oHelper.Screenshot("CTBA030_12.png")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.Screenshot("CTBA030_13.png")
        self.oHelper.WaitShow("Cadastro Cod Cl Val")
     
        self.oHelper.AssertTrue()

        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_cadastro_de_classe_valor")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CTBA060('test_cadastro_de_classe_valor_CRUD'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
