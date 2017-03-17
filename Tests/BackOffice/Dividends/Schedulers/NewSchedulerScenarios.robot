*** Settings ***
Documentation  Dividends Scenarios
Resource  Resources/BackOffice/Common.robot
Library  Resources/BackOffice/LoginPage.py
Library  Resources/BackOffice/TopMenuPage.py
Library  Resources/BackOffice/Dividends/DividendsConfigurationPage.py
Library  Resources/BackOffice/Rollover/NewSchedulerDialog.py
Library  Resources/BackOffice/CalendarDialog.py
Library  Resources/BackOffice/SideBarNavigation.py
Default Tags  Functional
Suite Setup  Run keywords
...          Begin Web Test  AND
...          LoginPage.login  ${USERNAME}  ${PASSWORD}  AND
...          SideBarNavigation.click_dividends_configuration
Suite Teardown  Run keywords
...             TopMenuPage.click_logout_link  AND
...             End Web Test

*** Test Cases ***
Create new scheduler
    DividendsConfigurationPage.click_new_scheduler_button
