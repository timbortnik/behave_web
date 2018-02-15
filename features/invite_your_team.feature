Feature: Invite your team via email

Background:
    Given we are on Hipchat Login Page
    When we enter login
    And we enter password
    Then we see Welcome title

Scenario: Invite team via email
    Given we are on Lobby Page
    When we click Invite your team
    And we add the emails
    And we delete one email
    And we send invite
    Then we see success message
