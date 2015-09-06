
Feature: Showing off behave and selenium for logging to HipChat

Scenario: Login to HipChat
    Given we are on Hipchat Home Page
    When we proceed to the Login Page
    And we login with valid credentials
    Then we see Welcome title
