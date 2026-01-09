from tir.technologies.core.base import By
from tir import Webapp
from pytest import mark
import unittest
from time import sleep
from os import getcwd
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')


#------------------------
# TESTE DE INCLUSÃO DE SINDICATO
#------------------------

class GPEA340(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        
        self.Codigo = '91'
        self.Descricao = "TESTE SINDICATO"
        self.DescricaoEdit = "TESTE SINDICATO EDITADO"
        self.CNPJ = "34.783.086/0001-98"
        self.Endereco = 'RUA FLORENTINO CARDOSO'
        self.Numero = "22"
        self.Complemento = 'CENTRO'
        self.Bairro = 'OLIVEIRA'
        self.CEP = '72000000'
        self.Estado = 'DF'
        self.Municipio = 'BRASILIA'
        self.CodMunicip = '00108'
        self.DDD = '61'
        self.Fone ='984060840'
        self.Email = 'TESTE123@GAMIL.COM'
        self.Verba = '232'
        self.filial = '02DF0001'
        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', DateSystem, '02', self.filial, '07') 
        self.oHelper.SetLateralMenu("Atualizações > Cadastros > Sindicatos")
         

    def test_cadastro_de_sindicato_CRUD(self):

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
            
        #----------------
        # INCLUSÃO DE SINDICATO
        #----------------
        
        self.oHelper.WaitShow("Cadastro de Sindicatos") 
        self.oHelper.Screenshot("GPEA340_01.png")  
        self.oHelper.SetButton("Incluir")
        sleep(1)
        
        self.oHelper.SearchBrowse(self.filial)
        self.oHelper.SetButton("OK")
        sleep(0.5)
        self.oHelper.Screenshot("GPEA340_01.png")
        self.oHelper.WaitShow("Sindicatos - INCLUIR")
        self.oHelper.Screenshot("GPEA340_02.png")   
        self.oHelper.SetValue("RCE_CODIGO",self.Codigo)
        self.oHelper.SetValue("RCE_DESCRI",self.Descricao)
        self.oHelper.SetValue("RCE_CGC",self.CNPJ,check_value=False)
        self.oHelper.SetValue("RCE_ENDER",self.Endereco)
        self.oHelper.SetValue("RCE_NUMER",self.Numero)
        self.oHelper.SetValue("RCE_COMPLE",self.Complemento)
        self.oHelper.SetValue("RCE_BAIRRO",self.Bairro)
        self.oHelper.SetValue("RCE_CEP",self.CEP)
        self.oHelper.SetValue("RCE_UF",self.Estado)
        self.oHelper.SetValue("RCE_CODMUN",self.CodMunicip)
        self.oHelper.SetValue("RCE_DDD",self.DDD)
        self.oHelper.SetValue("RCE_FONE",self.Fone)
        self.oHelper.SetValue("RCE_EMAIL",self.Email)
        sleep(0.5)  
        self.oHelper.ClickFolder("Mens Sindical") 
        self.oHelper.Screenshot("GPEA340_03.png")  
        self.oHelper.SetValue("RCE_XVBBAS",self.Verba)
        self.oHelper.Screenshot("GPEA340_02.png")
        
        sleep(0.5) 
        self.oHelper.ClickFolder("Cadastrais") 
        self.oHelper.SetButton("Confirmar")
        
        
        if self.oHelper.IfExists("Atenção"):
            self.oHelper.Screenshot("GPEA340_04.png")
            self.oHelper.WaitShow("Os dados alterados são válidos a partir da database atual e pode impactar no cálculo de dissídio.")
            self.oHelper.SetButton("Sim")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        self.oHelper.WaitShow("Registro inserido com sucesso.")
        self.oHelper.Screenshot("GPEA340_05.png")
        self.oHelper.SetButton("Fechar")
        sleep(1)  
        self.oHelper.WaitShow("Cadastro de Sindicatos")
        
        #----------------------------------
        # VISUALIZAR INCLUSÃO DE SINDICATO
        #----------------------------------
        
        self.oHelper.SetButton("Visualizar")
        sleep(0.5)
        self.oHelper.Screenshot("GPEA340_06.png")
        self.oHelper.WaitShow("Sindicatos - VISUALIZAR")
        self.oHelper.Screenshot("GPEA340_07.png")
        self.oHelper.CheckResult("RCE_CODIGO",self.Codigo)
        self.oHelper.CheckResult("RCE_DESCRI",self.Descricao)
        self.oHelper.CheckResult("RCE_ENDER",self.Endereco)
        self.oHelper.CheckResult("RCE_NUMER",self.Numero)
        self.oHelper.CheckResult("RCE_COMPLE",self.Complemento)
        self.oHelper.CheckResult("RCE_EMAIL",self.Email)  
        self.oHelper.ClickFolder("Mens Sindical")
        self.oHelper.Screenshot("GPEA340_08.png")   
        self.oHelper.CheckResult("RCE_XVBBAS",self.Verba)
        self.oHelper.Screenshot("GPEA340_09.png")
        sleep(0.5)  
        self.oHelper.ClickFolder("Cadastrais")
        self.oHelper.SetButton("Fechar")
        sleep(0.5)
        self.oHelper.WaitShow("Cadastro de Sindicatos")
        self.oHelper.Screenshot("GPEA340_10.png")
        
        #-----------------------------------
        # ALTERAR REGSTRO DE SINDICATO
        #---------------------------------
        
        self.oHelper.SetButton("Alterar")
        sleep(0.5)
        self.oHelper.WaitShow("Sindicatos - ALTERAR")
        self.oHelper.Screenshot("GPEA340_11.png")
        self.oHelper.SetValue("RCE_DESCRI",self.DescricaoEdit,check_value=False)
        self.oHelper.Screenshot("GPEA340_05.png")
        sleep(1)
        self.oHelper.SetButton("Confirmar")
        
        if self.oHelper.IfExists("Atenção"):
            self.oHelper.Screenshot("GPEA340_12.png")
            self.oHelper.WaitShow("Os dados alterados são válidos a partir da database atual e pode impactar no cálculo de dissídio.")
            self.oHelper.SetButton("Sim")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
        
        self.oHelper.WaitShow("Registro alterado com sucesso.") 
        self.oHelper.Screenshot("GPEA340_13.png")
        self.oHelper.SetButton("Fechar") 
        self.oHelper.WaitShow("Cadastro de Sindicatos")
        
        #-------------------------------
        # EXCLUSÃO DE REGISTRO DE SINDICATO
        #-------------------------------
        
        self.oHelper.SetButton("Outras Ações","Excluir") 
        sleep(0.5)
        self.oHelper.WaitShow("Tem certeza que deseja excluir o item abaixo?")
        sleep(0.5)
        self.oHelper.Screenshot("GPEA340_14.png") 
        self.oHelper.SetButton("Confirmar")
        
        if self.oHelper.IfExists("Atenção"):
            self.oHelper.WaitShow("Os dados alterados são válidos a partir da database atual e pode impactar no cálculo de dissídio.")
            self.oHelper.Screenshot("GPEA340_15.png")
            self.oHelper.SetButton("Sim")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
            
        self.oHelper.WaitShow("Registro excluído com sucesso.")
        self.oHelper.Screenshot("GPEA340_16.png")
        self.oHelper.SetButton("Fechar")  
        self.oHelper.AssertTrue()
        
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_CRUD_ de_sindicato")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")         
            
    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA340('test_cadastro_de_sindicato_CRUD'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
