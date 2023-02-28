import os

import pytest
from dotenv import load_dotenv
from selene.support.conditions import have
from selene.support.shared import browser

from utils.base_session import BaseSession


load_dotenv()


@pytest.fixture(scope='session')
def demoshop():
    api_url = os.getenv("API_URL")
    return BaseSession(api_url)


@pytest.fixture(scope='session')
def reqres():
    base_url = os.getenv('base_url')
    return BaseSession(base_url)


@pytest.fixture(autouse=True)
def window_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture()
def clean_cart():
    yield
    browser.open('https://demowebshop.tricentis.com/cart')
    for checkbox in browser.elements('[name="removefromcart"]'):
        checkbox.click()
    browser.element('[name="updatecart"]').click()
    browser.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))


@pytest.fixture()
def clean_wishlist():
    yield
    browser.open('https://demowebshop.tricentis.com/wishlist')
    for checkbox in browser.elements('[name="removefromcart"]'):
        checkbox.click()
    browser.element('[value="Update wishlist"]').click()
    browser.element('.wishlist-content').should(have.text('The wishlist is empty!'))


@pytest.fixture()
def clear_compare_list():
    yield




