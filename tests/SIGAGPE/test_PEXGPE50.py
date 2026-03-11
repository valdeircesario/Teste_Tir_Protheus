from pytest import mark
import unittest
from time import sleep
from os import getcwd
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')

#----------------------------------------------------------------
# INCORPORAÇÃO DE FUNÇÃO E CONFERENCIA NO HISTORICO SALARIAL PELA ROTINA GPEA250
#----------------------------------------------------------------

class PEXGPE50(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        from tir.technologies.core.base import By
        from tir import Webapp
                                                                        
        self.filial = '02DF0001'
        self.Matricula = '228383'
        self.Nome = "CLAUDIO RODRIGUES ALEXANDRE"
        self.IdentFuncao = "000610"
        self.TipoAumento = '005'
        self.dataref = (datetime.today()-timedelta(days=15)).strftime("%d/%m/%Y")
        
        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', DateSystem, '02', self.filial, '07')
        
        self.oHelper.SetLateralMenu("Atualizações > Especificos > Funcoes Incorporadas")
        #self.oHelper.SetButton('Confirmar') -- observar essas linha, em meu ambiete de trabalho, o browser não visualiza a tela de trocar modulos.
        

    def test_funcções_incorporativas(self):

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
            
            
        self.oHelper.WaitShow("Valores Incorporados")
        self.oHelper.Screenshot("Val_Incorporado_01") 
        
        #------------------------------------
        # PESQUISAR O FUNCIONARIO LANÇAMENTO
        #------------------------------------ 
        self.oHelper.SearchBrowse(self.filial + self.Matricula + self.Nome, key="Filial+matricula+Nome")
        sleep(0.5)
        self.oHelper.Screenshot("Val_Incorporado_02") 
        
        self.oHelper.SetButton("Alterar")
        sleep(1)
        
        #-----------------------------
        # INCLUINDO FUNÇÃO INCORPORADA
        #-----------------------------
        self.oHelper.WaitShow("Funcionários - ALTERAR")
        self.oHelper.Screenshot("Val_Incorporado_03")
        self.oHelper.SetValue("Tipo","02 - VPNI Salár",         grid=True,     grid_number=1,        check_value=False)
        self.oHelper.SetValue("Ident.Funcao","000610",          grid=True,     grid_number=1)
        self.oHelper.SetValue("Item FC","00005",                grid=True,     grid_number=1)
        self.oHelper.SetValue("Data Inicio",DateSystem,         grid=True,     grid_number=1,        check_value=False)
        self.oHelper.SetValue("Tipo Aumento",self.TipoAumento,  grid=True,     grid_number=1,        check_value=False)
        self.oHelper.SetValue("Observacao","TESTE AUTOMATIZADO",grid=True,     grid_number=1,        check_value=False)
        self.oHelper.LoadGrid()
        self.oHelper.Screenshot("Val_Incorporado_04")
        self.oHelper.SetButton("Confirmar")
        sleep(90)
        
        self.oHelper.WaitShow("Registro alterado com sucesso.")
        self.oHelper.Screenshot("Val_Incorporado_05")
        self.oHelper.SetButton('Fechar')
        self.oHelper.Screenshot("Val_Incorporado_06")
        
        
        #----------------------------------------------------------------------
        # CONFERIR HISTORICO SALARIAL PARA VALIDAR A ALTERAÇÃO: ROTINA > GPEA250   mensagem Registro alterado com sucesso.
        #------------------------------------------------------------------------
        
        self.oHelper.SetLateralMenu("Atualizações > Funcionários > Histórico Salário")
        #self.oHelper.SetButton('Confirmar') -- observar essas linha, em meu ambiete de trabalho, o browser não visualiza a tela de trocar modulos.
        sleep(2)
        self.oHelper.WaitShow('Alteraçöes Salariais')
        self.oHelper.SearchBrowse(self.filial + self.Matricula + self.Nome, key="Filial+matricula+Nome")
        sleep(2)
        self.oHelper.Screenshot("Val_Incorporado_07")
        self.oHelper.SetButton('Visualizar')
        sleep(2)
        self.oHelper.WaitShow('Funcionários - VISUALIZAR')
        self.oHelper.Screenshot("Val_Incorporado_08")
        
        self.oHelper.ScrollGrid("Data Aumento", match_value = DateSystem,         grid_number=2)
        self.oHelper.LoadGrid()
        self.oHelper.Screenshot("Val_Incorporado_09")
        self.oHelper.SetButton('Fechar')
        sleep(2)
        
        #-----------------------------
        # EXCLUIR FUNÇÃO INCORPORADA
        #-----------------------------
        
        self.oHelper.SetLateralMenu("Atualizações > Especificos > Funcoes Incorporadas")
        #self.oHelper.SetButton('Confirmar') -- observar essas linha, em meu ambiete de trabalho, o browser não visualiza a tela de trocar modulos.
        sleep(2)
        
        self.oHelper.WaitShow("Valores Incorporados")
        self.oHelper.Screenshot("Val_Incorporado_10") 
        
        #------------------------------------
        # PESQUISAR O FUNCIONARIO DA INCLUSÃO DA FUNÇAÕ INCORPORADA
        #------------------------------------ 
        self.oHelper.SearchBrowse(self.filial + self.Matricula + self.Nome, key="Filial+matricula+Nome")
        sleep(2)
        self.oHelper.Screenshot("Val_Incorporado_11") 
        
        self.oHelper.SetButton("Alterar")
        sleep(1)
        
        #-----------------------------
        # EXCLUIR FUNÇÃO INCORPORADA
        #-----------------------------
        self.oHelper.WaitShow("Funcionários - ALTERAR")
        self.oHelper.Screenshot("Val_Incorporado_12")
        self.oHelper.ScrollGrid("Ident.Funcao", match_value = self.IdentFuncao,         grid_number=1)
        self.oHelper.SetKey("DELETE", grid=True, grid_number=1)
        self.oHelper.LoadGrid()
        sleep(2)
        self.oHelper.Screenshot("Val_Incorporado_13")
        self.oHelper.SetButton("Confirmar")
        sleep(90)
        
        self.oHelper.WaitShow("Registro alterado com sucesso.")
        self.oHelper.Screenshot("Val_Incorporado_14")
        self.oHelper.SetButton('Fechar')
        self.oHelper.Screenshot("Val_Incorporado_15")
        
        self.oHelper.AssertTrue()
       
     
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_funcções_incorporativas")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
        
            

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(PEXGPE50('test_funcções_incorporativas'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
