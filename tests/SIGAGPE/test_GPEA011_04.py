from tir import Webapp
from os import getcwd
from pytest import mark
import unittest
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')

#-----------------------------------------
# LANÇAMENTO RETROATIVO ASSISTENCIA MEDICA
#-----------------------------------------

class GPEA011(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.filial = '01'
        cls.cpf = '01530041180'
        cls.matricula = '227900'

        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.diaant = (datetime.today()+timedelta(days=-110)).strftime("%d/%m/%Y") # Ajustar a data para o periodo em aberto!!!!
        cls.oHelper.Setup('SIGAMDI', cls.diaant, '99', cls.filial, '07')
        cls.oHelper.Program('GPEA011')
        cls.oHelper.SetButton('Confirmar')
        #self.oHelper.SetButton("Fechar")

    def test_teste_assitencia_medica(self):

        #----------
        # INCLUIR
        #----------
        

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()

        #-----------------------
        # Incluir Assitencia
        #------------------------
        print('--------------------Pesquisar')   
        self.oHelper.SetButton("Pesquisar")
        self.oHelper.SetValue("Filial", self.filial)
        self.oHelper.SetValue("Matricula", self.matricula)
        self.oHelper.SetButton("OK")


        print('-----------------------Incluir')
        self.oHelper.Screenshot("GPEA011_04_01")
        self.oHelper.SetButton("Outras Ações")
        self.oHelper.ClickMenuPopUpItem("Lancamentos")
        self.oHelper.ClickMenuPopUpItem("Val.Futuros")
        self.oHelper.ClickMenuPopUpItem("Alterar")
        self.oHelper.WaitShow("Valores Futuros")
        self.oHelper.Screenshot("GPEA011_04_02")
        self.oHelper.ScrollGrid(column="Codigo Verba", match_value= "525")
        self.oHelper.SetKey("DOWN",                   grid=True,                        wait_change=False)
        self.oHelper.SetValue('Codigo Verba',  "600",            grid=True,             check_value=False)
        self.oHelper.SetValue('Vr.Principal',  "50,00", direction='right', grid=True,   check_value=False)
        self.oHelper.SetValue('Nr. Parcelas',  "1",     direction='right', grid=True,   check_value=False)
        self.oHelper.LoadGrid()
        self.oHelper.Screenshot("GPEA011_04_03")
        
        self.oHelper.SetButton("Salvar")
        self.oHelper.WaitShow("Atenção")
        self.oHelper.SetButton("Confirma")
        self.oHelper.WaitShow("Cadastro Geral")

        #------------
        # VISUALIZAR
        #------------

        print('--------------------Visualizar')
        self.oHelper.SetButton("Outras Ações")
        self.oHelper.ClickMenuPopUpItem("Lancamentos")
        self.oHelper.ClickMenuPopUpItem("Val.Futuros")
        self.oHelper.ClickMenuPopUpItem("Visualizar")
        self.oHelper.WaitShow("Valores Futuros")
        self.oHelper.Screenshot("GPEA011_04_05")
        self.oHelper.SetButton("Confirmar")

        #-----------
        # EXCLUIR
        #-----------

        print('------------------------Excluir')
        self.oHelper.SetButton("Outras Ações")
        self.oHelper.ClickMenuPopUpItem("Lancamentos")
        self.oHelper.ClickMenuPopUpItem("Val.Futuros")
        self.oHelper.ClickMenuPopUpItem("Alterar")
        self.oHelper.WaitShow("Valores Futuros")
        self.oHelper.Screenshot("GPEA011_04_06")
        self.oHelper.LoadGrid()
        self.oHelper.ScrollGrid(column='Dt.Movimento', match_value= self.diaant)
        self.oHelper.LoadGrid()
        self.oHelper.SetKey("DELETE",        grid=True,                         check_value=False)
        self.oHelper.Screenshot("GPEA011_04_07")
        self.oHelper.SetButton("Salvar")
        self.oHelper.WaitShow("Cadastro Geral")
        self.oHelper.Screenshot("GPEA011_04_08")
        self.oHelper.AssertTrue()

        #--------------
        # CONFIRMAR EXCLUSÃO
        #--------------
        
        print('-----------------Confirmar Exclusão')
        self.oHelper.SetButton("Outras Ações")
        self.oHelper.ClickMenuPopUpItem("Lancamentos")
        self.oHelper.ClickMenuPopUpItem("Val.Futuros")
        self.oHelper.ClickMenuPopUpItem("Visualizar")
        self.oHelper.WaitShow("Valores Futuros")
        self.oHelper.Screenshot("GPEA011_04_09")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.Screenshot("GPEA011_04_10")
        self.oHelper.WaitShow("Cadastro Geral")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA011('test_test_teste_assitencia_medica'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)