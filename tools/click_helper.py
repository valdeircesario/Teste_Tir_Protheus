from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


class ClickHelper:
    """Classe para cliques em elementos com Selenium pelo ID"""
    
    def __init__(self, driver):
        """Inicializa com o driver do Selenium"""
        self.driver = driver
    
    def click_by_id(self, element_id, timeout=10, delay=0):
        """
        Clica em um elemento usando o ID.
        
        Args:
            element_id: ID do elemento
            timeout: Tempo máximo de espera em segundos
            delay: Delay após o clique em segundos
        
        Returns:
            bool: True se clicou com sucesso, False caso contrário
        
        Example:
            click = ClickHelper(driver)
            click.click_by_id("COMP4579", timeout=10, delay=0.5)
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.ID, element_id))
            )
            element.click()
            if delay > 0:
                sleep(delay)
            print(f"✓ Clicou com sucesso no elemento: {element_id}")
            return True
        except Exception as e:
            print(f"✗ Erro ao clicar no elemento '{element_id}': {str(e)}")
            return False
