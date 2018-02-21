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
