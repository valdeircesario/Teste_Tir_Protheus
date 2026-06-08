from os import getcwd

from tir import Webapp
from pytest import mark
import unittest
from datetime import datetime, timedelta
from time import sleep


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
        cls.cnpj = '93087344000160'
        cls.email = 'fornecedorteste@gmail.com' 
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '01')
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros > Fornecedores")
        cls.oHelper.SetButton('Confirmar')
        

    def test_cadastro_fornecedores(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')
            

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')
        
        sleep(5)
        self.oHelper.WaitShow("Fornecedores") 
        
        
        #--------------
        # INCLUISÃO
        #-------------
        
             
        self.oHelper.Screenshot("FORNECEDORES_01")
        self.oHelper.SetButton("Incluir")
        sleep(2) 
        self.oHelper.WaitShow("Fornecedores - Incluir")
        self.oHelper.Screenshot("FORNECEDORES_02")   
        self.oHelper.SetValue('A2_LOJA',"1542",                     check_value=False)
        self.oHelper.SetValue('A2_NOME',self.razaoSocial,           check_value=False)
        self.oHelper.SetValue('A2_XOBS','TESTE',                    check_value=False)
        self.oHelper.SetValue('A2_NREDUZ',self.fantasia,            check_value=False)
        self.oHelper.SetValue('A2_END',self.endereco,               check_value=False)
        self.oHelper.SetValue('A2_NR_END',self.numero,              check_value=False)
        self.oHelper.SetValue('A2_BAIRRO',self.bairro,              check_value=False)
        self.oHelper.SetValue('A2_EST','DF',                        check_value=False)
        self.oHelper.Screenshot("FORNECEDORES_03")
        self.oHelper.SetValue('A2_COD_MUN','00108',                 check_value=False)
        self.oHelper.SetValue('A2_MUN','BRASILIA',                  check_value=False)
        self.oHelper.SetValue('A2_CEP','70330040',                  check_value=False)
        self.oHelper.SetValue('A2_CGC',self.cnpj,                   check_value=False)
        self.oHelper.SetValue('A2_DDI','55',                        check_value=False)
        self.oHelper.SetValue('A2_PAIS','105',                      check_value=False)
        self.oHelper.SetValue('A2_EMAIL',self.email,                check_value=False)
        self.oHelper.Screenshot("FORNECEDORES_04")
        
        
        self.oHelper.SetButton("Confirmar")
        sleep(5)
        if self.oHelper.IfExists("Registro inserido com sucesso"):
            self.oHelper.Screenshot("FORNECEDORES_05")
            self.oHelper.SetButton('Fechar')
            
        self.oHelper.Screenshot("FORNECEDORES_06")    
        sleep(5)
        
        #-----------------------
        # VISUALIZAR INCLUSÃO 
        #------------------------
        
        
        self.oHelper.SetButton("Visualizar")
        sleep(2)
        self.oHelper.WaitShow("Fornecedores - Visualizar")
        self.oHelper.Screenshot("FORNECEDORES_07")
        
        self.oHelper.CheckResult('A2_NOME', self.razaoSocial)
        self.oHelper.CheckResult('A2_NREDUZ',self.fantasia)
        self.oHelper.CheckResult('A2_END',self.endereco)
        self.oHelper.CheckResult('A2_BAIRRO',self.bairro)
        self.oHelper.CheckResult('A2_CEP','70330040')
        self.oHelper.CheckResult('A2_CGC',self.cnpj)
        self.oHelper.CheckResult('A2_EMAIL',self.email)
        self.oHelper.Screenshot("FORNECEDORES_08")
        
        self.oHelper.SetButton("Fechar")
        
        #-------------------
        # EDITAR FORNECEDOR
        #-------------------
        
        
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow("Fornecedores - Alterar")
        self.oHelper.Screenshot("FORNECEDORES_09")
        self.oHelper.SetValue('A2_NOME',self.razaoSocialEdt,           check_value=False)
        self.oHelper.SetValue('A2_XOBS','TESTE EDIT',                    check_value=False)
        self.oHelper.SetValue('A2_NREDUZ',self.fantasiaEdt,            check_value=False)
        self.oHelper.Screenshot("FORNECEDORES_10")
        self.oHelper.SetButton("Confirmar")
        sleep(5)
        self.oHelper.Screenshot("FORNECEDORES_11")
        if self.oHelper.IfExists("Registro alterado com sucesso"):
            self.oHelper.SetButton('Fechar')
            
        #------------------------
        # VISUALIZAR EDIÇÃO
        #------------------------
        self.oHelper.SetButton("Visualizar")
        sleep(2)
        self.oHelper.WaitShow("Fornecedores - Visualizar")
        self.oHelper.Screenshot("FORNECEDORES_12") 
        self.oHelper.CheckResult('A2_NOME', self.razaoSocialEdt)
        self.oHelper.CheckResult('A2_NREDUZ',self.fantasiaEdt)
        self.oHelper.Screenshot("FORNECEDORES_13")
        self.oHelper.SetButton("Fechar")
        
        #--------------------
        # EXCLUIR FORNECEDOR
        #--------------------
        
        
        
        self.oHelper.SetButton("Outras Ações","Excluir")
        sleep(5)
        self.oHelper.Screenshot("FORNECEDORES_14")
        self.oHelper.WaitShow("Tem certeza que deseja excluir o item abaixo?")
        self.oHelper.SetButton("Confirmar")
        sleep(35)
        
        if self.oHelper.IfExists("Registro excluído com sucesso"):
            self.oHelper.Screenshot("FORNECEDORES_15")
            self.oHelper.SetButton('Fechar')
        
        
        self.oHelper.AssertTrue()
        
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
