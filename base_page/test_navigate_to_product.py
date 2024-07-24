import pytest

from base_page.navigate_to_product import TestNavigationToProduct


class TestNavigateToProduct:

    @pytest.mark.actual
    def test_navigate_to_product(self, driver):
        navigation_to_product = TestNavigationToProduct(driver)
        navigation_to_product._open()
        navigation_to_product.navigate_to_product("printed dress")
        assert navigation_to_product.is_dress_displayed

    @pytest.mark.negative_test
    @pytest.mark.actual
    def test_navigate_to_product_with_invalid_product_name(self, driver):
        navigation_to_product = TestNavigationToProduct(driver)
        navigation_to_product._open()
        navigation_to_product.navigate_to_product("abcde")
        assert navigation_to_product.is_dress_displayed

