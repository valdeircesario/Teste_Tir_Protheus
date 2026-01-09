from tir import Webapp
from os import getcwd
import unittest
from datetime import datetime, timedelta
from time import sleep

DateSystem = datetime.today().strftime('%d/%m/%Y')

#---------------------------------------------------
# ADICIONANDO SOLICITAÇÃO DE VIAGEM, PARA ENVIAR PARA APROVAÇÃO
#---------------------------------------------------

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
        # BUSCA SOLICITAÇÕES PARA CRIADAS, PARA ANULAR
        #------------------------
        self.oHelper.SetButton("filtrar")
        sleep(0.2)
        self.oHelper.WaitShow("Gerenciador de Filtros")
        self.oHelper.ClickCheckBox("Solicitação em Aberto",1)
        self.oHelper.Screenshot("PXFINA11_02_01.png")
        self.oHelper.SetButton("Aplicar filtros selecionados")
        sleep(0.6) 
        self.oHelper.Screenshot("PXFINA11_02_02.png") 
        
        #-------------------
        # ANULAR SOLICITAÇÃO
        #-------------------   
        
        self.oHelper.SetButton("Outras Ações","Anular Solicitação")
        sleep(0.9)
        
        
        if self.oHelper.IfExists("Atenção!"):
            self.oHelper.Screenshot("PXFINA11_02_03.png")
            self.oHelper.WaitShow("Anulação dessa solicitação é irreversível. Deseja continuar?")
            self.oHelper.SetButton('Sim')
            self.oHelper.AssertTrue()
            
        if self.oHelper.IfExists("doCancelar"):
            self.oHelper.Screenshot("PXFINA11_02_04.png")
            self.oHelper.WaitShow("Anulação realizada com sucesso!")
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        
             
        self.oHelper.AssertTrue()
        
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_cadastro_de_solicitacao_de_viagem_para_aprovacao")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(PXFINA11_01('test_Envio_Solicitacao_Viagem_para_Aprovacao'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)