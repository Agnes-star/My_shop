from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from base_page.base_pages import BasePage


class TestNavigationToProduct(BasePage):
    __url = "http://www.automationpractice.pl/index.php"
    __search_input = (By.XPATH, "//input[@id='search_query_top']")
    __search_button = (By.XPATH, "(//button[@name='submit_search'])[1]")
    __displayed_dress = (By.XPATH, "(//img[@title='Printed Dress'])[1]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def _open(self):
        super().open_url(self.__url)

    def navigate_to_product(self, product_name: str):
        super()._click(self.__search_input)
        super()._type(self.__search_input, product_name)
        super()._click(self.__search_button)

    @property
    def is_dress_displayed(self) -> bool:
        return super()._is_displayed(self.__displayed_dress)
