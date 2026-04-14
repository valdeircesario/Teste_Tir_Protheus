from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver import ActionChains

class SeleniumCommands:
    """Classe para envio de teclas de atalho com Selenium"""
    
    def __init__(self, driver):
        self.driver = driver
    
    def send_key(self, element_tag, key):
        """Envia uma única tecla para o elemento"""
        element = self.driver.find_element(By.TAG_NAME, element_tag)
        element.send_keys(key)


class ClickCommands:
    """Classe para cliques em elementos com Selenium usando seletores"""
    
    def __init__(self, driver):
        self.driver = driver
    
    def click_by_selector(self, selector, locator=By.CSS_SELECTOR, timeout=10, delay=0):
        """
        Clica em um elemento usando seletor CSS ou outro localizador.
        
        Args:
            selector (str): O seletor do elemento (ex: 'aside > button:nth-child(5)')
            locator: O tipo de localizador (By.CSS_SELECTOR, By.ID, By.XPATH, etc)
            timeout (int): Tempo máximo de espera em segundos
            delay (float): Delay após o clique em segundos
        
        Returns:
            bool: True se clicou com sucesso, False caso contrário
        
        Example:
            click = ClickCommands(driver)
            click.click_by_selector('aside > button:nth-child(5)', locator=By.CSS_SELECTOR)
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.element_to_be_clickable((locator, selector)))
            element.click()
            if delay > 0:
                sleep(delay)
            print(f"✓ Clicou com sucesso no elemento: {selector}")
            return True
        except Exception as e:
            print(f"✗ Erro ao clicar no elemento '{selector}': {str(e)}")
            return False
    
    def click_by_id(self, element_id, timeout=10, delay=0):
        """
        Clica em um elemento usando o ID.
        
        Args:
            element_id (str): ID do elemento
            timeout (int): Tempo máximo de espera em segundos
            delay (float): Delay após o clique em segundos
        
        Returns:
            bool: True se clicou com sucesso, False caso contrário
        
        Example:
            click = ClickCommands(driver)
            click.click_by_id('COMP4577')
        """
        return self.click_by_selector(element_id, locator=By.ID, timeout=timeout, delay=delay)
    
    def click_by_xpath(self, xpath, timeout=10, delay=0):
        """
        Clica em um elemento usando XPath.
        
        Args:
            xpath (str): XPath do elemento
            timeout (int): Tempo máximo de espera em segundos
            delay (float): Delay após o clique em segundos
        
        Returns:
            bool: True se clicou com sucesso, False caso contrário
        
        Example:
            click = ClickCommands(driver)
            click.click_by_xpath("//button[@id='submit']")
        """
        return self.click_by_selector(xpath, locator=By.XPATH, timeout=timeout, delay=delay)
    
    
    
    
    
    
    
def click_by_locator(self, selector, locator=Por.CSS_SELECTOR, right_click=False, timeout=10):
        """
        Clica em um elemento usando CSS, ID ou XPATH (padrão TIR)
        """

        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((locator, selector))
        )

        if right_click:
            from selenium.webdriver import ActionChains
            ActionChains(self.driver).context_click(element).perform()
        else:
            element.click()

    