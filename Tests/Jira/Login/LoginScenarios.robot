*** Settings ***
Documentation  Login Scenarios
Library  Resources/Jira/LoginPage.py
Resource  Resources/Jira/Common.robot
#Library  Resources/BackOffice/TopMenuPage.py
Default Tags  Functional
Suite Setup  Begin Web Test
Suite Teardown  End Web Test

*** Test Cases ***
Login With Valid Credentials
    select frame  id=gadget-0
    LoginPage.input_username   ${USERNAME}
    LoginPage.input_password   ${PASSWORD}
    LoginPage.click_login_button
    #TopMenuPage.should_contain_logout_link
    #TopMenuPage.should_contain_text  Welcome ${USERNAME}
    #[Teardown]  TopMenuPage.click_logout_link
