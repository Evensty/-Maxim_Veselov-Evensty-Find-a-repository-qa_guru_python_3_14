import os

import pytest
from dotenv import load_dotenv
from selene.support.conditions import have
from selene.support.shared import browser

from config import Hosts
from framework.demoqa_with_env import DemoQaWithEnv
from utils.base_session import BaseSession

load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--env")


@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope='session')
def demoshop(env):
    return DemoQaWithEnv(env).demoqa


@pytest.fixture(scope='session')
def reqres(env):
    return DemoQaWithEnv(env).reqres


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
    browser.element('.clear-list').click()
    browser.element('.page-body').should(have.text('You have no items to compare.'))







