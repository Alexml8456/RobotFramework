*** Settings ***
Documentation  Logout Scenarios
Library  Resources/LoginPage.py
Resource  Resources/Common.robot
Library  Resources/TopMenuPage.py
Default Tags  Functional
Suite Setup  Begin Web Test
Suite Teardown  End Web Test
Test Setup  LoginPage.login  ${USERNAME}  ${PASSWORD}

*** Test Cases ***
Logout
    TopMenuPage.click_logout_link
    LoginPage.should_contain_sing_in_button