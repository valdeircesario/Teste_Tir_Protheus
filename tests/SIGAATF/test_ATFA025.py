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


# TESTE DE CADASTRO DE Locais

class ATFA025(unittest.TestCase):	
    @classmethod
    def setUpClass(cls):
        cls.filial = '01'
        cls.codigo = '129'
        cls.descricao = 'TESTE LOCAIS 06'
        cls.descricaoEdt = 'TESTE LOCAIS ALTERADO 09'
        cls.tipo = '1 - Físico'
        configfile = getcwd() + '\\config.json'
        # 1. Instância base do TIR
        webapp_base = Webapp(configfile)
                
        # 2. Encapsula com o Agente de Relatório
        cls.oHelper = TirReportAgent(
            tir_instance=webapp_base,
            cod_modulo="01",
            nome_modulo="Ativo Fixo",
            ct_nome="test_ATFA025",
            descricao="Inclusão e Visualização, Alteração e Exclusão de Locais"
        )
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '01')
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros > Locais")
        cls.oHelper.SetButton('Confirmar')
        

    def test_cadastro_Locais(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')
            

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        try:
        
            self.oHelper.WaitShow("Cadastro de Locais") 
            
            
            #--------------
            # INCLUISÃO
            #-------------
            
                
            self.oHelper.Screenshot("Locais/001")
            print('-----------------------------Incluir')
            self.oHelper.SetButton("Incluir")
            self.oHelper.WaitShow("Cadastro de Locais - INCLUIR")
            #codLocais = self.oHelper.GetValue('Cod. Locais')
            #print(f"Codigo do Locais:{codLocais}")
            self.oHelper.Screenshot("Locais/002") 
            self.oHelper.SetValue('NL_CODIGO',self.codigo,      check_value=False) 
            self.oHelper.SetValue('NL_DESCRIC',self.descricao,  check_value=False)
            self.oHelper.SetValue('NL_TIPOLOC',self.tipo,       check_value=False)
            self.oHelper.SetValue('NL_BLOQ','2 - Não',          check_value=False)
            self.oHelper.Screenshot("Locais/003")
            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Registro inserido com sucesso") 
            self.oHelper.Screenshot("Locais/004")
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Cadastro de Locais")
            self.oHelper.Screenshot("Locais/005")
            
            #-----------------------
            # VISUALIZAR INCLUSÃO 
            #------------------------
            
            print('---------------------------------Visualizar')
            self.oHelper.SetButton("Visualizar")
            self.oHelper.WaitShow("Cadastro de Locais - VISUALIZAR")
            self.oHelper.Screenshot("Locais/007") 
            self.oHelper.CheckResult('NL_CODIGO',self.codigo) 
            self.oHelper.CheckResult('NL_DESCRIC',self.descricao)
            self.oHelper.CheckResult('NL_TIPOLOC',self.tipo)
            self.oHelper.CheckResult('NL_BLOQ','2 - Não')
            self.oHelper.Screenshot("Locais/008")    
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Cadastro de Locais")

            #-----------------------
            # EDITAR LOCAL 
            #------------------------
            
            print('---------------------------------Alterar')
            self.oHelper.SetButton("Alterar")
            self.oHelper.WaitShow("Cadastro de Locais - ALTERAR")
            self.oHelper.Screenshot("Locais/009") 
            self.oHelper.CheckResult('NL_CODIGO',self.codigo) 
            self.oHelper.SetValue('NL_DESCRIC',self.descricaoEdt,          check_value=False)
            self.oHelper.CheckResult('NL_TIPOLOC',self.tipo)
            self.oHelper.SetValue('NL_BLOQ','1 - Sim')
            self.oHelper.Screenshot("Locais/010")    
            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Registro alterado com sucesso") 
            self.oHelper.Screenshot("Locais/011")
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Cadastro de Locais")
            self.oHelper.Screenshot("Locais/012")

            #-----------------------
            # VISUALIZAR EDIÇÃO 
            #------------------------
            
            print('---------------------------------Visualizar')
            self.oHelper.SetButton("Visualizar")
            self.oHelper.WaitShow("Cadastro de Locais - VISUALIZAR")
            self.oHelper.Screenshot("Locais/013") 
            self.oHelper.CheckResult('NL_CODIGO',self.codigo) 
            self.oHelper.CheckResult('NL_DESCRIC',self.descricaoEdt)
            self.oHelper.CheckResult('NL_TIPOLOC',self.tipo)
            self.oHelper.CheckResult('NL_BLOQ','1 - Sim')
            self.oHelper.Screenshot("Locais/014")    
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Cadastro de Locais")

            #-----------------------
            # EXCLUSÃO
            #------------------------
            
            print('---------------------------------Excluir')
            self.oHelper.SetButton("Outras Ações","Excluir")
            self.oHelper.WaitShow("Tem certeza que deseja excluir o item abaixo?")
            self.oHelper.CheckResult('NL_CODIGO',self.codigo) 
            self.oHelper.CheckResult('NL_DESCRIC',self.descricaoEdt)
            self.oHelper.CheckResult('NL_TIPOLOC',self.tipo)
            self.oHelper.CheckResult('NL_BLOQ','1 - Sim')
            self.oHelper.Screenshot("Locais/015")    
            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Registro excluído com sucesso.")
            self.oHelper.Screenshot("Locais/016") 
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Cadastro de Locais")

            #-----------------------
            #  CONFIRMA EXCLUSÃO
            #------------------------
            
            print('---------------------------------Confirmação da Exclusão')
            self.oHelper.SetButton("Filtrar")
            self.oHelper.WaitShow("Selecione os filtros para aplicar à tabela:")
            self.oHelper.SetButton("Criar Filtro")
            self.oHelper.SetValue('Campo','Código')
            self.oHelper.SetValue('Expressão',self.codigo)
            self.oHelper.SetButton("Adicionar")
            self.oHelper.SetButton("Salvar")
            self.oHelper.ClickCheckBox("Código Igual a ",1)
            self.oHelper.SetButton("Aplicar filtros selecionados")
            self.oHelper.WaitShow("Sem registros para o filtro selecionado.")
            self.oHelper.Screenshot("Locais/017")

            
            self.oHelper.AssertTrue()

        except Exception as e:
            self.oHelper.registrar_erro(e)
            raise e
        finally:
            self.oHelper.salvar_relatorio()
        
        print("------------------------------------------------")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_cadastro_Locais")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
        
    

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ATFA025('test_cadastro_Locais'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
