from selenium.webdriver.common.by import By
import time

class ClickCSS:
    """Classe para clicar em elementos dentro de Shadow DOM"""
    
    def __init__(self, driver):
        self.driver = driver
    
    def click(self, host_css, target_css, timeout=10):
        """
        Clica em um elemento dentro de um Shadow DOM.
        
        Args:
            host_css: Seletor CSS do host element (ex: 'wa-print-preview')
            target_css: Seletor CSS do elemento dentro do Shadow DOM
            timeout: Tempo em segundos para tentar encontrar o elemento
        """
        for attempt in range(timeout):
            result = self.driver.execute_script(f"""
            let host = document.querySelector('{host_css}');
            if (host && host.shadowRoot) {{
                let el = host.shadowRoot.querySelector('{target_css}');
                if (el) {{
                    el.click();
                    return true;
                }}
            }}
            return false;
            """)
            
            if result:
                return True
            
            if attempt < timeout - 1:
                time.sleep(1)
        
        raise Exception(f"Elemento não encontrado após {timeout}s: {target_css} dentro de {host_css}")


# Função wrapper para compatibilidade com código existente
def click_css(oHelper, host_css, target_css, timeout=10):
    """
    Função wrapper para clicar em elementos dentro de Shadow DOM.
    Extrai o driver do Webapp e usa a classe ClickCSS.
    """
    driver = oHelper._Webapp__webapp.driver
    clicker = ClickCSS(driver)
    return clicker.click(host_css, target_css, timeout)