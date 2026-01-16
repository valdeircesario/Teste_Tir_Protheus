from tir.technologies.core.base import By
from tir import Webapp
from pytest import mark
import unittest
from time import sleep
from os import getcwd
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')

#.\venv\Scripts\python.exe -m pytest tests/Outros/test_pxgpea24.py -s

#------------------------
# Lançamento Avulso
#------------------------

class PXGPEA24(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.filial = '02DF0001'
        self.Matricula = '228419'
        self.Nome = 'MURILO AUGUSTO DA SILVA'
        self.dataref = (datetime.today()-timedelta(days=10)).strftime("%d/%m/%Y")
        self.Movimentacao = '1 - Titular'
        self.Movimentacaoedit = '3  - Ambos'
        self.ValorTitular = '256'
        self.ValorDependente = '128'
        self.Verba01 = '771'
        self.Verba02 = '773'
        self.Valor = '150'
        

        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', self.dataref, '02', self.filial, '07')
        
        #self.oHelper.SetLateralMenu("Atualizações > Lançamentos > Por Funcionário ")
        self.oHelper.SetLateralMenu("Atualizações > Lançamentos > Lancamentos Avulso")
        
        #self.oHelper.SetLateralMenu("Atualizações > Lançamentos > Lancamentos Avulso")
        #self.oHelper.SetButton('Confirmar')
        #self.oHelper.SetButton("Fechar")

    def test_Lançamento_Avulso(self):

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
            
        
        """ self.oHelper.WaitShow("Lançamentos por Período")
        
        self.oHelper.SearchBrowse(self.filial + self.Matricula, key="Filial+matricula+Nome")
        sleep(0.3)
        
        self.oHelper.SetButton("Alterar")
        sleep(5)
        
        self.oHelper.SetKey("F6")
        self.oHelper.WaitShow("Processando")
        sleep(40)
        
        self.oHelper.SetButton("OK")
        
        self.oHelper.SetKey("F7")
        sleep(5)
        
        self.oHelper.WaitShow("Lançamentos por Funcionário")
        self.oHelper.Screenshot("contracheque.png")
        
        if self.oHelper.IfExists("Codigo Verba"):
            self.oHelper.CheckResult("Codigo Verba",self.Verba,grid=True)
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
        
        
        
        
        
        self.oHelper.SetButton('Confirmar')
        
        self.oHelper.SetButton("Salvar")
        sleep(10) """
    
        #self.oHelper.SetLateralMenu("Atualizações > Lançamentos > Lancamentos Avulso")
        self.oHelper.SearchBrowse(self.filial + self.Matricula  + self.Nome, key="Filial+matricula+Nome")
        sleep(10)
        
        self.oHelper.WaitShow("Lançamentos Avulsos")
        self.oHelper.SetButton("Manutenção")
        sleep(5)
        self.oHelper.WaitShow("Funcionários - MANUTENÇÃO")
        
        
        self.oHelper.SetFocus("Verba","620")

        #oHelper.ScrollGrid(column="Verba", match_value="620", grid_number=2)
        self.oHelper.CheckResult("Verba", "704", grid=True, line=2)
        self.oHelper.SetKey("DOWN", grid= True) 
        self.oHelper.SetValue("Dt. Inclusao", self.dataref,                  grid= True, grid_number=2, check_value=False)
        self.oHelper.SetValue('Verba',  self.Verba01,                          grid= True, grid_number=2, check_value=False)
        self.oHelper.SetValue('Valor',  self.Valor,                          grid=True, grid_number=2, check_value=False)
        self.oHelper.SetValue('Dt. Venc.', self.dataref,                     grid=True, grid_number=2, check_value=False)
        self.oHelper.SetValue('Observacao', "TESTE AUTOMATIZADO",            grid=True, grid_number=2, check_value=False)
        self.oHelper.SetValue('Roteiro', "FOL",                              grid=True, grid_number=2, check_value=False)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Confirmar")
        
        
        
        
        
        
        
    
        
        
        """ self.oHelper.SetFocus("ZD_DESCONV")
        self.oHelper.SetValue("ZD_DESCONV", self.descricao)
        self.oHelper.SetKey("TAB")
       
        
        
        self.oHelper.SetValue("ZD_TPMOV",self.Movimentacao)
        self.oHelper.SetValue("ZD_TPALTSA","003")
        
        
        
        self.oHelper.WaitShow("Histórico")
         
        self.oHelper.SetValue("ZD_DATAINI", self.dataref, grid=True, grid_number=1)
        self.oHelper.SetValue("ZD_VLRTIT", self.ValorTitular,  grid=True, grid_number=1)
        self.oHelper.SetValue('ZD_VLRDEP', self.ValorDependente, grid=True, grid_number=1)
        self.oHelper.SetValue('ZD_PD', self.Verba, grid=True, grid_number=1)
        self.oHelper.SetValue('ZD_PD1', self.Verba, grid=True, grid_number=1)
        self.oHelper.LoadGrid()

        
        
        
        self.oHelper.SetFocus("Confirmar")
        self.oHelper.Setbutton("Confirmar")
        self.oHelper.WaitShow("Registro inserido com sucesso.")
        self.oHelper.SetButton("Fechar")
      
         # Visualizar

        self.oHelper.SetButton("Visualizar")
        self.oHelper.WaitShow("Tipos de Convenios - VISUALIZAR")
        
        self.oHelper.CheckResult("ZD_DESCONV", self.descricao)
        self.oHelper.CheckResult("Tp de Mov.", self.Movimentacao)
        self.oHelper.SetButton("Fechar")

        # Alterar

        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow("Tipos de Convenios - ALTERAR")
        
        
        self.oHelper.SetFocus("ZD_DESCONV")
        self.oHelper.SetValue("ZD_DESCONV", self.descricaoEdit)
        self.oHelper.SetKey("TAB")
        sleep(0.3)
        self.oHelper.SetKey("ENTER")
        sleep(0.3)
        
        self.oHelper.SetFocus("Tp de Mov.")
        self.oHelper.SetValue("ZD_TPMOV",self.Movimentacaoedit)
        #self.oHelper.SetValue("ZD_HISTORI","1 - Sim")
        
        self.oHelper.SetValue("ZD_TPALTSA","003")
        
        self.oHelper.SetFocus("Confirmar")
        self.oHelper.Setbutton("Confirmar")
        self.oHelper.WaitShow("Registro alterado com sucesso.")
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Tipos de Convênios")

        # Excluir
        
        

        self.oHelper.SetButton("Outras Ações", "Excluir")
        self.oHelper.WaitShow("Tem certeza que deseja excluir o item abaixo?")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Tipos de Convênios") """
        
        
        

       
        #self.oHelper.LoadGrid()

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(PXGPEA24('test_Lançamento_Avulso'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
