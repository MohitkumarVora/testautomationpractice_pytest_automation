# tests/steps/test_homepage_steps.py

from pytest_bdd import given, when, then, scenarios, parsers
from playwright.sync_api import Page, expect

# IMPORTING THE LOCATORS DIRECTLY
from locators.home_locators import HomeLocators

# Map all scenarios in the feature file to this steps file
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