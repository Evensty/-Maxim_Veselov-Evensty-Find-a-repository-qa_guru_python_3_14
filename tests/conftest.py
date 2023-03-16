import os

import pytest
from dotenv import load_dotenv
from selene.support.conditions import have
from selene.support.shared import browser

from framework.demoqa_with_env import DemoQaWithEnv


load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--env", default="prod")


@pytest.fixture(scope='session')
def demoshop(request):
    env = request.config.getoption("--env")
    return DemoQaWithEnv(env)


@pytest.fixture(scope='session')
def reqres(request):
    env = request.config.getoption("--env")
    return DemoQaWithEnv(env).reqres


@pytest.fixture(scope='session')
def cookie(demoshop):
    response = demoshop.login(os.getenv("LOGIN"), os.getenv("PASSWORD"))
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    return authorization_cookie


@pytest.fixture(scope='function')
def demoshop_session(demoshop, cookie):
    browser.config.base_url = demoshop.demoqa.url
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open("/Themes/DefaultClean/Content/images/logo.png")
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
    yield browser
    browser.quit()


@pytest.fixture()
def clean_cart():
    yield demoshop_session
    browser.open('https://demowebshop.tricentis.com/cart')
    for checkbox in browser.elements('[name="removefromcart"]'):
        checkbox.click()
    browser.element('[name="updatecart"]').click()
    browser.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))


@pytest.fixture()
def clean_wishlist():
    yield demoshop_session
    browser.open('https://demowebshop.tricentis.com/wishlist')
    for checkbox in browser.elements('[name="removefromcart"]'):
        checkbox.click()
    browser.element('[value="Update wishlist"]').click()
    browser.element('.wishlist-content').should(have.text('The wishlist is empty!'))


@pytest.fixture()
def clear_compare_list():
    yield demoshop_session
    browser.element('.clear-list').click()
    browser.element('.page-body').should(have.text('You have no items to compare.'))







