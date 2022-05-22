from .base_page import BasePage
from config import REGISTRATION_URL
from .locators import REGISTRATION_LOCATORS


class RegistrationPage(BasePage):
    _locators = REGISTRATION_LOCATORS
    _url = REGISTRATION_URL
    _form = REGISTRATION_LOCATORS['registration_form']

    def __init__(self, driver):
        super().__init__(driver)
        self.go_to(self._url)

    def _with(self, data=False):
        """
        Fills in form with given data. By default, empty form will be submitted.

        :param data: (dict) This argument, if given, should be a dictionary mapping field names to test value.
        """
        if data:
            fields = data.keys()
            for field in fields:
                locator = self._form[field]
                if locator['type'] == 'input_text':
                    self.fill(locator, data[field])
                elif locator['type'] == 'checkbox':
                    self.click_checkbox(locator, data[field])
        self.submit_btn()

    def submit_btn(self):
        # Submit registration form
        self.click_btn(self._locators['submit_btn'])

    def display_error_message(self, field):
        """
        Return error message related to form filed if present.
        :param field: (str) input field name
        :return:
            error_message (str)
        """
        return self.get_message(self._form[field]['error_msg'])

    def count_error_messages(self):
        # Return numbers of error messages
        errors = self.find_elements(self._locators['error_msgs'])
        return len(errors)

