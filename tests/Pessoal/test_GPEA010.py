from tir import Webapp
from os import getcwd
import unittest
from datetime import datetime
from time import sleep
DateSystem = datetime.today().strftime('%d/%m/%Y')

# .\venv\Scripts\python.exe -m pytest tests/Pessoal/test_GPEA010.py -v -s --html=report_GPEA010.html --self-contained-html
#------------------------------------------
#-- Teste GPEA010 - Cadastro de Funcionários
#------------------------------------------


class GPEA010(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
       
        cls.Nome = 'FABIANO PEREIRA NUNDES'
        cls.Mãe = 'MADALENA FERNANDES DA SILVA'
        cls.Pai = 'JORGE CESARIO DA SILVA'
        cls.Sexo = 'M - Masculino'# M - Masculino, F - Feminino
        cls.Nacimento = '01/01/1994'
        cls.EstadoCivil = 'C'
        cls.Apelido = 'FABIANO'
        cls.Email = 'FABIANO@GMAIL.COM'

        #Funcionais
        cls.CentroCusto = '002'

        #documentos
        cls.CPF = '741.250.390-11'#,986.608.380-25,672.118.440-00,337.884.870-70,526.253.600-03
        cls.Pis = '78170237440'#,06953700070,86292005064,21036015841,39350366875
        cls.RG = '542897'
        cls.DataEmisao = '01/06/2000'
        cls.UFEmisao = 'DF'

        #Endereço
        cls.Endereco = 'BAIRRO PAULISTA'
        cls.Logradouro = 'RUA DOS CRAVOS'
        cls.Numero = '10'
        cls.Complemento = 'CASA 02'
        cls.Bairro = 'SANTA MARIA'
        cls.CEP = '72605-410'
        cls.DDDFONE = '61'
        cls.TELEFON = '91234-900'

        cls.filial = '01'
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', DateSystem, '99', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Atualizações > Funcionários > Funcionários")
        

    def test_de_incluir_Funcionario(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        self.oHelper.WaitShow("Cadastro de Funcionários")
        
        self.oHelper.SetButton("Incluir")
        sleep(1)
        self.oHelper.WaitShow("Cadastro de Funcionários")

        self.oHelper.SetValue("RA_NOME", self.Nome, check_value = False)
        self.oHelper.SetValue("RA_MAE", self.Mãe, check_value = False)
        self.oHelper.SetValue("RA_PAI", self.Pai)
        self.oHelper.SetValue("Sexo", self.Sexo)
        self.oHelper.SetValue("Raca/Cor", "2 - Branca")
        self.oHelper.SetValue("RA_NASC", self.Nacimento)
        self.oHelper.SetValue("RA_ESTCIVI", self.EstadoCivil)
        self.oHelper.SetValue("RA_CPAISOR", "01058")
        self.oHelper.SetValue("RA_NACIONA", "10")
        self.oHelper.SetValue("RA_NATURAL", "DF")
        self.oHelper.SetValue("RA_CODMUNN", "00108")
        self.oHelper.SetValue("RA_APELIDO", self.Apelido)
        self.oHelper.SetValue("RA_GRINRAI", "55")
        self.oHelper.SetValue("RA_EMAIL", self.Email)

        self.oHelper.SetKey("TAB") 

        #-----------------------
        # Acesso a aba Funcionais
        #-----------------------

        self.oHelper.ClickFolder("Funcionais")

        self.oHelper.SetValue("RA_CC", self.CentroCusto)
        self.oHelper.SetValue("RA_ADMISSA", DateSystem)
        self.oHelper.SetValue("RA_TIPOADM", "1B")
        self.oHelper.SetValue("RA_HRSMES", "180", check_value = False)
        self.oHelper.SetValue("RA_PROCES", "00001", check_value = False)
        self.oHelper.SetValue("RA_CATFUNC", "M")
        self.oHelper.SetValue("RA_CODFUNC", "00011")
        self.oHelper.SetValue("RA_PGCTSIN", "N")
        self.oHelper.SetValue("RA_TIPOALT", "001")
        self.oHelper.SetValue("Ct.T.Parcial", "2 - Não")
        self.oHelper.SetValue("RA_SINDICA", "01")
        self.oHelper.SetValue("RA_TIPOPGT", "M")
        self.oHelper.SetValue("RA_VIEMRAI", "15")
        self.oHelper.SetValue("RA_CARGO", "0002")
        self.oHelper.SetValue("RA_CODTIT", "01")
        self.oHelper.SetValue("RA_DEPTO", "000000004", check_value = False)
        self.oHelper.SetValue("Comp. Sábado", "2 - Não", check_value = False)
        self.oHelper.SetKey("TAB") 

        #-----------------------
        # Acesso a aba Documentos
        #-----------------------

        self.oHelper.ClickFolder("No.documentos")

        self.oHelper.SetValue("RA_CIC", self.CPF)
        self.oHelper.SetValue("RA_PIS", self.Pis)
        self.oHelper.SetValue("RA_RG", self.RG)
        self.oHelper.SetValue("RA_DTRGEXP", self.DataEmisao)#
        self.oHelper.SetValue("RA_RGUF", "DF")
        self.oHelper.SetValue("RA_RGORG", "SSP")
        self.oHelper.SetValue("RA_NUMCP", "458795")
        self.oHelper.SetValue("RA_SERCP", "02")
        self.oHelper.SetValue("RA_UFCP", "DF")
        self.oHelper.SetValue("RA_DTCPEXP", self.DataEmisao)

        self.oHelper.SetKey("TAB")

        #-------------------------
        # Acesso a aba Benefícios
        #-------------------------
        self.oHelper.ClickFolder("Beneficios")
        sleep(1)

        # Sem beneficios, apenas acesso para teste

        #-----------------------
        # Acesso a aba Relogios Registrador
        #-----------------------

        self.oHelper.ClickFolder("Relógio Registrador")
        sleep(1)
        self.oHelper.SetValue("RA_TNOTRAB", "02")
        self.oHelper.SetKey("TAB")
        self.oHelper.SetValue("RA_CRACHA", "123458")

        self.oHelper.SetKey("TAB")

        #-----------------------
        # Acesso a aba de Outras Informações
        #-----------------------

        self.oHelper.ClickFolder("Outras Informacoes")
        sleep(1)
        # Sem outras informações, apenas acesso para teste

        #-------------------------
        # Acesso a aba de Cargo e Salarios
        #-------------------------

        self.oHelper.ClickFolder("Cargos e Salarios")
        sleep(1)
        # Sem cargos e salarios, apenas acesso para teste

        #-------------------------
        # Acesso a aba de Endereço
        #-------------------------

        self.oHelper.ClickFolder("Endereço")
        sleep(1)
        self.oHelper.SetValue("Tip.Endereço", "2 - Residencial")

        self.oHelper.SetValue("RA_LOGRDSC", self.Logradouro, check_value = False)
        self.oHelper.SetValue("RA_LOGRNUM", self.Numero, check_value = False)
        self.oHelper.SetValue("RA_ENDEREC", self.Endereco, check_value = False)
        self.oHelper.SetValue("RA_NUMENDE", "CENTRO", check_value = False)
        self.oHelper.SetValue("RA_COMPLEM", self.Complemento, check_value = False)
        self.oHelper.SetValue("RA_BAIRRO", self.Bairro, check_value = False)
        self.oHelper.SetValue("RA_ESTADO", "DF")
        self.oHelper.SetValue("RA_CODMUN", "00108")
        self.oHelper.SetValue("RA_MUNICIP", "BRASILIA")
        self.oHelper.SetValue("RA_CEP", self.CEP)
        self.oHelper.SetValue("RA_CEPCXPO", self.CEP)
        self.oHelper.SetValue("RA_DDDFONE", self.DDDFONE)
        self.oHelper.SetValue("RA_TELEFON", self.TELEFON)
        self.oHelper.SetKey("TAB")

        #-------------------------
        # Acessar a aba de Estrangeiros
        #-------------------------

        self.oHelper.ClickFolder("Estrangeiro")
        sleep(1)
        # Sem dados de estrangeiro, apenas acesso para teste

        #-------------------------
        # Acessar a aba Adicionais
        #-------------------------

        self.oHelper.ClickFolder("Adicionais")
        sleep(1)
        # Sem dados adicionais, apenas acesso para teste

        #-------------------------
        # Acessar a aba de Outros
        #-------------------------
        self.oHelper.ClickFolder("Outros")
        sleep(1)
        # Sem dados adicionais, apenas acesso para teste


        #-------------------------
        # Salvar o cadastro do funcionário
        #-------------------------

        self.oHelper.ClickFolder("Cadastrais")
        sleep(0.5)

        self.oHelper.SetButton("Salvar")

        sleep(0.5)
        self.oHelper.SetButton("Fechar", timeout=2)
        sleep(1.5)
       
        
        self.oHelper.AssertTrue()
        print("🎯 test_de_incluir_Funcionario")
        print("✅ Teste finalizado com sucesso")

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA010('test_de_incluir_Funcionario'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)