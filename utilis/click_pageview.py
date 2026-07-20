from selenium.webdriver.common.by import By

def click_pageview_button(oHelper, titulo):

    driver = oHelper._Webapp__webapp.driver

    driver.execute_script(f"""
    document
    .querySelector("[data-advpl='tpageview']")
    .shadowRoot
    .querySelector("button[title='{titulo}']")
    .click();
    """)
    
    #exemplos de usos do clique
    
#click_pageview_button(self.oHelper,"Ampliar (+)")
#click_pageview_button(self.oHelper, "Reduzir (-)")
        
#click_pageview_button(self.oHelper,"Próxima página")
#click_pageview_button(self.oHelper,"Página anterior")

# utils/click_pageview_visible.py

def click_pageview_visible_button(oHelper, titulo):
    """
    Clica nos botões do PageView visível.

    Exemplo:
        click_pageview_visible_button(self.oHelper, "Ampliar (+)")
        click_pageview_visible_button(self.oHelper, "Reduzir (-)")
        click_pageview_visible_button(self.oHelper, "Próxima página")
        click_pageview_visible_button(self.oHelper, "Página anterior")
    """

    driver = oHelper._Webapp__webapp.driver

    driver.execute_script(f"""
    const preview =
        [...document.querySelectorAll('wa-print-preview')]
        .find(e => getComputedStyle(e).visibility === 'visible');

    if (preview) {{
        preview.shadowRoot
               .querySelector("button[title='{titulo}']")
               .click();
    }}
    """)
