import pytest
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome of firefox")
    parser.addoption('--language', action='store', default='None', help="Choose browser language like (en ,fr, ru)")


def set_language_chrome(language):
    options = webdriver.ChromeOptions()

    # I've tried to construction presented bellow but it doesn't work for me. So, the workaround have been applied
    # options.add_experimental_option('prefs', {'intl.accept_languages': 'fr'})

    options.add_argument(f"--lang={language}")
    print(f"\nstart chrome browser for tests with language {language}..")
    browser = webdriver.Chrome(options=options)
    return browser


def set_language_firefox(language):
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", language)
    print(f"\nstart firefox browser for test with language {language}..")
    browser = webdriver.Firefox(firefox_profile=fp)
    return browser


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")

    if browser_name != "chrome" and browser_name != "firefox":
        raise pytest.UsageError("\n--browser_name should be chrome or firefox")

    if language is not None:
        if browser_name == "chrome":
            browser = set_language_chrome(language)
        else:
            browser = set_language_firefox(language)
    else:
        raise pytest.UsageError("\n--language should be mentioned like (es ,fr, ru)")

    yield browser
    print("\nquit browser..")
    browser.quit()
