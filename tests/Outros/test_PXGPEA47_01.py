from pytest import mark
import unittest
from time import sleep
from os import getcwd
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')


#----------------------------------------------------------------
# DESLIGAMENTO E CANCELAMENTO DO JOVEM APRENDIZ
#----------------------------------------------------------------

class PXGPEA47_01(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        from tir.technologies.core.base import By
        from tir import Webapp
                                                                        
        self.filial = '02DF0001'
        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', DateSystem, '02', self.filial, '07')
        
        self.oHelper.SetLateralMenu("Atualizações > Especificos > Jovem Aprendiz")
        

    def test_desligamento_e_cancelamento_Jovem_Aprendiz(self):

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
            
        #------------------------------------
        # PESQUISAR O JOVEM APRENDIZ ATIVO
        #------------------------------------
            
        self.oHelper.WaitShow("Jovem Aprendiz")
        self.oHelper.Screenshot("jovem001")  
        sleep(0.5)
        self.oHelper.SetButton("Filtrar")
        sleep(0.5)
        self.oHelper.WaitShow("Gerenciador de Filtros")
        self.oHelper.ClickCheckBox("Situação Normal",1)
        self.oHelper.Screenshot("jovem002")
        self.oHelper.SetButton("Aplicar filtros selecionados")
        sleep(0.6) 
        self.oHelper.Screenshot("jovem003")
        
        #----------------------------
        # VISULAIZAR JOVEM APRENDIZ
        #----------------------------
        
        self.oHelper.SetButton("Outras Ações","Visualizar")
        sleep(1)
        
        self.Nome_Jovem = self.oHelper.GetValue("Nome")
        print(f"Nome do jovem aprendiz para desligamento: {self.Nome_Jovem}")
        self.oHelper.Screenshot("jovem004")
        self.oHelper.SetButton("Fechar")
        sleep(0.5)
        self.oHelper.WaitShow("Jovem Aprendiz")
    
        #----------------------------
        # DELIGAMENTO DO JOVEM APRENDIZ
        #----------------------------
        
        self.oHelper.SetButton("Outras Ações","Efetiva/Cancela - Desligamento")
        sleep(1)
        self.oHelper.SetValue("Dt. Desligamento ?",DateSystem)
        self.oHelper.SetValue("Motivo desligamento ?","7-Desligamento por abandono")
        self.oHelper.Screenshot("jovem005")
        self.oHelper.SetButton("OK")
        sleep(1)
        
        mensagem = f"O aprendiz, {self.Nome_Jovem} será desligado, podemos confirmar?"

        if self.oHelper.IfExists(mensagem):
            self.oHelper.Screenshot("jovem006")
            self.oHelper.SetButton('Sim')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertFalse()  
            
        if self.oHelper.IfExists("Aprendiz desligado com sucesso!"):
            self.oHelper.Screenshot("jovem007")
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        self.oHelper.WaitShow("Jovem Aprendiz")
        self.oHelper.Screenshot("jovem008")
        
        #------------------------
        # VISUALIDAR DESLIGAMENTO
        #------------------------
        
        self.oHelper.SetButton("Filtrar")
        sleep(0.5)
        self.oHelper.WaitShow("Gerenciador de Filtros")
        self.oHelper.ClickCheckBox("Situação Normal",1)
        self.oHelper.Screenshot("jovem009")
        self.oHelper.SetButton("Aplicar filtros selecionados")
        sleep(0.6) 
        self.oHelper.Screenshot("jovem0010")
        sleep(1) 
        self.oHelper.SearchBrowse(self.Nome_Jovem, key= "Filial+nome")
        sleep(2) 
        
        self.oHelper.Screenshot("jovem0011")
        self.oHelper.SetButton("Outras Ações","Visualizar")
        self.oHelper.CheckResult("ZRA_NOME", self.Nome_Jovem)
        self.oHelper.Screenshot("jovem0012")    
        
        self.oHelper.ClickFolder("Dados Funcionais")
        sleep(0.5)  
        self.oHelper.CheckResult("Sit. Folha", "D")  
        mensagem_esperada = "Informações do desligamento do jovem aprendiz:" 
        self.oHelper.CheckResult("Mot.Desliga", mensagem_esperada)
        self.oHelper.Screenshot("jovem0013")
        sleep(1)
        self.oHelper.SetButton("Fechar")
        sleep(0.5)
        self.oHelper.WaitShow("Jovem Aprendiz") 
        
        #----------------------------------------
        # CANCELAR DESLIGAMENTO DO JOVEM APRENDIZ
        #----------------------------------------
        
        self.oHelper.SetButton("Outras Ações","Efetiva/Cancela - Desligamento")
        sleep(1) 
        mensagem02 = f"Aprendiz, {self.Nome_Jovem} já desligado, Deseja cancelar o Desligamento?"

        if self.oHelper.IfExists(mensagem02):
            self.oHelper.Screenshot("jovem0014")
            self.oHelper.SetButton('Sim')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertFalse()
        
    
            
        if self.oHelper.IfExists("Desligamento cancelado com sucesso!"):
            self.oHelper.Screenshot("jovem0015")
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        self.oHelper.WaitShow("Jovem Aprendiz")
        self.oHelper.Screenshot("jovem0016")
     
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_desligamento_e_cancelamento_Jovem_Aprendiz")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
        
            

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(PXGPEA47_01('test_desligamento_e_cancelamento_Jovem_Aprendiz'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
