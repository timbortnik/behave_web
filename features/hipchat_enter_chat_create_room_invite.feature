
Feature: Entering the app, creating mate, relogin, accept, deleting

Scenario: Login to HipChat
    Given we are on Hipchat Login Page
    When we enter login
    And we enter password
    Then we see Welcome title


Scenario: Enter the app, create room, invite member
    Given we are on Hipchat Lobby Page
    Then we create a room
    Then we invite member
    @create

Scenario: Relogin and accept the invitation
    Given we are on Hipchat Login Page
    When we enter other login
    And we enter other password
    Then we see Welcome title
    Given we are on Hipchat Lobby Page
    Then we accept the invitation

@delete_room
Scenario: Relogin to 1st acc and delete room
    Given we are on Hipchat Login Page
    When we enter login
    And we enter password
    Then we see Welcome title
    Given we are on Hipchat Lobby Page
    Then we delete the room