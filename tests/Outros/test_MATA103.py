from time import sleep
from tir import Webapp
from os import getcwd
from pytest import mark
from datetime import datetime, timedelta
import unittest
DateSystem = datetime.today().strftime('%d/%m/%Y')

# CRUD DOCUMENTO DE ENTRADA

class MATA103(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.filial = "02DF0001"
        self.lcontinua = True
        configfile = getcwd() + '\\config.json'
        #self.diaprox = (datetime.today()+timedelta(days=-30)).strftime("%d/%m/%Y")
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', DateSystem, '02', self.filial, '02')
        self.oHelper.SetLateralMenu("Atualizações > Movimentos > Documento Entrada")
        #self.oHelper.SetButton('Confirmar')

    def test_MATA103(self):

        #----------------------------------
        # INCLUSÃO DE DOCUMENTO DE ENTRADA
        #-----------------------------------


        if self.oHelper.IfExists("Reforma Tributária"):
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
            
        self.oHelper.WaitShow("Documento de Entrada")
        self.oHelper.Screenshot("MATA103_01.png")
        
        self.oHelper.SetFocus("Incluir")

        self.oHelper.SetButton("Incluir")
        sleep(1)
        self.oHelper.Screenshot("MATA103_02.png")
        self.oHelper.SetBranch("02DF0001")
        self.oHelper.SetValue('Numero', '9991127XA')
        self.oHelper.SetValue('Serie', '01')
        self.oHelper.SetValue('Fornecedor', '057032', direction='right')
        self.oHelper.SetValue('Espec.Docum.', 'NFE')
        self.oHelper.Screenshot("MATA103_03.png")
         
        self.oHelper.SetValue("Produto",'000000000000418',          grid=True, grid_number=1)
        self.oHelper.SetValue("Quantidade",'1',                     grid=True, grid_number=1, check_value=False)
        self.oHelper.SetValue("Vlr.Unitario",'10',                  grid=True, grid_number=1, check_value=False)
        self.oHelper.SetValue("Centro Custo",'000000271',           grid=True, grid_number=1, check_value=False)
        self.oHelper.SetValue("Tipo Entrada",'241',                 grid=True, grid_number=1, check_value=False)
        self.oHelper.SetValue("Forn/Client",'057032',               grid=True, grid_number=1, check_value=False)
        self.oHelper.SetValue("Loja",'0001',                        grid=True, grid_number=1, check_value=False)
        self.oHelper.SetValue("Serie",'1',                          grid=True, grid_number=1, check_value=False)
        self.oHelper.SetValue("Cc Des Depr",'000000271',            grid=True, grid_number=1, check_value=False)
        self.oHelper.SetValue("Cc Depr Ac",'000000271',             grid=True, grid_number=1, check_value=False)
        self.oHelper.SetValue("Grupo",'0001',                       grid=True, grid_number=1, check_value=False)
        self.oHelper.LoadGrid()
        sleep(1)
        
        self.oHelper.ClickFolder("Duplicatas")
        sleep(1)
        self.oHelper.Screenshot("MATA103_04.png")   
        self.oHelper.SetValue("Natureza","2220001")
        sleep(1)  
        if self.oHelper.IfExists("A T E N Ç Ã O..."):
            self.oHelper.SetButton('Sim')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        self.oHelper.ClickFolder("Totais")   
        self.oHelper.Screenshot("MATA103_05.png")
        self.oHelper.SetButton("Salvar")
        
        if self.oHelper.IfExists("Natureza de Rendimentos"):
            self.oHelper.Screenshot("MATA103_06.png")
            self.oHelper.SetButton('Sim')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
        
        self.oHelper.WaitShow("Tipo de Pagamento")
        self.oHelper.SetValue('Tipo de Pagamento:', '03')
        self.oHelper.Screenshot("MATA103_07.png")
        self.oHelper.SetButton("Confirmar")
        sleep(1) 
        self.oHelper.WaitShow("Documento de Entrada - INCLUIR")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.WaitShow("Documento de Entrada")
        self.oHelper.Screenshot("MATA103_08.png")

        #------------------
        # VISUALIZAR
        #------------------
        
        self.oHelper.SetButton("Visualizar")
        self.oHelper.WaitShow("Documento de Entrada - VISUALIZAR")
        self.oHelper.CheckResult("Fornecedor","028050")
        self.oHelper.Screenshot("MATA103_09.png")
        self.oHelper.SetButton("Confirmar")
        sleep(1)
        
        #-----------------------------
        # CLASSIFICAR NOTA PELO ATIVO
        #----------------------------
        
        self.oHelper.Program('ATFA240')#309262  SN1.Dt.Aquisicao Maior ou igual a Item 001 e SN1.Dt.Aquisicao Menor ou Igual a Item 002
        sleep(2)
        self.oHelper.SetButton("Filtrar")
        sleep(0.5)
        self.oHelper.WaitShow("Gerenciador de Filtros")
        self.oHelper.ClickCheckBox("SN1.Dt.Aquisicao Maior ou igual a Item 001 e SN1.Dt.Aquisicao Menor ou Igual a Item 002",1)
        self.oHelper.Screenshot("PXFINA11_02_01.png")
        self.oHelper.SetButton("Aplicar filtros selecionados")
        sleep(0.6)
        if self.oHelper.IfExists("Filtro através de perguntas"):
            self.oHelper.SetValue('Dt.Aquisicao Maior ou igual a', DateSystem)
            self.oHelper.SetValue('Dt.Aquisicao Menor ou igual a', DateSystem)
            self.oHelper.SetButton('Confirmar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        self.oHelper.SetButton('Classificar')
        self.oHelper.SetBranch("02DF0001")
        self.oHelper.WaitShow("Ativo Imobilizado - Classificacao de Ativos Imobilizados")
        
        self.oHelper.SetButton("Confirmar")
        
        if self.oHelper.IfExists("Registro alterado com sucesso."):
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()
        else:
            self.oHelper.AssertTrue()
            
        #----------------------------------
        # IMPRIMIR RELATORIO ATIVOS
        #---------------------------
        
        self.oHelper.SetLateralMenu("Relatorios > Movimentos > Aquisições")
        sleep(1)
        
        
        
        
        
        

        #Autorizações

        self.oHelper.SetButton("Outras Ações","Autorizações")
        self.oHelper.WaitShow("Visão de autorizações - Consulta de autorizações")
        self.oHelper.LoadGrid()
        self.oHelper.SetValue("Autorizador",'02383219169',       grid=True, grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Documento de Entrada")
        self.oHelper.SetButton("Outras Ações","Responder Autorizações")
        self.oHelper.SetValue("MV_PAR01", "Sim")
        self.oHelper.SetButton("Ok")
        self.oHelper.WaitShow("Resposta processada com sucesso!")
        self.oHelper.SetButton("Fechar")

        #Excluir

        self.oHelper.SetButton("Outras Ações","Excluir")
        self.oHelper.WaitShow("Documento de Entrada - Excluir")
        self.oHelper.CheckResult("Numero","999")
        self.oHelper.CheckResult("Fornecedor","028050")
        self.oHelper.SetButton("Confirmar")


    @classmethod
    def tearDownClass(inst):

        inst.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MATA103('test_MATA103'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)