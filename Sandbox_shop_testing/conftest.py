import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('--statr-maximized')
    options.add_argument('--window-size = 1650,900')
    return options


@pytest.fixture(scope="function")
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(executable_path='E:\GitRepo\PyTest-and-Selenium_Demo\Sandbox_shop_testing\chromedriver', options=options)
    yield driver
    print("\nquit browser..")
    driver.quit()
