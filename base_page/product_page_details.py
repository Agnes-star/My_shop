from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from base_page.base_pages import BasePage


class DisplayedSuccessfullyPage(BasePage):
    __url = ("http://www.automationpractice.pl/index.php?controller=search&orderby=position&orderway=desc&search_query"
             "=printed+dress&submit_search=")
    __header_locator = (By.XPATH, "//h1[1]")
    __displayed_dress = (By.LINK_TEXT, "(//a[contains(@title,'Printed Dress')][normalize-space()='Printed "
                                       "Dress'])[2]")
    __add_to_cart_button = (By.XPATH, "(//div[@class='button-container'])[2]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self.__url

    @property
    def header(self) -> str:
        return super()._get_text(self.__header_locator)

    @property
    def is_dress_displayed(self) -> bool:
        return super()._is_displayed(self.__displayed_dress)

    @property
    def is_add_to_cart_button_displayed(self) -> bool:
        return super()._is_displayed(self.__add_to_cart_button)

