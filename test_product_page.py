import pytest
import time
from .pages.product_page import ProductPage


url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
promo_codes = ['?promo=offer'+str(code) for code in range(0,10)]
promo_links = [url+promo for promo in promo_codes]
promo_links[7] = pytest.param(promo_links[7], marks=pytest.mark.xfail)

@pytest.mark.parametrize('promo_link', promo_links)
def test_guest_can_add_product_to_basket(browser, promo_link):
    page = ProductPage(browser, promo_link)
    page.open()
    product_name = page.get_product_name()
    price = page.get_price()
    page.add_to_basket()

    page.should_be_product_name(product_name=product_name)  # проверка соответствия имени товара в корзине
    page.should_be_price(price=price)   # проверка соответствия цены товара в корзине
