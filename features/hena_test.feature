Feature: Tst

Background:
    Given we are on Hipchat Login Page
    When we enter login
    And we enter password
    Then we see Welcome title

Scenario: test
    Given we are create token