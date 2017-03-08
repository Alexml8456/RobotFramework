*** Settings ***
Documentation  Login Scenarios
Library  Resources/LoginPage.py
Resource  Resources/Common.robot
Library  Resources/TopMenuPage.py
Default Tags  Functional
Suite Setup  Begin Web Test
Suite Teardown  End Web Test

*** Test Cases ***
Login With Valid Credentials
    LoginPage.input_username   ${USERNAME}
    LoginPage.input_password   ${PASSWORD}
    LoginPage.click_sing_in_button
    TopMenuPage.should_contain_logout_link
    TopMenuPage.should_contain_text  Welcome ${USERNAME}
    [Teardown]  TopMenuPage.click_logout_link

Login Without Permissions
    LoginPage.input_username   mk893779
    LoginPage.input_password   qwerty
    LoginPage.click_sing_in_button
    LoginPage.alert_message_should_contain  Authentication Failed: User does not have required permissions

Login With Wrong Credentials
    LoginPage.input_username   test_user
    LoginPage.input_password   test_user
    LoginPage.click_sing_in_button
    LoginPage.alert_message_should_contain  Authentication Failed: Invalid credentials