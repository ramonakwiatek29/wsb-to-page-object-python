from .base_page import BasePage
from config import BOOKS_URL
from .locators import BOOKS_LOCATORS
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BooksPage(BasePage):
    _locators = BOOKS_LOCATORS
    _url = BOOKS_URL

    def __init__(self, driver):
        super().__init__(driver)
        self.go_to(self._url)

    def all_books_count(self):
        return len(self.find_elements(self._locators['book_price']))

    def filter_by_max_price(self):
        self.clear(self._locators['max_price'])
        self.fill(self._locators['max_price'], '100')
        element = self.find_element(self._locators['filter_enabled'])


    def filter_by_min_price(self):
        self.clear(self._locators['min_price'])
        self.fill(self._locators['min_price'], 500)
        element = self.find_element(self._locators['filter_enabled'])

    def sort_by_price_asc(self):
        self.click_btn(self._locators['sorter_button'])
        self.click_btn(self._locators['price_asc'])

    def sort_by_price_desc(self):
        self.click_btn(self._locators['sorter_button'])
        self.click_btn(self._locators['price_desc'])

    def sort_by_name_desc(self):
        self.click_btn(self._locators['sorter_button'])
        self.click_btn(self._locators['name_desc'])

    def sort_by_name_asc(self):
        self.click_btn(self._locators['sorter_button'])
        self.click_btn(self._locators['name_asc'])

    def books_price(self):
        prices = self.find_elements(self._locators['book_price'])
        list =[]
        for price in prices:
            discounted = price.find_element(By.TAG_NAME, "b")
            list.append(discounted.text)
        new_list = []
        for i in list:
            x = i.replace(",", ".")
            new_list.append(float(x))
        return new_list

    def books_title(self):
        titles = self.find_elements(self._locators['book_title'])
        list = []
        for title in titles:
            list.append(title.text)
        return list



