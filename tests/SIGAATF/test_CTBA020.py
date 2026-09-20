from os import getcwd, path
import sys
from tir import Webapp
from pytest import mark
import unittest
from datetime import datetime, timedelta
from time import sleep

# Garante a importação dos módulos da pasta utilis
PROJECT_ROOT = path.abspath(path.join(path.dirname(__file__), '..', '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tir import Webapp
from utilis.md_reporter import TirReportAgent

DateSystem = datetime.today().strftime('%d/%m/%Y')


# TESTE DE CADASTRO DE CONTA PAGAR

class CTBA020(unittest.TestCase):	
    @classmethod
    def setUpClass(cls):
        cls.filial = '01'
        cls.codigo = '1234'
        cls.descricao = 'TESTE CONTA PAGAR 01'
        cls.descricaoEdt = 'TESTE ALTERAR CONTA PAGAR 01'
        configfile = getcwd() + '\\config.json'
        # 1. Instância base do TIR
        webapp_base = Webapp(configfile)
                
        # 2. Encapsula com o Agente de Relatório
        cls.oHelper = TirReportAgent(
            tir_instance=webapp_base,
            cod_modulo="01",
            nome_modulo="Ativo Fixo",
            ct_nome="test_CTBA020",
            descricao="Inclusão e Visualização ,Ateração e Exclusão de uma Conta a Pagar"
        )
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '01')
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros > Planos de Contas")
        cls.oHelper.SetButton('Confirmar')
        

    def test_cadastro_Rateio(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')
            

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        try:
        
            self.oHelper.WaitShow("Cadastro Plano de Contas") 
             
            #--------------
            # INCLUISÃO
            #-------------
            
                
            self.oHelper.Screenshot("Cont_Pagar/001")
            print('-----------------------------Incluir')
            self.oHelper.SetButton("Incluir")
            self.oHelper.WaitShow("Cadastro Plano de Contas - INCLUIR")
            #codCont_Pagar = self.oHelper.GetValue('Cod. Cont_Pagar')
            #print(f"Codigo do Cont_Pagar:{codCont_Pagar}")
            self.oHelper.Screenshot("Cont_Pagar/002") 
            self.oHelper.SetValue('CT1_CONTA',self.codigo,          check_value=False) 
            self.oHelper.SetValue('CT1_DESC01',self.descricao,      check_value=False)
            self.oHelper.SetValue('CT1_CLASSE',"2 - Analitica",     check_value=False)
            self.oHelper.SetValue('CT1_NORMAL',"1 - Devedora",      check_value=False)
            self.oHelper.Screenshot("Cont_Pagar/002")
            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Registro inserido com sucesso.")
            self.oHelper.Screenshot("Cont_Pagar/003") 
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Cadastro Plano de Contas")
            self.oHelper.Screenshot("Cont_Pagar/004") 
            
            #-----------------------
            # VISUALIZAR INCLUSÃO 
            #------------------------
            
            print('---------------------------------Visualizar')
            self.oHelper.SetButton("Outras Ações","Visualizar")
            self.oHelper.WaitShow("Cadastro Plano de Contas - VISUALIZAR")
            self.oHelper.CheckResult('CT1_CONTA',self.codigo) 
            self.oHelper.CheckResult('CT1_DESC01',self.descricao)
            self.oHelper.CheckResult('CT1_CLASSE',"2 - Analitica")
            self.oHelper.CheckResult('CT1_NORMAL',"1 - Devedora")
            self.oHelper.Screenshot("Cont_Pagar/005")    
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Cadastro Plano de Contas")

            #-----------------------
            # ALTERAR INCLUSÃO 
            #------------------------
            
            print('---------------------------------Alterar')
            self.oHelper.SetButton("Alterar")
            self.oHelper.WaitShow("Cadastro Plano de Contas - ALTERAR")
            self.oHelper.Screenshot("Cont_Pagar/006") 
            self.oHelper.CheckResult('CT1_CONTA',self.codigo) 
            self.oHelper.CheckResult('CT1_DESC01',self.descricao)
            self.oHelper.SetValue('CT1_DESC01',self.descricaoEdt,       check_value=False)
            self.oHelper.CheckResult('CT1_CLASSE',"2 - Analitica")
            self.oHelper.CheckResult('CT1_NORMAL',"1 - Devedora")
            self.oHelper.SetValue('CT1_NORMAL',"2 - Credora",           check_value=False)
            self.oHelper.Screenshot("Cont_Pagar/007")    
            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Registro alterado com sucesso.") 
            self.oHelper.Screenshot("Cont_Pagar/008")
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Cadastro Plano de Contas")
            self.oHelper.Screenshot("Cont_Pagar/009")

            #-----------------------
            # EXCLUSÃO 
            #------------------------
            
            print('---------------------------------Exclusão')
            self.oHelper.SetButton("Outras Ações","Excluir")
            self.oHelper.WaitShow("Tem certeza que deseja excluir o item abaixo?")
            self.oHelper.CheckResult('CT1_CONTA',self.codigo) 
            self.oHelper.CheckResult('CT1_DESC01',self.descricaoEdt)
            self.oHelper.CheckResult('CT1_CLASSE',"2 - Analitica")
            self.oHelper.CheckResult('CT1_NORMAL',"2 - Credora")
            self.oHelper.Screenshot("Cont_Pagar/010")    
            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Registro excluído com sucesso.")
            self.oHelper.Screenshot("Cont_Pagar/011") 
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Cadastro Plano de Contas")

            #-----------------------
            #  CONFIRMA EXCLUSÃO
            #------------------------
            
            print('---------------------------------Confirmação da Exclusão')
            self.oHelper.SetButton("Filtrar")
            self.oHelper.WaitShow("Selecione os filtros para aplicar à tabela:")
            self.oHelper.SetButton("Criar Filtro")
            self.oHelper.SetValue('Campo','Cod Conta')
            self.oHelper.SetValue('Expressão',self.codigo)
            self.oHelper.SetButton("Adicionar")
            self.oHelper.SetButton("Salvar")
            self.oHelper.ClickCheckBox("Cod Conta Igual a",1)
            self.oHelper.SetButton("Aplicar filtros selecionados")
            self.oHelper.WaitShow("Sem registros para o filtro selecionado.")
            self.oHelper.Screenshot("Cont_Pagar/012")

            self.oHelper.AssertTrue()

        except Exception as e:
            self.oHelper.registrar_erro(e)
            raise e
        finally:
            self.oHelper.salvar_relatorio()
        
        print("------------------------------------------------")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_cadastro_Cont_Pagar")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
        
    

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CTBA020('test_cadastro_Rateio'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
