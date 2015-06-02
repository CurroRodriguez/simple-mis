Feature: Client api feature
  Test the functionality and interface of the client

  Background: We connect to the client with valid credentials
    Given we provide valid credentials and callback

    Scenario: Access to the api endpoint
      When we call get in client
      Then the result is ok

    Scenario: Access to the models collection
      Given a models collection resource
      When we get resource
      Then the result is ok

    Scenario: Access to a model
      Given a model resource
      When we get resource
      Then the result is ok

    Scenario: Access to a proposal
      Given a proposal resource
      When we get resource
      Then the result is ok

    Scenario: Access to an object collection
      Given an object collection resource
      When we get resource
      Then the result is ok

    Scenario: Access to an object
      Given an object resource
      When we get resource
      Then the result is ok