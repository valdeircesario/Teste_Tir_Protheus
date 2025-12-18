from tir import Webapp
from os import getcwd
import unittest
from datetime import datetime, timedelta
from time import sleep

DateSystem = datetime.today().strftime('%d/%m/%Y')

#---------------------------------------------------
# ADICIONANDO SOLICITAÇÃO DE VIAGEM, PARA ENVIAR PARA APROVAÇÃO
#---------------------------------------------------

# .\venv\Scripts\python.exe -m pytest tests/test_PXFINA11_01.py -s

class PXFINA11_01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.filial = '02DF0001'
        cls.Descrição = 'TESTE AUTOMATIZADO'
        cls.UTA = '000000677'
        cls.ValorPrev = '4500'
        cls.ValorReal = '5500'
        cls.Motivo = 'USO PARA TESTE AUTOMATIZADO'
        cls.Tipo = '1 - Servico'
        cls.Favorecido = '227884'
        cls.dataref_inicio = (datetime.today()+timedelta(days=5)).strftime("%d/%m/%Y")
        cls.dataref_fim = (datetime.today()+timedelta(days=10)).strftime("%d/%m/%Y")  
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', DateSystem, '02', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Atualizações > Gestao de Viagens > Solicitações")

    def test_Cadastro_Orcamento_Viagem(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        self.oHelper.WaitShow("Solicitação de Viagens/Treinamento")
        
        #------------------------
        # CRIA UMA NOVA SOLICITAÇÃO PARA ENVIAR PARA APROVAÇÃO
        #------------------------
        self.oHelper.SetButton("Incluir")
        sleep(0.2)
        self.oHelper.SearchBrowse(self.filial)
        self.oHelper.SetButton("OK")
        sleep(0.2)
        
        
        self.oHelper.WaitShow("Solicitacoes de Viagens - INCLUIR")
        
        #----------
        # Capturar o código da solicitação gerado automaticamente
        #----------
        
        self.codigo_solicitacao = self.oHelper.GetValue("Codigo")
        print(f"Código da solicitação criada: {self.codigo_solicitacao}")
        #----------
        
        self.oHelper.SetValue("ZV3_DESCRI", self.Descrição)
        self.oHelper.SetValue("ZV3_DTINI", self.dataref_inicio)
        self.oHelper.SetValue("ZV3_DTFIM", self.dataref_fim)
        
        sleep(1) 

        self.oHelper.SetValue("ZV3_CC", self.UTA)
        self.oHelper.SetValue("ZV3_TIPO", self.Tipo)  
        self.oHelper.SetValue("ZV3_OBS","TESTE DE SOLICITAÇÃO DE VIAGEM", check_value =False)
        self.oHelper.SetKey("TAB", grid=True) 
        
        
          
        self.oHelper.SetValue('Favorecido',  '227884',    grid=True,     grid_number=1)
        self.oHelper.LoadGrid()
        
        
        self.oHelper.ClickFolder("Transporte")
        
        self.oHelper.SetValue("Tipo","1 - Aereo", grid=True, grid_number=1, check_value=False)
        self.oHelper.SetKey("TAB", grid=True) 
        self.oHelper.SetValue("Partida", self.dataref_inicio, grid=True, grid_number=1, check_value=False)
        self.oHelper.SetKey("TAB", grid=True)
        self.oHelper.SetValue("Hora Partida", "08:00", grid=True, grid_number=1, check_value=False)
        self.oHelper.SetKey("TAB", grid=True)
        self.oHelper.SetValue("Origem", "DF00108", grid=True, grid_number=1, check_value=False)
        self.oHelper.SetKey("TAB", grid=True)
        self.oHelper.SetValue("Destino", "GO08707", grid=True, grid_number=1, check_value=False)
        self.oHelper.SetKey("TAB", grid=True)
        self.oHelper.SetValue("Chegada", self.dataref_inicio, grid=True, grid_number=1, check_value=False)
        self.oHelper.SetKey("TAB", grid=True)
        self.oHelper.SetValue("Hora Chegada", "12:00", grid=True, grid_number=1, check_value=False)
        self.oHelper.LoadGrid()
        sleep(0.5)
        
        
        
    
        self.oHelper.SetButton("Confirmar")
        
        if self.oHelper.IfExists("Valores de treinamento e/ou servico ultrapassam o limite orcado-Atenção-PXFINA11X"):
            self.oHelper.CheckResult('Valor do orçamento', 'R$ 0,00')
            self.oHelper.SetButton('Fechar')
        
        if self.oHelper.IfExists("Help: FWMODELPOS"):
            self.oHelper.WaitShow('Problema: Modelo invalido')
            self.oHelper.SetButton('Fechar')
            
        if self.oHelper.IfExists("Registro inserido com sucesso."):
            self.oHelper.SetButton('Fechar')
       
        self.oHelper.WaitShow("Solicitação de Viagens/Treinamento") 
        
        sleep(0.5)
        
        #self.oHelper.SearchBrowse(self.filial+self.codigo_solicitacao)
        
        #-------------------
        # ENVIO PARA APROVAÇÃO
        #-------------------   
        
        self.oHelper.SetButton("Outras Ações","Env. p/ Aprovação")
        sleep(0.9)
        
        
        if self.oHelper.IfExists("ZA1MAIL"):
            
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
            
        if self.oHelper.IfExists("ZA1MAIL"):
            
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        
        if self.oHelper.IfExists("MTALCDOC"):
            self.oHelper.WaitShow("Aprovação enviada com sucesso!")
            self.oHelper.SetButton('Fechar')
             
        self.oHelper.AssertTrue()
        

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(PXFINA11_01('test_Envio_Solicitacao_Viagem_para_Aprovacao'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)