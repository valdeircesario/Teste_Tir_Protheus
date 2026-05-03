import os

from tir import Poui
import unittest
import sys
import logging
from time import sleep
from os import getcwd, path
from datetime import datetime, time, timedelta
from pytest import mark
import unittest
from time import sleep
from os import getcwd
sys.path.insert(0, path.abspath(path.join(path.dirname(__file__), '../../')))

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tools.Selenium_commands import SeleniumCommands

from tir import Webapp

# .\venv\Scripts\python.exe -m pytest .\TESTS\Outros\test_PXGPER35.py -s





class PXGPER35(unittest.TestCase):
    

    @classmethod
    def setUpClass(cls):
        
        
        cls.oHelper_Poui = Poui()
        cls.filial = '02DF0001'
        cls.dataref = (datetime.today() - timedelta(days=5)).strftime("%d/%m/%Y")

        configfile = getcwd() + '\\config.json'
        cls.oHelper = Webapp(configfile)


        cls.oHelper.Setup('SIGAMDI', cls.dataref, '02', cls.filial, '07')
        cls.oHelper.SetLateralMenu("Atualizações > Especificos > Extrato Abono Assiduidade")
        cls.oHelper.SetButton('Confirmar')

        # Tratativas padrão de ambiente
        if cls.oHelper.IfExists("Este ambiente utiliza base de Homologação."):
            cls.oHelper.SetButton('Fechar')

        if cls.oHelper.IfExists("Moedas"):
            cls.oHelper.SetButton('Confirmar')


    # ==================================================
    # TESTE
    # ==================================================
    def test_Extrato_Abono_Assiduidade(self):
        # Diretório onde o Protheus salva o arquivo
        download_path = r"C:\temp"   # 🔴 AJUSTE aqui conforme seu ambiente

        # Prefixo ou nome do arquivo (ajuste conforme sua rotina)
        nome_parcial = "Abono"

        # ✅ Snapshot antes da ação
        arquivos_antes = set(os.listdir(download_path))

        # Evidência inicial
        self.oHelper.WaitShow("Extrato de Abono")
        self.oHelper.SetValue('Data Inicio','01082025',check_value=False)
        self.oHelper.SetValue('Data Fim','30042026',check_value=False)
        #self.oHelper.ClickLabel('Individual')
        #self.oHelper.SetValue('Individual','227884',check_value=False)
        sleep(10)

        self.oHelper.SetButton('Confirmar')

        # Preenche o diálogo de salvar arquivo com a pasta de destino
        self.oHelper.SetFilePath(download_path, "save")

        # Aguardar o arquivo aparecer na pasta de download
        arquivo_baixado = None
        for _ in range(30):
            arquivos_depois = set(os.listdir(download_path))
            novos_arquivos = [f for f in arquivos_depois - arquivos_antes if nome_parcial in f]
            if novos_arquivos:
                arquivo_baixado = os.path.join(download_path, novos_arquivos[0])
                break
            sleep(1)

        assert arquivo_baixado is not None, "Arquivo não foi baixado!"
        assert os.path.exists(arquivo_baixado), "Arquivo não encontrado no caminho!"
        assert os.path.getsize(arquivo_baixado) > 0, "Arquivo vazio!"

        print(f"Arquivo baixado com sucesso: {arquivo_baixado}")
        print(f"Arquivo baixado com sucesso: {arquivo_baixado}")

    @classmethod
    def tearDownClass(cls):
        logging.info("Encerrando teste")
        cls.oHelper_Poui.TearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(PXGPER35('test_Extrato_Abono_Assiduidade'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)