import re
from tir import Webapp
from pytest import mark
import unittest
import os
from os import getcwd
from datetime import date
from datetime import datetime, timedelta
from time import sleep

DateSystem = datetime.today().strftime('%d/%m/%Y')

# TRANSFERENCIA FUNCIONÁRIO PARA OUTRO DEPARTAMENTO /TRANSMITIR PARA O AD/ GERAÇÃO GLPI
# ESTE TESTE E INTEGRADO COM A TRANSFERENCIA, ROINA > GPEA180 COM A ROTINA PXGPEA36

class GPEA180_03(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.filial = '02DF0001'
        self.mat = '228399' # O TESTE DEVE SEMPRE PROCURAR UM FUNCIONARIO DO CENTRO DE CUSTOS 000000677 PARA MELHOR RESULTADO
        self.DP_destino = '000000879' # USE SEMPRE UM DOS DEPATAMENTOS AQUI  >  DP_destino = 000000866,000000868,000000869,000000870,000000876,000000877,000000879,000000880,000000881,000000882,000000883,000000884,000000885,000000886,000000894
        self.dataref = (datetime.today()-timedelta(days=5)).strftime("%d/%m/%Y")# AJUSTAR DATA PARA PERIODO EM ABERTO 
    
        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', self.dataref, '02', self.filial, '07')
        self.oHelper.SetLateralMenu("Atualizações > Especificos > Manutencao AD")
        

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
            
        """ if self.oHelper.IfExists("Departamento possui centro de custo diferente do centro de custos do funcionário"):
            self.oHelper.SetButton('Fechar')
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
        
            self.oHelper.AssertTrue()
        sleep(2)
            
        self.oHelper.WaitShow("Transferências")
        self.oHelper.Screenshot("AD_GLPI_01.png")
        self.oHelper.SetButton("Pesquisar")
        self.oHelper.SetButton("Parâmetros")
        self.oHelper.SetValue("Filial", self.filial)
        self.oHelper.SetValue("Matricula", self.mat)
        self.oHelper.SetButton("Ok")
        self.oHelper.Screenshot("AD_GLPI_02.png")
        self.oHelper.SetButton('Outras Ações', 'Transferir')
        sleep(0.8)
        
        self.oHelper.WaitShow('Transferências - TRANSFERIR')
        self.oHelper.ClickBox("Matricula", self.mat,   grid_number=1)
        self.oHelper.Screenshot("AD_GLPI_03.png")
        self.oHelper.SetButton('Confirmar')
        
        self.oHelper.WaitShow('Transferências - TRANSFERIR')
        self.oHelper.Screenshot("AD_GLPI_04.png")
        
        self.Nome = self.oHelper.GetValue("Nome", grid=True, grid_number=1)
        print(f" {self.Nome}")
        
        self.oHelper.SetValue("RA_DEPTO", self.DP_destino, grid=True, grid_number=2)
        self.oHelper.LoadGrid()
        self.oHelper.Screenshot("AD_GLPI_05.png")
        self.oHelper.SetButton('Confirmar')
          
        if self.oHelper.IfExists("Confirma a Transferência ? "):
            self.oHelper.Screenshot("AD_GLPI_06.png")
            self.oHelper.SetButton('Sim')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        sleep(0.5) 
        
        if self.oHelper.IfExists("O funcionário é responsavel por um departamento, deseja desassociá-lo?"):
            self.oHelper.Screenshot("AD_GLPI_06.1.png")
            self.oHelper.SetButton('Sim')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        sleep(0.5)   
        if self.oHelper.IfExists("Deseja enviar e-mail dessa Transferência?"):
            self.oHelper.Screenshot("AD_GLPI_07.png")
            self.oHelper.SetButton('Sim')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            sleep(0.5)     
            
        if self.oHelper.IfExists("Deseja inserir a Data da Portaria?"):
            self.oHelper.Screenshot("AD_GLPI_08.png")
            self.oHelper.SetButton('Sim')
            self.oHelper.SetValue("Data da Portaria", self.dataref)
            self.oHelper.Screenshot("AD_GLPI_09.png")
            self.oHelper.SetButton('Confirmar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        sleep(0.9)
        self.oHelper.Screenshot("AD_GLPI_10.png") 
        
        if self.oHelper.IfExists("Retorno - Ifractal"):
            self.oHelper.Screenshot("AD_GLPI_07.png")
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue() 
        
        sleep(0.5)
        self.oHelper.WaitShow("Log de Ocorrencias - Gestão de Pessoal - Versao 12")
        if self.oHelper.IfExists("Log de Ocorrencias - Gestão de Pessoal - Versao 12"):
            self.oHelper.ClickLabel("Em Disco")
            self.oHelper.Screenshot("AD_GLPI_11.png")
            self.oHelper.SetButton("OK")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
        sleep(25)
        self.oHelper.Screenshot("AD_GLPI_12.png")
        self.oHelper.SetButton("Sair")
        sleep(10)
        self.oHelper.SetButton("Cancelar")
        self.oHelper.Screenshot("AD_GLPI_13.png")
        
        sleep(10)
        
        #-------------------------
        # ACESSO A ROTINA PXGPEA36
        #--------------------------
        
        self.oHelper.SetLateralMenu("Atualizações > Especificos > Manutencao AD") """
        
        self.oHelper.WaitShow("Bloqueio e Desbloqueio AD") 
        self.oHelper.Screenshot("AD_GLPI_14.png")
        
        #-------------------------------
        # FILTAR O FUNCIONARIO PARA O AD
        #--------------------------------
        
        self.oHelper.SetButton("Filtrar")
        sleep(0.2)
        self.oHelper.WaitShow("Gerenciador de Filtros")
        self.oHelper.Screenshot("AD_GLPI_15.png")
        self.oHelper.SetButton("Criar Filtro")
        sleep(0.5)
        self.oHelper.SetValue("Campo","Matricula",check_value=False)
        self.oHelper.SetValue("Expressão",self.mat,check_value=False)
        self.oHelper.SetButton('Adicionar')
        self.oHelper.Screenshot("AD_GLPI_16.png")
        sleep(1)
        self.oHelper.SetButton("Salvar")
        filtro_texto = f"Matricula Igual a '{self.mat}'"
        
        self.oHelper.ClickCheckBox(filtro_texto,1)
        self.oHelper.Screenshot("AD_GLPI_17.png")
        self.oHelper.SetButton("Aplicar filtros selecionados")
        sleep(2)
        self.oHelper.Screenshot("AD_GLPI_18.png")
        
        self.oHelper.ScrollGrid(column="Data Inicial", match_value = self.dataref, grid_number=1)
        self.oHelper.Screenshot("AD_GLPI_19.png")
        
        """ self.oHelper.SetButton("Alterar") 
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
        sleep(1)
        self.oHelper.Screenshot("AD_GLPI_21.png")
        self.oHelper.SetButton("Ok")
        sleep(0.5)
        self.oHelper.LoadGrid()
        
        self.oHelper.SetButton('Fechar')
        self.oHelper.Screenshot("AD_GLPI_22.png") """
        
        
        #---------------------
        # TRANSMITIR PARA AD
        #---------------------
        
        self.oHelper.SetButton("Outras Ações", "Transmitir")
        
        sleep(1) 
        if self.oHelper.IfExists("Não haverá integração com AD, pois esse ambiente não é produção!"):
            self.oHelper.Screenshot("AD_GLPI_23.png")
            self.oHelper.SetButton('Fechar')
        else:
            self.oHelper.AssertTrue()
        sleep(1)
        
        
        if self.oHelper.IfExists("Item adicionado com sucesso:"):
            self.oHelper.Screenshot("AD_GLPI_24.png")
            self.oHelper.SetButton('Fechar')
        else:
            self.oHelper.AssertTrue()
            
        self.oHelper.Screenshot("AD_GLPI_25.png")
    
            
        sleep(1) 
        if self.oHelper.IfExists("Não haverá integração com AD, pois esse ambiente não é produção!"):
            self.oHelper.Screenshot("AD_GLPI_26.png")
            self.oHelper.SetButton('Fechar')
        else:
            self.oHelper.AssertTrue()
        sleep(1)
        self.oHelper.Screenshot("AD_GLPI_27.png")
        
        #---------------------------------------
        # VALIDAR A TRANFERÊNCIA DO ADD E O GLPI
        #---------------------------------------
        
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
        sleep(1)
        self.oHelper.Screenshot("AD_GLPI_29.png")  
        self.oHelper.SetButton("OK")
        sleep(1)
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Bloqueio e Desbloqueio AD")

        self.oHelper.AssertTrue()
        
        print("------------------------------------------------")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_transferencia_funcionario_de_departamento_transmitir_AD_gerar_GLPI")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
    

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(0001('test_transferencia_funcionario_de_departamento_transmitir_AD_gerar_GLPI'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
