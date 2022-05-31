Feature: Add and Delete User

  Scenario: Add a user and validate the user has been added to the table
    Given I launch Chrome browser
    When I Open "http://www.way2automation.com/angularjs-protractor/webtables/" page
    And Click on Add user button
    And Enter user information
    And Click on Save button
    Then User must be successfully saved