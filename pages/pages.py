from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import data
import helpers
import time

class UrbanRoutesPage(BasePage):
    """Classe base para as páginas do Urban Routes."""

    # Localizadores
    COMFORT_PLAN = (By.CLASS_NAME, "tariff__name")
    PHONE_INPUT = (By.ID, "phone-input")
    SMS_CODE_INPUT = (By.ID, "code-input")

    def select_comfort_plan(self):
        """Seleciona o plano Comfort se ainda não estiver ativo."""
        tariffs = self.driver.find_elements(*self.COMFORT_PLAN)

        for plan in tariffs:
            if "Comfort" in plan.text:
                parent = plan.find_element(By.XPATH, "..")
                if "tariff__active" not in parent.get_attribute("class"):
                    plan.click()
                break

    def fill_phone_number(self):
        """Preenche o número de telefone e o código SMS."""
        self.type(*self.PHONE_INPUT, data.PHONE_NUMBER)
        self.click(*self.PHONE_INPUT)  # Dá foco para acionar envio do SMS
        time.sleep(2)  # Aguarda para garantir que o código seja emitido

        # Código simulado, já que não temos rede no mock local
        code = "1234"
        self.type(*self.SMS_CODE_INPUT, code)

    def fill_card(self):
        """Preenche os dados do cartão de crédito e ativa o botão Link."""
        wait = WebDriverWait(self.driver, 10)

        # Espera e clica no botão de adicionar cartão
        add_card_button = wait.until(
            EC.element_to_be_clickable((By.ID, "add-card-button"))
        )
        add_card_button.click()

        # Preenche os campos do cartão
        card_number_input = wait.until(
            EC.visibility_of_element_located((By.ID, "card-number"))
        )
        card_code_input = wait.until(
            EC.visibility_of_element_located((By.ID, "card-cvv"))
        )

        card_number_input.send_keys(data.CARD_NUMBER)
        card_code_input.send_keys(data.CARD_CODE)

        # Simula perda de foco no campo CVV clicando fora
        self.driver.find_element(By.TAG_NAME, "body").click()

        # Espera o botão Link ficar clicável e clica
        link_button = wait.until(
            EC.element_to_be_clickable((By.ID, "link-card-button"))
        )
        link_button.click()