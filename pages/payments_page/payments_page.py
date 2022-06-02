from pages.base_page import BasePage
from config import CART_PAGE_URL
from pages.payments_page.selectors import PAYMENTS_LOCATORS
from selenium.webdriver.common.by import By

class PaymentsPage(BasePage):
    _locators = PAYMENTS_LOCATORS
    _url = CART_PAGE_URL

    def buy_without_login(self):
        self.click_btn(self._locators['make_order'])
        self.fill(self._locators['order_without_login_by_email'],'jk@wp.pl')
        self.fill(self._locators['order_without_login_by_phone'],'123456789')
        self.fill(self._locators['order_without_login_by_name'],'Jan')
        self.fill(self._locators['order_without_login_by_surname'],'Kowalski')
        self.fill(self._locators['order_without_login_by_street'],'Szeroka')
        self.fill(self._locators['order_without_login_by_number_of_house'],'44')
        self.fill(self._locators['order_without_login_by_city'],'Warszawa')
        self.fill(self._locators['order_without_login_by_codepost'],'11-001')
        self.click_btn(self._locators['order_without_login_checkbox_required'])
        self.click_btn(self._locators['order_without_login_order_and_pay'])

    def buy_with_login(self):
        self.click_btn(self._locators['make_order_login'])
        self.click_btn(self._locators['make_order_my_account'])
        #self.fill(self._locators['order_login_email'],'realkaka17@wp.pl')
        self.fill(self._locators['order_login_password'],'haslo123')
        self.click_btn(self._locators['make_order_again'])
        self.fill(self._locators['order_login_phone'],'333-333-333')
        self.fill(self._locators['order_login_name'],'Anna')
        self.fill(self._locators['order_login_surname'],'Nowak')
        self.fill(self._locators['order_login_street'],'Cicha')
        self.fill(self._locators['order_login_number_of_house'],'13')
        self.fill(self._locators['order_login_city'],'Lublin')
        self.fill(self._locators['order_login_codepost'],'33-033')
        self.click_checkbox(self._locators['order_login_checkbox_required'])
        self.click_btn(self._locators['order_login_order_and_pay'])

    def buy_without_login_firm(self):
        self.click_btn(self._locators['make_order_by_firm'])
        self.fill(self._locators['order_without_login_by_firm_by_email'],'firma@wp.pl')
        self.fill(self._locators['order_without_login_by_firm_by_phone'],'666.666.666')
        self.click_checkbox(self._locators['order_without_login_by_firm_checkbox_invoice'])
        self.click_btn(self._locators['order_without_login_by_firm_choice'])
        self.fill(self._locators['order_without_login_by_firm_firm_name'],'BigFirm')
        self.fill(self._locators['order_without_login_by_firm_nip'],'5840203593')
        self.fill(self._locators['order_without_login_by_firm_name'],'Adam')
        self.fill(self._locators['order_without_login_by_firm_surname'],'Nowak')
        self.fill(self._locators['order_without_login_by_firm_street'],'Sucha')
        self.fill(self._locators['order_without_login_by_firm_number_of_house'],'55')
        self.fill(self._locators['order_without_login_by_firm_city'],'Warszawa')
        self.fill(self._locators['order_without_login_by_firm_codepost'],'12-123')
        self.click_btn(self._locators['order_without_login_by_firm_checkbox_required'])
        self.click_btn(self._locators['order_without_login_by_firm_order_and_pay'])

    def successful_buy(self):
        element = self.find_element(self._locators['successful_buy'])
        message = element.text
        return message

