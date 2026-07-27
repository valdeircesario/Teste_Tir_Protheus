from selenium.webdriver.common.by import By as SelBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def clicar_busca_avancada(oHelper_Poui, oHelper=None, timeout=10):
    """
    Função utilitária para forçar o clique na 'Busca avançada' de telas PO UI.
    Captura a instância correta do driver e dispara o clique via JS para
    evitar problemas de tempo e sobreposição do Angular.
    
    :param oHelper_Poui: Instância da classe Poui do TIR.
    :param oHelper: Instância da classe Webapp do TIR (opcional, como fallback).
    :param timeout: Tempo máximo de espera pelo elemento em segundos (Padrão: 10).
    """
    # Captura a instância exata do driver do Selenium em execução
    if hasattr(oHelper_Poui, '_Poui__poui') and hasattr(oHelper_Poui._Poui__poui, 'driver'):
        driver = oHelper_Poui._Poui__poui.driver
    elif oHelper and hasattr(oHelper, '_Webapp__webapp') and hasattr(oHelper._Webapp__webapp, 'driver'):
        driver = oHelper._Webapp__webapp.driver
    else:
        raise AttributeError("Não foi possível capturar a instância do driver do Selenium.")

    # Aguarda o elemento da Busca Avançada estar presente no DOM
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((SelBy.CSS_SELECTOR, ".po-page-list-filter-search-link"))
    )
    
    # Dispara o clique nativo via JavaScript
    driver.execute_script("arguments[0].click();", element)
    print("✅ 'Busca avançada' clicada com sucesso!")