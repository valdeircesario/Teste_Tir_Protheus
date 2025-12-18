from tir import Webapp
from os import getcwd
import unittest
from datetime import datetime
from time import sleep

DateSystem = datetime.today().strftime('%d/%m/%Y')

#---------------------------------------------------
#CRUD DE PONTO FIXO  E EDIÇÃO DE PONTO EXISTENTE , E ENVIO PARA O AD
#---------------------------------------------------

# cd c:\Users\97137227104\Desktop\cloneTirProthus\tir\tests; C:\Users\97137227104\Desktop\cloneTirProthus\.venv\Scripts\python.exe PXPEA41/test_PXPEA41.py

class PXPEA41(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.filial = '02DF0001'
        cls.descricao = 'TESTE INCLUSAO DE PONTO FIXO'
        cls.descricaoEdit = 'TESTE EDITADO PONTO FIXO'
        cls.telefone = '(61)888888888'
        cls.telefoneEdit = '(61)XXXXXXXXXX'
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', DateSystem, '02', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Atualizações > Especificos > Ponto Fixo")

    def test_Ponto_fixo(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        self.oHelper.WaitShow("Ponto Fixo")
        
        #------------------------
        #INCLUIR
        #------------------------
        self.oHelper.SetButton("Incluir")
        self.oHelper.WaitShow("Ponto Fixo Poupex - INCLUIR")
        
        self.oHelper.SetFocus("ZW_DESCRIC")
        self.oHelper.SetValue("ZW_DESCRIC", self.descricao)
        self.oHelper.WaitFieldValue("ZW_DESCRIC", self.descricao)
        self.oHelper.SetKey("TAB")
        sleep(0.2)
        
        self.oHelper.SetFocus("ZW_TELEFON")
        self.oHelper.SetValue("ZW_TELEFON", self.telefone)
        self.oHelper.WaitFieldValue("ZW_TELEFON", self.telefone)
        self.oHelper.SetKey("TAB")
        sleep(0.2)
        
        if not self.oHelper.CheckResult("ZW_TELEFON", self.telefone):
            self.oHelper.Screenshot(filename="erro_preenchimento.png")

        #------------------------
        # CONFIRMAR INCLUSÃO
        #------------------------
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Registro inserido com sucesso.")
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Ponto Fixo")
        sleep(0.2)
        
        #------------------------
        #VISUALIZA
        #------------------------
        
        self.oHelper.SetButton("Outras Ações", "Visualizar")
        self.oHelper.WaitShow("Ponto Fixo Poupex - VISUALIZAR")
        self.oHelper.CheckResult("ZW_DESCRIC", self.descricao)
        self.oHelper.CheckResult("ZW_TELEFON", self.telefone)
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Ponto Fixo")
        sleep(0.2)
            
        #------------------------
        # EDITAR
        #------------------------
        
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow("Ponto Fixo Poupex - ALTERAR")
        self.oHelper.SetFocus("ZW_DESCRIC")
        self.oHelper.SetValue("ZW_DESCRIC", self.descricaoEdit)
        self.oHelper.WaitFieldValue("ZW_DESCRIC", self.descricaoEdit)
        self.oHelper.SetKey("TAB")
        sleep(0.2)
        
        self.oHelper.SetFocus("ZW_TELEFON")
        self.oHelper.SetValue("ZW_TELEFON", self.telefoneEdit)
        self.oHelper.WaitFieldValue("ZW_TELEFON", self.telefoneEdit)
        self.oHelper.SetKey("TAB")
        sleep(0.2)

        # Tira print se não avançar
        if not self.oHelper.CheckResult("ZW_TELEFON", self.telefoneEdit):
            self.oHelper.Screenshot(filename="erro_preenchimento.png")

        #------------------------
        # CONFIRMAR EDIÇÃO
        #------------------------
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        
        #------------------------
        #EXCLUIR
        #------------------------
        
        self.oHelper.WaitShow("Ponto Fixo")
        self.oHelper.SetButton("Outras Ações", "Excluir")
        self.oHelper.WaitShow("Tem certeza que deseja excluir o item abaixo?")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Registro excluído com sucesso.")
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Ponto Fixo")
        sleep(0.2)
        
        #------------------------
        #TESTE DE EDIÇÃO DE UM REGISTRO INEXISTENTE
        #------------------------
        
        self.oHelper.SetButton("Outras Ações", "Pesquisar")
        self.oHelper.SetButton("Parâmetro")
        self.oHelper.SetValue("Codigo", "000011")
        self.oHelper.SetButton("Ok")
        sleep(0.2)
        
        self.oHelper.SetButton("Alterar")
        sleep(0.2)
        
        self.oHelper.WaitShow("Ponto Fixo Poupex - ALTERAR")
        
        
        valor_anterior_tel   = self.oHelper.GetValue("ZW_TELEFON")# Armazena valor anterior do telefone para restauração posterior
        
        self.oHelper.SetFocus("ZW_TELEFON")
        self.oHelper.SetValue("ZW_TELEFON", self.telefoneEdit)
        self.oHelper.WaitFieldValue("ZW_TELEFON", self.telefoneEdit)
        self.oHelper.SetKey("TAB")
        sleep(0.3)
        
        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Registro alterado com sucesso.")
        self.oHelper.SetButton("Fechar")
        sleep(0.2)
        self.oHelper.WaitShow("Ponto Fixo")
        
        # -------------------------
        # VISUALIZAÇÃO DA EDIÇÃO
        # -------------------------
        self.oHelper.SetButton("Outras Ações","Visualizar")
        self.oHelper.WaitShow("Ponto Fixo Poupex - VISUALIZAR")
        self.oHelper.CheckResult("ZW_TELEFON", self.telefoneEdit)
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Ponto Fixo")
        sleep(0.2)
        
        # -------------------------
        # RESTAURA VALORES ANTERIORES
        # -------------------------
        
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow("Ponto Fixo Poupex - ALTERAR")
        self.oHelper.SetFocus("ZW_TELEFON")
        self.oHelper.SetValue("ZW_TELEFON", valor_anterior_tel)
        self.oHelper.WaitFieldValue("ZW_TELEFON", valor_anterior_tel)
        self.oHelper.SetKey("TAB")
        sleep(0.3)
        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Registro alterado com sucesso.")
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Ponto Fixo")
        sleep(0.2)
        
        # -------------------------
        # EDITAR REGISTRO INEXISTENTE - FINALIZAR TESTE CAMPO DESCRIÇÃO
        # -------------------------
        self.oHelper.SetButton("Outras Ações", "Pesquisar")
        self.oHelper.SetButton("Parâmetro")
        self.oHelper.SetValue("Codigo", "000021")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Alterar")
        sleep(0.2)
        self.oHelper.WaitShow("Ponto Fixo Poupex - ALTERAR")
        
        valor_anterior_desc   = self.oHelper.GetValue("ZW_DESCRIC")# Armazena valor da decição para restauração posterior
        
        self.oHelper.SetFocus("ZW_DESCRIC")
        self.oHelper.SetValue("ZW_DESCRIC", self.descricaoEdit)
        self.oHelper.WaitFieldValue("ZW_DESCRIC", self.descricaoEdit)
        self.oHelper.SetKey("TAB")
        sleep(0.3)
        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Registro alterado com sucesso.")
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Ponto Fixo")
        sleep(0.2)
        
        # -------------------------
        # VISUALIZAR EDIÇÃO  
        # -------------------------
        self.oHelper.SetButton("Outras Ações","Visualizar")
        self.oHelper.WaitShow("Ponto Fixo Poupex - VISUALIZAR")
        self.oHelper.CheckResult("ZW_DESCRIC", self.descricaoEdit)
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Ponto Fixo")
        sleep(0.2)
        
        # -------------------------
        # RESTAURA VALORES ANTERIORES
        # -------------------------
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow("Ponto Fixo Poupex - ALTERAR")
        self.oHelper.SetFocus("ZW_DESCRIC")
        self.oHelper.SetValue("ZW_DESCRIC", valor_anterior_desc)
        self.oHelper.WaitFieldValue("ZW_DESCRIC", valor_anterior_desc)
        self.oHelper.SetKey("TAB")
        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Registro alterado com sucesso.")
        self.oHelper.SetButton("Fechar")
        sleep(0.2) 
        self.oHelper.WaitShow("Ponto Fixo")
        
        #------------------------
        #TESTE DE ENVIO E PONTO FIXO PARA O AD
        #---------------------------------
        
        self.oHelper.SetButton("Outras Ações", "Atualizar AD")
        self.oHelper.WaitShow("Esta rotina envia todos os funcionarios vinculados aos ponto fixos para atualizar telefone no AD!")
        self.oHelper.SetButton("Sim")
        sleep(0.2) 
    
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(PXPEA41('test_Ponto_fixo'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)