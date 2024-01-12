Feature: Testing login to Foresight

  @fixture.browser.firefox
  Scenario: Login page
     Given I navigate to Foresight
      Then I see the login page with the title 'Piscada Cloud'

#  @fixture.browser.firefox
#  Scenario: Successful login
#     Given I navigate to Foresight
#      When I log in as 'integration-test-user-1'
#      Then I see the portal page with the menu button
