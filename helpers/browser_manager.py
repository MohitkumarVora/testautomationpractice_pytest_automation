from playwright.sync_api import sync_playwright
import configparser
import os

class BrowserManager:
    def __init__(self):
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.properties')
        self.config = configparser.RawConfigParser()
        self.config.read(config_path)

    def launch_browser(self):
        browser_type = self.config.get('DEFAULT', 'browser')
        headless = self.config.getboolean('DEFAULT', 'headless')

        p = sync_playwright().start()
        browser = getattr(p, browser_type).launch(headless=headless)
        context = browser.new_context()
        page = context.new_page()
        page.goto(self.config.get('DEFAULT', 'base_url'))
        return p, browser, page

    def close_browser(self, p, browser):
        browser.close()
        p.stop()