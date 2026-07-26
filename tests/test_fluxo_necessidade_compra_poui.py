import unittest
from datetime import datetime, timedelta
from os import getcwd
from tir import Webapp, Poui
from tir.technologies.core.base import By
#from tir import Poui



class TestNecessidadeCompraPOUI(unittest.TestCase):

    # ==================================================
    # SETUP
    # ==================================================
    @classmethod
    def setUpClass(cls):
        cls.filial = "01"
        cls.data_ref = (datetime.today() - timedelta(days=1)).strftime("%d/%m/%Y")

        config_path = getcwd() + "\\config.json"
        
        # Instanciação dos Helpers do TIR (Webapp para Protheus base e Poui para Angular)
        cls.oHelper = Webapp(config_path)
        cls.oHelper_Poui = Poui(config_path)

        # Login e ambiente
        cls.oHelper.Setup("SIGAMDI", cls.data_ref, "99", cls.filial, "02")

        # Tratamento de modais/avisos iniciais do Protheus
        if cls.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            cls.oHelper.SetButton("Fechar")

        if cls.oHelper.IfExists("Moedas"):
            cls.oHelper.SetButton("Confirmar")

        # Acessa a rotina principal
        cls.oHelper.SetLateralMenu("Atualizações > Novo Fluxo de Compras > Novo Fluxo de Compras")
        cls.oHelper.SetButton('Confirmar')
        
        if cls.oHelper.IfExists("Confirmar"):
            cls.oHelper.SetButton('Confirmar')
            
        print(">>> Rotina 'Novo Fluxo de Compras' aberta com sucesso!")

    # ==================================================
    # TESTE
    # ==================================================
    def test_consultar_necessidade_compra(self):

        if self.oHelper.IfExists("Moedas"):
                    self.oHelper.SetButton("Confirmar")

        # 1. Interage diretamente com o menu lateral interno em PO UI da rotina
        self.oHelper_Poui.ClickMenu('Necessidade de Compra')
        
        # 2. Insira aqui as ações/preenchimentos dentro da tela de Necessidade de Compra
        self.oHelper_Poui.InputValue('Filtro', '000001')

        
        # Usa o ClickButton do Poui apontando para a legenda
        self.oHelper_Poui.ClickButton('Compra Centralizada')

        # titulos de cabeçalho 
        self.oHelper_Poui.POtabs(label='Em Aberto')

        # Marca o checkbox da linha onde a Solicitação é '000001'
        self.oHelper_Poui.ClickTable(columns='Solicitação', values='000001', checkbox=True)
        
        # 3. Validação do resultado do teste
        self.oHelper.AssertTrue()

    # ==================================================
    # TEARDOWN
    # ==================================================
    @classmethod
    def tearDownClass(cls):
        # Finaliza os processos do navegador
        cls.oHelper_Poui.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    # Adiciona a classe e o nome exato da função de teste
    suite.addTest(TestNecessidadeCompraPOUI('test_consultar_necessidade_compra'))
    
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)