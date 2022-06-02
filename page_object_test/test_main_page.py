import pytest
from page_object_test.pages.main_page import MainPage
from page_object_test.pages.login_page import LoginPage


@pytest.mark.smoke
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    # login_page = page.go_to_login_page()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

