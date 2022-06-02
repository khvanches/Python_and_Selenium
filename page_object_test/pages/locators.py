from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPagLocators (BasePageLocators):
    def __init__(self, *args, **kwargs):
        super(MainPagLocators, self).__init__(*args, **kwargs)


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class CatalogPageLocators:
    APPEND_TO_BASKET_LOCATOR = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME_LOCATOR = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    PRODUCT_IN_BASKET_NOTIFICATION_LOCATOR = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRODUCT_PRICE_LOCATOR = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    PRODUCT_PRICE_IN_BASKET_LOCATOR = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")
