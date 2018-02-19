
Feature: Checking status in chat

Background:
    Given we are on Hipchat Login Page
    When we enter login
    And we enter password
    And we are on Account settings Page
    Then we get full user name from settings

Scenario: Checking status
    Given we are in chat window
    Then we change status to "away"
    Then we change status to "do not disturb"
    Then we change status to "available"





