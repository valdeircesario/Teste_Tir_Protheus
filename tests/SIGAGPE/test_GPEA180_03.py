from tir import Webapp
from pytest import mark
import unittest
import os
from os import getcwd
from datetime import date
from datetime import datetime, timedelta
from time import sleep

from utilis.click_pageview import click_pageview_visible_button

DateSystem = datetime.today().strftime('%d/%m/%Y')

# TRANSFERENCIA FUNCIONÁRIO PARA OUTRO DEPARTAMENTO /TRANSMITIR PARA O AD/ GERAÇÃO GLPI
# ESTE TESTE E INTEGRADO COM A TRANSFERENCIA, ROINA > GPEA180 COM A ROTINA PXGPEA36

class GPEA180(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.filial = '01'
        cls.mat = '00124'   
        cls.DP_destino = '0012' 
        cls.dataref = (datetime.today()-timedelta(days=5)).strftime("%d/%m/%Y")# AJUSTAR DATA PARA PERIODO EM ABERTO 
    
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', cls.dataref, '02', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Atualizações > Funcionários > Transferências")
        

    def test_transferencia_funcionario_de_departamento_transmitir_AD_gerar_GLPI(self):

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
            
        
        sleep(2)
        print('--------------------------Pesquisando funcionario')    
        self.oHelper.WaitShow("Transferências")
        self.oHelper.Screenshot("AD_GLPI_01.png")
        self.oHelper.SetButton("Pesquisar")
        self.oHelper.SetButton("Parâmetros")
        self.oHelper.SetValue("Filial", self.filial)
        self.oHelper.SetValue("Matricula", self.mat)
        self.oHelper.SetButton("Ok")
        self.oHelper.Screenshot("AD_GLPI_02.png")
        self.oHelper.SetButton('Outras Ações', 'Transferir')

        print('--------------------------Transferindo')
        self.oHelper.WaitShow('Transferências - TRANSFERIR')
        self.oHelper.ClickBox("Matricula", self.mat,   grid_number=1)
        self.oHelper.Screenshot("AD_GLPI_03.png")
        self.oHelper.SetButton('Confirmar')
        
        self.oHelper.WaitShow('Transferências - TRANSFERIR')
        self.oHelper.Screenshot("AD_GLPI_04.png")
        
        self.oHelper.SetValue("RA_DEPTO", self.DP_destino, grid=True, grid_number=2)
        self.oHelper.LoadGrid()
        self.oHelper.Screenshot("AD_GLPI_05.png")
        self.oHelper.SetButton('Confirmar')

        print('--------------------------Confirmar Transferencia')  
        self.oHelper.WaitShow("Confirma a Transferência ? ")
        self.oHelper.Screenshot("AD_GLPI_06.png")
        self.oHelper.SetButton('Sim')   
        sleep(2) 
        
        if self.oHelper.IfExists("O funcionário é responsavel por um departamento, deseja desassociá-lo?"):
            self.oHelper.Screenshot("AD_GLPI_06.1.png")
            self.oHelper.SetButton('Sim')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        sleep(2)   
        if self.oHelper.IfExists("Deseja enviar e-mail dessa Transferência?"):
            self.oHelper.Screenshot("AD_GLPI_07.png")
            self.oHelper.SetButton('Sim')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
    
        print('--------------------------Conferindo os Logs')
        self.oHelper.WaitShow("Log de Ocorrencias - Gestão de Pessoal - Versao 12")
        self.oHelper.ClickLabel("Em Disco")
        self.oHelper.Screenshot("AD_GLPI_11.png")
        self.oHelper.SetButton("OK")
        sleep(10)
        click_pageview_visible_button(self.oHelper, "Ampliar (+)")
        self(2)
        click_pageview_visible_button(self.oHelper, "Ampliar (+)")
        self(2)
        click_pageview_visible_button(self.oHelper, "Ampliar (+)")
        self(2)
        self.oHelper.Screenshot("GPEA180_12.png")
        self.oHelper.SetButton("Sair")
        sleep(5)
        self.oHelper.SetButton("Cancelar")
        self.oHelper.WaitShow("Transferências")
        self.oHelper.Screenshot("AD_GLPI_13.png")
        
        sleep(10)
        
        #-------------------------
        # ACESSO A ROTINA PXGPEA36
        #--------------------------
        print('--------------------------Acessando a rotina do AD')
        self.oHelper.SetLateralMenu("Atualizações > Especificos > Manutencao AD")
        
        self.oHelper.WaitShow("Bloqueio e Desbloqueio AD") 
        self.oHelper.Screenshot("AD_GLPI_14.png")
        
        #-------------------------------
        # FILTAR O FUNCIONARIO PARA O AD
        #--------------------------------
        print('--------------------------Filtrar Funcionario')
        self.oHelper.SetButton("Filtrar")
        self.oHelper.WaitShow("Gerenciador de Filtros")
        self.oHelper.Screenshot("AD_GLPI_15.png")
        self.oHelper.SetButton("Criar Filtro")
        self.oHelper.SetValue("Campo","Matricula",check_value=False)
        self.oHelper.SetValue("Expressão",self.mat,check_value=False)
        self.oHelper.SetButton('Adicionar')
        self.oHelper.Screenshot("AD_GLPI_16.png")
        self.oHelper.SetButton("Salvar")
        filtro_texto = f"Matricula Igual a '{self.mat}'"
        self.oHelper.ClickCheckBox(filtro_texto,1)
        self.oHelper.Screenshot("AD_GLPI_17.png")
        self.oHelper.SetButton("Aplicar filtros selecionados")
        self.oHelper.Screenshot("AD_GLPI_18.png")
        
        # DESCE ATE A CRID DA DATA PARA TRANSFERIR AD
        #--------------------------------------------


        print('--------------------------sleciona o funcionario e faz a verificação')
        self.oHelper.ScrollGrid(column="Data Inicial", match_value = self.dataref, grid_number=1)
        self.oHelper.Screenshot("AD_GLPI_19.png")
        
        self.oHelper.SetButton("Alterar") 
        self.oHelper.WaitShow("Bloqueio/Desbloqueio acesso ao AD - ALTERAR")
        self.oHelper.Screenshot("AD_GLPI_20.png")
        
        self.oHelper.ScrollGrid(column="Data Final", match_value = self.dataref, grid_number=1)
        
        self.oHelper.SetKey("RIGHT",grid=True,step=0.1, wait_change=False)
        self.oHelper.SetKey("RIGHT",grid=True,step=0.1, wait_change=False)
        self.oHelper.SetKey("RIGHT",grid=True,step=0.1, wait_change=False)
        self.oHelper.SetKey("RIGHT",grid=True,step=0.1, wait_change=False)
        self.oHelper.SetKey("RIGHT",grid=True,step=0.1, wait_change=False)
        self.oHelper.SetKey("RIGHT",grid=True,step=0.1, wait_change=False)
        self.oHelper.SetKey("ENTER", grid=True)
        self.oHelper.Screenshot("AD_GLPI_21.png")
        self.oHelper.SetButton("Ok")
        self.oHelper.LoadGrid()
        
        self.oHelper.SetButton('Fechar')
        self.oHelper.Screenshot("AD_GLPI_22.png")
        
        
        #---------------------
        # TRANSFERIR AD
        #------------------
        print('--------------------------Transmitir para o AD')
        self.oHelper.SetButton("Outras Ações", "Transmitir")
        
        sleep(1) 
        if self.oHelper.IfExists("Não haverá integração com AD, pois esse ambiente não é produção!"):
            self.oHelper.Screenshot("AD_GLPI_23.png")
            self.oHelper.SetButton('Fechar')
        else:
            self.oHelper.AssertTrue()
        
        self.oHelper.IfExists("Item adicionado com sucesso: Alteração UTA/EQUIPE do Funcionário")
        self.oHelper.Screenshot("AD_GLPI_24.png")
        self.oHelper.SetButton('Fechar')
        self.oHelper.Screenshot("AD_GLPI_27.png")
        
        #-------------------------------------
        # VALIDAR A TRANFERÊNCIA DO ADD E O GLPI
        #-------------------------------------
        
        print('--------------------------Validar a transmição do AD')
        self.oHelper.SetButton("Alterar")  
        self.oHelper.WaitShow("Bloqueio/Desbloqueio acesso ao AD - ALTERAR")
        self.oHelper.Screenshot("AD_GLPI_28.png")
        
        self.oHelper.ScrollGrid(column="Data Final", match_value = self.dataref, grid_number=1)
        
        self.oHelper.SetKey("RIGHT",grid=True,step=0.1, wait_change=False)
        self.oHelper.SetKey("RIGHT",grid=True,step=0.1, wait_change=False)
        self.oHelper.SetKey("RIGHT",grid=True,step=0.1, wait_change=False)
        self.oHelper.SetKey("RIGHT",grid=True,step=0.1, wait_change=False)
        self.oHelper.SetKey("RIGHT",grid=True,step=0.1, wait_change=False)
        self.oHelper.SetKey("RIGHT",grid=True,step=0.1, wait_change=False)

        self.oHelper.SetKey("ENTER", grid=True)
        self.oHelper.Screenshot("AD_GLPI_29.png")  
        self.oHelper.SetButton("OK")
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Bloqueio e Desbloqueio AD")

        self.oHelper.AssertTrue()
        
        print("------------------------------------------------")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_transferencia_funcionario_de_departamento_transmitir_AD_gerar_GLPI")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
    

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA180('test_transferencia_funcionario_de_departamento_transmitir_AD_gerar_GLPI'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
