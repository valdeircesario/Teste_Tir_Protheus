
from time import sleep

from tir import Poui, Webapp
import unittest
from datetime import datetime
from os import getcwd

class PGCA010(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        configfile = getcwd() + '\\config.json'
        cls.oHelper_Poui = Poui(configfile)
        cls.oHelper_Webapp = Webapp(configfile, autostart=False)
        cls.oHelper_Webapp.Setup("SIGAMDI", datetime.today().strftime('%d/%m/%Y'), "02", "02DF0001", '02')
        cls.oHelper_Webapp.Program('PGCA010')
        cls.oHelper_Webapp.SetButton('Confirmar')
        
        
    def test_PGCA010_001(self):
        sleep(5)
        self.oHelper_Poui.ClickMenu('Abrir menu')
        self.oHelper_Poui.ClickSelect('Visão', 'Compras')

        if self.oHelper_Webapp.IfExists("Este ambiente utiliza base de Homologação."):
            self.oHelper_Webapp.SetButton('Fechar')
            self.oHelper_Webapp.AssertTrue()
        else:
            self.oHelper_Webapp.AssertTrue()

        if self.oHelper_Webapp.IfExists("Moedas"):
            self.oHelper_Webapp.CheckResult('Dolar', '0,0000')
            self.oHelper_Webapp.SetButton('Confirmar')
            self.oHelper_Webapp.AssertTrue()
        else:
            self.oHelper_Webapp.AssertTrue()

        self.oHelper_Poui.ClickWidget(title='Lead Time SC x PC', action='Detalhes')
        self.oHelper_Poui.ClickButton('Fechar')
        self.oHelper_Poui.AssertTrue()

    @classmethod
    def tearDownClass(cls):
        cls.oHelper_Poui.TearDown()


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
