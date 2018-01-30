
Feature: Create room, check if created in main room page

Background:
    Given we are on Hipchat Login Page
    When we enter login
    And we enter password
    Then we see Welcome title

Scenario: Check room and check if created
    Given we are on Lobby Page
    Then we create room by name
    Given we are on Lobby Page
    Then we open created room
