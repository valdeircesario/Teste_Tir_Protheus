from tir import Webapp
from os import getcwd
import unittest
from datetime import datetime, timedelta
from time import sleep

DateSystem = datetime.today().strftime('%d/%m/%Y')

#---------------------------------------------------
# ADICIONANDO APROVADOR PARA SOLICITAÇÃO DE VIAGEM
#---------------------------------------------------

# .\venv\Scripts\python.exe -m pytest tests/test_PXFINA11_03.py -s

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

    def test_Cadastro_Orcamento_Viagem(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        self.oHelper.WaitShow("Cadastro de Aprovadores")
        
        #------------------------
        # INCLUIR APROVADOR
        #------------------------
        self.oHelper.SetButton("Incluir")
        sleep(0.2)
        self.oHelper.WaitShow("Aprovadores - INCLUIR")
        
        self.oHelper.SetValue("AK_USER", self.Usuario,check_value=False)
        self.oHelper.SetValue("AK_APROSUP", self.Aprovador,check_value=False)
        self.oHelper.SetValue("AK_MOEDA","1",check_value=False)
        self.oHelper.SetValue("AK_LIMITE",self.Limite,check_value=False)
        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Registro inserido com sucesso.")
        self.oHelper.SetButton("Fechar")
        sleep(0.9)
        
        self.oHelper.WaitShow("Cadastro de Aprovadores")
        
        #-------------------
        # VISUALIZAR APROVADOR 
        #-------------------
        
        self.oHelper.SetButton("Visualizar")
        sleep(0.9)
        self.oHelper.WaitShow("Aprovadores - VISUALIZAR")
        self.oHelper.CheckResult("AK_USER",self.Usuario)
        self.oHelper.CheckResult("AK_APROSUP",self.Aprovador)
        self.oHelper.SetButton("Fechar")
        sleep(0.9)
        self.oHelper.WaitShow("Cadastro de Aprovadores")
        
        #-------------------
        # EDITAR APROVADOR
        #-------------------
        
        self.oHelper.SetButton("Alterar")
        sleep(0.9)
        self.oHelper.WaitShow("Aprovadores - ALTERAR")
        self.oHelper.SetValue("AK_LIMITE",'8888888',check_value=False)
        self.oHelper.SetButton("Confirmar")
        
        if self.oHelper.IfExists("Atencao!"):
            self.oHelper.WaitShow("O limite do aprovador foi alterado.")
            self.oHelper.SetButton("Confirma")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
            
        self.oHelper.WaitShow("Registro alterado com sucesso.")
        self.oHelper.SetButton("Fechar")
        sleep(0.9)
        self.oHelper.WaitShow("Cadastro de Aprovadores")
        
        #-------------------
        # EXCLUIR APROVADOR
        #-------------------
        self.oHelper.SetButton("Outras Ações","Excluir")
        sleep(0.9)
        self.oHelper.WaitShow("Tem certeza que deseja excluir o item abaixo?")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Registro excluído com sucesso.")
        self.oHelper.SetButton("Fechar")
        sleep(0.9)
        self.oHelper.WaitShow("Cadastro de Aprovadores") 
             
        self.oHelper.AssertTrue()
        

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MATA095('test_Cadastro_de_aprovadores_Viagem'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)