
Feature: Checking user name in people room

Background:
    Given we are on Hipchat Login Page
    When we enter login
    And we enter password
    And we are on Account settings Page
    Then we get full user name from settings

Scenario: Check user name in people page
  Given we are on Hipchat People Page
  When we compare name of current user match the name on Welcome title
  When we move to user page (on People Page)
  Then we compare name of current user match the name in user page

