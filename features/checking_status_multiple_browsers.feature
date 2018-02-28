Feature: checking status through multiple browsers

Scenario: Login with 2 browsers
    Given we are on the login page from 1st
    And we are on the login page from 2nd
    When we enter login on 1st
    And we enter login on 2nd
    And we enter pass on 1st
    And we enter pass on 2nd

Scenario: Enter the application and chatting between 2 browsers
    And we are on Account settings Page
    Then we get full user name from settings
    Given we are in chat window
    And we are in chat window on 2nd
    Then we change status to "away"
    Then we check changing status to "away" on 2nd
#    And we enter in room from 2nd
#    And we send message from 1st
#    And we send message from 2nd