from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def select_grid_combobox_option(
    oHelper,
    texto_opcao,
    grid_id="COMP6127"
):
    """
    Abre o ComboBox da célula selecionada e escolhe uma opção.

    Exemplo:
        select_grid_combobox_option(
            self.oHelper,
            "DFTRANS - TCB"
        )
    """

    driver = oHelper._Webapp__webapp.driver

    # Abre o editor da célula
    driver.find_element(By.ID, grid_id).send_keys(Keys.F3)

    time.sleep(1)

    return driver.execute_script(f"""
    const combo =
        [...document.querySelectorAll('wa-combobox')]
        .find(c => getComputedStyle(c).visibility === 'visible');

    if (!combo) return false;

    const select = combo.shadowRoot.querySelector('select');

    const option = [...select.options]
        .find(o => o.text.includes('{texto_opcao}'));

    if (!option) return false;

    select.value = option.value;

    select.dispatchEvent(
        new Event('change', {{ bubbles: true }})
    );

    return true;
    """)


def get_grid_cell_value(
    oHelper,
    grid_id="COMP6127",
    row=0,
    col=0
):
    """
    Retorna o valor atual da célula da grid.

    Exemplo:
        valor = get_grid_cell_value(
            self.oHelper,
            "COMP6127",
            0,
            0
        )
    """

    driver = oHelper._Webapp__webapp.driver

    return driver.execute_script(f"""
    const grid = document.querySelector("#{grid_id}");

    if (!grid) return null;

    const cells = [
        ...grid.shadowRoot.querySelectorAll(
            "tbody tr:nth-child({row + 1}) td"
        )
    ];

    if (!cells[{col}]) return null;

    return cells[{col}].textContent.trim();
    """)
    
def grid_cell_has_value(
    oHelper,
    grid_id="COMP6127",
    row=0,
    col=0
):
    """
    Retorna True se a célula possuir valor.
    Retorna False se estiver vazia.
    """

    valor = get_grid_cell_value(
        oHelper,
        grid_id,
        row,
        col
    )

    if valor is None:
        return False

    valor = str(valor).strip()

    return valor != ""