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
                                                                        
        self.filial = '01'
        self.Matricula = '222557'
        self.Nome = 'VANDERLI CESARIO DA SILVA'
        self.Roteiro = "VTR"
        self.Processo = '00001'
        
        
        self.dataref = (datetime.today()-timedelta(days=15)).strftime("%d/%m/%Y")
        
        configfile = getcwd() + '\\config.json'
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', self.dataref, '99', self.filial, '07')
        
        self.oHelper.SetLateralMenu("Miscelanea > Cálculos > Integrações")
        
        #self.oHelper.SetLateralMenu("Atualizações > Beneficios > Vt / Vr / Va > Atualização")
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
            
            
        """ self.oHelper.WaitShow("Atualização Vales")
        self.oHelper.Screenshot("vale_transporte_01") 
        
        #------------------------------------
        # PESQUISAR O FUNCIONARIO PARA O CALCULO
        #------------------------------------ 
        self.oHelper.SearchBrowse(self.filial + self.Matricula + self.Nome, key="Filial+matricula+Nome")
        sleep(0.5)
        self.oHelper.Screenshot("vale_transporte_02")
        sleep(1)
        
        self.oHelper.SetButton('Manutenção')
        sleep(2)
        
        
        if self.oHelper.IfExists("Ao Deletar um registro a rotina verifica se existem dados vinculados àquele Benefício"):
            self.oHelper.Screenshot("vale_transporte_03")
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
        
        self.oHelper.Screenshot("vale_transporte_04")
        
        self.oHelper.SetButton('Confirmar')
        
        if self.oHelper.IfExists("Registro alterado com sucesso"):
            self.oHelper.Screenshot("vale_transporte_05")
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        self.oHelper.WaitShow('Atualização Vales')
        sleep(1)
        
        self.oHelper.SetButton("Visualizar")
        sleep(1)
        
        self.oHelper.WaitShow('Funcionários - VISUALIZAR')
        self.oHelper.Screenshot("vale_transporte_06")
        self.oHelper.SetButton('Fechar')
        sleep(2)
        
        
        #-------------------------------------------------------------
        # VALIDAR INTEGRAÇÃO DO SISTEMA PARA GERAR CALCULO ROTEIRO VRT ROTINA CTBA211
        #-------------------------------------------------------------
        
        self.oHelper.SetLateralMenu("Miscelanea > Cálculos > Integrações") """
        
        #self.oHelper.Screenshot("vale_transporte_07")
        
        sleep(2)
        self.oHelper.SetValue("Processo","00001")
        sleep(1)
        self.oHelper.ScrollGrid(column="Roteiro", match_value = self.Roteiro)
        self.oHelper.ClickBox("Roteiro", "VTR")
        sleep(2)
        self.oHelper.Screenshot("vale_transporte_08")
        
        self.oHelper.SetButton('Cancelar Integração')
        
        if self.oHelper.IfExists("Integrações Com a Folha de Pagamento"):
            self.oHelper.Screenshot("vale_transporte_08_1")
            self.oHelper.SetButton('Executar')
            sleep(1)
        else:
            self.oHelper.AssertTrue()


        self.oHelper.CheckHelp(text="Nenhum roteiro selecionado.", button="Fechar")
        sleep(1)
            
        sleep(5)
        
        
        #------------------------
        # CALCULAR ROTEIRO VTR
        #-----------------------
        
        self.oHelper.SetLateralMenu("Miscelanea > Cálculos (13)> Por Roteiros")
        
        self.oHelper.WaitShow("Processo de Calculo")
        self.oHelper.WaitShow("Este programa realiza processos de calculos")
        self.oHelper.Screenshot("roteiroVTR_01.png")
        
        self.oHelper.SetButton("Parametros")
        sleep(5)
        self.oHelper.SetValue("Processo ?",self.Processo,           check_value=False)
        self.oHelper.SetValue("Roteiro ?",self.Roteiro,             check_value=False)
        sleep(0.5)
        self.oHelper.Screenshot("roteiroVTR_02.png")
        
        self.oHelper.SetButton("OK")
        sleep(5)
        
        
        if self.oHelper.IfExists("Parametros"):
            sleep(1)
            self.oHelper.Screenshot("roteiroVTR_03.png")
            self.oHelper.SetButton("OK")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()


        self.oHelper.SetButton("Filtro Rapido")
        self.oHelper.SetValue("Campos:","Matricula")
        self.oHelper.SetValue("Expressäo:","222557")
        self.oHelper.Screenshot("roteiroVTR_03.png")
        self.oHelper.SetButton("Adiciona")
        sleep(1)
        self.oHelper.SetButton("OK")
        sleep(1)


        self.oHelper.SetButton("Calcular")
        self.oHelper.Screenshot("roteiroVTR_04.png")
        
        
        if self.oHelper.IfExists("Confirma configuracäo dos parametros?"):
            self.oHelper.Screenshot("roteiroVTR_05.png")
            self.oHelper.SetButton("Sim")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        if self.oHelper.IfExists("Nenhum filtro foi selecionado! Processar toda a tabela?"):
            self.oHelper.Screenshot("roteiroVTR_06.png")
            self.oHelper.SetButton("Sim")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        sleep(300) 
        
        self.oHelper.Screenshot("roteiroVTR_07.png")
        sleep(30)
        self.oHelper.Screenshot("roteiroVTR_08.png")
        sleep(30)
        
        self.oHelper.WaitShow("Log de Ocorrencias no Processo de Calculo") 
        
        if self.oHelper.IfExists("Log de Ocorrencias no Processo de Calculo"):
            self.oHelper.ClickLabel("Em Disco")
            self.oHelper.Screenshot("roteiroVTR_09.png")
            self.oHelper.SetButton("OK")
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        sleep(25)
        self.oHelper.Screenshot("roteiroVTR_10.png")
    
        self.oHelper.SetButton("Sair")
        sleep(10)

        #------------------------------------------
        # CANCELAR INTEGRAÇÃO PARA CALCULAR A FOLHA
        #--------------------------------------------


        self.oHelper.SetLateralMenu("Miscelanea > Cálculos > Integrações") 
        
        #self.oHelper.Screenshot("vale_transporte_07")
        
        sleep(2)
        self.oHelper.SetValue("Processo","00001")
        sleep(1)
        self.oHelper.ScrollGrid(column="Roteiro", match_value = self.Roteiro)
        self.oHelper.ClickBox("Roteiro", "VTR")
        sleep(2)
        self.oHelper.Screenshot("vale_transporte_08")
        
        self.oHelper.SetButton('Integrar')
        
        if self.oHelper.IfExists("Integrações Com a Folha de Pagamento"):
            self.oHelper.Screenshot("vale_transporte_08_1")
            self.oHelper.SetButton('Executar')
            if self.oHelper.IfExists("Integração de Beneficios"):
                self.oHelper.SetButton('Ok')
                sleep(200)
        else:
            self.oHelper.AssertTrue()

        sleep(200)

        #--------------------------------------------------
        # CALCULAR FOLHA E VALIDAR INCLUSÃO DO VTR NA FOLHA
        #---------------------------------------------------

        self.oHelper.SetLateralMenu("Atualizações > Lançamentos > Por Funcionário ")
        sleep(10)
        self.oHelper.Screenshot("vale_transporte_08_1")
        
        self.oHelper.SearchBrowse(self.filial + self.Matricula + self.Nome, key="Filial+matricula+Nome")
        sleep(1)
        self.oHelper.Screenshot("vale_transporte_08_1")
        self.oHelper.SetButton("Alterar")
        sleep(1)
        self.oHelper.WaitShow("Lançamentos por Funcionário")
        self.oHelper.Screenshot("vale_transporte_08_1")
        self.oHelper.SetKey("F6")
        sleep(1)
        self.oHelper.SetButton('x')
        
        

        
        


       
            
            
        
        
        
        

        
        
  
        
       
        self.oHelper.AssertTrue()
       
     
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_lancamento_vale_transporte_e_claculo_folha")
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
