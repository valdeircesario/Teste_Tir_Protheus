from tir import Webapp
from os import getcwd
import unittest
from datetime import datetime, timedelta
from time import sleep

DateSystem = datetime.today().strftime('%d/%m/%Y')

#---------------------------------------------------
# ADICIONANDO APROVADOR PARA SOLICITAÇÃO DE VIAGEM
#---------------------------------------------------

#cd Testes-Protheus; & .\venv\Scripts\Activate.ps1; pytest TESTS/SIGAGPE/MATA095/test_MATA095.py

class MATA095(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.filial = '02DF0001'
        cls.Usuario = '001016'
        cls.Aprovador = '000005'
        cls.Limite = '9999999'
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', DateSystem, '02', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Atualizações > Gestao de Viagens > Controle de Alcada (5) > Aprovadores")

    def test_Cadastro_Orcamento_Viagem_CRUD(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        self.oHelper.WaitShow("Cadastro de Aprovadores")
        self.oHelper.Screenshot("MATA095_01.png")
        
        #------------------------
        # INCLUIR APROVADOR
        #------------------------
        self.oHelper.SetButton("Incluir")
        sleep(0.2)
        self.oHelper.WaitShow("Aprovadores - INCLUIR")
        self.oHelper.Screenshot("MATA095_02.png")
        
        self.oHelper.SetValue("AK_USER", self.Usuario,check_value=False)
        self.oHelper.SetValue("AK_APROSUP", self.Aprovador,check_value=False)
        self.oHelper.SetValue("AK_MOEDA","1",check_value=False)
        self.oHelper.SetValue("AK_LIMITE",self.Limite,check_value=False)
        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Registro inserido com sucesso.")
        self.oHelper.Screenshot("MATA095_03.png")
        self.oHelper.SetButton("Fechar")
        sleep(0.9)
        
        self.oHelper.WaitShow("Cadastro de Aprovadores")
        self.oHelper.Screenshot("MATA095_04.png")
        
        #-------------------
        # VISUALIZAR APROVADOR 
        #-------------------
        
        self.oHelper.SetButton("Visualizar")
        sleep(0.9)
        self.oHelper.WaitShow("Aprovadores - VISUALIZAR")
        self.oHelper.Screenshot("MATA095_05.png")
        self.oHelper.CheckResult("AK_USER",self.Usuario)
        self.oHelper.CheckResult("AK_APROSUP",self.Aprovador)
        self.oHelper.SetButton("Fechar")
        sleep(0.9)
        self.oHelper.WaitShow("Cadastro de Aprovadores")
        self.oHelper.Screenshot("MATA095_06.png")
        
        #-------------------
        # EDITAR APROVADOR
        #-------------------
        
        self.oHelper.SetButton("Alterar")
        sleep(0.9)
        self.oHelper.WaitShow("Aprovadores - ALTERAR") 
        self.oHelper.SetValue("AK_LIMITE",'8888888',check_value=False)
        self.oHelper.Screenshot("MATA095_07.png")
        self.oHelper.SetButton("Confirmar")
        
        if self.oHelper.IfExists("Atencao!"):
            self.oHelper.Screenshot("MATA095_08.png")
            self.oHelper.WaitShow("O limite do aprovador foi alterado.")
            self.oHelper.SetButton("Confirma")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
            
        self.oHelper.WaitShow("Registro alterado com sucesso.")
        self.oHelper.Screenshot("MATA095_09.png")
        self.oHelper.SetButton("Fechar")
        sleep(0.9)
        self.oHelper.WaitShow("Cadastro de Aprovadores")
        self.oHelper.Screenshot("MATA095_10.png")
        
        #-------------------
        # EXCLUIR APROVADOR
        #-------------------
        self.oHelper.SetButton("Outras Ações","Excluir")
        sleep(0.9)
        self.oHelper.WaitShow("Tem certeza que deseja excluir o item abaixo?")
        self.oHelper.Screenshot("MATA095_11.png")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Registro excluído com sucesso.")
        self.oHelper.Screenshot("MATA095_12.png")
        self.oHelper.SetButton("Fechar")
        sleep(0.9)
        self.oHelper.WaitShow("Cadastro de Aprovadores") 
             
        self.oHelper.AssertTrue()
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_cadastro_de_aprovadores_de_viagem_CRUD")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MATA095('test_Cadastro_de_aprovadores_Viagem_CRUD'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)