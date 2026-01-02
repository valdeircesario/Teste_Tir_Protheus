from tir import Webapp
from os import getcwd
import unittest
from datetime import datetime
from time import sleep

DateSystem = datetime.today().strftime('%d/%m/%Y')

class CASO_DE_USO(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.Mat = '221658'# Matricula de um colaborador com ponto fixo para teste: (216743 = 000004),(221658 = 000005),(228204 = 000011),(227891 = 000019),(224584 = 000008)
        cls.cpf= '88477738068'
        cls.tel = '(61)11111888'# Novo telefone para alteração no ponto fixo
        cls.ponto = '000044'
        cls.filial = '02DF0001'
        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)
        cls.oHelper.Setup('SIGAMDI', DateSystem, '02', cls.filial, '07')
        #cls.oHelper.SetLateralMenu("Atualizações > Especificos > Ponto Fixo")
        cls.oHelper.SetLateralMenu("Atualizações > Especificos > Manutencao AD")

    def test_Ponto_fixo_caso_de_uso(self):

        if self.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper.SetButton('Fechar')

        if self.oHelper.IfExists("Moedas"):
            self.oHelper.CheckResult('Dolar', '0,0000')
            self.oHelper.SetButton('Confirmar')

        """ self.oHelper.WaitShow("Ponto Fixo")
        
        self.oHelper.SetButton("Outras Ações", "Pesquisar")
        self.oHelper.SetButton("Parâmetro")
        self.oHelper.SetValue("Codigo", self.ponto)
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Alterar")
        
        self.oHelper.WaitShow("Ponto Fixo Poupex - ALTERAR")
        

        valor_anterior_tel   = self.oHelper.GetValue("ZW_TELEFON")# Armazena valor anterior do telefone para restauração posterior
        
        # -------------------------
        # Edição dos campos
        # -------------------------
        

        self.oHelper.SetFocus("ZW_TELEFON")
        self.oHelper.SetValue("ZW_TELEFON", self.tel)
        self.oHelper.WaitFieldValue("ZW_TELEFON", self.tel)
        self.oHelper.SetKey("TAB")

        # Verifica o resultado
        assert_tel = self.oHelper.CheckResult("ZW_TELEFON", self.tel)
        if not assert_tel:
            self.oHelper.Screenshot(filename="erro_preenchimento.png")

        # -------------------------
        # Confirma alteração
        # -------------------------
        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Registro alterado com sucesso.")
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Ponto Fixo")

        
        # -------------------------
        # Visualizar alteração
        # -------------------------
        self.oHelper.SetButton("Outras Ações","Visualizar")
        self.oHelper.WaitShow("Ponto Fixo Poupex - VISUALIZAR")
        self.oHelper.CheckResult("ZW_TELEFON", self.tel)
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Ponto Fixo") """
        
        
        # -------------------------
        # Atualizar AD
        # -------------------------
        
        #self.oHelper.SetButton("Outras Ações", "Atualizar AD")
        #self.oHelper.WaitShow("Esta rotina envia todos os funcionarios vinculados aos ponto fixos para atualizar telefone no AD!")
        #self.oHelper.SetButton("Sim")
        sleep(0.2)
        
        
        # -------------------------
        # Acessar módulo de Manutenção AD
        # -------------------------
    
        #self.oHelper.SetLateralMenu("Atualizações > Especificos > Manutencao AD")
    
        
        self.oHelper.WaitShow("Bloqueio e Desbloqueio AD")  # Ajuste para o texto da tela que aparece
        
        #self.oHelper.SearchBrowse(f'225829', 'Maticula')
        #self.oHelper.SearchBrowse(self.Mat+DateSystem,key=2,index=True)
        
        #self.oHelper.ScrollGrid(column="Data Registro",match_value=DateSystem)
        #self.oHelper.SetButton("Alterar")
        
        


        # Por exemplo: acessar funcionalidades do novo módulo
        self.oHelper.SetButton("Outras Ações", "Pesquisar")
        
        self.oHelper.ClickLabel("atricula+data Inicio",grid_number=2)  
        
        self.oHelper.LoadGrid()

        #self.oHelper.ClickLabel("Coluna")
        #self.oHelper.ClickListBox("Matricula+data Inicio")
        self.oHelper.SetValue("CCAMPO", self.Mat,DateSystem)
        #self.oHelper.SetButton("Ok")

        
        
        
        
        
        
        
        # -------------------------
        ##volta para ponto fixo para restaurar telefone
        # -------------------------
        
        
        """ self.oHelper.SetLateralMenu("Atualizações > Especificos > Ponto Fixo")
        
        self.oHelper.WaitShow("Ponto Fixo")
        
        self.oHelper.SetButton("Outras Ações", "Pesquisar")
        self.oHelper.SetButton("Parâmetro")
        self.oHelper.SetValue("Codigo", self.ponto)
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow("Ponto Fixo Poupex - ALTERAR") """

        # -------------------------
        # Edita telefone (restaura)
        # -------------------------
        
        """ self.oHelper.SetFocus("ZW_TELEFON")
        #self.oHelper.SetValue("ZW_TELEFON", valor_anterior_tel)
        #self.oHelper.WaitFieldValue("ZW_TELEFON", valor_anterior_tel)
        self.oHelper.SetKey("TAB") """

        #assert_tel_restore = self.oHelper.CheckResult("ZW_TELEFON", valor_anterior_tel)
        #if not assert_tel_restore:
            #self.oHelper.Screenshot(filename="erro_preenchimento_restore.png")

        # -------------------------
        # Confirma restauração
        # -------------------------
        """ self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Registro alterado com sucesso.")
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Ponto Fixo") """
        
       
        #self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(cls):
        cls.oHelper.TearDown()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CASO_DE_USO('test_Ponto_fixo_caso_de_uso'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)