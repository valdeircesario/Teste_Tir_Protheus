import sys
from time import sleep

from tir import Webapp
from os import getcwd, path
from pytest import mark
from datetime import datetime, timedelta
import unittest
# Garante a importação dos módulos da pasta utilis
PROJECT_ROOT = path.abspath(path.join(path.dirname(__file__), '..', '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tir import Webapp
from utilis.md_reporter import TirReportAgent


DateSystem = datetime.today().strftime('%d/%m/%Y')

#  DOCUMENTO DE ENTRADA

class MATA103(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.filial = "01"
        cls.numero = "999"
        cls.lcontinua = True
        configfile = getcwd() + '\\config.json'
        '''cls.diaprox = (datetime.today()+timedelta(days=-30)).strftime("%d/%m/%Y")'''
        # 1. Instância base do TIR
        webapp_base = Webapp(configfile)
                
        # 2. Encapsula com o Agente de Relatório
        cls.oHelper = TirReportAgent(
            tir_instance=webapp_base,
            cod_modulo="02",
            nome_modulo="Compras",
            ct_nome="test_MATA103",
            descricao="Inclusão e Excluir um documento de entrada"
        )
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '02')
        cls.oHelper.SetLateralMenu("Atualizações > Movimentos > Documento Entrada")
        cls.oHelper.SetButton('Confirmar')

    def test_MATA103(self):

        #Inclusão de documento entrada


        if self.oHelper.IfExists("Reforma Tributária"):
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

        try:

            self.oHelper.WaitShow("Documento de Entrada")
            self.oHelper.Screenshot("DocumentoEntrada/001")


            print('----------------------Incluir')
            self.oHelper.SetButton("Incluir")
            self.oHelper.WaitShow("Documento de Entrada - INCLUIR")
            self.oHelper.Screenshot("DocumentoEntrada/002")
            self.oHelper.SetValue('Numero', self.numero,        check_value = False)
            self.oHelper.SetValue('Serie', '01',                check_value = False)
            self.oHelper.SetValue('Fornecedor', '000004',       check_value = False)
            self.oHelper.SetValue('Espec.Docum.', 'NF',         check_value = False)
            self.oHelper.Screenshot("DocumentoEntrada/003")

            self.oHelper.SetValue("Produto",'000000000000011',  grid=True,  check_value = False)
            self.oHelper.SetValue("Quantidade",'1,00',          grid=True,  check_value = False)
            self.oHelper.SetValue("Vlr.Unitario",'10,0000',     grid=True,  check_value = False)
            self.oHelper.SetValue("Vlr.Total",'10,0000',        grid=True,  check_value = False)
            self.oHelper.SetValue("Tipo Entrada",'001',         grid=True,  check_value = False)
            self.oHelper.SetValue("Centro Custo",'007',         grid=True,  check_value = False)
            self.oHelper.LoadGrid()
            self.oHelper.Screenshot("DocumentoEntrada/004")
            self.oHelper.SetButton("Salvar")
            self.oHelper.WaitShow("Documento de Entrada - INCLUIR")
            self.oHelper.SetButton("Cancelar")
            self.oHelper.WaitShow("Documento de Entrada")
            self.oHelper.Screenshot("DocumentoEntrada/005")


            #Excluir
            print('-----------------------Excluir')
            self.oHelper.SetButton("Outras Ações","Excluir")
            self.oHelper.WaitShow("Documento de Entrada - Excluir")
            self.oHelper.Screenshot("DocumentoEntrada/006")
            self.oHelper.CheckResult("Numero","999")
            self.oHelper.CheckResult("Fornecedor","000004")
            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Documento de Entrada")
            self.oHelper.Screenshot("DocumentoEntrada/008")

            # Confirmar Exclusão
            print('--------------------Confirmar Exclusão')
            self.oHelper.SetButton('Filtrar')
            self.oHelper.WaitShow("Selecione os filtros para aplicar à tabela:")
            self.oHelper.SetButton('Criar Filtro')
            self.oHelper.SetValue("Campo","Numero",        check_value = False)
            self.oHelper.SetValue("Expressão",self.numero,  check_value = False)
            self.oHelper.SetButton('Adicionar')
            self.oHelper.SetButton('Salvar')
            self.oHelper.ClickCheckBox("Numero Igual a")
            self.oHelper.SetButton("Aplicar filtros selecionados")
            self.oHelper.WaitShow("Sem registros para o filtro selecionado.")
            self.oHelper.Screenshot("DocumentoEntrada/009")
            self.oHelper.AssertTrue()

        except Exception as e:
            self.oHelper.registrar_erro(e)
            raise e
        finally:
            self.oHelper.salvar_relatorio()

        print('---------------------------------')
        print("🎯 test_de_incluir_documento_entrada")
        print("✅ Teste finalizado com sucesso")
        print('---------------------------------')


    @classmethod
    def tearDownClass(cls):

        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MATA103('test_MATA103'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)