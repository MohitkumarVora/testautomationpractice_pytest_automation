Feature: Home page smoke checks
  As a visitor
  I want the home page to load and show important elements

  Scenario: Home page loads and shows header
    Given I open the home page
    When I check that the page loaded
    Then I should see the header text