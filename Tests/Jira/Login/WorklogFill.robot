*** Settings ***
Documentation  Login Scenarios
Library  Resources/Jira/LoginPage.py
Library  Resources/Jira/Dashboard.py
Library  Resources/Jira/Worklog.py
Resource  Resources/Jira/Common.robot
Default Tags  Functional
Suite Setup  Begin Web Test
Suite Teardown  End Web Test

*** Test Cases ***
Worklog filling
    LoginPage.login  ${USERNAME}  ${PASSWORD}
    Dashboard.click_user_options
    Dashboard.click_worklog
    Worklog.fill_worklog
    Dashboard.click_user_options
    Dashboard.click_logout