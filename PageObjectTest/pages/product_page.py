from selenium.common.exceptions import NoAlertPresentException
from PageObjectTest.pages.base_page import BasePage
from PageObjectTest.pages.locators import CatalogPageLocators
import math


class ProductPage(BasePage):

    def is_appended_to_basket(self):
        product_name = self.browser.find_element(*CatalogPageLocators.PRODUCT_NAME_LOCATOR).text
        product_in_basket_name = self.browser.find_element(*CatalogPageLocators.PRODUCT_IN_BASKET_NOTIFICATION_LOCATOR)\
            .text
        assert product_name == product_in_basket_name

    def verify_product_cost(self):
        product_price = self.browser.find_element(*CatalogPageLocators.PRODUCT_PRICE_LOCATOR).text
        product_price_in_basket = self.browser.find_element(*CatalogPageLocators.PRODUCT_PRICE_IN_BASKET_LOCATOR).text
        assert product_price == product_price_in_basket

    def verify_product_in_basket(self):
        self.is_appended_to_basket()
        self.verify_product_cost()

    # Method just to check verification
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def append_to_basket(self):
        button = self.browser.find_element(*CatalogPageLocators.APPEND_TO_BASKET_LOCATOR)
        button.click()
        self.solve_quiz_and_get_code()
        self.verify_product_in_basket()

    # Negative check
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*CatalogPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    # Negative check
    def should_disappeared_success_message(self):
        assert self.is_disappeared(*CatalogPageLocators.SUCCESS_MESSAGE), \
            "Success message should disappeare, but not"

