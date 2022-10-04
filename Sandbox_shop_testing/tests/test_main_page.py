from ..pages.main_page import MainPage


def test_guest_can_go_to_login_page(get_webdriver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(get_webdriver, link)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(get_webdriver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(get_webdriver, link)
    page.open()
    page.should_be_login_link()
