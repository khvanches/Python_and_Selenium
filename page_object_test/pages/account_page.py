from page_object_test.pages.base_page import BasePage
from .locators import AccountPageLocators

class AccountPage(BasePage):

    def remove_current_user(self, password):
        self.browser.find_element(*AccountPageLocators.DELETE_PROFILE).click()
        self.browser.find_element(*AccountPageLocators.DELETE_PROFILE_PASSWORD).send_keys(password)
        self.browser.find_element(*AccountPageLocators.DELETE_PROFILE_CONFIRM).click()

