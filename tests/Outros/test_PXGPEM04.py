from tir.technologies.core.base import By
from tir import Webapp
from pytest import mark
import unittest
from time import sleep
from os import getcwd
from datetime import datetime, timedelta
from tir.technologies.core.base import By
DateSystem = datetime.today().strftime('%d/%m/%Y')

#  .\venv\Scripts\python.exe -m pytest tests/test_PXGPEM04.py -s
#------------------------
# CRUD TIPO DE COVENIO
#------------------------

class PXGPEM04(unittest.TestCase):# PEXGPE28
    @classmethod
    def setUpClass(self):
        self.filial = '02DF0001'
        self.descricao = 'TESTE INCLUSAO'
        self.descricaoEdit = 'TESTE ALTERADO'
        self.dataref = (datetime.today()-timedelta(days=30)).strftime("%d/%m/%Y")
        self.Movimentacao = '1 - Titular'
        self.Movimentacaoedit = '3 - Ambos'
        self.ValorTitular = '256'
        self.ValorDependente = '128'
        self.Verba = '010'
        self.ValorTitular01 = '256'
        self.ValorDependente01 = '128'
        self.DataFim = (datetime.today()+timedelta(days=30)).strftime("%d/%m/%Y")
        

        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', self.dataref, '02', self.filial, '07')
        self.oHelper.SetLateralMenu("Atualizações > Especificos > Tipo de Convenio")
        #self.oHelper.SetButton('Confirmar')
        #self.oHelper.SetButton("Fechar")

    def test_Convenio(self):

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
            
        
        self.oHelper.WaitShow("Tipos de Convênios")
        self.oHelper.SetButton("Incluir")
        
        self.oHelper.WaitShow("Tipos de Convenios - INCLUIR")
        
        self.oHelper.SetFocus("ZD_DESCONV")
        self.oHelper.SetValue("ZD_DESCONV", self.descricao)
        self.oHelper.SetKey("TAB")  
        self.oHelper.SetValue("ZD_TPMOV",self.Movimentacao)
        self.oHelper.SetValue("ZD_TPALTSA","003")  
        
            
        self.oHelper.WaitShow("Histórico")
        self.oHelper.SetValue("Data Inicio", self.dataref, grid=True, grid_number=1,check_value=False)
        self.oHelper.SetKey("TAB", grid=True)
        self.oHelper.SetValue("Vlr Titular", self.ValorTitular, grid= True, grid_number=1,check_value=False)
        self.oHelper.SetKey("TAB", grid=True)    
        self.oHelper.SetValue("Vlr Dependen", self.ValorDependente, grid=True, grid_number=1,check_value=False)
        self.oHelper.SetKey("TAB", grid=True)
        self.oHelper.SetValue("Verba", self.Verba, grid=True, grid_number=1,check_value=False)
        self.oHelper.SetKey("TAB", grid=True)
        self.oHelper.SetValue("Verba s/Inci", self.Verba, grid=True, grid_number=1,check_value=False)
        self.oHelper.SetKey("TAB", grid=True)
        self.oHelper.LoadGrid()
        sleep(0.2)
        
        self.oHelper.SetButton("Confirmar")
        
        self.oHelper.WaitShow("Registro inserido com sucesso.")
        self.oHelper.SetButton("Fechar")
        
        self.oHelper.WaitShow("Tipos de Convênios")
        
        #------------------------
        # VISUALIZAR CONVENIO
        #------------------------
        
        self.oHelper.SetButton("Visualizar")
        self.oHelper.WaitShow("Tipos de Convenios - VISUALIZAR")
        self.oHelper.Screenshot("convenio.png")
        self.oHelper.SetButton("Fechar")
        sleep(0.3)
        self.oHelper.WaitShow("Tipos de Convênios")
        
        
        #------------------------
        # ALTERAR CONVENIO
        #------------------------
        
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow("Tipos de Convenios - ALTERAR")
        self.oHelper.SetValue("ZD_DESCONV", self.descricaoEdit)
        self.oHelper.SetKey("TAB")
        sleep(0.3)
        self.oHelper.SetValue("ZD_TPMOV",self.Movimentacaoedit)
        
        self.oHelper.WaitShow("Histórico")
        self.oHelper.SetValue("Data Inicio", self.dataref, grid=True, grid_number=2,check_value=False)
        self.oHelper.SetKey("TAB", grid=True)
        self.oHelper.SetValue("Vlr Titular", self.ValorTitular01, grid= True, grid_number=2,check_value=False)
        self.oHelper.SetKey("TAB", grid=True)    
        self.oHelper.SetValue("Vlr Dependen", self.ValorDependente01, grid=True, grid_number=2,check_value=False)
        self.oHelper.SetKey("TAB", grid=True)
        self.oHelper.SetValue("Verba", self.Verba, grid=True, grid_number=2,check_value=False)
        self.oHelper.SetKey("TAB", grid=True)
        self.oHelper.SetValue("Verba s/Inci", self.Verba, grid=True, grid_number=2,check_value=False)
        self.oHelper.SetKey("TAB", grid=True)
        self.oHelper.LoadGrid()
        sleep(0.2)
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Registro alterado com sucesso.") 
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Tipos de Convênios")
        
        #------------------------
        # EXCLUIR CONVENIO  
        #------------------------
        self.oHelper.SetButton("Outras Ações","Excluir")
        self.oHelper.WaitShow("Tem certeza que deseja excluir o item abaixo?")
        self.oHelper.WaitShow("Esta operação não poderá ser desfeita após a confirmação da exclusão.")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Registro excluído com sucesso.")
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Tipos de Convênios")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(PXGPEM04('test_Convenio'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
