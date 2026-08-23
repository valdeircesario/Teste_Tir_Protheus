import os
from os import path
import sys

from tir import Webapp
from os import getcwd
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

# FUNÇÃO QUE GERAR O ARQUIVO HTML DE HOMOLAÇÃO ---- PARA PASTA C:\Relatorios_Homologacao.... LOCAL
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'tools')))
#from gerador_relatorio import gerar_guia_homologacao


#------------------------------------------
# Teste de centro de custo
#------------------------------------------


class CTBA030(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       
        cls.CentroCusto = '033'# SEMPRE USAR 3 DIGITOS
        cls.Descricao = 'DEPEM'# SEMPRE RENOMEAR
        cls.DescricaoEdt = 'DEPEDR'
        cls.filial = '01'
        configfile = getcwd() + '\\config.json'
        # 1. Instância base do TIR
        webapp_base = Webapp(configfile)
                
        # 2. Encapsula com o Agente de Relatório
        cls.oHelper = TirReportAgent(
            tir_instance=webapp_base,
            cod_modulo="07",
            nome_modulo="Gestão de Pessoal",
            ct_nome="test_CTBA030",
            descricao="Inclusão, Visualização, Alteração  e exclusão de Centro Custo"
        )
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros > Centro de Custos")
        cls.oHelper.SetButton('Confirmar')

    def test_de_incluir_Centro_de_Custo(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        #----------------------
        # INCLUIR 
        #----------------------

        try:


            self.oHelper.WaitShow("Cadastro C Custo")
            self.oHelper.Screenshot("CentroCusto/001")

            print('--------------------Incluir')
            self.oHelper.SetButton("Incluir")
            self.oHelper.WaitShow("Cadastro C Custo - INCLUIR")
            self.oHelper.Screenshot("CentroCusto/002")   
            self.oHelper.SetValue("CTT_CUSTO", self.CentroCusto4,        check_value=False)
            self.oHelper.SetValue("CTT_DESC01", self.Descricao,         check_value=False)
            self.oHelper.Screenshot("CentroCusto/003")
            self.oHelper.SetButton("Salvar")
            self.oHelper.SetButton("Cancelar")
            self.oHelper.WaitShow("Cadastro C Custo")
            self.oHelper.Screenshot("CentroCusto/004")

            #-------------------------
            # Visualização da inclusão
            #-------------------------

            print('--------------------Visualizar')
            self.oHelper.SetButton("Visualizar")
            self.oHelper.WaitShow("Centro de Custo - VISUALIZAR")
            self.oHelper.CheckResult("CTT_CUSTO", self.CentroCusto)
            self.oHelper.CheckResult("CTT_DESC01", self.Descricao)
            self.oHelper.Screenshot("CentroCusto/005")
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Cadastro C Custo")

            #-------------------------
            # Alterar
            #-------------------------

            print('--------------------Alterar')
            self.oHelper.SetButton("Alterar")
            self.oHelper.WaitShow("Cadastro C Custo - INCLUIR")
            self.oHelper.CheckResult("CTT_CUSTO", self.CentroCusto)
            self.oHelper.SetValue("CTT_DESC01", self.DescricaoEdt,        check_value=False)
            self.oHelper.Screenshot("CentroCusto/006")
            self.oHelper.SetButton("Salvar")
            self.oHelper.WaitShow("Cadastro C Custo")
            self.oHelper.Screenshot("CentroCusto/007")

            #-------------------------
            # Exclusão
            #-------------------------

            print('--------------------Excluir')
            self.oHelper.SetButton("Outras Ações","Excluir")
            self.oHelper.WaitShow("Cadastro C Custo - EXCLUIR")
            self.oHelper.CheckResult("CTT_CUSTO", self.CentroCusto)
            self.oHelper.Screenshot("CentroCusto/008")
            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Cadastro C Custo")
            self.oHelper.Screenshot("CentroCusto/009")

            self.oHelper.AssertTrue()

        except Exception as e:
            self.oHelper.registrar_erro(e)
            raise e
        finally:
            self.oHelper.salvar_relatorio()

        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_incluir_Centro_de_Custo")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()
        #gerar_guia_homologacao(__file__)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CTBA030('test_de_incluir_Centro_de_Custo'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)