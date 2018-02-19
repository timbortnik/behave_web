
Feature: Testing search function in search page of HipChat search page

Scenario: Login to Hipchat
    Given we are on Hipchat Login Page
    When we enter login
    And we enter password

Scenario: Add data in search form and check this data ib other form
    Given we are on search page
    Then we input data in top search form
    When we check data from middle search

Scenario: Check search with correct data and incorrect data
    Given we get correct data
    When we input correct data in middle search
    Then we check search answer
    When we generate and input incorrect data
    Then we check incorrect data
