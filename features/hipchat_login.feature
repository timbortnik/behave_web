
Feature: Showing off behave and selenium for logging to HipChat

Scenario: Login to HipChat
    Given we are on Hipchat Login Page
    When we enter login
    And we enter password
    Then we see Welcome title
