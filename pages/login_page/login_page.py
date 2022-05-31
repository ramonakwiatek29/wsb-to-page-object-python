from pages.base_page import BasePage
from config import LOGIN_URL
from pages.login_page.selectors import LOGIN_LOCATORS


class LoginPage(BasePage):
    _locators = LOGIN_LOCATORS
    _url = LOGIN_URL
    _form = LOGIN_LOCATORS['login_form']

    def __init__(self, driver):
        super().__init__(driver)
        self.go_to(self._url)

    def _with(self, data=None):
        if data is None:
            data = {}
        fields = data.keys()
        for field in fields:
            locator = self._form[field]
            self.fill(locator, data[field])
        self.submit_btn()

    def submit_btn(self):
        self.click_btn(self._form['submit_btn'])

    def get_error_message(self, field):
        return self.get_message(self._form[field]['error_msg'])

    def check_how_many_error_messages_are_displayed(self):
        errors = self.find_elements(self._locators['validation_error_msgs'])
        return len(errors)