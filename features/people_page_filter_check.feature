Feature: Checking filter on the people page

Scenario: Login to HipChat
    Given we are on Hipchat Login page
    When we enter login
    And we enter password
    Then we see Welcome title

Scenario: Enter people page, check filter
    Given we are on Hipchat People Page
    When we show only admins
    And we show all users
    Then we see all users on page
