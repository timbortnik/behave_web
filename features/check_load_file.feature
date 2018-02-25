Feature: Uploading files

Background:
    Given we are on Hipchat Login page
    When we enter login
    And we enter password
    Then we see Welcome title

Scenario: Upload file
     Given we are on Hipchat chat Page
     When we click Attachment
     And we upload a file
     And we click Enter
     Then we see new file
