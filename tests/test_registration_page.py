import pytest
from .base_test import TestBase
from .messages import REGISTRATION_MESSAGES
from pages.registration_page import RegistrationPage


class TestRegistrationPage(TestBase):
    _error_msgs = REGISTRATION_MESSAGES['error_msgs']
    _success_msgs = REGISTRATION_MESSAGES['success_msgs']

    @pytest.fixture(autouse=True)
    def setup(self):
        self.register = RegistrationPage(self.driver)
        yield
        self.driver.delete_all_cookies()

    def test_register_with_empty_form(self):
        self.register._with(data={})
        assert self._error_msgs['email'] == self.register.display_error_message('email')
        assert self._error_msgs['password'] == self.register.display_error_message('password')
        assert self._error_msgs['terms_and_conditions'] == self.register.display_error_message('terms_and_conditions')
        assert self.register.count_error_messages() == 3

    def test_register_with_invalid_email(self):
        self.register._with(data={
            'email': 'invalid_email',
            'password': '123qwe',
            'rpassword': '123qwe',
            'newsletter': True,
            'terms_and_conditions': True,
        })
        assert self._error_msgs['email'] == self.register.display_error_message('email')
        assert self.register.count_error_messages() == 1

    def test_register_with_terms_and_conditions_not_selected(self):
        self.register._with(data={
            'email': 'iko.asdas@vp.ppl',
            'password': '123qwe',
            'rpassword': '123qwe',
            'newsletter': True,
            'terms_and_conditions': False,
        })
        assert self._error_msgs['terms_and_conditions'] == self.register.display_error_message('terms_and_conditions')
        assert self.register.count_error_messages() == 1

    def test_register_without_password(self):
        self.register._with(data={
            'email': 'validmail@gggg.pl',
            'password': '',
            'rpassword': '1223qwe',
            'newsletter': True,
            'terms_and_conditions': True,
        })
        assert self._error_msgs['password'] == self.register.display_error_message('password')
        assert self._error_msgs['rpassword'] == self.register.display_error_message('rpassword')
        assert self.register.count_error_messages() == 2

    def test_register_with_password_less_then_minimum_length(self):
        self.register._with(data={
            'email': 'validmail@gggg.pl',
            'password': 'dom',
            'rpassword': 'dom',
            'newsletter': True,
            'terms_and_conditions': True,
        })
        assert self._error_msgs['password'] == self.register.display_error_message('password')
        assert self.register.count_error_messages() == 1

    def test_register_with_different_confirmation_password(self):
        self.register._with(data={
            'email': 'validmail@gggg.pl',
            'password': '123qwe',
            'rpassword': 'qweqwe',
            'newsletter': True,
            'terms_and_conditions': True,
        })
        assert self.register.count_error_messages() == 1
        assert self._error_msgs['rpassword'] == self.register.display_error_message('rpassword')