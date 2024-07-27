import pytest
from base_page.navigate_to_product import TestNavigationToProduct


class TestNavigateToProduct:

    @pytest.mark.actual
    def test_navigate_to_product(self, driver):
        navigation_to_product = TestNavigationToProduct(driver)
        navigation_to_product._open()
        navigation_to_product.navigate_to_product("printed dress")


