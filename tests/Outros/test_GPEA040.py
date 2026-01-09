from tir import Webapp
from os import getcwd
from pytest import mark
import unittest
from time import sleep
from datetime import datetime
DateSystem = datetime.today().strftime('%d/%m/%Y')
DateSystem01 = datetime.today().strftime('%Y/%m')

#-------------------------
# TESTE DE CRUD DE VERBA
#-------------------------

class GPEA040(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.lcontinua = True
        self.filial = '02DF0001'
        self.Codigo = '9B5'
        self.Descricao = 'TESTE_01'
        self.Natureza = '1000'
        self.DescricaoEdit = 'TESTE ALTERADO'
        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', DateSystem, '02', self.filial, '07')
        self.oHelper.SetLateralMenu("Atualizações > Definições Cálculo > Verbas")

        #--------------------------
        #INCLUSÃO DE VERBA
        #-----------------------

    def test_GPEA040(self):

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
            
        self.oHelper.WaitShow("Cadastro de Verbas")

        self.oHelper.Screenshot("GPEA040_01.png")
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetValue('RV_COD',self.Codigo)
        self.oHelper.SetValue('RV_DESC',self.Descricao)
        self.oHelper.SetValue('RV_TIPOCOD','1 - Provento')
        self.oHelper.SetValue('RV_TIPO','H - Horas')
        self.oHelper.ClickFolder('eSocial')
        self.oHelper.SetValue('RV_NATUREZ',self.Natureza)
        self.oHelper.SetValue('RV_INCIRF','11')
        self.oHelper.SetValue('RV_INCFGTS','00')
        self.oHelper.SetValue('RV_INCSIND','00')
        self.oHelper.SetValue('RV_INCCP','00')
        self.oHelper.Screenshot("GPEA040_02")
        self.oHelper.SetButton('Confirmar')
        self.oHelper.Screenshot("GPEA040_02.png")
        self.oHelper.SetButton('OK')
        
        if self.oHelper.IfExists("Atenção!"):
            self.oHelper.WaitShow('Registro enviado para o TAF com sucesso!')
            self.oHelper.Screenshot("GPEA040_03.png")
            self.oHelper.SetButton('OK')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        self.oHelper.WaitShow('Registro inserido com sucesso.')
        self.oHelper.Screenshot("GPEA040_04.png") 
        self.oHelper.SetButton('Fechar')
        self.oHelper.WaitShow("Cadastro de Verbas")
        self.oHelper.Screenshot("GPEA040_05.png")
        
        
        #------------------------------------------
        #VISUALIZAR INCLUSÃO DE VERBA
        #---------------------------------

        self.oHelper.SetButton('Visualizar')
        sleep(0.4)
        self.oHelper.WaitShow('Cadastro de Verbas - VISUALIZAR')
        
        self.oHelper.CheckResult('RV_COD',self.Codigo)
        self.oHelper.CheckResult('RV_DESC',self.Descricao)
        self.oHelper.Screenshot("GPEA040_06.png")
        self.oHelper.ClickFolder('eSocial')
        self.oHelper.CheckResult('RV_NATUREZ',self.Natureza)
        self.oHelper.Screenshot("GPEA040_07.png")
        self.oHelper.SetButton('Fechar')
        sleep(0.2)
        self.oHelper.WaitShow("Cadastro de Verbas")
        
        #--------------------------------
        # ALTERAR VERBA DE INCLUSÃO
        #-------------------------------

        self.oHelper.SetButton('Alterar')
        self.oHelper.WaitShow("Cadastro de Verbas - ALTERAR")
        self.oHelper.SetValue('RV_DESC',self.DescricaoEdit)
        self.oHelper.Screenshot("GPEA040_08.png")
        self.oHelper.SetButton('Confirmar')
        self.oHelper.Screenshot("GPEA040_09.png")
        self.oHelper.SetButton("OK")
        
        if self.oHelper.IfExists("Atenção!"):
            self.oHelper.Screenshot("GPEA040_10.png")
            self.oHelper.WaitShow('Registro enviado para o TAF com sucesso!')
            self.oHelper.SetButton('OK')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
        
        self.oHelper.WaitShow("Registro alterado com sucesso.")
        self.oHelper.Screenshot("GPEA040_11.png")
        self.oHelper.SetButton('Fechar')
        sleep(0.4)
        self.oHelper.WaitShow("Cadastro de Verbas")
        self.oHelper.Screenshot("GPEA040_12.png")
       
        #-----------------------
        # EXCLUIR VERBA DE TESTE
        #----------------------
        

        self.oHelper.SetButton("Outras Ações", "Excluir")
        
        if self.oHelper.IfExists("Atenção"):
            self.oHelper.WaitShow("Confirma a exclusäo da Verba?")
            self.oHelper.Screenshot("GPEA040_13.png")
            self.oHelper.SetButton('Sim')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        if self.oHelper.IfExists("Atenção"):
            self.oHelper.Screenshot("GPEA040_14.png")
            self.oHelper.WaitShow("Deseja gerar Log?")
            self.oHelper.SetButton('Não')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        sleep(7)
        
        self.oHelper.WaitShow("Tem certeza que deseja excluir o item abaixo?")
        self.oHelper.Screenshot("GPEA040_15.png")
        self.oHelper.CheckResult('RV_COD',self.Codigo)
        self.oHelper.CheckResult('RV_DESC',self.DescricaoEdit)
        self.oHelper.SetButton('Confirmar')
        self.oHelper.Screenshot("GPEA040_16.png")
        self.oHelper.SetButton('OK')
        
        
        if self.oHelper.IfExists("Atenção!"):
            self.oHelper.Screenshot("GPEA040_17.png")
            self.oHelper.WaitShow('Registro enviado para o TAF com sucesso!')
            self.oHelper.SetButton('OK')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        sleep(2)
        
        if self.oHelper.IfExists("Registro excluído com sucesso."):
            self.oHelper.Screenshot("GPEA040_18.png")
            
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        self.oHelper.WaitShow("Cadastro de Verbas")
        self.oHelper.Screenshot("GPEA040_19.png")

        self.oHelper.AssertTrue()
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_CRUD_ de_verba")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()