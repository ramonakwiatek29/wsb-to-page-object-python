from .base_page import BasePage
from config import CART_PAGE_URL
from .locators import CART_LOCATORS


class ItemPage(BasePage):
    _locators = CART_LOCATORS
    _url = CART_PAGE_URL

    def check_that_cart_is_empty(self):
        self.get_message(['empty_cart_msg'])

    def check_that_item_is_in_cart(self):
        self.get_message(['item_in_cart'])

    def plus_one_item(self):
        self.click_btn(['plus_btn_2'])

    def remove_item(self):
        self.click_btn(['remove_btn'])

    def clear_cart(self):
        self.click_btn(['clear_cart_btn'])

    def check_how_many_items_is_in_cart(self):
        item_price = self.get_message(['price_of_one_item'])
        cart_value = self.get_message(['cart_value'])
        print(cart_value / item_price)

