from selenium.webdriver.common.by import By

REGISTRATION_LOCATORS = {
    'registration_form': {
        'email': {
            'by': By.ID,
            'value': 'b-email',
            'type': 'input_text',
            'error_msg': {
                'by': By.CSS_SELECTOR,
                'value': 'label[for="b-email"] + div.form-hint'
            }
        },
        'password': {
            'by': By.ID,
            'value': 'b-password',
            'type': 'input_text',
            'error_msg': {
                'by': By.CSS_SELECTOR,
                'value': 'label[for="b-password"] + div.form-hint'
            }
        },
        'rpassword': {
            'by': By.ID,
            'value': 'b-rpassword',
            'type': 'input_text',
            'error_msg': {
                'by': By.CSS_SELECTOR,
                'value': 'label[for="b-rpassword"] + div.form-hint'
            }
        },
        'newsletter': {
            'by': By.ID,
            'value': 'check-nl-register',
            'type': 'checkbox',
            'error_msg': {
                'by': By.CSS_SELECTOR,
                'value': 'label[for="b-check-nl-register"] + div.form-hint'
            }

        },
        'terms_and_conditions': {
            'by': By.ID,
            'value': 'check-regshop',
            'type': 'checkbox',
            'error_msg': {
                'by': By.CSS_SELECTOR,
                'value': 'label[for="check-regshop"] + div.form-hint'
            }
        }
    },
    'submit_btn': {
        'by': By.CSS_SELECTOR,
        'value': 'button[class="confirm-button active-button"]'
    },
    'error_msgs': {
        'by': By.CSS_SELECTOR,
        'value': 'form  div.form-hint'
    },
}