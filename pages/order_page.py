from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
import data

class OrderPage(BasePage):
    # Localizadores
    ADDRESS_FROM = (By.ID, "address-from")
    ADDRESS_TO = (By.ID, "address-to")
    BUTTON_SUBMIT = (By.ID, "submit")

    # Ações
    def set_route(self):
        """Preenche os campos de endereço e envia a rota."""
        self.type(*self.ADDRESS_FROM, data.ADDRESS_FROM)
        self.type(*self.ADDRESS_TO, data.ADDRESS_TO)
        self.click(*self.BUTTON_SUBMIT)

        # Validação: espera o campo de telefone aparecer após envio
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "phone"))
            )
        except TimeoutException:
            raise Exception("A tela de autenticação por telefone não foi carregada após envio da rota.")