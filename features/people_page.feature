Feature: Checking user name in people room

Background:
    Given we are on Hipchat Login Page
    When we enter login
    And we enter password
    Then we see Welcome title
    Given we are on Account settings Page
    When we get full user name from settings

Scenario: Check user name in people room
  Given we are on Hipchat People Page
  When we compare name of current user with name on Welcome title
  When we move to user page (on People Page)
  Then we compare name of current user with name in user page