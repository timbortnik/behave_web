Feature: 2 browser work

Scenario: Login with 2 browsers
    Given we are on the login page from "1st browser"
    And we are on the login page from "2nd browser"
    When we enter login on "1st browser"
    And we enter login on "2nd browser"
    And we enter pass on "1st browser"
    And we enter pass on "2nd browser"
    Then we see Welcome title on "1st browser"
    And we see Welcome title on "2nd browser"

Scenario: Enter the application and chatting between 2 browsers
    Given we are on Hipchat Lobby Page on "1st browser"
    And we are on Hipchat Lobby Page on "2nd browser"
    When we enter in room from "1st browser"
    And we enter in room from "2nd browser"
    And we send message from "1st browser"
    And we send message from "2nd browser"


