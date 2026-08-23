from tir import Webapp
from os import getcwd
import unittest
from datetime import datetime, timedelta
from time import sleep

DateSystem = datetime.today().strftime('%d/%m/%Y')

#---------------------------------------------------
# ADICIONANDO SOLICITAÇÃO DE VIAGEM POR UTA
# PARA FAZER UMA SOLICITAÇÃO DE VIAGEM É NECESSÁRIO TER ORÇAMENTO CADASTRADO NA UTA DO SOLICITANTE NO SISTEMA, NO PERIODO REFERENTE A VIAGEM.
#---------------------------------------------------

# 

class PXFINA11(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.filial = '01'
        cls.Descrição = 'USO PARA TESTE AUTOMATIZADO'
        cls.DescriçãoEdt = 'USO PARA TESTE AUTOMATIZADO EDIÇÃO'
        cls.UTA = '007'
        cls.ClasseValor = '0001.2'
        cls.ItemContabil = '0001'
        cls.ValorPrev = '450'
        cls.ValorReal = '500'
        cls.Motivo = 'USO PARA TESTE AUTOMATIZADO'
        cls.Tipo = '1 - Servico'
        cls.Favorecido = '2202'
        cls.dataref_inicio = (datetime.today()+timedelta(days=5)).strftime("%d/%m/%Y")
        cls.dataref_fim = (datetime.today()+timedelta(days=10)).strftime("%d/%m/%Y")
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Atualizações > Gestao de Viagens > Solicitações")

    def test_Cadastro_Orcamento_Viagem_CRUD(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        self.oHelper.WaitShow("Solicitação de Viagens/Treinamento")
        self.oHelper.Screenshot("PXFINA11_01.png")
        
        #------------------------
        #INCLUIR
        #------------------------
        self.oHelper.SetButton("Incluir")
        sleep(0.2)
        self.oHelper.SearchBrowse(self.filial)
        self.oHelper.Screenshot("PXFINA11_02.png")
        self.oHelper.SetButton("OK")
        sleep(0.2)
        
        self.oHelper.WaitShow("Solicitacoes de Viagens - INCLUIR")
        self.oHelper.Screenshot("PXFINA11_03.png")
        
        # Capturar o código da solicitação gerado automaticamente
        
        self.codigo_solicitacao = self.oHelper.GetValue("Codigo")
        print(f"Código da solicitação criada: {self.codigo_solicitacao}")
        
        self.oHelper.SetValue("ZV3_DESCRI", self.Descrição)
        self.oHelper.SetValue("ZV3_DTINI", self.dataref_inicio)
        self.oHelper.SetValue("ZV3_CLVL",self.ClasseValor)
        self.oHelper.SetValue("ZV3_DTFIM", self.dataref_fim)  
        sleep(1) 
        self.oHelper.Screenshot("PXFINA11_03.png")

        self.oHelper.SetValue("ZV3_CC", self.UTA)
        self.oHelper.SetValue("ZV3_ITCONT",self.ItemContabil)
        
        self.oHelper.SetValue("ZV3_TIPO", self.Tipo)  
        self.oHelper.SetValue("ZV3_OBS","TESTE DE SOLICITAÇÃO DE VIAGEM", check_value =False)
        self.oHelper.SetKey("TAB", grid=True)  
        self.oHelper.SetValue('Favorecido',  '227884',    grid=True,     grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.Screenshot("PXFINA11_04.png")
        self.oHelper.ClickFolder("Transporte")
        self.oHelper.Screenshot("PXFINA11_05.png")
        
        self.oHelper.SetValue("Tipo","1 - Aereo",                   grid=True, grid_number=1, check_value=False)
        self.oHelper.SetKey("TAB", grid=True) 
        self.oHelper.SetValue("Partida", self.dataref_inicio,       grid=True, grid_number=1, check_value=False)
        self.oHelper.SetKey("TAB", grid=True)
        self.oHelper.SetValue("Hora Partida", "08:00",              grid=True, grid_number=1, check_value=False)
        self.oHelper.SetKey("TAB", grid=True)
        self.oHelper.SetValue("Origem", "DF00108",                  grid=True, grid_number=1, check_value=False)
        self.oHelper.SetKey("TAB", grid=True)
        self.oHelper.SetValue("Destino", "GO08707",                 grid=True, grid_number=1, check_value=False)
        self.oHelper.SetKey("TAB", grid=True)
        self.oHelper.SetValue("Chegada", self.dataref_inicio,       grid=True, grid_number=1, check_value=False)
        self.oHelper.SetKey("TAB", grid=True)
        self.oHelper.SetValue("Hora Chegada", "12:00",              grid=True, grid_number=1, check_value=False)
        self.oHelper.SetKey("TAB", grid=True)
        self.oHelper.SetValue("Vl Previsto", self.ValorPrev,        grid=True, grid_number=1, check_value=False)
        self.oHelper.LoadGrid()
        self.oHelper.Screenshot("PXFINA11_06.png")
        sleep(0.5)
        
        self.oHelper.ClickFolder("Treinamento")
        sleep(0.8)
        self.oHelper.ClickFolder("Transporte")
        
    
        self.oHelper.SetButton("Confirmar")
        
        if self.oHelper.IfExists("Valores de treinamento e/ou servico ultrapassam o limite orcado-Atenção-PXFINA11X"):
            self.oHelper.Screenshot("PXFINA11_07.png")
            self.oHelper.CheckResult('Valor do orçamento', 'R$ 0,00')
            self.oHelper.SetButton('Fechar')
        
        if self.oHelper.IfExists("Help: FWMODELPOS"):
            self.oHelper.Screenshot("PXFINA11_08.png")
            self.oHelper.WaitShow('Problema: Modelo invalido')
            self.oHelper.SetButton('Fechar')
            
        if self.oHelper.IfExists("Registro inserido com sucesso."):
            self.oHelper.Screenshot("PXFINA11_09.png")
            self.oHelper.SetButton('Fechar')
       
        self.oHelper.WaitShow("Solicitação de Viagens/Treinamento") 
        self.oHelper.Screenshot("PXFINA11_10.png")
        
        sleep(0.5)
        
        self.oHelper.SearchBrowse(self.filial+self.codigo_solicitacao) 
         
        #------------------------
        # VISUALIZAR
        #------------------------
        
        self.oHelper.SetButton("Visualizar")
        self.oHelper.WaitShow("Solicitacoes de Viagens - VISUALIZAR")  
        self.oHelper.Screenshot("PXFINA11_11.png")
        
        self.oHelper.ClickFolder("Transporte")
        sleep(0.5)
        self.oHelper.ClickFolder("Treinamento")
        sleep(0.5)
        self.oHelper.ClickFolder("Diárias")     
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Solicitação de Viagens/Treinamento")
        
        #------------------------
        # EDITAR
        #------------------------ 
        
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow("Solicitacoes de Viagens - ALTERAR") 
        self.oHelper.Screenshot("PXFINA11_12.png")
        self.oHelper.SetValue("ZV3_DESCRI", self.DescriçãoEdt,check_value=False)
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Registro alterado com sucesso.")
        self.oHelper.Screenshot("PXFINA11_13.png")
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Solicitação de Viagens/Treinamento")
        
        
        #------------------------
        #  EXCLUIR
        #------------------------
        
        self.oHelper.SetButton("Outras Ações","Excluir")
        self.oHelper.WaitShow("Tem certeza que deseja excluir o item abaixo?")
        self.oHelper.Screenshot("PXFINA11_14.png")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Registro excluído com sucesso.")
        self.oHelper.Screenshot("PXFINA11_15.png")
        self.oHelper.SetButton("Fechar")
       
        self.oHelper.AssertTrue()
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_cadastro_de_solicitacao_de_viagem_CRUD")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(PXFINA11('test_Solicitacao_Viagem_UTA'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)