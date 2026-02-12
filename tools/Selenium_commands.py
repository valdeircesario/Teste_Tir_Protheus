from selenium.webdriver.common.by import By

class SeleniumCommands:
    """Classe para envio de teclas de atalho com Selenium"""
    
    def __init__(self, driver):
        self.driver = driver
    
    def send_key(self, element_tag, key):
        """Envia uma única tecla para o elemento"""
        element = self.driver.find_element(By.TAG_NAME, element_tag)
        element.send_keys(key)
    
    