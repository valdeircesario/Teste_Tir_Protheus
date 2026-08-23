from tir import Webapp
from os import getcwd
import unittest
from datetime import datetime
from time import sleep
DateSystem = datetime.today().strftime('%d/%m/%Y')

#------------------------------------------
#-- Teste calendario contabil
#------------------------------------------




class CTBA010(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       
        cls.Codigo = '000000000000003'
        cls.Descrição = 'IMPRESSORA 3D'
        cls.Tipo = 'ME'
        cls.Unidade = 'PC'
        cls.Armazem = '01'
        cls.Grupo = '0003'
        cls.Preco = '99,00'
        cls.NomeCientifico = 'IMPRESSORA 3D NOME CIENTIFICO'
        cls.filial = '01'
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '34')
        cls.oHelper.SetLateralMenu("Atualizações > Cadastros > Calendário Contábil")
        cls.oHelper.SetButton("Confirmar")

    def test_de_incluir_produtos(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        self.oHelper.WaitShow("Cadastro Calendário Contábil")

        #-------------------------
        # calendario contabil
        #-------------------------
        """ self.oHelper.SetButton("Filtrar")
        self.oHelper.SetButton("Criar Filtro")
        self.oHelper.SetValue("Campo","Status Per")
        self.oHelper.SetValue("Opções",'1 - Aberto')
        self.oHelper.SetButton('Adicionar')
        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton("Criar Filtro")
        self.oHelper.SetValue("Campo","Exercicio")
        self.oHelper.SetValue("Expressão",'2026')
        self.oHelper.SetButton('Adicionar')
        self.oHelper.SetButton('Salvar')
        self.oHelper.ClickCheckBox('Status Per Igual a')
        self.oHelper.ClickCheckBox('Exercicio Igual a')
        self.oHelper.SetButton('Aplicar filtros selecionados') """

        self.oHelper.SetButton('Alterar')
        self.oHelper.WaitShow('Cadastro Calendário Contábil')
        self.oHelper.ScrollGrid(column='Dt Inicio',match_value='01/08/2026')
        self.oHelper.SetValue("Status Per","2 - Fechado",grid=True,check_value=False)
        self.oHelper.GetGrid()








        
        self.oHelper.SetButton("Incluir")
        sleep(1)
        self.oHelper.WaitShow("Atualizacao de Produtos - Incluir")
        self.oHelper.SetValue("B1_COD", self.Codigo)
        self.oHelper.SetValue("B1_DESC", self.Descrição)
        self.oHelper.SetValue("B1_TIPO", self.Tipo)
        self.oHelper.SetValue("B1_UM", self.Unidade)
        self.oHelper.SetValue("B1_LOCPAD", self.Armazem)
        self.oHelper.SetValue("B1_GRUPO", self.Grupo)
        self.oHelper.SetValue("B1_UPRC", self.Preco)
        self.oHelper.SetValue("B5_CEME", self.NomeCientifico)

        self.oHelper.SetButton("Confirmar")
        sleep(0.5)


       
        self.oHelper.WaitShow("Registro inserido com sucesso.")
        self.oHelper.SetButton("Fechar")
        sleep(1)
        self.oHelper.WaitShow("Atualizacao de Produtos:")
        

        #-------------------------
        # Visualização da inclusão
        #-------------------------
        self.oHelper.SetButton("Visualizar")
        self.oHelper.WaitShow("Atualizacao de Produtos - Visualizar")
        self.oHelper.CheckResult("B1_DESC", self.Descrição)
        self.oHelper.CheckResult("B1_GRUPO", self.Grupo)
        self.oHelper.CheckResult("B5_CEME", self.NomeCientifico)
        self.oHelper.CheckResult("B1_UPRC", self.Preco)
        self.oHelper.CheckResult("B1_LOCPAD", self.Armazem)
        self.oHelper.CheckResult("B1_TIPO", self.Tipo)
        self.oHelper.CheckResult("B1_UM", self.Unidade)
        self.oHelper.SetButton("Fechar")

        sleep(0.5)

        self.oHelper.WaitShow("Atualizacao de Produtos:")

        self.oHelper.AssertTrue()
        print("🎯 test_de_incluir_produtos")
        print("✅ Teste finalizado com sucesso")

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CTBA010('test_de_incluir_produtos'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)