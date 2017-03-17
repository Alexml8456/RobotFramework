*** Settings ***
Documentation  Logout Scenarios
Library  Resources/BackOffice/LoginPage.py
Resource  Resources/BackOffice/Common.robot
Library  Resources/BackOffice/TopMenuPage.py
Default Tags  Functional
Suite Setup  Begin Web Test
Suite Teardown  End Web Test
Test Setup  LoginPage.login  ${USERNAME}  ${PASSWORD}

*** Test Cases ***
Logout
    TopMenuPage.click_logout_link
    LoginPage.should_contain_sing_in_button