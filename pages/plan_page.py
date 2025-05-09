from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PlanPage(BasePage):
    COMFORT_PLAN = (By.CLASS_NAME, "tariff__name")

    def select_comfort_plan(self):
        """Seleciona o plano Comfort se ainda não estiver ativo."""
        tariffs = self.driver.find_elements(*self.COMFORT_PLAN)

        if not tariffs:
            raise Exception("Nenhum plano encontrado na página.")

        for plan in tariffs:
            if "Comfort" in plan.text:
                parent = plan.find_element(By.XPATH, "..")
                if "tariff__active" not in parent.get_attribute("class"):
                    plan.click()
                break