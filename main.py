import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.order_page import OrderPage
from pages.pages import UrbanRoutesPage
import data
import helpers
import time


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if data.URBAN_ROUTES_URL:
            if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
                print("✅ Conectado ao servidor Urban Routes")
            else:
                print("❌ Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado.")
        else:
            print("⚠️ URBAN_ROUTES_URL está vazio. Atualize com o link do servidor assim que disponível.")

        options = Options()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        cls.driver = webdriver.Chrome(options=options)

        if data.URBAN_ROUTES_URL:
            cls.driver.get(data.URBAN_ROUTES_URL)
        else:
            # Caso esteja testando localmente
            cls.driver.get("file:///Users/matheus/PycharmProjects/QA-Brazil_Python_Automation/urban_routes_mock.html")

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_set_route(self):
        """Preenche os campos de endereço e envia a rota."""
        page = OrderPage(self.driver)
        page.set_route()

    def test_fill_phone_number(self):
        """Preenche o número de telefone e o código SMS."""
        page = UrbanRoutesPage(self.driver)
        page.fill_phone_number()

    def test_fill_card(self):
        """Preenche os dados do cartão e clica em Link."""
        page = UrbanRoutesPage(self.driver)
        page.fill_card()

    def test_comment_for_driver(self):
        """Adiciona um comentário para o motorista."""
        comment_box = self.driver.find_element("id", "comment")
        comment_box.clear()
        comment_box.send_keys(data.MESSAGE_FOR_DRIVER)
        time.sleep(1)

    def test_order_blanket_and_handkerchiefs(self):
        """Solicita cobertor e lenços."""
        blanket_checkbox = self.driver.find_element("id", "order-blanket")
        handkerchief_checkbox = self.driver.find_element("id", "order-handkerchiefs")

        if not blanket_checkbox.is_selected():
            blanket_checkbox.click()

        if not handkerchief_checkbox.is_selected():
            handkerchief_checkbox.click()

        time.sleep(1)

    def test_order_2_ice_creams(self):
        """Solicita dois sorvetes."""
        ice_cream_button = self.driver.find_element("id", "order-ice-cream")

        for _ in range(2):
            ice_cream_button.click()
            time.sleep(0.5)

    def test_car_search_model_appears(self):
        """Verifica se o modelo do carro aparece após iniciar busca."""
        search_button = self.driver.find_element("id", "search")
        search_button.click()
        time.sleep(3)

        car_model = self.driver.find_element("class name", "car__model")
        assert car_model.is_displayed()