Feature: Authentication
  We provide a consumer key and secret, plus a callback to the connect function
  and the library goes through the authentication process.

  Background: we connect to the client with valid credentials
    Given we provide valid credentials and callback


  Scenario: We can access MIS resources
    Given a models collection resource
    When we get resource
    Then the result is ok
