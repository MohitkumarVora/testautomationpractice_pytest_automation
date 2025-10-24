# tests/steps/test_homepage_steps.py
import pytest
from pytest_bdd import scenarios, given, when, then
from pages.home_page import HomePage
from helpers.logger import logger

scenarios('../../features/homepage.feature')

# --- GIVEN STEP ---

@given("the user is on the automation testing practice home page")
def user_is_on_home_page(page: Page):
    """Navigate to the home page URL."""
    page.goto(HomeLocators.BASE_URL)

# --- THEN STEPS ---

@then(parsers.parse('the page title should be "{expected_title}"'))
def verify_page_title(page: Page, expected_title):
    """Verifies the browser tab title."""
    expect(page).to_have_title(expected_title)

@then(parsers.parse('the main header "{expected_header}" should be visible'))
def verify_main_header(page: Page, expected_header):
    """Verifies the text and visibility of the main blog header using the imported locator."""

    # Locate the element using the imported locator string
    header_locator = page.locator(HomeLocators.MAIN_HEADER)

    # 1. Assert the header is visible
    expect(header_locator).to_be_visible()

    # 2. Assert the text content matches
    expect(header_locator).to_have_text(expected_header)
@pytest.fixture
def home(page, config):
    """Page object fixture for home page"""
    return HomePage(page, config["base_url"])

@given("I open the home page")
def open_home(home):
    logger.info("Navigating to home page")
    home.goto()

@when("I check that the page loaded")
def check_loaded(home):
    # example: wait for header to be present
    home.page.wait_for_selector("h1")

@then("I should see the header text")
def see_header(home):
    header = home.get_header_text()
    assert header and header.strip() != "", f"Header not found or empty: {header}"
