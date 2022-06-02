import pytest
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.smoke
def test_smoke(browser):
    browser.get(link)
    basket_button = browser.find_element(By.CLASS_NAME, "add-to-basket")
    assert basket_button.is_enabled()
