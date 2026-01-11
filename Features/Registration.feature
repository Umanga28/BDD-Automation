Feature: Verifying registration functionality
    Scenario: registration with valid data
    Given user is on Registration Page
    When user enters firstname
    And user enter lastname
    And user enters birth_month
    And user enters birth_day
    And user enters birth_year
    And user click gender
    And user enters phone_number
    And user enters password
    And user click on Signup button
    Then user should be registered successfully



    Scenario: registration with duplicate phone_number
    Given user is on Registration Page
    When user enters firstname
    And user enter lastname
    And user enters birth_month
    And user enters birth_day
    And user enters birth_year
    And user click gender
    And user enters duplicate phone_number
    And user enters password
    And user click on Signup button
    Then user should get duplicate phone_number message