# features/homepage.feature

Feature: Check homepage navigation and check top navigation menus
  Verify that each top navigation menu navigates to the expected page or external site.


  Background:
    Given the user is on the automation testing practice home page

  @smoke
  Scenario: Verify that the Home page loads and shows header
    Then the page title should be Automation Testing Practice
    And the main header Automation Testing Practice should be visible