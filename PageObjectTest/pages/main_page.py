from selenium.webdriver.common.by import By
from PageObjectTest.pages.base_page import BasePage
from .locators import BasePageLocators
from .login_page import LoginPage

class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        # If you would like to use indirect page transferring in browser
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_presented(*BasePageLocators.LOGIN_LINK)
        self.browser.find_element(*BasePageLocators.LOGIN_LINK)

