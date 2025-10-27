# features/homepage.feature

Feature: Home page smoke checks
  As as visitor
  I want the home page to load and show important elements

  @smoke
  Scenario: Verify that the Home page loads and shows header
    Given the user is on the automation testing practice home page
    Then the page title should be "Automation Testing Practice"
    And the main header "Automation Testing Practice" should be visible