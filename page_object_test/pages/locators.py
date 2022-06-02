from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_BUTTON = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')


class MainPagLocators (BasePageLocators):
    def __init__(self, *args, **kwargs):
        super(MainPagLocators, self).__init__(*args, **kwargs)


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD_CONFIRM = (By.ID, "id_registration-password2")
    REGISTER_SUBMIT = (By.NAME, "registration_submit")


class CatalogPageLocators:
    APPEND_TO_BASKET_LOCATOR = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME_LOCATOR = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    PRODUCT_IN_BASKET_NOTIFICATION_LOCATOR = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRODUCT_PRICE_LOCATOR = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    PRODUCT_PRICE_IN_BASKET_LOCATOR = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")


class AccountPageLocators:
    DELETE_PROFILE = (By.ID, "delete_profile")
    DELETE_PROFILE_PASSWORD = (By.ID, "id_password")
    DELETE_PROFILE_CONFIRM = (By.XPATH, '//*[@id="delete_profile_form"]/div[3]/button')


class BasketPageLocators:
    PRODUCTS_LIST = (By.ID, "basket_formset")
    BASKET_STATE_MESSAGE = (By.ID, "content_inner")
