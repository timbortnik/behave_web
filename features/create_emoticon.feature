Feature: Creating custom emoticon

Background:
    Given we are on Hipchat Login page
    When we enter login
    And we enter password
    Then we see Welcome title

Scenario: Create custom emoticon
     Given we are on Hipchat Emoticons Page
     When we go to emoticons constructor
     And we upload a picture
     And we click "Add emoticon"
     And we see new emoticon
     And we delete emoticon
