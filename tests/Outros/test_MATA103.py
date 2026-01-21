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
        '''self.diaprox = (datetime.today()+timedelta(days=-30)).strftime("%d/%m/%Y")'''
        self.oHelper = Webapp(configfile)
        self.oHelper.Setup('SIGAMDI', DateSystem, '02', self.filial, '02')
        self.oHelper.SetLateralMenu("Atualizações > Movimentos > Documento Entrada")
        #self.oHelper.SetButton('Confirmar')

    def test_MATA103(self):

        #Inclusão de PC

        self.oHelper.WaitShow("Atenção - Reforma Tributária")

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

        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("02DF0001")
        self.oHelper.WaitShow("Documento de Entrada - INCLUIR")
        self.oHelper.SetValue('Numero', '999')
        self.oHelper.SetValue('Serie', '01')
        self.oHelper.SetValue('Fornecedor', '028050', direction='right')
        self.oHelper.SetValue('Espec.Docum.', 'NF')
        self.oHelper.SetValue("Produto",'000000000000418',       grid=True, grid_number=1)
        self.oHelper.SetValue("Quantidade",'10,00',              grid=True, grid_number=1)
        self.oHelper.SetValue("Vlr.Unitario",'10,0000',          grid=True, grid_number=1)
        self.oHelper.SetValue("Centro Custo",'000000677',        grid=True, grid_number=1)
        self.oHelper.SetValue("Tipo Entrada",'241',              grid=True, grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.Screenshot("MATA103_01")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Sim")
        self.oHelper.WaitShow("Tipo de Pagamento")
        self.oHelper.SetValue('Tipo de Pagamento:', '01')
        self.oHelper.SetValue('Terceiro:', '028050')
        self.oHelper.Screenshot("MATA103_02")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Documento de Entrada - INCLUIR")
        self.oHelper.SetButton("Cancelar")

        #Visualizar

        self.oHelper.SetButton("Visualizar")
        self.oHelper.WaitShow("Documento de Entrada - VISUALIZAR")
        self.oHelper.CheckResult("Fornecedor","028050")
        self.oHelper.SetButton("Confirmar")

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