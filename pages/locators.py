from selenium.webdriver.common.by import By


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
        'value': '.return-button'
    },
    'plus_btn': {
        'by': By.CSS_SELECTOR,
        'value': '.plus'
    },
    'add_few_product_btn': {
        'by': By.CSS_SELECTOR,
        'value': "#addproductamount"
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
    'item_in_cart': {
        'by': By.CSS_SELECTOR,
        'value': '.productcart-info > a:nth-child(1)'
    },
    'price_of_one_item': {
        'by': By.CSS_SELECTOR,
        'value': '.price > strong:nth-child(2)'
    },
    'value': {
        'by': By.CSS_SELECTOR,
        'value': '.value-items > strong:nth-child(1)'
    },
    'cart_value': {
        'by': By.XPATH,
        'value': "//input[@type='tel']"
    },
    'cart': {
        'by': By.CSS_SELECTOR,
        'value': '#cart-box > span:nth-child(1)'
    },
    'count': {
        'by': By.CSS_SELECTOR,
        'value': '.recalculate-all'
    },
    'back_to_shopping': {
        'by': By.CSS_SELECTOR,
        'value': '.cart-back-link'
    },
    'back_url': {
        'by': By.CSS_SELECTOR,
        'value': '.main-greeting-headline'
    },
    'minus': {
        'by': By.CSS_SELECTOR,
        'value': '.minus'
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
        'value': '.sorter-listing > span:nth-child(1) > label:nth-child(2)'},
}

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
