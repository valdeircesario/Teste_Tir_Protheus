from tir import Webapp
from pytest import mark
import unittest
import os
from os import getcwd
from datetime import date
from datetime import datetime, timedelta
from time import sleep

#----------------------------
# TRANSFERENCIA FUNCIONÁRIO
#-----------------------------

class GPEA180(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        
        # FILIAL E MATRICULA DE ORIGEM
        self.filial = '02BA0051'
        self.mat = '209410' # SEMPRE USAR MATRICULA DIFERENTE, E VERIFICAR SE E UNICA " PODE CONTER DUAS MATRICULAR IGUAIS" 228290 ,202173,209410
        
        # FILIAL E MATRICULA DE DESTINO
        self.Fl_destino = "02DF0001"
        self.CC_destino = '000000678'
        self.DP_destino = '000000865'
        
        ## SUGESTÕES ##
        # CENTRO DE CUSTO GESIN > 000000678 // USAR ESSES DEPARTAMENTO  > 000000865,000000871,000000872,
        # 000000878,000000887,000000888,000000889,000000890,000000891,000000895

        # CENTRO DE CUSTO GESIT > 000000677 // USAR ESSES DEPARTAMENTO > 000000866,000000868,000000869,000000870,000000876,
        # 000000877,000000879,000000880,000000881,000000882,000000883,000000884,000000885,000000886,000000894
         
        self.dataref = (datetime.today()-timedelta(days=0)).strftime("%d/%m/%Y") # AJUSTAR DATAS PARA PEIODO EM ABERTO
        self.Periodo_Para = (datetime.today()+timedelta(days=-0)).strftime("%Y%m") # AJUSTAR DATAS PARA PEIODO EM ABERTO
        self.Nro_Pagto_Para = '01'
        

        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', self.dataref, '02', self.filial, '07')
        self.oHelper.SetLateralMenu("Atualizações > Funcionários > Transferências")
        

    def test_transferencia_funcionario_de_filial(self):

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
            
        if self.oHelper.IfExists("Departamento possui centro de custo diferente do centro de custos do funcionário"):
            self.oHelper.SetButton('Fechar')
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
        
            self.oHelper.AssertTrue()
        
           
        self.oHelper.WaitShow("Transferências")
        sleep(0.8)
        self.oHelper.Screenshot("GPEA180_01.png")
        self.oHelper.SetButton("Pesquisar")
        self.oHelper.SetButton("Parâmetros")
        self.oHelper.SetValue("Filial", self.filial)
        self.oHelper.SetValue("Matricula", self.mat)
        self.oHelper.SetButton("Ok")
        sleep(0.8)
        self.oHelper.Screenshot("GPEA180_02.png")
        self.oHelper.SetButton('Outras Ações', 'Transferir')
        sleep(2)
        
        self.oHelper.WaitShow('Transferências - TRANSFERIR')  
        self.oHelper.ClickBox("Matricula", self.mat,   grid_number=1)
        self.oHelper.Screenshot("GPEA180_03.png") # RECOMENDA-SE NESSA EVIDENCIA PEGAR O C CUSTO, E O DEPATAMENTO DA ULTIMA TRANFERENCIA PARA REPETIR NOVO TESTE.
        self.oHelper.SetButton('Confirmar')
        sleep(1)
        self.oHelper.Screenshot("GPEA180_04.png")
        self.oHelper.SetValue("RA_FILIAL", self.Fl_destino,  grid=True, grid_number=2)
        self.oHelper.SetValue("RA_CC", self.CC_destino,      grid=True, grid_number=2)
        self.oHelper.SetValue("RA_DEPTO", self.DP_destino,   grid=True, grid_number=2)
        self.oHelper.SetValue("RA_PROCES", "00001",          grid=True, grid_number=2)
        self.oHelper.SetValue("RA_ITEM", "0001",             grid=True, grid_number=2)
        self.oHelper.SetValue("RA_CLVL", "0001.1",           grid=True, grid_number=2)
        self.oHelper.LoadGrid()
        self.oHelper.Screenshot("GPEA180_05.png")
        self.oHelper.SetButton('Confirmar')
        sleep(2)
        
        
        if self.oHelper.IfExists("Departamento possui centro de custo diferente do centro de custos do funcionário"):
            self.oHelper.Screenshot("GPEA180_05.1.png")
            self.oHelper.SetButton('Fechar')
            sleep(0.8)
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
            
        if self.oHelper.IfExists("Departamento possui centro de custo diferente do centro de custos do funcionário"):
            self.oHelper.Screenshot("GPEA180_05.2.png")
            self.oHelper.SetButton('Fechar')
            sleep(0.8)
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
        
        
        
        self.oHelper.WaitShow("Confirma a Transferência ?")
        self.oHelper.Screenshot("GPEA180_06.png")
        
        self.oHelper.SetButton('Sim')
        sleep(5)
        
        
        if self.oHelper.IfExists("Transferências - TRANSFERIR"):
            sleep(1)
            self.oHelper.Screenshot("GPEA180_06.1.png")
            self.oHelper.SetValue("Periodo Para",self.Periodo_Para,         grid=True, grid_number=1)
            self.oHelper.SetValue("Nro. Pagto Para",self.Nro_Pagto_Para,    grid=True, grid_number=1)
            self.oHelper.LoadGrid()
            # NESSA VERIFICAÇÃO, PARA ALGUMAS TARNFERENCIAS PODEM APARECER DUAS GRIDS, ESSE TESTE PRENCHE APENAS UMA, CASO TENHA DUAS O TESTE PODE FALHAR
            # ACONSENHO TENTAR OUTRO FUNCIONARIO DE OUTRA FILIAL, OU IMPLEMANTAR LOGICA PARA TRATAR A IMPLEMANTAÇÃO
            self.oHelper.Screenshot("GPEA180_06.2.png")
            self.oHelper.SetButton('Confirmar') 
            sleep(0.8) 
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
        self.oHelper.Screenshot("GPEA180_07.png") 
        sleep(1)
        
        self.oHelper.CheckHelp(text="ATENÇÃO", button="Fechar")
        sleep(0.5)  
        self.oHelper.Screenshot("GPEA180_08.png")
                  
        
        self.oHelper.CheckHelp(text="ATENÇÃO", button="Fechar")
        sleep(1)
        
        
        if self.oHelper.IfExists("Departamento"):
            self.oHelper.WaitShow("O funcionário é responsavel por um departamento, deseja desassociá-lo?")
            self.oHelper.Screenshot("GPEA180_09.png")
            self.oHelper.SetButton('Sim')
            sleep(0.8)
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()

    
        if self.oHelper.IfExists("Deseja enviar e-mail dessa Transferência?"):
            self.oHelper.Screenshot("GPEA180_10.png")
            self.oHelper.SetButton('Sim')
            sleep(0.8)
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
            
        
        if self.oHelper.IfExists("Deseja inserir a Data da Portaria?"):
            self.oHelper.Screenshot("GPEA180_11.png")
            self.oHelper.SetButton('Sim')
            sleep(0.8)
            self.oHelper.SetValue("Data da Portaria", self.dataref)
            self.oHelper.Screenshot("GPEA180_12.png")
            self.oHelper.SetButton('Confirmar')
            sleep(0.8)
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
            
        sleep(0.9)
        self.oHelper.Screenshot("GPEA180_13.png") 
        self.oHelper.SetButton('fechar')
        sleep(0.8)
        
        sleep(10)
        self.oHelper.WaitShow("Log de Ocorrencias - Gestão de Pessoal - Versao 12")
        if self.oHelper.IfExists("Log de Ocorrencias - Gestão de Pessoal - Versao 12"):
            self.oHelper.ClickLabel("Em Disco")
            self.oHelper.Screenshot("GPEA180_14.png")
            self.oHelper.SetButton("OK")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
        sleep(25)
        self.oHelper.Screenshot("GPEA180_15.png")
        self.oHelper.SetButton("Sair")
        sleep(10)
        self.oHelper.SetButton("Cancelar")
        sleep(10)
        self.oHelper.AssertTrue()
        
        print("------------------------------------------------")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_transferencia_funcionario_de_filial")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
    

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA180('test_transferencia_funcionario_de_filial'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
