from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#logi0n_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#registuer_form')

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRUDUCT_NAME = (By.CSS_SELECTOR, 'div.product_main > h1')
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, 'div.alertinner > strong')
    PRICE = (By.CSS_SELECTOR, 'div.product_main > p.price_color')
    ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.alertinner > p > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div.alert-success')