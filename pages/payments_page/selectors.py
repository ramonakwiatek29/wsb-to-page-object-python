from selenium.webdriver.common.by import By

PAYMENTS_LOCATORS = {
    'make_order': {
        'by': By.CSS_SELECTOR,
        'value': 'button.confirm-button:nth-child(2)'
    },
    'order_without_login_by_email': {
        'by': By.CSS_SELECTOR,
        'value': '#b-email'
    },
    'order_without_login_by_phone': {
        'by': By.CSS_SELECTOR,
        'value': '#b-phone'
    },
    'order_without_login_by_name': {
        'by': By.CSS_SELECTOR,
        'value': '#b-name'
    },
    'order_without_login_by_surname': {
        'by': By.CSS_SELECTOR,
        'value': '#b-subname'
    },
    'order_without_login_by_street': {
        'by': By.CSS_SELECTOR,
        'value': '#b-street'
    },
    'order_without_login_by_number_of_house': {
        'by': By.CSS_SELECTOR,
        'value': '#b-house'
    },
    'order_without_login_by_city': {
        'by': By.CSS_SELECTOR,
        'value': '#b-city'
    },
    'order_without_login_by_codepost': {
        'by': By.CSS_SELECTOR,
        'value': '#b-codepost'
    },
    'order_without_login_checkbox_required': {
        'by': By.XPATH,
        'value': '//*[@id="content"]/section/form[1]/div/div[1]/fieldset[4]/div[2]/label'
    },
    'order_without_login_order_and_pay': {
        'by': By.CSS_SELECTOR,
        'value': 'button.confirm-button:nth-child(2)'
    },
    'make_order_by_firm': {
        'by': By.CSS_SELECTOR,
        'value': 'button.confirm-button:nth-child(2)'
    },
    'order_without_login_by_firm_by_email': {
        'by': By.CSS_SELECTOR,
        'value': '#b-email'
    },
    'order_without_login_by_firm_by_phone': {
        'by': By.CSS_SELECTOR,
        'value': '#b-phone'
    },
    'order_without_login_by_firm_choice': {
        'by': By.CSS_SELECTOR,
        'value': 'div.check-simple:nth-child(3) > label:nth-child(2)'
    },
    'order_without_login_by_firm_checkbox_invoice': {
        'by': By.CSS_SELECTOR,
        'value': '.checkbox-inline > label:nth-child(2)'
    },
    'order_without_login_by_firm_firm_name': {
        'by': By.CSS_SELECTOR,
        'value': '#b-company'
    },
    'order_without_login_by_firm_nip': {
        'by': By.CSS_SELECTOR,
        'value': '#b-nip'
    },
    'order_without_login_by_firm_name': {
        'by': By.CSS_SELECTOR,
        'value': '#b-name'
    },
    'order_without_login_by_firm_surname': {
        'by': By.CSS_SELECTOR,
        'value': '#b-subname'
    },
    'order_without_login_by_firm_street': {
        'by': By.CSS_SELECTOR,
        'value': '#b-street'
    },
    'order_without_login_by_firm_number_of_house': {
        'by': By.CSS_SELECTOR,
        'value': '#b-house'
    },
    'order_without_login_by_firm_city': {
        'by': By.CSS_SELECTOR,
        'value': '#b-city'
    },
    'order_without_login_by_firm_codepost': {
        'by': By.CSS_SELECTOR,
        'value': '#b-codepost'
    },
    'order_without_login_by_firm_checkbox_required': {
        'by': By.XPATH,
        'value': '//*[@id="content"]/section/form[1]/div/div[1]/fieldset[4]/div[2]/label'
    },
    'order_without_login_by_firm_order_and_pay': {
        'by': By.CSS_SELECTOR,
        'value': 'button.confirm-button:nth-child(2)'
    },
    'make_order_login': {
        'by': By.CSS_SELECTOR,
        'value': 'button.confirm-button:nth-child(2)'
    },
    'make_order_my_account': {
        'by': By.CSS_SELECTOR,
        'value': '.checkout-tab > ul:nth-child(1) > li:nth-child(2)'
    },
    'order_login_email': {
        'by': By.ID,
        'value': 'login-login'
    },
    'order_login_password': {
        'by': By.ID,
        'value': 'login-password'
    },
    'login_btn': {
        'by': By.CSS_SELECTOR,
        'value': 'button.confirm-button:nth-child(4)'
    },
    'finalize_order': {
        'by': By.CSS_SELECTOR,
        'value': 'button.confirm-button:nth-child(2)'
    },
    'order_login_phone': {
        'by': By.CSS_SELECTOR,
        'value': '#b-phone'
    },
    'order_login_name': {
        'by': By.CSS_SELECTOR,
        'value': '#b-name'
    },
    'order_login_surname': {
        'by': By.CSS_SELECTOR,
        'value': '#b-subname'
    },
    'order_login_street': {
        'by': By.CSS_SELECTOR,
        'value': '#b-street'
    },
    'order_login_number_of_house': {
        'by': By.CSS_SELECTOR,
        'value': '#b-house'
    },
    'order_login_city': {
        'by': By.CSS_SELECTOR,
        'value': '#b-city'
    },
    'order_login_codepost': {
        'by': By.CSS_SELECTOR,
        'value': '#b-codepost'
    },
    'order_login_checkbox_required': {
        'by': By.XPATH,
        'value': '/html/body/div[2]/div[2]/section/div[2]/section/form/div/div[1]/fieldset[3]/div/label'
    },
    'order_login_order_and_pay': {
        'by': By.CSS_SELECTOR,
        'value': 'button.confirm-button:nth-child(2)'
    },
    'successful_buy': {
        'by': By.CSS_SELECTOR,
        'value': '#content > section > div.user-custom-content.headtxt'
    },

}
