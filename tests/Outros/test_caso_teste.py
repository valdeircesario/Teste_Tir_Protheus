from tir import Webapp
from os import getcwd
import unittest
from datetime import datetime, timedelta
from time import sleep

DateSystem = datetime.today().strftime('%d/%m/%Y')

class CASO_DE_USO(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.Mat = '225327'# 
        cls.filial = '02DF0001'
        cls.dataref = (datetime.today()-timedelta(days=5)).strftime("%d/%m/%Y")
        cls.datafim = (datetime.today()-timedelta(days=0)).strftime("%d/%m/%Y")
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI',cls.dataref , '02', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Atualizações > Especificos > Manutencao AD")

    def test_Ponto_fixo_caso_de_uso(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')
        else:
            self.oHelper.AssertTrue()

        
        self.oHelper.WaitShow("Bloqueio e Desbloqueio AD") 
        self.oHelper.Screenshot("AD_01.png")
        
        #-------------------------------
        # FILTAR O FUNCIONARIO PARA O AD
        #--------------------------------
        self.oHelper.SetButton("Filtrar")
        sleep(0.2)
        self.oHelper.WaitShow("Gerenciador de Filtros")
        self.oHelper.Screenshot("AD_02.png")
        self.oHelper.SetButton("Criar Filtro")
        sleep(0.5)
        self.oHelper.SetValue("Campo","Matricula",check_value=False)
        self.oHelper.SetValue("Expressão",self.Mat,check_value=False)
        self.oHelper.SetButton('Adicionar')
        self.oHelper.Screenshot("AD_03.png")
        sleep(1)
        self.oHelper.SetButton("Salvar")
        filtro_texto = f"Matricula Igual a '{self.Mat}'"
        
        self.oHelper.ClickCheckBox(filtro_texto,1)
        self.oHelper.Screenshot("AD_04.png")
        self.oHelper.SetButton("Aplicar filtros selecionados")
        sleep(2)
        self.oHelper.Screenshot("AD_05.png") 
        
        # DESCE ATE A CRID DA DATA PARA TRANSFERIR AD
        self.oHelper.ScrollGrid(column="Data Inicial", match_value = self.dataref, grid_number=1)
        self.oHelper.Screenshot("AD_06.png")
        
        self.oHelper.SetButton("Alterar") 
        self.oHelper.WaitShow("Bloqueio/Desbloqueio acesso ao AD - ALTERAR")
        self.oHelper.Screenshot("AD_07.png")
        
        self.oHelper.ScrollGrid(column="Data Final", match_value = self.dataref, grid_number=1)
        
        self.oHelper.SetKey("RIGHT",grid=True,step=0.1, wait_change=False)
        self.oHelper.SetKey("RIGHT",grid=True,step=0.1, wait_change=False)
        self.oHelper.SetKey("RIGHT",grid=True,step=0.1, wait_change=False)
        self.oHelper.SetKey("RIGHT",grid=True,step=0.1, wait_change=False)
        self.oHelper.SetKey("RIGHT",grid=True,step=0.1, wait_change=False)
        self.oHelper.SetKey("RIGHT",grid=True,step=0.1, wait_change=False)

        self.oHelper.SetKey("ENTER", grid=True)
        sleep(1)
        self.oHelper.Screenshot("AD_08.png")
        self.oHelper.SetButton("Ok")
        sleep(0.5)
        self.oHelper.LoadGrid()
        
        self.oHelper.SetButton('Fechar')
        self.oHelper.Screenshot("AD_09.png")
        
        
        #---------------------
        # TRANSFERIR AD
        #------------------
        
        self.oHelper.SetButton("Outras Ações", "Transmitir")
        
        sleep(1) 
        if self.oHelper.IfExists("Não haverá integração com AD, pois esse ambiente não é produção!"):
            self.oHelper.Screenshot("AD_12.png")
            self.oHelper.SetButton('Fechar')
        else:
            self.oHelper.AssertTrue()
        sleep(1)
        
        if self.oHelper.IfExists("Item adicionado com sucesso: Alteração UTA/EQUIPE do Funcionário"):
            self.oHelper.Screenshot("AD_10.png")
            self.oHelper.WaitShow("Item adicionado com sucesso:")#Alteração UTA/EQUIPE do Funcionário WESLEY VALENTE LIMA (293696)
            self.oHelper.Screenshot("Ponto_Fixo_02")
            self.oHelper.SetButton('Fechar')
        else:
            self.oHelper.AssertTrue()
            
        self.oHelper.Screenshot("AD_11.png")
            
        sleep(1) 
        if self.oHelper.IfExists("Não haverá integração com AD, pois esse ambiente não é produção!"):
            self.oHelper.Screenshot("AD_12.png")
            self.oHelper.SetButton('Fechar')
        else:
            self.oHelper.AssertTrue()
        sleep(1)
        
        #-------------------------------------
        # VALIDAR A TRANFERÊNCIA DO ADD E O GLPI
        #-------------------------------------
        
        self.oHelper.SetButton("Alterar")
        
        self.oHelper.WaitShow("Bloqueio/Desbloqueio acesso ao AD - ALTERAR")
        self.oHelper.Screenshot("AD_13.png")
        
        self.oHelper.ScrollGrid(column="Data Final", match_value = self.dataref, grid_number=1)
        
        self.oHelper.SetKey("RIGHT",grid=True,step=0.1, wait_change=False)
        self.oHelper.SetKey("RIGHT",grid=True,step=0.1, wait_change=False)
        self.oHelper.SetKey("RIGHT",grid=True,step=0.1, wait_change=False)
        self.oHelper.SetKey("RIGHT",grid=True,step=0.1, wait_change=False)
        self.oHelper.SetKey("RIGHT",grid=True,step=0.1, wait_change=False)
        self.oHelper.SetKey("RIGHT",grid=True,step=0.1, wait_change=False)

        self.oHelper.SetKey("ENTER", grid=True)
        sleep(1)
        self.oHelper.Screenshot("AD_08.png")
        self.oHelper.WaitShow(self.datafim)
        self.oHelper.Screenshot("AD_15.png")
        self.oHelper.SetButton("OK")
        sleep(1)
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Bloqueio e Desbloqueio AD")
        
        
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CASO_DE_USO('test_Ponto_fixo_caso_de_uso'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)