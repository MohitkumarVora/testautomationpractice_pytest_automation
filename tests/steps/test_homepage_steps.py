# tests/steps/test_homepage_steps.py
import pytest
from pytest_bdd import scenarios, given, when, then
from pages.home_page import HomePage

scenarios('../../features/homepage.feature')

@pytest.fixture
def home(page, config):
    """Page object fixture for home page"""
    return HomePage(page, config["base_url"])

@given("I open the home page")
def open_home(home):
    home.goto()

@when("I check that the page loaded")
def check_loaded(home):
    # example: wait for header to be present
    home.page.wait_for_selector("h1")

@then("I should see the header text")
def see_header(home):
    header = home.get_header_text()
    assert header and header.strip() != "", f"Header not found or empty: {header}"