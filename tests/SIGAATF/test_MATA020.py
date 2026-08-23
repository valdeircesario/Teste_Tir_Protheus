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

# python -m pytest tests/SIGAATF/test_MATA020.py -v -s --html=reports/report_MATA020.html --self-contained-html

# TESTE DE CADASTRO DE FORNECEDORES

class MATA020(unittest.TestCase):	
    @classmethod
    def setUpClass(cls):
        cls.filial = '01'
        cls.razaoSocial = 'TESTE FORNECEDOR'
        cls.razaoSocialEdt = 'TESTE FORNECEDOR EDITADO'
        cls.fantasia = "TESTE AUTOMATIZADO"
        cls.fantasiaEdt = "TESTE AUT EDITADO"
        cls.endereco = "QUADRA SHIN QI 1 CONJUNTO 8"
        cls.numero = '20'
        cls.bairro = "SETOR NORTE"
        cls.cnpj = '73391799000168'
        cls.email = 'fornecedorteste@gmail.com' 
        configfile = getcwd() + '\\config.json'
        # 1. Instância base do TIR
        webapp_base = Webapp(configfile)
                
        # 2. Encapsula com o Agente de Relatório
        cls.oHelper = TirReportAgent(
            tir_instance=webapp_base,
            cod_modulo="01",
            nome_modulo="Ativo Fixo",
            ct_nome="test_MATA020",
            descricao="Inclusão, Visualização, Alteração  e exclusão de Fornecedor"
        )
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '01')
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros > Fornecedores")
        cls.oHelper.SetButton('Confirmar')
        

    def test_cadastro_fornecedores(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')
            

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        try:
        
            self.oHelper.WaitShow("Fornecedores") 
            
            
            #--------------
            # INCLUISÃO
            #-------------
            
                
            self.oHelper.Screenshot("Fornecedor/001")
            print('-----------------------------Incluir')
            self.oHelper.SetButton("Incluir")
            self.oHelper.WaitShow("Fornecedores - Incluir")
            self.oHelper.Screenshot("Fornecedor/002") 
            self.oHelper.SetValue('A2_COD',"1542",                      check_value=False)  
            self.oHelper.SetValue('A2_LOJA',"10",                       check_value=False)
            self.oHelper.SetValue('A2_NOME',self.razaoSocial,           check_value=False)
            self.oHelper.SetValue('A2_NREDUZ',self.fantasia,            check_value=False)
            self.oHelper.SetValue('A2_END',self.endereco,               check_value=False)
            self.oHelper.SetValue('A2_BAIRRO',self.bairro,              check_value=False)
            self.oHelper.SetValue('A2_EST','DF',                        check_value=False)
            self.oHelper.Screenshot("Fornecedor/003")
            self.oHelper.SetValue('A2_COD_MUN','00108',                 check_value=False)
            self.oHelper.SetValue('A2_MUN','BRASILIA',                  check_value=False)
            self.oHelper.SetValue('A2_CEP','70330040',                  check_value=False)
            self.oHelper.SetValue('Tipo',"J - Juridico",                check_value=False)
            self.oHelper.SetValue('A2_CGC',self.cnpj,                   check_value=False)
            self.oHelper.SetValue('A2_DDI','55',                        check_value=False)
            self.oHelper.SetValue('A2_DDD',"61",                        check_value=False)
            self.oHelper.SetValue('A2_TEL',"98745212",                  check_value=False)
            self.oHelper.SetValue('A2_PAIS','105',                      check_value=False)
            self.oHelper.SetValue('A2_EMAIL',self.email,                check_value=False)
            self.oHelper.Screenshot("Fornecedor/004")  
            
            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Registro inserido com sucesso")
            self.oHelper.Screenshot("Fornecedor/005")
            self.oHelper.SetButton('Fechar')
            self.oHelper.WaitShow("Fornecedores")     
            self.oHelper.Screenshot("Fornecedor/006")    
            
            #-----------------------
            # VISUALIZAR INCLUSÃO 
            #------------------------
            
            print('---------------------------------Visualizar')
            self.oHelper.SetButton("Visualizar")
            self.oHelper.WaitShow("Fornecedores - Visualizar")
            self.oHelper.Screenshot("Fornecedor/007")   
            self.oHelper.CheckResult('A2_NOME', self.razaoSocial)
            self.oHelper.CheckResult('A2_NREDUZ',self.fantasia)
            self.oHelper.CheckResult('A2_END',self.endereco)
            self.oHelper.CheckResult('A2_BAIRRO',self.bairro)
            self.oHelper.CheckResult('A2_CEP','70330040')
            self.oHelper.CheckResult('A2_CGC',self.cnpj)
            self.oHelper.CheckResult('A2_EMAIL',self.email)
            self.oHelper.Screenshot("Fornecedor/008")    
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Fornecedores")
            
            #-------------------
            # EDITAR FORNECEDOR
            #-------------------
            
            print('---------------------------------Aterar')
            self.oHelper.SetButton("Alterar")
            self.oHelper.WaitShow("Fornecedores - Alterar")
            self.oHelper.Screenshot("Fornecedor/009")
            self.oHelper.SetValue('A2_NOME',self.razaoSocialEdt,           check_value=False)
            self.oHelper.SetValue('A2_NREDUZ',self.fantasiaEdt,            check_value=False)
            self.oHelper.Screenshot("Fornecedor/010")
            self.oHelper.SetButton("Confirmar")
            sleep(5)
            self.oHelper.Screenshot("Fornecedor/011")
            if self.oHelper.IfExists("Registro alterado com sucesso"):
                self.oHelper.SetButton('Fechar')

            self.oHelper.WaitShow("Fornecedores")

                
            #------------------------
            # VISUALIZAR EDIÇÃO
            #------------------------
            print('---------------------------------Visualizar Alteração')
            self.oHelper.SetButton("Visualizar")
            self.oHelper.WaitShow("Fornecedores - Visualizar")
            self.oHelper.Screenshot("Fornecedor/012") 
            self.oHelper.CheckResult('A2_NOME', self.razaoSocialEdt)
            self.oHelper.CheckResult('A2_NREDUZ',self.fantasiaEdt)
            self.oHelper.Screenshot("Fornecedor/013")
            self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Fornecedores")
            
            #--------------------
            # EXCLUIR FORNECEDOR
            #--------------------
            
            
            print('---------------------------------Excluir')
            self.oHelper.SetButton("Outras Ações","Excluir")
            self.oHelper.Screenshot("Fornecedor/014")
            self.oHelper.WaitShow("Tem certeza que deseja excluir o item abaixo?")
            self.oHelper.SetButton("Confirmar")
            
            self.oHelper.WaitShow("Registro excluído com sucesso")
            self.oHelper.Screenshot("Fornecedor/015")
            self.oHelper.SetButton('Fechar')
            self.oHelper.WaitShow("Fornecedores")
            
            
            self.oHelper.AssertTrue()

        except Exception as e:
            self.oHelper.registrar_erro(e)
            raise e
        finally:
            self.oHelper.salvar_relatorio()
        
        print("------------------------------------------------")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_cadastro_fornecedores")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
        
    

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MATA020('test_cadastro_fornecedores'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
