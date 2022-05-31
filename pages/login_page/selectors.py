from selenium.webdriver.common.by import By

LOGIN_LOCATORS = {
    'login_form': {
        'email': {
            'by': By.ID,
            'value': 'login',
            'error_msg': {
                'by': By.CSS_SELECTOR,
                'value': 'label[for="login"] + div.form-hint'
            }
        },
        'password':{
            'by': By.ID,
            'value': 'password',
            'error_msg': {
                'by': By.CSS_SELECTOR,
                'value': 'label[for="password"] + div.form-hint'
            }
        },
        'submit_btn':{
            'by': By.XPATH,
            'value': '//button[@type="submit" and contains(text(), "Zaloguj się")]'
        }
    },

    'validation_error_msgs': {
        'by': By.CSS_SELECTOR,
        'value': 'form  div.form-hint'
    },
    'login_error_msg': {
        'by': By.CLASS_NAME,
        'value': 'infobox-message'
    },
}
