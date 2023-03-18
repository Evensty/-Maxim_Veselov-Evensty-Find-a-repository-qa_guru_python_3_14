import os

from faker import Faker
from allure_commons._allure import step
from selene import have
from selene.support.conditions import be
from selene.support.shared import browser

fake = Faker()


def test_check_cart_quantity(demoshop, demoshop_session, clean_cart):
    demoshop_session.open("")
    demoshop.add_computing_and_internet_book_to_cart(count=4)
    demoshop.add_book_fiction_to_cart(count=3)
    demoshop.add_health_book_to_cart(count=2)
    demoshop_session.element('.ico-cart .cart-label').click()
    with step('check cart size'):
        demoshop_session.element('.cart-label~.cart-qty').should(have.text('(9)'))


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
    demoshop.add_3rd_album_to_wishlist()
    demoshop.add_music2_blue_to_wishlist()
    demoshop.add_music2_yellow_to_wishlist()
    demoshop_session.element('#topcartlink~li .ico-wishlist').click()
    with step('check wishlist content'):
        demoshop_session.element('.share-link').should(be.existing).click()
        demoshop_session.all('.product>[href]').should(have.texts('3rd Album', 'Music 2', 'Music 2'))


def test_compare_desktop_pc(demoshop, demoshop_session, clear_compare_list):
    demoshop_session.open('https://demowebshop.tricentis.com/desktops')
    demoshop_session.element('.product-title>[href="/build-your-cheap-own-computer"]').click()
    demoshop_session.element('[type="radio"][value="65"]').click()
    demoshop_session.element('[type="radio"][value="55"]').click()
    demoshop_session.element('[type="radio"][value="58"]').click()
    demoshop_session.element('[type="checkbox"][value="94"]').click()
    demoshop_session.element('[type = "button"][value="Add to compare list"]').click()
    demoshop_session.open('https://demowebshop.tricentis.com/notebooks')
    demoshop_session.element('.product-title>[href="/141-inch-laptop"]').click()
    demoshop_session.element('[type = "button"][value="Add to compare list"]').click()
    demoshop_session.save_screenshot('compare.png')
    with step('check screenshot not empty'):
        assert os.path.getsize('compare.png') != 0
    os.remove('compare.png')














    













