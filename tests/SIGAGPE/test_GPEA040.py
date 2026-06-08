from tir import Webapp
from os import getcwd
import unittest
from datetime import datetime
from time import sleep
DateSystem = datetime.today().strftime('%d/%m/%Y')

 # # python -m pytest tests/SIGAGPE/test_GPEA040.py -v -s --html=reports/report_GPEA040.html --self-contained-html

#------------------------------------------
#-- Teste GPEA040 - Cadastro de Verbas
#------------------------------------------


class GPEA040(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       
        cls.CodVerba = '222'
        cls.Descricao = 'TESTE DE VERBA'
        cls.DescricaoEdit = 'GRATIFICAÇÕES'
        cls.filial = '01'
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Atualizações > Definições Cálculo > Verbas")

    def test_incluir_verba(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        self.oHelper.WaitShow("Cadastro de Verbas")
        self.oHelper.Screenshot("Verba/001")
        
        self.oHelper.SetButton("Incluir")
        sleep(1)
        self.oHelper.WaitShow("Cadastro de Verbas - INCLUIR")
        self.oHelper.Screenshot("Verba/002")
        self.oHelper.SetValue("RV_COD", self.CodVerba)
        self.oHelper.SetValue("RV_DESC", self.Descricao)
        self.oHelper.SetValue("RV_TIPOCOD", "1 - Provento")
        self.oHelper.SetValue("RV_CODCORR", "001")
        self.oHelper.SetValue("RV_CODFOL", "0048")
        self.oHelper.SetValue("RV_TIPO", "V - Valor")
        self.oHelper.SetKey("TAB")
        self.oHelper.Screenshot("Verba/003") 
        self.oHelper.SetButton("Confirmar")

        if self.oHelper.IfExists("Atenção!"):
            self.oHelper.Screenshot("Verba/004")
            self.oHelper.WaitShow("O(s)  seguinte(s) campos (e)sao obrigatorios na eSocial.")
            self.oHelper.SetButton("Fechar")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertFalse()

        if self.oHelper.IfExists("Atenção!"):
            self.oHelper.Screenshot("Verba/005")
            self.oHelper.WaitShow("Ocorreram inconsistências na validação.")
            self.oHelper.SetButton("Fechar")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertFalse()

        if self.oHelper.IfExists("Registro inserido com sucesso"): 
            self.oHelper.Screenshot("Verba/006") 
            self.oHelper.SetButton("Fechar")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertFalse()       
        
        self.oHelper.WaitShow("Cadastro de Verbas")
        self.oHelper.Screenshot("Verba/007")
        #-------------------------
        # Visualização da inclusão
        #-------------------------
        self.oHelper.SetButton("Visualizar")

        self.oHelper.WaitShow("Cadastro de Verbas - VISUALIZAR")
        self.oHelper.Screenshot("Verba/008")
        self.oHelper.CheckResult("RV_COD", self.CodVerba)
        self.oHelper.CheckResult("RV_DESC", self.Descricao)
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Cadastro de Verbas")

        #---------------------------
        # Editar a Verba Incluída
        #---------------------------
        self.oHelper.SetButton("Alterar")
        sleep(1) 
        self.oHelper.WaitShow("Cadastro de Verbas - ALTERAR")
        self.oHelper.Screenshot("Verba/009")
        self.oHelper.SetValue("RV_DESC", self.DescricaoEdit)
        self.oHelper.SetButton("Confirmar")
        sleep(1)

        if self.oHelper.IfExists("Atenção!"):
            self.oHelper.Screenshot("Verba/010")
            self.oHelper.WaitShow("O(s)  seguinte(s) campos (e)sao obrigatorios na eSocial.")
            self.oHelper.SetButton("Fechar")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertFalse()

        if self.oHelper.IfExists("Atenção!"):
            self.oHelper.Screenshot("Verba/011")
            self.oHelper.WaitShow("Ocorreram inconsistências na validação.")
            self.oHelper.SetButton("Fechar")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertFalse()

        if self.oHelper.IfExists("Registro alterado com sucesso."): 
            self.oHelper.Screenshot("Verba/012") 
            self.oHelper.SetButton("Fechar")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertFalse()       
        
        self.oHelper.WaitShow("Cadastro de Verbas")
        self.oHelper.Screenshot("Verba/013")

        #-------------------------
        # exclusão da Verba Incluída
        #-------------------------

        self.oHelper.SetButton("Outras Ações", "Excluir")

        if self.oHelper.IfExists("Atenção"): 
            self.oHelper.Screenshot("Verba/014")
            self.oHelper.WaitShow("Confirma a exclusäo da Verba?")
            self.oHelper.SetButton("Sim") 
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertFalse()

        if self.oHelper.IfExists("Atenção"):
            self.oHelper.Screenshot("Verba/015") 
            self.oHelper.WaitShow("Deseja gerar Log?")
            self.oHelper.SetButton("Não") 
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertFalse()

        self.oHelper.WaitShow("Tem certeza que deseja excluir o item abaixo?")
        self.oHelper.WaitShow("Esta operação não poderá ser desfeita após a confirmação da exclusão.")
        self.oHelper.Screenshot("Verba/016")
        self.oHelper.SetButton("Confirmar")

        if self.oHelper.IfExists("Registro excluído com sucesso."): 
            self.oHelper.Screenshot("Verba/017")
            self.oHelper.SetButton("Fechar") 
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertFalse()

        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_incluir_verba")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")



    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA040('test_incluir_verba'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)