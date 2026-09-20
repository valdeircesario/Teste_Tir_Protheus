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
#-- Teste MATA360 condições de pagamento
#------------------------------------------

class MATA360(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       
        cls.Codigo = '006'
        cls.Tipo = '3'
        cls.ConPgt = "1,2,3"
        cls.ConPgtEdt = "1,2,3,4"
        cls.Descrição = 'A PRAZO'
        cls.DescriçãoEdt = 'A PRAZO EDTI'
        cls.filial = '01'
        configfile = getcwd() + '\\config.json'
        # 1. Instância base do TIR
        webapp_base = Webapp(configfile)
                
        # 2. Encapsula com o Agente de Relatório
        cls.oHelper = TirReportAgent(
            tir_instance=webapp_base,
            cod_modulo="02",
            nome_modulo="Compras",
            ct_nome="test_MATA360",
            descricao="Inclusão,Visualização, Alteração e Exclusão de Condição de Pagamento"
        )
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '02')
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros > Condição de Pagamento")
        cls.oHelper.SetButton("Confirmar")

    def test_de_incluir_condições_de_pagamento(self):

        sleep(5)
        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')
        sleep(5)
        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        try:

            #-------------------------
            # Inclusão de forma de pagamento
            #-------------------------

            self.oHelper.WaitShow("Condiçäo de Pagamento:")
            self.oHelper.Screenshot("Cond_Pagamento/001") 

            print('--------------------------Incluir')
            self.oHelper.SetButton("Incluir")
            self.oHelper.WaitShow("Condiçäo de Pagamento - INCLUIR")
            self.oHelper.Screenshot("Cond_Pagamento/002")
            self.oHelper.SetValue("E4_CODIGO", self.Codigo,     check_value=False)
            self.oHelper.SetValue("E4_TIPO", self.Tipo,         check_value=False)
            self.oHelper.SetValue("E4_COND", self.ConPgt,       check_value=False)
            self.oHelper.SetValue("E4_DESCRI", self.Descrição,  check_value=False)
            self.oHelper.Screenshot("Cond_Pagamento/003")
            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Registro inserido com sucesso.")
            self.oHelper.Screenshot("Cond_Pagamento/004")
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Condiçäo de Pagamento:")
            self.oHelper.Screenshot("Cond_Pagamento/005")
            
            #-------------------------
            # Visualização da inclusão
            #-------------------------

            print('-------------------Visualizar')
            self.oHelper.SetButton("Visualizar")
            self.oHelper.WaitShow("Condiçäo de Pagamento - VISUALIZAR")
            self.oHelper.CheckResult("E4_CODIGO", self.Codigo)
            self.oHelper.CheckResult("E4_TIPO", self.Tipo)
            self.oHelper.CheckResult("E4_COND", self.ConPgt)
            self.oHelper.CheckResult("E4_DESCRI", self.Descrição)
            self.oHelper.Screenshot("Cond_Pagamento/006")
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Condiçäo de Pagamento:")

            #----------------------
            # Alteração 
            #----------------------

            print('-----------------------Alterar')
            self.oHelper.SetButton("Alterar")
            self.oHelper.WaitShow("Condiçäo de Pagamento - ALTERAR")
            self.oHelper.Screenshot("Cond_Pagamento/007")
            self.oHelper.SetValue("E4_COND", self.ConPgtEdt)
            self.oHelper.SetValue("E4_DESCRI", self.DescriçãoEdt)
            self.oHelper.Screenshot("Cond_Pagamento/008")
            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Registro alterado com sucesso")
            self.oHelper.Screenshot("Cond_Pagamento/009")
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Condiçäo de Pagamento:")
            self.oHelper.Screenshot("Cond_Pagamento/010")

            #----------------------
            # Exclusão
            #----------------------

            print('-----------------------Exclusão')
            self.oHelper.SetButton("Outras Ações","Excluir")
            self.oHelper.WaitShow("Tem certeza que deseja excluir o item abaixo?")
            self.oHelper.SetValue("E4_COND", self.ConPgtEdt)
            self.oHelper.SetValue("E4_DESCRI", self.DescriçãoEdt)
            self.oHelper.Screenshot("Cond_Pagamento/011")
            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Registro excluído com sucesso.")
            self.oHelper.Screenshot("Cond_Pagamento/012")
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Condiçäo de Pagamento:")

            #-----------------------
            #  CONFIRMA EXCLUSÃO
            #------------------------
            
            print('---------------------------------Confirmação da Exclusão')
            self.oHelper.SetButton("Filtrar")
            self.oHelper.WaitShow("Selecione os filtros para aplicar à tabela:")
            self.oHelper.SetButton("Criar Filtro")
            self.oHelper.SetValue('Campo','Codigo')
            self.oHelper.SetValue('Expressão',self.Codigo)
            self.oHelper.SetButton("Adicionar")
            self.oHelper.SetButton("Salvar")
            self.oHelper.ClickCheckBox("Codigo Igual a ",1)
            self.oHelper.SetButton("Aplicar filtros selecionados")
            self.oHelper.WaitShow("Sem registros para o filtro selecionado.")
            self.oHelper.Screenshot("Cond_Pagamento/013")

            self.oHelper.AssertTrue()
        except Exception as e:
            self.oHelper.registrar_erro(e)
            raise e
        finally:
            self.oHelper.salvar_relatorio()
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X🎯 test_de_incluir_condições_de_pagamento")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MATA360('test_de_incluir_condições_de_pagamento'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    