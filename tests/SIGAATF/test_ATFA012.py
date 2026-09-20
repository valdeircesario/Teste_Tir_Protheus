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


# TESTE DE CADASTRO DE ATIVOS

class ATFA012(unittest.TestCase):	
    @classmethod
    def setUpClass(cls):
        cls.filial = '01'
        cls.codBem = 'ATIVO 2'
        cls.item = "451"
        cls.chapa ="987"
        cls.descricao = 'TESTE ATIVO PROTHES'
        cls.descricaoEdt = "TESTE ATIVO AUT EDITADO"
        configfile = getcwd() + '\\config.json'
        # 1. Instância base do TIR
        webapp_base = Webapp(configfile)
                
        # 2. Encapsula com o Agente de Relatório
        cls.oHelper = TirReportAgent(
            tir_instance=webapp_base,
            cod_modulo="01",
            nome_modulo="Ativo Fixo",
            ct_nome="test_ATFA012",
            descricao="Inclusão, Visualização, Alteração  e exclusão de Ativos"
        )
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '01')
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros > Ativos")
        cls.oHelper.SetButton('Confirmar')
        

    def test_cadastro_Ativos(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')
            

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        try:
        
            self.oHelper.WaitShow("Atualização de Ativos Imobilizados:") 
            
            
            #--------------
            # INCLUISÃO
            #-------------
            
                
            self.oHelper.Screenshot("Ativos/001")
            print('-----------------------------Incluir')
            self.oHelper.SetButton("Incluir")
            self.oHelper.WaitShow("Ativo Imobilizado - Incluir")
            self.oHelper.Screenshot("Ativos/002") 
            self.oHelper.SetValue('N1_PATRIM',"N - Ativo Imobilizado",          check_value=False)  
            self.oHelper.SetValue('N1_CBASE',self.codBem,                       check_value=False)
            self.oHelper.SetValue('N1_ITEM',self.item,                          check_value=False)
            self.oHelper.SetValue('N1_QUANTD',"12",                             check_value=False)
            self.oHelper.SetValue('N1_AQUISIC',DateSystem,                      check_value=False)
            self.oHelper.SetValue('N1_DESCRIC',self.descricao,                  check_value=False)
            self.oHelper.SetValue('N1_CHAPA',self.chapa,                        check_value=False)
            self.oHelper.Screenshot("Ativos/003")
            
            self.oHelper.ClickFolder('Dados Gerais')
            self.oHelper.SetValue('Tipo Ativo','01',                            check_value=False) 
            self.oHelper.SetValue('Historico','TESTE ATIVO IMOBILIARIO',        check_value=False)

            self.oHelper.ClickFolder('Classificação Contábil')
            self.oHelper.SetValue('Conta','01111',                              check_value=False)

            self.oHelper.ClickFolder('Valores')
            self.oHelper.SetValue('Val Orig M1','125',                          check_value=False)

            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Registro inserido com sucesso")
            self.oHelper.Screenshot("Ativos/005")
            self.oHelper.SetButton('Fechar')
            self.oHelper.WaitShow("Atualização de Ativos Imobilizados:")     
            self.oHelper.Screenshot("Ativos/006")    
            
            #-----------------------
            # VISUALIZAR INCLUSÃO 
            #------------------------
            
            print('---------------------------------Visualizar')
            self.oHelper.SetButton("Visualizar")
            self.oHelper.WaitShow("Ativo Imobilizado - VISUALIZAR")
            self.oHelper.Screenshot("Ativos/007")   
            self.oHelper.CheckResult('N1_CBASE',self.codBem)
            self.oHelper.CheckResult('N1_ITEM',self.item)
            self.oHelper.CheckResult('N1_AQUISIC',DateSystem)
            self.oHelper.CheckResult('N1_DESCRIC',self.descricao)
            self.oHelper.Screenshot("Ativos/008")    
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Atualização de Ativos Imobilizados:")
            
            #-------------------
            # EDITAR Ativos
            #-------------------
            
            print('---------------------------------Aterar')
            self.oHelper.SetButton("Alterar")
            self.oHelper.WaitShow("Ativo Imobilizado - Ativo Imobilizado")
            self.oHelper.Screenshot("Ativos/009")
            self.oHelper.CheckResult('N1_CBASE',self.codBem)
            self.oHelper.CheckResult('N1_ITEM',self.item)
            self.oHelper.CheckResult('N1_AQUISIC',DateSystem)
            self.oHelper.CheckResult('N1_DESCRIC',self.descricao)
            self.oHelper.SetValue('N1_DESCRIC',self.descricaoEdt,              check_value=False)
            self.oHelper.Screenshot("Ativos/010")
            self.oHelper.SetButton("Confirmar")
            self.oHelper.Screenshot("Ativos/011")
            self.oHelper.WaitShow("Registro alterado com sucesso")
            self.oHelper.SetButton('Fechar')
            self.oHelper.WaitShow("Atualização de Ativos Imobilizados:")

                
            #------------------------
            # VISUALIZAR EDIÇÃO
            #------------------------
            print('---------------------------------Visualizar Alteração')
            self.oHelper.SetButton("Visualizar")
            self.oHelper.WaitShow("Ativo Imobilizado - VISUALIZAR")
            self.oHelper.Screenshot("Ativos/012") 
            self.oHelper.CheckResult('N1_CBASE',self.codBem)
            self.oHelper.CheckResult('N1_ITEM',self.item)
            self.oHelper.CheckResult('N1_AQUISIC',DateSystem)
            self.oHelper.SetValue('N1_DESCRIC',self.descricaoEdt,              check_value=False)
            self.oHelper.Screenshot("Ativos/013")
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Atualização de Ativos Imobilizados:")
            
            #--------------------
            # EXCLUIR Ativos
            #--------------------
            
            
            print('---------------------------------Excluir')
            self.oHelper.SetButton("Outras Ações","Excluir")
            self.oHelper.WaitShow("Tem certeza que deseja excluir o item abaixo?")
            self.oHelper.Screenshot("Ativos/014")
            self.oHelper.CheckResult('N1_CBASE',self.codBem)
            self.oHelper.CheckResult('N1_ITEM',self.item)
            self.oHelper.CheckResult('N1_AQUISIC',DateSystem)
            self.oHelper.SetValue('N1_DESCRIC',self.descricaoEdt,              check_value=False)
            self.oHelper.SetButton("Confirmar")
            
            self.oHelper.WaitShow("Registro excluído com sucesso")
            self.oHelper.Screenshot("Ativos/015")
            self.oHelper.SetButton('Fechar')
            self.oHelper.WaitShow("Atualização de Ativos Imobilizados:")
            
            
            self.oHelper.AssertTrue()

        except Exception as e:
            self.oHelper.registrar_erro(e)
            raise e
        finally:
            self.oHelper.salvar_relatorio()
        
        print("------------------------------------------------")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_cadastro_Ativos")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
        
    

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ATFA012('test_cadastro_Ativos'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
