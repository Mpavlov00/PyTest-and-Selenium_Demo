from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, get_webdriver, url, timeout=10):
        self.browser = get_webdriver
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, selector_type, selector):
        try:
            self.browser.find_element(selector_type, selector)
        except (NoSuchElementException):
            return False
        return True
