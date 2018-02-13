
Feature: Checking account settings

Background:
    Given we are on Hipchat Login Page
    When we enter login
    And we enter password
    Then we see Welcome title

Scenario: Check pingbot room
    Given we open pingbot room
    When we send message
    Then we receive pingbot reply
