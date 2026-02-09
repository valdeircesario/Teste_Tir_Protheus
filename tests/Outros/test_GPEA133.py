from pytest import mark
import unittest
from time import sleep
from os import getcwd
from datetime import datetime, timedelta
DateSystem = datetime.today().strftime('%d/%m/%Y')

#----------------------------------------------------------------
# LANÇAMENTO DE VALE TRANSPORTE E CALCULO NA FOLHA E VALIDAÇÃO
#----------------------------------------------------------------
#python -m pytest tests/Outros/test_GPEA133.py -v -s

#python -m pytest tests/Outros/test_GPEA133.py -v -s --html=reports/report_GPEA133.html --self-contained-html
#python tests/Outros/test_GPEA133.py
#python -m unittest tests.Outros.test_GPEA133.GPEA133.test_lancamento_vale_transporte_e_claculo_folha -v
class GPEA133(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        from tir.technologies.core.base import By
        from tir import Webapp
                                                                        
        self.filial = '02DF0001'
        self.Matricula = '228368'
        self.Nome = 'GABRIEL MOREIRA DA SILVA DE FARIA'
        self.Roteiro = "VTR"
        self.Processo = '00001'
        self.Verba = '620'
        
        
        self.dataref = (datetime.today()-timedelta(days=15)).strftime("%d/%m/%Y")
        
        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', self.dataref, '02', self.filial, '07')
                
        self.oHelper.SetLateralMenu("Atualizações > Beneficios > Vt / Vr / Va > Atualização")
        #self.oHelper.SetButton('Confirmar') -- observar essas linha, em meu ambiete de trabalho, o browser não visualiza a tela de trocar modulos.

        

    def test_lancamento_vale_transporte_e_claculo_folha(self):

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
            
            
        self.oHelper.WaitShow("Atualização Vales")
        self.oHelper.Screenshot("VTR/Incluindo_VTR_01") 
        
        #------------------------------------
        # PESQUISAR O FUNCIONARIO PARA O CALCULO
        #------------------------------------ 
        self.oHelper.SearchBrowse(self.filial + self.Matricula + self.Nome, key="Filial+matricula+Nome")
        sleep(0.5)
        self.oHelper.Screenshot("VTR/Incluindo_VTR_02")
        sleep(1)
        
        self.oHelper.SetButton('Manutenção')
        sleep(2)
        
        
        if self.oHelper.IfExists("Ao Deletar um registro a rotina verifica se existem dados vinculados àquele Benefício"):
            self.oHelper.Screenshot("VTR/Incluindo_VTR_03")
            self.oHelper.SetButton('OK')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        sleep(2)
        self.oHelper.WaitShow('Funcionários - MANUTENÇÃO')
        sleep(2)
        self.oHelper.SetKey("ENTER")
        sleep(2)
        self.oHelper.SetKey("ENTER")
        sleep(1)     
        
        self.oHelper.Screenshot("VTR/Incluindo_VTR_04")
        
        self.oHelper.SetButton('Confirmar')
        
        if self.oHelper.IfExists("Registro alterado com sucesso"):
            self.oHelper.Screenshot("VTR/Incluindo_VTR_05")
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        self.oHelper.WaitShow('Atualização Vales')
        sleep(1)
        
        self.oHelper.SetButton("Visualizar")
        sleep(1)
        
        self.oHelper.WaitShow('Funcionários - VISUALIZAR')
        self.oHelper.Screenshot("VTR/Incluindo_VTR_06")
        self.oHelper.SetButton('Fechar')
        sleep(10)
        
        
        #-------------------------------------------------------------
        # VALIDAR INTEGRAÇÃO DO SISTEMA PARA GERAR CALCULO ROTEIRO VRT ROTINA CTBA211
        #-------------------------------------------------------------
        
        self.oHelper.SetLateralMenu("Miscelanea > Cálculos > Integrações")
        
        self.oHelper.SetValue("Processo","00001")

        self.oHelper.Screenshot("VTR/Cancelar_Integração_01")
        self.oHelper.SetButton("Outras Ações","Apenas Integrados")
        sleep(3)
        self.oHelper.Screenshot("VTR/Cancelar_Integração_02")
        
        self.oHelper.SetButton("Cancelar Integração")
        
        if self.oHelper.IfExists("Integrações Com a Folha de Pagamento"):
            self.oHelper.SetButton("Executar")
            self.oHelper.Screenshot("VTR/Cancelar_Integração_03")
            sleep(90)
            self.oHelper.Screenshot("VTR/Cancelar_Integração_04")
            sleep(90)
            self.oHelper.Screenshot("VTR/Cancelar_Integração_05")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
        
        self.oHelper.Screenshot("VTR/Cancelar_Integração_06")

        self.oHelper.CheckHelp(text="Nenhum roteiro selecionado.", button="Fechar")
        sleep(1)
        self.oHelper.SetButton("x")
        
        
        #------------------------
        # CALCULAR ROTEIRO VTR
        #-----------------------
        
        self.oHelper.SetLateralMenu("Miscelanea > Cálculos (13)> Por Roteiros")
        
        self.oHelper.WaitShow("Processo de Calculo")
        self.oHelper.WaitShow("Este programa realiza processos de calculos")
        self.oHelper.Screenshot("VTR/Calculo_roteiroVTR_01.png")
        
        self.oHelper.SetButton("Parametros")
        sleep(5)
        self.oHelper.SetValue("Processo ?",self.Processo,           check_value=False)
        self.oHelper.SetValue("Roteiro ?",self.Roteiro,             check_value=False)
        sleep(0.5)
        self.oHelper.Screenshot("VTR/Calculo_roteiroVTR_02.png")
        
        self.oHelper.SetButton("OK")
        sleep(5)
        
        
        if self.oHelper.IfExists("Parametros"):
            sleep(1)
            self.oHelper.Screenshot("VTR/Calculo_roteiroVTR_03.png")
            self.oHelper.SetButton("OK")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()


        self.oHelper.SetButton("Filtro Rapido")
        self.oHelper.SetValue("Campos:","Matricula")
        self.oHelper.SetValue("Expressäo:",self.Matricula)
        self.oHelper.Screenshot("VTR/Calculo_roteiroVTR_03.png")
        self.oHelper.SetButton("Adiciona")
        sleep(1)
        self.oHelper.SetButton("OK")
        sleep(1)


        self.oHelper.SetButton("Calcular")
        self.oHelper.Screenshot("VTR/Calculo_roteiroVTR_04.png")
        
        
        if self.oHelper.IfExists("Confirma configuracäo dos parametros?"):
            self.oHelper.Screenshot("VTR/Calculo_roteiroVTR_05.png")
            self.oHelper.SetButton("Sim")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        if self.oHelper.IfExists("Nenhum filtro foi selecionado! Processar toda a tabela?"):
            self.oHelper.Screenshot("VTR/Calculo_roteiroVTR_06.png")
            self.oHelper.SetButton("Sim")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        sleep(20) 
        
        self.oHelper.Screenshot("VTR/Calculo_roteiroVTR_07.png")
        sleep(20)
        self.oHelper.Screenshot("VTR/Calculo_roteiroVTR_08.png")
        sleep(20)
        
        self.oHelper.WaitShow("Log de Ocorrencias no Processo de Calculo") 
        
        if self.oHelper.IfExists("Log de Ocorrencias no Processo de Calculo"):
            self.oHelper.ClickLabel("Em Disco")
            self.oHelper.Screenshot("VTR/Calculo_roteiroVTR_09.png")
            self.oHelper.SetButton("OK")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        sleep(25)
        self.oHelper.Screenshot("VTR/Calculo_roteiroVTR_10.png")
    
        self.oHelper.SetButton("Sair")
        sleep(10) 

        #----------------------------------------------
        # GARANTE A INTEGRAÇÃO DO SISTEMA PARA CALCULAR FOLHA
        #-------------------------------------------------------
                
        self.oHelper.SetLateralMenu("Miscelanea > Cálculos > Integrações") 
        
        self.oHelper.Screenshot("VTR/integração_01")
        
        sleep(2)
        self.oHelper.SetValue("Processo","00001")
        sleep(1)
        self.oHelper.SetButton("Outras Ações","Inverter Seleção")
        sleep(3)
        self.oHelper.SetButton('Integrar')
        
        
        
        if self.oHelper.IfExists("Integrações Com a Folha de Pagamento"):
            self.oHelper.Screenshot("VTR/integração_02")
            self.oHelper.SetButton('Executar') 
            self.oHelper.SetButton('Ok')
            sleep(100)
            self.oHelper.Screenshot('VTR/integração_03')
            sleep(100)
            self.oHelper.Screenshot('VTR/integração_04')
            sleep(100)
            self.oHelper.Screenshot('VTR/integração_05')
            sleep(50)
        else:
            self.oHelper.AssertTrue()
            
        self.oHelper.Screenshot('VTR/integração_06')

        sleep(5)
        self.oHelper.SetButton('x')
        # FAZER UM TRATAMENTO AQUI DE UMA MENSAGEM
        

        #-------------------------------------------
        # CALCULAR FOLHA PARA VALIDAR A INCLUSÃO DO VTR
        #--------------------------------------------
        
        
        self.oHelper.SetLateralMenu("Atualizações > Lançamentos > Por Funcionário ")
        sleep(10)
        self.oHelper.Screenshot("VTR/Calcular_folha_01")
        
        self.oHelper.SearchBrowse(self.filial + self.Matricula + self.Nome, key="Filial+matricula+Nome")
        sleep(1)
        self.oHelper.Screenshot("VTR/Calcular_folha_02")
        self.oHelper.SetButton("Alterar")
        sleep(1)
        self.oHelper.WaitShow("Lançamentos por Funcionário")
        self.oHelper.ScrollGrid(column="Cod Verba", match_value = self.Verba,         grid_number=1)
        self.oHelper.Screenshot("VTR/Calcular_folha_03")
        self.oHelper.LoadGrid()
        self.oHelper.SetKey("F6")
        sleep(30)
        self.oHelper.Screenshot("VTR/Calcular_folha_04")
        self.oHelper.SetButton('OK')
        sleep(5)
        self.oHelper.SetKey("F7")
        sleep(5)
        self.oHelper.ScrollGrid(column="Codigo Verba", match_value = self.Verba,         grid_number=1)
        self.oHelper.Screenshot("VTR/Calcular_folha_05")
        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Confirmar')
        sleep(5)
        self.oHelper.SetButton('Salvar')
        sleep(1)
        self.oHelper.AssertTrue()
       
     
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_lancamento_vale_transporte_e_calculo_folha")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
        
            

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA133('test_lancamento_vale_transporte_e_claculo_folha'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
