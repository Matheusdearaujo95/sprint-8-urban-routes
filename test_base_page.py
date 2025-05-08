from selenium import webdriver
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


def test_base_page_methods():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

    base = BasePage(driver)

    # Testa se consegue encontrar o campo de busca do Google
    search_box = base.find(By.NAME, "q")
    assert search_box is not None

    # Testa se o elemento está visível
    assert base.is_visible(By.NAME, "q")

    # Testa o envio de texto
    base.type(By.NAME, "q", "TripleTen")

    # Fecha o navegador
    driver.quit()