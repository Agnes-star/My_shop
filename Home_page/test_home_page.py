import pytest
from selenium.webdriver.common.by import By


class Test_home_page:

    @pytest.mark.home_page
    def test_home_page_title(self, driver):
        driver.get("http://www.automationpractice.pl/index.php")
        title = driver.title
        assert title == "My Shop"

    @pytest.mark.home_page
    def test_verify_contactus_page_link(self, driver):
        driver.get("http://www.automationpractice.pl/index.php")
        driver.find_element(By.XPATH, "//a[normalize-space()='Contact us']").click()
        assert driver.find_element(By.XPATH,
                                   "(//h1[normalize-space()='Customer service - Contact us'])[1]").text == ("CUSTOMER "
                                                                                                            "SERVICE "
                                                                                                            "- "
                                                                                                            "CONTACT "
                                                                                                            "US")

    @pytest.mark.home_page
    def test_verify_signin_page_link(self, driver):
        driver.get("http://www.automationpractice.pl/index.php")
        driver.find_element(By.XPATH, "(//a[normalize-space()='Sign in'])[1]").click()
        assert driver.find_element(By.XPATH,
                                   "(//h3[normalize-space()='Create an account'])[1]").text == "CREATE AN ACCOUNT"

    @pytest.mark.home_page
    def test_verify_cart_page_link(self, driver):
        driver.get("http://www.automationpractice.pl/index.php")
        driver.find_element(By.XPATH, "//b[normalize-space()='Cart']").click()
        assert driver.find_element(By.XPATH,
                                   "(//h1[normalize-space()='Shopping-cart summary'])[1]").text == ("SHOPPING-CART "
                                                                                                    "SUMMARY")
