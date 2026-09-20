import sys

from tir import Webapp
from os import getcwd, path
import unittest
from datetime import datetime
# Garante a importação dos módulos da pasta utilis
PROJECT_ROOT = path.abspath(path.join(path.dirname(__file__), '..', '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tir import Webapp
from utilis.md_reporter import TirReportAgent



from time import sleep
DateSystem = datetime.today().strftime('%d/%m/%Y')

#------------------------------------------
#-- Teste MATA110  solicitação de compras
#------------------------------------------

class MATA110(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       
        cls.produto = "000000000000011"
        cls.produto2 = "000000000000015"
        cls.Quantidade = '11'
        cls.comprador = "124"
        cls.Observacao = "TESTE DE SOLIC DE COMPRAS"
        cls.filial = '01'
        cls.CentroCusto = "006"
        configfile = getcwd() + '\\config.json'
        # 1. Instância base do TIR
        webapp_base = Webapp(configfile)
                
        # 2. Encapsula com o Agente de Relatório
        cls.oHelper = TirReportAgent(
            tir_instance=webapp_base,
            cod_modulo="02",
            nome_modulo="Compras",
            ct_nome="test_MATA110",
            descricao="Inclusão,Visualização, Alteração e Exclusão de Solicitação de Compras"
        )
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '02')
        cls.oHelper.SetLateralMenu("Atualizações > Solicitações > Solicitação de Compras")
        cls.oHelper.SetButton('Confirmar')


    def test_de_incluir_solicitação_de_compras(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')
            
        try:

            #-------------------------
            # Inclusão de solicitação de compras
            #-------------------------

            self.oHelper.WaitShow("Solicitaçäo de Compras") 
            self.oHelper.Screenshot("Solicitação_Compra/001.png")

            print('-------------------------Incluir')
            self.oHelper.SetButton("Incluir")
            self.oHelper.WaitShow("Solicitaçäo de Compras - Incluir")
            numero = self.oHelper.GetValue('Número')
            print(f"Numero da solicitação: {numero}")
            self.oHelper.Screenshot("Solicitação_Compra/002.png")

            self.oHelper.SetValue("Cod. Comprador", self.comprador,                 check_value=False)
            self.oHelper.ClickGridCell(column="Produto", row=1,      grid_number=1)

            self.oHelper.SetValue("Produto", self.produto,              grid=True,  check_value=False)
            self.oHelper.LoadGrid()
            self.oHelper.SetValue("Quantidade", self.Quantidade,        grid=True,  check_value=False)
            self.oHelper.LoadGrid()
            self.oHelper.SetValue("Observacao", self.Observacao,        grid=True,  check_value=False)
            self.oHelper.LoadGrid()
            self.oHelper.SetValue("Centro Custo", self.CentroCusto,     grid=True,  check_value=False)
            self.oHelper.LoadGrid()
            self.oHelper.Screenshot("Solicitação_Compra/003.png")

            self.oHelper.SetButton("Salvar")
            self.oHelper.WaitShow("Solicitaçäo de Compras - Incluir")
            self.oHelper.SetButton("Cancelar")
            self.oHelper.Screenshot("Solicitação_Compra/004.png")
            self.oHelper.WaitShow("Solicitaçäo de Compras")

            #-------------------
            # VISUALIZAR
            #-------------------
            
            print('----------------------------Visualizar')
            self.oHelper.SetButton("Visualizar")
            self.oHelper.WaitShow("Solicitaçäo de Compras")
            self.oHelper.CheckResult("Cod. Comprador", self.comprador)
            self.oHelper.CheckResult("Produto", self.produto,           grid=True)
            self.oHelper.CheckResult("Observacao", self.Observacao,     grid=True)
            self.oHelper.CheckResult("Centro Custo", self.CentroCusto,  grid=True)
            self.oHelper.Screenshot("Solicitação_Compra/005.png")
            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Solicitaçäo de Compras")

            #-------------------
            # ALTERAR
            #-------------------

            print('-------------------------------Alterar')
            self.oHelper.SetButton("Alterar")
            self.oHelper.WaitShow("Solicitaçäo de Compras - Alterar")
            self.oHelper.CheckResult("Cod. Comprador", self.comprador)
            self.oHelper.ClickGridCell(column="Produto", row=1,      grid_number=1)
            self.oHelper.SetKey("DOWN",   grid=True,wait_change=True)
            self.oHelper.LoadGrid()
            self.oHelper.Screenshot("Solicitação_Compra/006.png") 
            self.oHelper.SetValue("Produto", self.produto2,         grid=True,      check_value=False)
            self.oHelper.LoadGrid()
            self.oHelper.SetValue("Quantidade", self.Quantidade,    grid=True,      check_value=False)
            self.oHelper.LoadGrid()
            self.oHelper.SetValue("Observacao", self.Observacao,    grid=True,      check_value=False)
            self.oHelper.LoadGrid()
            self.oHelper.SetValue("Centro Custo", self.CentroCusto, grid=True,      check_value=False)
            self.oHelper.LoadGrid() 
            self.oHelper.Screenshot("Solicitação_Compra/007.png")   
            self.oHelper.Screenshot("Solicitação_Compra01.png")
            self.oHelper.SetButton("Salvar")
            self.oHelper.WaitShow("Solicitaçäo de Compras")

            #-------------------
            # EXCLUIR
            #-------------------

            print('-----------------------Excluir')
            self.oHelper.SetButton("Outras Ações","Excluir")
            self.oHelper.WaitShow("Solicitaçäo de Compras - Excluir")
            self.oHelper.CheckResult("Cod. Comprador", self.comprador)
            self.oHelper.ClickGridCell(column="Produto", row=1,      grid_number=1)
            self.oHelper.ClickGridCell(column="Produto", row=2,      grid_number=1)
            self.oHelper.Screenshot("Solicitação_Compra/008.png")
            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Solicitaçäo de Compras")

            #-----------------------
            #  CONFIRMA EXCLUSÃO
            #------------------------
            
            print('---------------------------------Confirmação da Exclusão')
            self.oHelper.SetButton("Filtrar")
            self.oHelper.WaitShow("Selecione os filtros para aplicar à tabela:")
            self.oHelper.SetButton("Criar Filtro")
            self.oHelper.SetValue('Campo','Numero da SC')
            self.oHelper.SetValue('Expressão',numero, check_value=False)
            self.oHelper.SetButton("Adicionar")
            self.oHelper.SetButton("Salvar")
            self.oHelper.ClickCheckBox("Numero da SC Igual a ",1)
            self.oHelper.SetButton("Aplicar filtros selecionados")
            self.oHelper.WaitShow("Sem registros para o filtro selecionado.")
            self.oHelper.Screenshot("Solicitação_Compra/009.png")

            self.oHelper.AssertTrue()

        except Exception as e:
            self.oHelper.registrar_erro(e)
            raise e
        finally:
            self.oHelper.salvar_relatorio()

        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_incluir_solicitação_de_compras")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MATA110('test_de_incluir_solicitação_de_compras'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)