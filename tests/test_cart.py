import pytest
from tests.base_test import TestBase
from pages.cart_page import CartPage
from pages.item_page import ItemPage


class TestCartPage(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.cart = CartPage(self.driver)
        self.item = ItemPage(self.driver)
        yield
        self.driver.delete_all_cookies()

    def test_empty_cart(self):
        assert self.cart.check_that_cart_is_empty() == 'Twój koszyk jest pusty'

    def test_item_is_in_cart(self):
        self.item.add_item_to_cart()
        assert self.cart.check_how_many_items_is_in_cart() == '1'

    def test_remove_item(self):
        self.item.add_item_to_cart()
        self.cart.remove_item()
        assert self.cart.empty_cart() == 'Twój koszyk jest pusty'

    def test_minus_one_item(self):
            self.item.add_two_item_to_cart()
            self.cart.minus_one_item()
            element = self.cart.check_how_many_items_is_in_cart()
            assert element == '1'

    def test_clear_cart(self):
        self.item.add_item_to_cart()
        self.cart.clear_cart()
        assert self.cart.empty_cart() == 'Twój koszyk jest pusty'

    def test_add_same_item(self):
        self.item.add_again_the_same_item()
        assert self.cart.check_how_many_items_is_in_cart() == '2'

    def test_add_2_items_by_using_plus(self):
        self.item.add_two_item_to_cart()
        assert self.cart.check_how_many_items_is_in_cart() == '2'

    def test_using_plus_on_cart_site(self):
        self.item.add_item_to_cart()
        self.cart.plus_one_item()
        assert self.cart.check_how_many_items_is_in_cart() == '2'

    def test_add_100_items(self):
        self.item.add_100_same_items()
        assert self.cart.check_how_many_items_is_in_cart() == '100'

    def test_adding_more_than_is_available(self):
        self.item.adding_999_items()
        self.item.to_cart()
        available = self.cart.check_how_many_items_is_in_cart()
        self.cart.plus_one_item()
        over = self.cart.check_how_many_items_is_in_cart()
        assert over == available

    def test_recalculate(self):
        self.item.add_item_to_cart()
        self.cart.recalculate_cart()
        assert self.cart.check_how_many_items_is_in_cart() == '5'

    def test_back_to_shopping(self):
        self.item.add_item_to_cart()
        self.cart.back_to_shopping()
        assert self.cart.back_url() == 'WITAJ W SKLEPIE\nDemo GOSHOP'
