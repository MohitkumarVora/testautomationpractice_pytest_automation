from locators.login_page_locators import LoginPageLocators

class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self, username, password):
        self.page.fill(LoginPageLocators.USERNAME_INPUT, username)
        self.page.fill(LoginPageLocators.PASSWORD_INPUT, password)
        self.page.click(LoginPageLocators.LOGIN_BUTTON)

    def get_error_message(self):
        return self.page.text_content(LoginPageLocators.ERROR_MESSAGE)