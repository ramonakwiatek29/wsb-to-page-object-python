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
ITEM_LOCATORS = {
    'add_to_cart_btn': {
        'by': By.CSS_SELECTOR,
        'value': '.buy-button'
    },
    'go_to_cart_btn': {
        'by': By.CSS_SELECTOR,
        'value': 'a.confirm-button'
    },
    'return_btn': {
        'by': By.CSS_SELECTOR,
        'value': 'return_button'
    },
    'plus_btn': {
        'by': By.CSS_SELECTOR,
        'value': '.plus'
    },
    'add_few_product_btn': {
        'by': By.CSS_SELECTOR,
        'value': "#addproductamount"
    },
    'available_number': {
        'by': By.CSS_SELECTOR,
        'value': ".goshop-modal > section:nth-child(2) > ul:nth-child(4) > li:nth-child(1) > strong:nth-child(2)"
    },
}
CART_LOCATORS = {
    'clear_cart_btn': {
        'by': By.CSS_SELECTOR,
        'value': '.clear-cart'
    },
    'remove_btn': {
        'by': By.CSS_SELECTOR,
        'value': '.removepos'
    },
    'cart_btn': {
        'by': By.CSS_SELECTOR,
        'value': '#cart-box > span:nth-child(1)'
    },
    'empty_cart_msg': {
        'by': By.CSS_SELECTOR,
        'value': '.infobox-headline'
    },
    'plus_btn_2': {
        'by': By.CSS_SELECTOR,
        'value': '.plus'
    },
}
BOOKS_LOCATORS = {
    'book_price': {
        'by': By.CLASS_NAME,
        'value': 'product-price '
    },
    'max_price': {
        'by': By.CSS_SELECTOR,
        'value': '#filter-price2'
    },
    'min_price': {
        'by': By.CSS_SELECTOR,
        'value': '#filter-price1'
    },
    'filter_enabled': {
        'by': By.CSS_SELECTOR,
        'value': '.single-pill > span:nth-child(1) > b:nth-child(1)'
    },
    'sorter_button': {
        'by': By.CSS_SELECTOR,
        'value': '.sorter-button'
    },
    'price_desc': {
        'by': By.CSS_SELECTOR,
        'value': '.sorter-listing > span:nth-child(4) > label:nth-child(2)'
    },
    'price_asc': {
        'by': By.CSS_SELECTOR,
        'value': '.sorter-listing > span:nth-child(3) > label:nth-child(2)'
    },
    'book_title': {
        'by': By.CLASS_NAME,
        'value': 'product-name'
    },
    'name_desc': {
        'by': By.CSS_SELECTOR,
        'value': '.sorter-listing > span:nth-child(2) > label:nth-child(2)'
    },
    'name_asc': {
        'by': By.CSS_SELECTOR,
        'value': '.sorter-listing > span:nth-child(1) > label:nth-child(2)'
    }

}

