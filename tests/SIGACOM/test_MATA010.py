import sys

from tir import Webapp
from os import getcwd, path
import unittest
from datetime import datetime
from time import sleep

# Garante a importação dos módulos da pasta utilis
PROJECT_ROOT = path.abspath(path.join(path.dirname(__file__), '..', '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
from tir import Webapp
from utilis.md_reporter import TirReportAgent


DateSystem = datetime.today().strftime('%d/%m/%Y')

#------------------------------------------
#-- Teste MATA010 - Cadastro de produtos
#------------------------------------------




class MATA010(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       
        cls.Codigo = '000000000000015'
        cls.Descricao = 'MOUSE SEM FIO POSITIVO'
        cls.DescricaoEdt = 'MOUSE SEM FIO POSITIVO BRANCO'
        cls.Tipo = 'ME'
        cls.Unidade = 'PC'
        cls.Armazem = '01'
        cls.Grupo = '0003'
        cls.Preco = '150,00'
        cls.NomeCientifico = 'MOUSE NOME POSITIVO'
        cls.filial = '01'
        configfile = getcwd() + '\\config.json'
        # 1. Instância base do TIR
        webapp_base = Webapp(configfile)
                
        # 2. Encapsula com o Agente de Relatório
        cls.oHelper = TirReportAgent(
            tir_instance=webapp_base,
            cod_modulo="02",
            nome_modulo="Compras",
            ct_nome="test_MATA010",
            descricao="Inclusão, Visualização e Alteração  de Produto"
        )
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '02')
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros > Produtos")
        cls.oHelper.SetButton('Confirmar')

    def test_de_incluir_produtos(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        try:

            self.oHelper.WaitShow("Atualizacao de Produtos:")
            self.oHelper.Screenshot("Produto/001")

            #-------------------------
            # Inclusão de produto
            #-------------------------

            print('---------------------Incluir')
            self.oHelper.SetButton("Incluir")
            self.oHelper.WaitShow("Atualizacao de Produtos - Incluir")
            self.oHelper.Screenshot("Produto/002")
            self.oHelper.SetValue("B1_COD", self.Codigo,                check_value=False)
            self.oHelper.SetValue("B1_DESC", self.Descricao,            check_value=False)
            self.oHelper.SetValue("B1_TIPO", self.Tipo,                 check_value=False)
            self.oHelper.SetValue("B1_UM", self.Unidade,                check_value=False)
            self.oHelper.SetValue("B1_LOCPAD", self.Armazem,            check_value=False)
            self.oHelper.SetValue("B1_GRUPO", self.Grupo,               check_value=False)
            self.oHelper.SetValue("B1_UPRC", self.Preco,                check_value=False)
            self.oHelper.SetValue("B5_CEME", self.NomeCientifico,       check_value=False)
            self.oHelper.Screenshot("Produto/003")
            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Registro inserido com sucesso.")
            self.oHelper.Screenshot("Produto/004")
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Atualizacao de Produtos:")
            self.oHelper.Screenshot("Produto/005")
            

            #-------------------------
            # Visualização da inclusão
            #-------------------------
            print('------------------------Visualizar')
            self.oHelper.SetButton("Visualizar")
            self.oHelper.WaitShow("Atualizacao de Produtos - Visualizar")
            self.oHelper.CheckResult("B1_DESC", self.Descricao)
            self.oHelper.CheckResult("B1_GRUPO", self.Grupo)
            self.oHelper.CheckResult("B5_CEME", self.NomeCientifico)
            self.oHelper.CheckResult("B1_UPRC", self.Preco)
            self.oHelper.CheckResult("B1_LOCPAD", self.Armazem)
            self.oHelper.CheckResult("B1_TIPO", self.Tipo)
            self.oHelper.CheckResult("B1_UM", self.Unidade)
            self.oHelper.Screenshot("Produto/006")
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Atualizacao de Produtos:")

            #-------------------------
            # Alterar
            #-------------------------
            print('-----------------------Aterar')
            self.oHelper.SetButton("Alterar")
            self.oHelper.WaitShow("Atualizacao de Produtos - Alterar")
            self.oHelper.Screenshot("Produto/007")
            self.oHelper.SetValue("B1_DESC", self.DescricaoEdt,           check_value=False)
            self.oHelper.CheckResult("B1_GRUPO", self.Grupo)
            self.oHelper.CheckResult("B5_CEME", self.NomeCientifico)
            self.oHelper.CheckResult("B1_UPRC", self.Preco)
            self.oHelper.CheckResult("B1_LOCPAD", self.Armazem)
            self.oHelper.CheckResult("B1_TIPO", self.Tipo)
            self.oHelper.CheckResult("B1_UM", self.Unidade)
            self.oHelper.Screenshot("Produto/008")
            self.oHelper.SetButton("confirmar")
            self.oHelper.WaitShow("Registro alterado com sucesso")
            self.oHelper.Screenshot("Produto/009")
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Atualizacao de Produtos:")
            self.oHelper.Screenshot("Produto/010")

            self.oHelper.AssertTrue()
        except Exception as e:
            self.oHelper.registrar_erro(e)
            raise e
        finally:
            self.oHelper.salvar_relatorio()

        print('---------------------------------')
        print("🎯 test_de_incluir_produtos")
        print("✅ Teste finalizado com sucesso")
        print('---------------------------------')

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MATA010('test_de_incluir_produtos'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)