from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import data
import helpers

class UrbanRoutesPage(BasePage):
    """Classe base para as páginas do Urban Routes."""

    # Localizadores
    COMFORT_PLAN = (By.CLASS_NAME, "tariff__name")
    PHONE_INPUT = (By.ID, "phone")
    SMS_CODE_INPUT = (By.ID, "code")

    def select_comfort_plan(self):
        """Seleciona o plano Comfort se ainda não estiver ativo."""
        tariffs = self.driver.find_elements(*self.COMFORT_PLAN)

        if not tariffs:
            raise Exception("Nenhum plano encontrado")

        for plan in tariffs:
            if "Comfort" in plan.text:
                # Tenta verificar se o plano já está ativo sem usar XPath
                parent_classes = plan.get_attribute("class")
                if "tariff__active" not in parent_classes:
                    plan.click()
                break

    def fill_phone_number(self):
        """Preenche o número de telefone e o código SMS."""
        self.type(*self.PHONE_INPUT, data.PHONE_NUMBER)
        self.click(*self.PHONE_INPUT)  # Dá foco para acionar envio do SMS

        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver: "api/v1/number?number" in str(driver.get_log("performance")))

        code = helpers.retrieve_phone_code(self.driver)
        self.type(*self.SMS_CODE_INPUT, code)

    def fill_card(self):
        """Preenche os dados do cartão de crédito e ativa o botão Link."""
        wait = WebDriverWait(self.driver, 10)

        add_card_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "payment__card-add"))
        )
        add_card_button.click()

        card_number_input = wait.until(
            EC.visibility_of_element_located((By.ID, "number"))
        )
        card_code_input = wait.until(
            EC.visibility_of_element_located((By.ID, "code"))
        )

        card_number_input.send_keys(data.CARD_NUMBER)
        card_code_input.send_keys(data.CARD_CODE)

        self.driver.find_element(By.CLASS_NAME, "modal__overlay").click()

        link_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "button--link"))
        )
        link_button.click()