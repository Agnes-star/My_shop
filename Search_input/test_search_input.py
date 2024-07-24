import pytest
from selenium.webdriver.common.by import By
from Home_page import conftest


class Test_search_input:

    @pytest.mark.search
    def test_search_input_with_valid_product_name(self, driver):
        driver.get("http://www.automationpractice.pl/index.php")
        search_input = driver.find_element(By.XPATH, "//input[@id='search_query_top']")
        search_input.click()
        search_input.send_keys("printed dress")
        driver.find_element(By.XPATH, "(//button[@name='submit_search'])[1]").click()
        assert driver.find_element(By.XPATH, "(//a[@title='Printed Summer Dress'][normalize-space()='Printed Summer "
                                             "Dress'])[1]").text == "Printed Summer Dress"

    @pytest.mark.search
    def test_search_input_with_invalid_product_name(self, driver):
        driver.get("http://www.automationpractice.pl/index.php")
        search_input = driver.find_element(By.XPATH, "//input[@id='search_query_top']")
        search_input.click()
        search_input.send_keys("abcde")
        driver.find_element(By.XPATH, "(//button[@name='submit_search'])[1]").click()
        assert driver.find_element(By.CSS_SELECTOR, ".alert.alert-warning").text == ("No results "
                                                                                     "were found"
                                                                                     " for your "
                                                                                     "search "
                                                                                     "\"abcde\"")

