Feature: checking status through multiple browsers

Scenario: Login with 2 browsers
    Given we are on the login page from "1st browser"
    And we are on the login page from "2nd browser"
    When we enter login on "1st browser"
    And we enter login on "2nd browser"
    And we enter pass on "1st browser"
    And we enter pass on "2nd browser"

Scenario: Changing status in first browser and checking this changing from second browser
    Given we are on Account settings Page
    Then we get full user name from settings
    And we are in chat window on "1st browser"
    And we are in chat window on "2nd browser"
    Then we change status to "away"
    Then we check changing status to "away" on "2nd browser"
    Then we change status to "do not disturb"
    Then we check changing status to "do not disturb" on "2nd browser"
    Then we change status to "available"
    Then we check changing status to "available" on "2nd browser"