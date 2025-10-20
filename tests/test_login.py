from helpers.browser_manager import BrowserManager
from pages.login_page import LoginPage

def test_login_valid_credentials():
    bm = BrowserManager()
    p, browser, page = bm.launch_browser()

    login_page = LoginPage(page)
    login_page.login("test_user", "test_pass")

    assert page.title() == "Dashboard"

    bm.close_browser(p, browser)