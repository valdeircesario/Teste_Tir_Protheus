from tir import Webapp
from os import getcwd
from pytest import mark
import unittest
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')

#-----------------------------------------
# LANÇAMENTO RETROATIVO ASSISTENCIA MEDICA
#-----------------------------------------

class GPEA011_04(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        self.filial = '02DF0001'
        self.cpf = '01530041180'
        self.matricula = '227900'

        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.diaant = (datetime.today()+timedelta(days=-110)).strftime("%d/%m/%Y") # Ajustar a data para o periodo em aberto!!!!
        self.oHelper.Setup('SIGAMDI', self.diaant, '02', self.filial, '07')
        self.oHelper.Program('GPEA011')
        #self.oHelper.SetButton('Confirmar')
        #self.oHelper.SetButton("Fechar")

    def test_GPEA011_04(self):

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
            
        """ self.oHelper.SetButton("Pesquisar")
        self.oHelper.SetValue("Filial", self.filial)
        self.oHelper.SetValue("Matricula", self.matricula)
        self.oHelper.SetButton("OK") """

        self.oHelper.SearchBrowse(self.filial + self.cpf, key="Filial+cpf")
        self.oHelper.Screenshot("GPEA011_04_01")
        self.oHelper.SetButton("Outras Ações")
        self.oHelper.ClickMenuPopUpItem("Lancamentos")
        self.oHelper.ClickMenuPopUpItem("Val.Futuros")
        self.oHelper.ClickMenuPopUpItem("Alterar")
        self.oHelper.WaitShow("Valores Futuros")
        self.oHelper.Screenshot("GPEA011_04_02")
        self.oHelper.ScrollGrid(column="Codigo Verba", match_value= "525", grid_number=1)
        self.oHelper.SetKey("DOWN",                                                   grid=True)
        self.oHelper.SetValue('Codigo Verba',  "600",                                 grid=True)
        self.oHelper.SetValue('Vr.Principal',  "50,00", direction='right',            grid=True)
        self.oHelper.SetValue('Nr. Parcelas',  "1",     direction='right',            grid=True)
        self.oHelper.LoadGrid()
        self.oHelper.Screenshot("GPEA011_04_03")
        
        self.oHelper.SetButton("Salvar")
        if self.oHelper.IfExists("Atenção"):
            self.oHelper.SetButton("Confirma")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
        self.oHelper.WaitShow("Cadastro Geral")

        #------------
        # VISUALIZAR
        #------------


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


        self.oHelper.SetButton("Outras Ações")
        self.oHelper.ClickMenuPopUpItem("Lancamentos")
        self.oHelper.ClickMenuPopUpItem("Val.Futuros")
        self.oHelper.ClickMenuPopUpItem("Alterar")
        self.oHelper.WaitShow("Valores Futuros")
        self.oHelper.Screenshot("GPEA011_04_06")
        self.oHelper.LoadGrid()
        self.oHelper.ScrollGrid(column='Dt.Movimento', match_value= self.diaant, grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetKey("DELETE",                                               grid=True)
        self.oHelper.Screenshot("GPEA011_04_07")
        self.oHelper.SetButton("Salvar")
        self.oHelper.WaitShow("Cadastro Geral")
        self.oHelper.Screenshot("GPEA011_04_08")
        self.oHelper.AssertTrue()

        #--------------
        # CONFIRMAR EXCLUSÃO
        #--------------

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
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA011_04('test_GPEA011_04'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)