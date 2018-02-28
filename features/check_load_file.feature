Feature: Uploading files

#Background:
#    Given we are on Hipchat Login page
#    When we enter login
#    And we enter password
#    Then we see Welcome title

Background:
    Given we are on Hipchat Login Page
    When we enter login
    And we enter password
    And we are on Account settings Page
    Then we get full user name from settings

Scenario: Upload file
     Given we are on Hipchat chat Page
     When we click Attachment
     And we upload a file
     Then we see new file
