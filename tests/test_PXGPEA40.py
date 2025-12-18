from tir import Webapp
from os import getcwd
import unittest
from datetime import datetime
from time import sleep

DateSystem = datetime.today().strftime('%d/%m/%Y')

#---------------------------------------------------
# ADICIONANDO ORCAMENTO DE VIAGEM POR UTA
#---------------------------------------------------

# .\venv\Scripts\python.exe -m pytest tests/test_PXGPEA40.py -s

class PXGPEA40(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.filial = '02DF0001'
        cls.Ano = '2025'
        cls.Valor = '15000'
        cls.Valor01 = '11000'
        cls.Motivo = 'USO PARA TESTE AUTOMATIZADO'
        cls.Motivo01 = 'USO PARA TESTE AUTOMATIZADO EDIÇÃO'
        cls.Tipo = '2 - Treinamento'
        cls.contabil = '817750000000001'
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', DateSystem, '02', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Atualizações > Gestao de Viagens > Cadastro (5) > Orcamento por UTA")

    def test_Cadastro_Orcamento_Viagem(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        self.oHelper.WaitShow("Centro de Custo vs Orçamento")
        
        #------------------------
        #INCLUIR
        #------------------------
        self.oHelper.SetButton("Incluir")
        self.oHelper.WaitShow("Modelo de Dados do Cadastro Centro de Custo vs Orçamento - INCLUIR")
        self.oHelper.SetValue("Z91_ANO", self.Ano)
        self.oHelper.SetValue("Z91_TIPO", self.Tipo) 
        self.oHelper.SetFocus("Z91_CONTAB")
        self.oHelper.SetValue("Z91_CONTAB", self.contabil)  
        self.oHelper.SetValue("Z91_CC","000000086", check_value =False)
        self.oHelper.SetKey("TAB", grid=True)   
        self.oHelper.SetFocus("Centro de Custo vs Valor")
        self.oHelper.WaitShow("Centro de Custo vs Valor")  
        self.oHelper.SetValue("Valor", self.Valor, grid=True, grid_number=1, check_value=False)
        self.oHelper.SetKey("TAB", grid=True)
        self.oHelper.SetValue("Motivo", self.Motivo, grid=True, grid_number=1)
        self.oHelper.SetKey("TAB", grid=True)     
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Registro inserido com sucesso.")
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Centro de Custo vs Orçamento")
        sleep(0.2)
            
        #------------------------
        # VISUALIZAR
        #------------------------
        
        self.oHelper.SetButton("Outras Ações","Visualizar")
        self.oHelper.WaitShow("odelo de Dados do Cadastro Centro de Custo vs Orçamento - VISUALIZAR")
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Centro de Custo vs Orçamento")
        sleep(0.2)  
        
        #------------------------
        # EDITAR
        #------------------------
        self.oHelper.SetButton("Alterar")  
        self.oHelper.SetValue("Valor", self.Valor01, grid=True, grid_number=1, check_value=False)
        self.oHelper.SetKey("TAB", grid=True)
        self.oHelper.SetValue("Motivo", self.Motivo01, grid=True, grid_number=1, check_value=False)
        self.oHelper.SetKey("TAB", grid=True)     
        self.oHelper.LoadGrid()  
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Registro alterado com sucesso.")
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Centro de Custo vs Orçamento")
        sleep(0.2) 
        
        #------------------------
        #  EXCLUIR
        #------------------------
        
        self.oHelper.SetButton("Outras Ações", "Excluir")
        self.oHelper.WaitShow("Tem certeza que deseja excluir o item abaixo?")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Registro excluído com sucesso.")
        self.oHelper.SetButton("Fechar")
       
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(PXGPEA40('test_Cadastro_Orcamento_Viagem'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)