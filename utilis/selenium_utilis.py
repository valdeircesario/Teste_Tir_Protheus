from selenium.webdriver.common.by import By

def click_child_by_id(oHelper, element_id, child_tag="button"):
    """
    Clica em um elemento filho de um componente identificado por ID.

    Exemplo:
        click_child_by_id(oHelper, "COMP6006")
        click_child_by_id(oHelper, "COMP6006", "input")
        click_child_by_id(oHelper, "COMP6006", "span")
        
        driver = self.oHelper._Webapp__webapp.driver
        driver.find_element(By.XPATH,'//*[@id="COMP6006"]/button').click()
    """

    driver = oHelper._Webapp__webapp.driver

    driver.find_element(
        By.XPATH,
        f'//*[@id="{element_id}"]/{child_tag}'
    ).click()
    
  