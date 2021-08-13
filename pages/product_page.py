from .base_page import BasePage
from .locators import  ProductPageLocators


class ProductPage(BasePage):
    def get_product_name(self):
        """ Получает имя товара, добавляемого в корзину """
        product_name = self.browser.find_element(*ProductPageLocators.PRUDUCT_NAME).text
        return product_name

    def get_price(self):
        """ Получает цену товара, добавляемого в корзину """
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        return price

    def add_to_basket(self):
        """ Добавляет товар в корзину """
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()


    def should_be_product_name(self,product_name):
        """ Проверяет соответствие названия товара в корзине """
        assert product_name == self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text,\
        'Product name is not correct!'

    def should_be_price(self, price):
        """ Проверяет соответствие цены товара в корзине """
        assert price == self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text,\
        'Product price is not correct!'