Feature checking messaging in multiple browsers

  Scenario: sending message to room
    Given we are on the login page from "1st browser"
    And we are on the login page from "2nd browser"
    When we enter login on "1st browser"
    And we enter login on "2nd browser"
    And we enter pass on "1st browser"
    And we enter pass on "2nd browser"
    And we are in chat window on "1st browser"
    And we are in chat window on "2nd browser"
    And we create a room
    And we enter the room from "2nd browser"
    And we send message to the room
    Then we check message on "1st browser"
    And we check message on "2nd browser"
