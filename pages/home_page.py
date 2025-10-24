# pages/home_page.py
from locators.home_locators import HomeLocators

class HomePage:
    def __init__(self, page, base_url):
        self.page = page
        self.base_url = base_url

    def goto(self):
        self.page.goto(self.base_url)

    def get_header_text(self):
        return self.page.text_content(HomeLocators.HEADER)

    def is_post_visible(self):
        return self.page.is_visible(HomeLocators.FIRST_POST)

    def click_contact(self):
        self.page.click(HomeLocators.CONTACT_LINK)