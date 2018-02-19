
Feature: Check Pingbot Integration

Background:
    Given we are on Hipchat Login Page
    When we enter login
    And we enter password
    Then we see Welcome title


Scenario: Check pingbot room
    And we get mention name name from settings
    Given we open pingbot room
    When we send message
    Then we receive pingbot reply
