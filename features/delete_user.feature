Feature: Delete User

  Scenario: Delete the user "novak" from the table and validate the user has been deleted
    Given I launch browser
    When I open webpage
    And Delete 'novak' user by clicking on 'x' button
    Then Confirm user must be successfully deleted