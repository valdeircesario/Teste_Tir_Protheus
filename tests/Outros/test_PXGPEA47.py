from pytest import mark
import unittest
from time import sleep
from os import getcwd
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')


#----------------------------------------------------------------
# CRUD COMPLETO DO JOVEM APRENDIZ
#----------------------------------------------------------------

class PXGPEA47(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        from tir.technologies.core.base import By
        from tir import Webapp
                                                                        
        self.filial = '01'
        self.CPF = '54214723023'
        self.Nome = 'TESTE JOVEM APRENDIZ'
        self.NomeEdit = 'EDIÇÃO JOVEM APRENDIZ'
        self.DataFim = (datetime.today()+timedelta(days= 365)).strftime("%d/%m/%Y")
        self.DaferiasFim = (datetime.today()+timedelta(days=394)).strftime("%d/%m/%Y")
        

        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', DateSystem, '02', self.filial, '07')
        
        self.oHelper.SetLateralMenu("Atualizações > Especificos > Jovem Aprendiz")
        

    def test_CRUD_Jovem_Aprendiz(self):

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
        # INCLUIR JOVEM APRENDIZ
        #------------------------------------
            
        self.oHelper.WaitShow("Jovem Aprendiz")
        self.oHelper.Screenshot("jovem01")  
        sleep(0.5)
        self.oHelper.SetButton("Incluir")
        sleep(1)
        self.oHelper.SearchBrowse(self.filial)
        self.oHelper.Screenshot("jovem02")
        self.oHelper.SetButton("OK")
        sleep(1)
        self.oHelper.WaitShow("Férias Jovem Aprendiz - INCLUIR")
        self.oHelper.Screenshot("jovem03")
        self.oHelper.SetValue("ZRA_NOME", self.Nome)
        self.oHelper.SetValue("ZRA_CPF", self.CPF)
        self.oHelper.SetValue("ZRA_DTNASC", '15082007')
        self.oHelper.SetValue("ZRA_UTA", '000000677')
        self.oHelper.SetValue("ZRA_EQUIPE", '000000866')
        self.oHelper.SetValue("ZRA_ADMISS", DateSystem)
        self.oHelper.SetValue("ZRA_INIPOU", DateSystem)
        self.oHelper.SetValue("ZRA_TELCAN", "61999999999")
        self.oHelper.SetValue("ZRA_TELRES", "61988888888")
        self.oHelper.SetValue("ZRA_MAILAP", "JOVEMAPRENDIZ123@GMAIL.COM")
        sleep(0.5)
        self.oHelper.Screenshot("jovem04")
        self.oHelper.ClickFolder("Dados Funcionais")
        sleep(0.5)
        self.oHelper.SetValue("ZRA_DIACAP", "SEG - Segunda")
        self.oHelper.SetValue("ZRA_HRENTR", "0900",check_value=False)
        self.oHelper.SetValue("ZRA_DTTERM", self.DataFim, check_value=False)
        self.oHelper.SetValue("ZRA_JUSTIF", "TESTE AUTOMATIZADO", check_value=False)
        self.oHelper.SetValue("ZRA_SUPERV", "227884", check_value=False)
        sleep(0.5)
        self.oHelper.Screenshot("jovem05")
        
        self.oHelper.SetValue('Data Inicio',self.DataFim,    grid=True,     grid_number=1, check_value=False)
        self.oHelper.LoadGrid()
        
        if self.oHelper.IfExists("A data está fora do período de trabalho do Jovem Aprendiz."):
            self.oHelper.Screenshot("jovem06")
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
        sleep(0.5)
        
          
        self.oHelper.SetValue('Data Fim', self.DaferiasFim,    grid=True,     grid_number=1, check_value=False)
        self.oHelper.LoadGrid()
        
        self.oHelper.Screenshot("jovem07")
        self.oHelper.SetButton("Confirmar")
        
        if self.oHelper.IfExists("Registro inserido com sucesso."):
            self.oHelper.Screenshot("jovem08")
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        self.oHelper.WaitShow("Jovem Aprendiz")     
        self.oHelper.Screenshot("jovem09")
        
        #--------------------------
        # VISUALIZAR JOVEM APRENDIZ
        #--------------------------
        self.oHelper.SetButton("Outras Ações","Visualizar")
        
        self.oHelper.WaitShow("Férias Jovem Aprendiz - VISUALIZAR")
        self.oHelper.Screenshot("jovem10")
        self.oHelper.CheckResult("ZRA_NOME", self.Nome)
        self.oHelper.CheckResult("ZRA_CPF", self.CPF)
        self.oHelper.CheckResult("ZRA_UTA", '000000677')
        self.oHelper.CheckResult("ZRA_EQUIPE", '000000866')
        self.oHelper.CheckResult("ZRA_ADMISS", DateSystem)
        self.oHelper.CheckResult("ZRA_TELCAN", "61999999999")
        
        self.oHelper.CheckResult("ZRA_TELRES", "61988888888")
        self.oHelper.CheckResult("ZRA_MAILAP", "JOVEMAPRENDIZ123@GMAIL.COM")
        
        self.oHelper.ClickFolder("Dados Funcionais")
        sleep(0.5)
        self.oHelper.CheckResult("ZRA_DIACAP", "SEG - Segunda")
        self.oHelper.CheckResult("ZRA_JUSTIF", "TESTE AUTOMATIZADO")
        self.oHelper.CheckResult("ZRA_SUPERV", "227884")
        self.oHelper.Screenshot("jovem11")
        self.oHelper.SetButton("Fechar")
        sleep(0.5)
        self.oHelper.WaitShow("Jovem Aprendiz") 
        #----------------------------
        # ALTERAR JOVEM APRENDIZ
        #----------------------------
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow("Férias Jovem Aprendiz - ALTERAR")
        self.oHelper.Screenshot("jovem12")
        self.oHelper.SetValue("ZRA_NOME", self.NomeEdit,check_value=False)
        self.oHelper.SetValue("ZRA_TELRES", "61966666666")
        self.oHelper.SetValue("ZRA_MAILAP", "JOVEMAPREDIZALTERADO@GMAIL.COM")
        self.oHelper.Screenshot("jovem013")
        
        self.oHelper.ClickFolder("Dados Funcionais")
        sleep(2)
        self.oHelper.Screenshot("jovem14")
        self.oHelper.SetButton("Confirmar")
        
        
        if self.oHelper.IfExists("Registro alterado com sucesso."):
            self.oHelper.Screenshot("jovem15")
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        self.oHelper.WaitShow("Jovem Aprendiz")
        self.oHelper.Screenshot("jovem016")
        
        #-------------------------
        # EXCLUIR JOVEM APRENDIZ
        #------------------------- 
        self.oHelper.SetButton("Outras Ações","Excluir")
        sleep(1)
        
        self.oHelper.WaitShow("Tem certeza que deseja excluir o item abaixo?")
        self.oHelper.WaitShow("Esta operação não poderá ser desfeita após a confirmação da exclusão.")
        self.oHelper.Screenshot("jovem17")
        self.oHelper.SetButton('Confirmar')
        sleep(1)
            
        if self.oHelper.IfExists("Registro excluído com sucesso."):
            self.oHelper.Screenshot("jovem18")
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        self.oHelper.WaitShow("Jovem Aprendiz")
        self.oHelper.Screenshot("jovem19")
        self.oHelper.AssertTrue()
       
     
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_CRUD_Jovem_Aprendiz")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
        
            

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(PXGPEA47('test_CRUD_Jovem_Aprendiz'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
