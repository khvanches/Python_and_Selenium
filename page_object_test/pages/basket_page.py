from page_object_test.pages.base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def is_products_presented_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.PRODUCTS_LIST)

    def no_products_in_basket(self):
        assert not self.is_element_present(*BasketPageLocators.PRODUCTS_LIST)

    def is_empty_message_presented(self):
        expect_message = 'Your basket is empty'
        result_message = self.browser.find_element(*BasketPageLocators.BASKET_STATE_MESSAGE).text.split(".")[0]
        assert expect_message == result_message

    def basket_page_is_empty(self):
        self.no_products_in_basket()
        self.is_empty_message_presented()
