
Feature: Showing off behave and selenium for logging to HipChat

Background:
    Given we are on Hipchat Login page

Scenario: Login to HipChat
    When we enter login
    And we enter password
    Then we see Welcome title

Scenario: Check incorrect and not valid login to Hipchat
    When we enter incorrect login
    Then we see incorrect login tooltip
    When we enter not valid login
    Then we see login validation tooltip

Scenario: Check disabled button
    When we check disabled next button

Scenario: Check incorrect password to Hipchat
    When we enter login
    And we enter incorrect password
    Then we see password validation tooltip

Scenario: Check backspace button, logining with Enter
    Then we check backspace icon
    When we check logining with press Enter
