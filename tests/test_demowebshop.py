import os

from faker import Faker
from allure_commons._allure import step
from selene import have
from selene.support.conditions import be
from selene.support.shared import browser

fake = Faker()


def test_check_cart_quantity(demoshop, demoshop_session, clean_cart):
    demoshop_session.open("")
    demoshop.demoqa.post('/addproducttocart/catalog/13/1/1')
    demoshop.demoqa.post('/addproducttocart/catalog/22/1/1')
    demoshop.demoqa.post('/addproducttocart/catalog/45/1/1')
    demoshop_session.element('.ico-cart .cart-label').click()
    with step('check cart size'):
        demoshop_session.element('.cart-label~.cart-qty').should(have.text('(3)'))


def test_gift_cards_match(demoshop, demoshop_session, clean_cart):
    demoshop_session.open('https://demowebshop.tricentis.com/gift-cards')
    recipient_info = {
        "name": fake.first_name(),
        "email": fake.email()
    }

    def fill_recipient_info():
        demoshop_session.element('.recipient-name').type(recipient_info["name"])
        demoshop_session.element(".recipient-email").type(recipient_info["email"])
        demoshop_session.element('[id|=add-to-cart-button][type="button"]').click()

    demoshop_session.element('.product-title>[href="/25-virtual-gift-card"]').click()
    fill_recipient_info()
    response = demoshop.demoqa.get('/cart')
    with step('Check recipient info'):
        assert recipient_info['name'], recipient_info['email'] in response.text
        demoshop_session.element('.ico-cart .cart-label').click()


def test_books_match(demoshop, demoshop_session, clean_cart):
    demoshop_session.open('https://demowebshop.tricentis.com/books')
    for book in browser.elements('[type = "button"][value = "Add to cart"]'):
        book.click()
        browser.wait_until(book.should(be.clickable))
    response = demoshop.demoqa.get('/cart')
    with step('check total price'):
        assert '44.00' in response.text


def test_add_digital_downloads_to_wishlist(demoshop, demoshop_session, clean_wishlist):
    demoshop_session.open("")
    demoshop.demoqa.post('/addproducttocart/details/53/2')
    demoshop.demoqa.post('/addproducttocart/details/51/2')
    demoshop.demoqa.post('/addproducttocart/details/52/2')
    browser.element('#topcartlink~li .ico-wishlist').click()
    with step('check wishlist content'):
        browser.element('.share-link').should(be.existing).click()
        browser.all('.product>[href]').should(have.texts('3rd Album', 'Music 2', 'Music 2'))


def test_compare_desktop_pc(demoshop, demoshop_session, clear_compare_list):
    demoshop_session.open('https://demowebshop.tricentis.com/desktops')
    browser.element('.product-title>[href="/build-your-cheap-own-computer"]').click()
    browser.element('[type="radio"][value="65"]').click()
    browser.element('[type="radio"][value="55"]').click()
    browser.element('[type="radio"][value="58"]').click()
    browser.element('[type="checkbox"][value="94"]').click()
    browser.element('[type = "button"][value="Add to compare list"]').click()
    browser.open('https://demowebshop.tricentis.com/notebooks')
    browser.element('.product-title>[href="/141-inch-laptop"]').click()
    browser.element('[type = "button"][value="Add to compare list"]').click()
    browser.save_screenshot('compare.png')
    with step('check screenshot not empty'):
        assert os.path.getsize('compare.png') != 0
    os.remove('compare.png')














    













