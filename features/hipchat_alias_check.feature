
Feature: Check Alias Functional

Background:
    Given we are on Hipchat Login Page
    When we enter login
    And we enter password
    Then we see Welcome title

Scenario: Login, Open Alias Room, Create Alias, Check

    When we create new alias in chat
    When we create new alias with click buttons

