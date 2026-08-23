from tir.technologies.core.base import By
from tir import Webapp
from pytest import mark
import unittest
from time import sleep
from os import getcwd
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')

# .\venv\Scripts\python.exe -m pytest tests/Outros/test_CSAA100.py -s


#------------------------
# TESTE DE INCLUSÃO DE DEPARATAMENTOS
#------------------------

class CSAA100(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.filial = '01'
        self.CentoCusto = '007'
        self.MatriculaResp = "XXX000"
        self.DepartSuper = "00005"
        self.DescricaoAD = "TESTE DEPARTAMENTO"
        self.DescricaoADEdt = "TESTE EDITADO"
        self.DescricaoEdt = 'TESTE 01'
        self.Dotacao = "5"
        self.Tipo = '2'
        self.Processo = '00001'
        

        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', DateSystem, '99', self.filial, '07')
        
        self.oHelper.SetLateralMenu("Atualizações > Cadastros > Departamentos")
        
    

    def test_de_inclusão_de_deparatamento(self):

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
        # teste de incluir novo deparatamento
        #----------------
        self.oHelper.WaitShow("Departamento")
        self.oHelper.Screenshot("CSAA100_01.png")   
        self.oHelper.SetButton("Incluir")
        sleep(1)
        
        self.oHelper.WaitShow("Departamento - INCLUIR")
        self.oHelper.Screenshot("CSAA100_02.png")
        
        self.oHelper.SetValue("QB_FILRESP",self.filial,         check_value=False)
        self.oHelper.SetValue("QB_CC",self.CentoCusto)
        #self.oHelper.SetValue("QB_FILRESP",self.filial)
        self.oHelper.SetValue("QB_MATRESP",self.MatriculaResp,  check_value=False)
        self.oHelper.SetValue("QB_DEPSUP",self.DepartSuper)
        self.oHelper.SetValue("QB_XDESCRI",self.DescricaoAD)
        self.oHelper.SetValue("QB_XDTINI",DateSystem)
        self.oHelper.SetValue("QB_XVAGAS",self.Dotacao)
        self.oHelper.SetValue("QB_XTIPO",self.Tipo,              check_value=False)
        self.oHelper.Screenshot("CSAA100_02.png")
        
        self.oHelper.SetButton("Salvar")
        
        if self.oHelper.IfExists("Retorno - Ifractal"):
            self.oHelper.Screenshot("CSAA100_03.png")
            self.oHelper.SetButton("Fechar")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        if self.oHelper.IfExists("Integração funcionários x Departamento realizada com sucesso!"):
            self.oHelper.Screenshot("CSAA100_04.png")
            self.oHelper.SetButton("Fechar")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
        
        sleep(1)
        
        
        self.oHelper.SetButton("Cancelar")
        self.oHelper.Screenshot("CSAA100_05.png")
        
        sleep(0.5)
        self.oHelper.WaitShow("Departamento")
        
        #----------------------------------
        # Visualizar inclusão de departamento
        #----------------------------------
        
        self.oHelper.SetButton("Visualizar")
        sleep(0.5)
        self.oHelper.WaitShow("Departamento - VISUALIZAR")
        self.oHelper.Screenshot("CSAA100_06.png")
        
        self.oHelper.CheckResult("QB_FILRESP",      self.filial)
        self.oHelper.CheckResult("QB_CC",           self.CentoCusto)
        self.oHelper.CheckResult("QB_FILRESP",      self.filial)
        self.oHelper.CheckResult("QB_MATRESP",      self.MatriculaResp)
        self.oHelper.CheckResult("QB_DEPSUP",       self.DepartSuper)
        self.oHelper.CheckResult("QB_XDESCRI",      self.DescricaoAD)
        self.oHelper.CheckResult("QB_XDTINI",       DateSystem)
        self.oHelper.CheckResult("QB_XVAGAS",       self.Dotacao)
        self.oHelper.CheckResult("QB_TIPO",         self.Tipo)
        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.Screenshot("CSAA100_07.png")
        sleep(0.5)
        self.oHelper.WaitShow("Departamento")
        
        #-----------------------------------
        # Aterar registro de departamento
        #---------------------------------
        
        self.oHelper.SetButton("Alterar")
        sleep(0.5)
        self.oHelper.WaitShow("Departamento - ALTERAR")
        self.oHelper.Screenshot("CSAA100_08.png")
        self.oHelper.SetValue("QB_XDESCRI",     self.DescricaoADEdt)
        self.oHelper.SetValue("QB_DESCRIC",     self.DescricaoEdt)
        self.oHelper.SetButton("Salvar")
        
        if self.oHelper.IfExists("Retorno - Ifractal"):
            self.oHelper.Screenshot("CSAA100_09.png")
            self.oHelper.SetButton("Fechar")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        if self.oHelper.IfExists("Integração funcionários x Departamento realizada com sucesso!"):
            self.oHelper.Screenshot("CSAA100_10.png")
            self.oHelper.SetButton("Fechar")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
        
        sleep(1)
        
        self.oHelper.WaitShow("Departamento")
        self.oHelper.Screenshot("CSAA100_11.png")
        
        #-------------------------------
        # exclusão de departamento , não esta excluindo
        #-------------------------------
        
        self.oHelper.SetButton("Outras Ações","Excluir")
        
        sleep(0.5)
        self.oHelper.WaitShow("Departamento - EXCLUIR")
        self.oHelper.Screenshot("CSAA100_12.png")
        
        
        self.oHelper.SetButton("Confirmar")
        sleep(0.1)
        
        if self.oHelper.IfExists("Retorno - Ifractal"):
            self.oHelper.Screenshot("CSAA100_13.png")
            self.oHelper.SetButton("Fechar")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        if self.oHelper.IfExists("Integração funcionários x Departamento realizada com sucesso!"):
            self.oHelper.Screenshot("CSAA100_14.png")
            self.oHelper.SetButton("Fechar")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        if self.oHelper.IfExists("Departamento - EXCLUIR - Log de verificaçäo de exclusäo"):
            self.oHelper.WaitShow("O sistema irá efetuar a verificaçäo para ver se o registro selecionado para exclusäo está sendo utilizado. A verificaçäo pode ser demorada.")
            self.oHelper.WaitShow("Confirma a exclusäo?")
            self.oHelper.Screenshot("CSAA100_15.png")
            self.oHelper.SetButton("Sim")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        if self.oHelper.IfExists("Departamento - EXCLUIR - Log de verificaçäo de exclusäo"):
            self.oHelper.WaitShow("Deseja gerar Log?")
            self.oHelper.Screenshot("CSAA100_16.png")
            self.oHelper.SetButton("Não")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        if self.oHelper.IfExists("Departamento - EXCLUIR - Log de verificaçäo de exclusäo"):
            self.oHelper.WaitShow("Demonstrar o Log Sinteticamente ?")
            self.oHelper.Screenshot("CSAA100_17.png")
            self.oHelper.SetButton("Não")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        if self.oHelper.IfExists("Log de verificaçäo de exclusäo"):
            self.oHelper.Screenshot("CSAA100_18.png")
            self.oHelper.SetButton("OK")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            sleep(1)
            
        
            
        if self.oHelper.IfExists("Departamento - EXCLUIR - Log de verificaçäo de exclusäo"):
            self.oHelper.WaitShow("A chave a ser excluida está sendo utilizada. Até que as referências a ela sejam eliminadas a mesma näo pode ser excluida.")
            self.oHelper.Screenshot("CSAA100_19.png")
            self.oHelper.SetButton("Fechar")
            self.oHelper.AssertTrue()
            
            print("------------------------------------------------")
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            print("X 🎯 test_de_incluir_departamento")
            print("X ✅ Teste finalizado com sucesso")
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                   
        
          
            

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CSAA100('test_inclusão_departamento'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
