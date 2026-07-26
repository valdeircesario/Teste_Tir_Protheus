from tir import Webapp
from os import getcwd
import unittest
from datetime import datetime
from time import sleep
DateSystem = datetime.today().strftime('%d/%m/%Y')

# # python -m pytest tests/SIGAGPE/test_GPEA010.py -v -s --html=reports/report_GPEA010.html --self-contained-html
# # .\venv\Scripts\python.exe 
#------------------------------------------
#-- Teste GPEA010 - Cadastro de Funcionários
#------------------------------------------


class GPEA010(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
       
        cls.Nome = 'CASSIANO PEREIRA CAMARGO'
        cls.Mãe = 'LENA FERNANDES DA SILVA'
        cls.Pai = 'JORGE OLIVEIRA DA SILVA'
        cls.Sexo = 'M - Masculino'# M - Masculino, F - Feminino
        cls.Nacimento = '01/01/1996'
        cls.EstadoCivil = 'C'
        cls.Apelido = 'CIANO'
        cls.Email = 'CASSIANO123@GMAIL.COM'

        #Funcionais
        cls.CentroCusto = '002'

        #documentos
        cls.CPF = '986.608.380-25'#672.118.440-00,337.884.870-70,526.253.600-03
        cls.Pis = '06953700070'#86292005064,21036015841,39350366875
        cls.RG = '5428982'
        cls.DataEmisao = '01/06/2001'
        cls.UFEmisao = 'DF'

        #Endereço
        cls.Endereco = 'BAIRRO SANTACRUZ'
        cls.Logradouro = 'RUA PASSA QUARTRO'
        cls.Numero = '18'
        cls.Complemento = 'CASA 20'
        cls.Bairro = 'SANTA MARIA'
        cls.CEP = '72605-410'
        cls.DDDFONE = '61'
        cls.TELEFON = '91234-654'

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
        self.oHelper.Screenshot('Funcionario/GPEA010_01')
        # --------------------
        # Incluir
        #---------------------

        print('--------------------Incluir')
        self.oHelper.SetButton("Incluir")
        self.oHelper.WaitShow("Cadastro de Funcionários")
        self.oHelper.Screenshot('Funcionario/GPEA010_02')
        self.oHelper.SetValue("RA_NOME", self.Nome,         check_value = False)
        self.oHelper.SetValue("RA_MAE", self.Mãe,           check_value = False)
        self.oHelper.SetValue("RA_PAI", self.Pai,           check_value=False)
        self.oHelper.SetValue("Sexo", self.Sexo,            check_value=False)
        self.oHelper.Screenshot('Funcionario/GPEA010_03')
        self.oHelper.SetValue("Raca/Cor", "2 - Branca",     check_value=False)
        self.oHelper.SetValue("RA_NASC", self.Nacimento,    check_value=False)
        self.oHelper.SetValue("RA_ESTCIVI",self.EstadoCivil,check_value=False)
        self.oHelper.SetValue("RA_CPAISOR", "01058",        check_value=False)
        self.oHelper.SetValue("RA_NACIONA", "10",           check_value=False)
        self.oHelper.SetValue("RA_NATURAL", "DF",           check_value=False)
        self.oHelper.SetValue("RA_CODMUNN", "00108",        check_value=False)
        self.oHelper.Screenshot('Funcionario/GPEA010_04')
        self.oHelper.SetValue("RA_APELIDO", self.Apelido,   check_value=False)
        self.oHelper.SetValue("RA_GRINRAI", "55",           check_value=False)
        self.oHelper.SetValue("RA_EMAIL", self.Email,       check_value=False)
        self.oHelper.SetKey("TAB",wait_change=False) 

        #-----------------------
        # Acesso a aba Funcionais
        #-----------------------
        print('---------------------Dados Funcionais')
        self.oHelper.ClickFolder("Funcionais")
        self.oHelper.Screenshot('Funcionario/GPEA010_05')
        self.oHelper.SetValue("RA_CC", self.CentroCusto,      check_value=False)
        self.oHelper.SetValue("RA_ADMISSA", DateSystem,       check_value=False)
        self.oHelper.SetValue("RA_TIPOADM", "1B",             check_value=False)
        self.oHelper.SetValue("RA_HRSMES", "180",             check_value = False)
        self.oHelper.SetValue("RA_PROCES", "00001",           check_value = False)
        self.oHelper.SetValue("RA_CATFUNC", "M",              check_value=False)
        self.oHelper.Screenshot('Funcionario/GPEA010_06')
        self.oHelper.SetValue("RA_CODFUNC", "00011",          check_value=False)
        self.oHelper.SetValue("RA_PGCTSIN", "N",              check_value=False)
        self.oHelper.SetValue("RA_TIPOALT", "001",            check_value=False)
        self.oHelper.SetValue("Ct.T.Parcial", "2 - Não",      check_value=False)
        self.oHelper.SetValue("RA_SINDICA", "01",             check_value=False)
        self.oHelper.SetValue("RA_TIPOPGT", "M",              check_value=False)
        self.oHelper.Screenshot('Funcionario/GPEA010_07')
        self.oHelper.SetValue("RA_VIEMRAI", "15",             check_value=False)
        self.oHelper.SetValue("RA_CARGO", "0002",             check_value=False)
        self.oHelper.SetValue("RA_CODTIT", "01",              check_value=False)
        self.oHelper.SetValue("RA_DEPTO", "000000004",        check_value = False)
        self.oHelper.SetValue("Comp. Sábado", "2 - Não",      check_value = False)
        self.oHelper.SetKey("TAB",wait_change=False) 
        self.oHelper.Screenshot('Funcionario/GPEA010_08')

        #-----------------------
        # Acesso a aba Documentos
        #-----------------------
        print('--------------Numeros de documentos')
        self.oHelper.ClickFolder("No.documentos")
        self.oHelper.Screenshot('Funcionario/GPEA010_09')
        self.oHelper.SetValue("RA_CIC", self.CPF,               check_value=False)
        self.oHelper.SetValue("RA_PIS", self.Pis,               check_value=False)
        self.oHelper.SetValue("RA_RG", self.RG,                 check_value=False)
        self.oHelper.SetValue("RA_DTRGEXP", self.DataEmisao,    check_value=False)#
        self.oHelper.SetValue("RA_RGUF", "DF",                  check_value=False)
        self.oHelper.Screenshot('Funcionario/GPEA010_10')
        self.oHelper.SetValue("RA_RGORG", "SSP",                check_value=False)
        self.oHelper.SetValue("RA_NUMCP", "458795",             check_value=False)
        self.oHelper.SetValue("RA_SERCP", "02",                 check_value=False)
        self.oHelper.SetValue("RA_UFCP", "DF",                  check_value=False)
        self.oHelper.SetValue("RA_DTCPEXP", self.DataEmisao,    check_value=False)
        self.oHelper.Screenshot('Funcionario/GPEA010_11')
        self.oHelper.SetKey("TAB",wait_change=False)

        #-------------------------
        # Acesso a aba Benefícios
        #-------------------------
        print('--------------------Beneficios')
        self.oHelper.ClickFolder("Beneficios")
        sleep(1)

        # Sem beneficios, apenas acesso para teste

        #-----------------------
        # Acesso a aba Relogios Registrador
        #-----------------------
        print('---------------------Relogio Registrador')
        self.oHelper.ClickFolder("Relógio Registrador")
        self.oHelper.SetValue("RA_TNOTRAB", "02",       check_value=False)
        self.oHelper.SetKey("TAB",wait_change=False)
        self.oHelper.SetValue("RA_CRACHA", "123458",    check_value=False)
        self.oHelper.SetKey("TAB",wait_change=False)
        self.oHelper.Screenshot('Funcionario/GPEA010_12')

        #-----------------------
        # Acesso a aba de Outras Informações
        #-----------------------
        print('----------------------Outras Informações')
        self.oHelper.ClickFolder("Outras Informacoes")
        sleep(1)
        # Sem outras informações, apenas acesso para teste

        #-------------------------
        # Acesso a aba de Cargo e Salarios
        #-------------------------
        print('-------------------------Cargos e Salarios')
        self.oHelper.ClickFolder("Cargos e Salarios")
        sleep(1)
        # Sem cargos e salarios, apenas acesso para teste

        #-------------------------
        # Acesso a aba de Endereço
        #-------------------------
        print('-----------------------Endereço')
        self.oHelper.ClickFolder("Endereço")
        self.oHelper.Screenshot('Funcionario/GPEA010_13')
        self.oHelper.SetValue("Tip.Endereço", "2 - Residencial",    check_value=False)

        self.oHelper.SetValue("RA_LOGRDSC", self.Logradouro,        check_value = False)
        self.oHelper.SetValue("RA_LOGRNUM", self.Numero,            check_value = False)
        self.oHelper.SetValue("RA_ENDEREC", self.Endereco,          check_value = False)
        self.oHelper.SetValue("RA_NUMENDE", "CENTRO",               check_value = False)
        self.oHelper.Screenshot('Funcionario/GPEA010_14')
        self.oHelper.SetValue("RA_COMPLEM", self.Complemento,       check_value = False)
        self.oHelper.SetValue("RA_BAIRRO", self.Bairro,             check_value = False)
        self.oHelper.SetValue("RA_ESTADO", "DF",                    check_value=False)
        self.oHelper.SetValue("RA_CODMUN", "00108",                 check_value=False)
        self.oHelper.SetValue("RA_MUNICIP", "BRASILIA",             check_value=False)
        self.oHelper.SetValue("RA_CEP", self.CEP,                   check_value=False)
        self.oHelper.SetValue("RA_CEPCXPO", self.CEP,               check_value=False)
        self.oHelper.SetValue("RA_DDDFONE", self.DDDFONE,           check_value=False)
        self.oHelper.SetValue("RA_TELEFON", self.TELEFON,           check_value=False)
        self.oHelper.SetKey("TAB",wait_change=False)
        self.oHelper.Screenshot('Funcionario/GPEA010_15')

        #-------------------------
        # Acessar a aba de Estrangeiros
        #-------------------------
        print('---------------------Estrangeiro')
        self.oHelper.ClickFolder("Estrangeiro")
        sleep(1)
        # Sem dados de estrangeiro, apenas acesso para teste

        #-------------------------
        # Acessar a aba Adicionais
        #-------------------------
        print('-----------------------Adicionais')
        self.oHelper.ClickFolder("Adicionais")
        sleep(1)
        # Sem dados adicionais, apenas acesso para teste

        #-------------------------
        # Acessar a aba de Outros
        #-------------------------
        print('---------------------Outros')
        self.oHelper.ClickFolder("Outros")
        sleep(1)
        # Sem dados adicionais, apenas acesso para teste


        #-------------------------
        # Salvar o cadastro do funcionário
        #-------------------------
        print('--------------------Voltar ao cadastro e salvar')
        self.oHelper.ClickFolder("Cadastrais")
        self.oHelper.Screenshot('Funcionario/GPEA010_16')
        self.oHelper.SetButton("Salvar")
        self.oHelper.Screenshot('Funcionario/GPEA010_17')
        self.oHelper.CheckHelp(text="CAMPO NÃO PREENCHIDO", button="Fechar")
        self.oHelper.Screenshot('Funcionario/GPEA010_18')
       
        
        self.oHelper.AssertTrue()
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X 🎯 test_de_incluir_Funcionario")
        print("X ✅ Teste finalizado com sucesso")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GPEA010('test_de_incluir_Funcionario'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)