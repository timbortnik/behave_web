Feature: 2 browser work

Scenario: Login with 2 browsers
    Given we are on the login page from 1st
    And we are on the login page from 2nd
    When we enter login on 1st
    And we enter login on 2nd
    And we enter pass on 1st
    And we enter pass on 2nd
    Then we see Welcome title on 1st
    And we see Welcome title on 2nd

Scenario: Enter the application and chatting between 2 browsers
    Given we are on Hipchat Lobby Page on 1st
    And we are on Hipchat Lobby Page on 2nd
    When we enter in room from 1st
    And we enter in room from 2nd
    And we send message from 1st
    And we send message from 2nd


