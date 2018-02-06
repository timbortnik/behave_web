
Feature: Testing search function in search page of HipChat search page

Background:
    Given we are on Hipchat Login Page
    When we enter login
    And we enter password

Scenario: Check search function
    Given we open search page
    Then we input data in top search form
    When we check data from middle search
    When we input correct data in middle search
    Then we check search answer
