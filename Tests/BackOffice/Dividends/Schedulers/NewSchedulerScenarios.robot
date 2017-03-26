*** Settings ***
Documentation  Dividends Scenarios
Resource  Resources/BackOffice/Common.robot
Library  Resources/BackOffice/LoginPage.py
Library  Resources/BackOffice/TopMenuPage.py
Library  Resources/BackOffice/Dividends/DividendsConfigurationPage.py
Library  Resources/BackOffice/Dividends/NewSchedulerDialog.py
Library  Resources/BackOffice/CalendarDialog.py
Library  Resources/BackOffice/SideBarNavigation.py

Default Tags  Functional
Suite Setup  Run keywords
...          Begin Web Test  AND
...          LoginPage.login  ${USERNAME}  ${PASSWORD}  AND
...          SideBarNavigation.click_dividends_configuration  AND
...          DividendsConfigurationPage.delete_all_schedulers
Suite Teardown  Run keywords
...             DividendsConfigurationPage.delete_all_schedulers  AND
...             TopMenuPage.click_logout_link  AND
...             End Web Test

*** Test Cases ***
Create new scheduler
    DividendsConfigurationPage.click_new_scheduler_button
    NewSchedulerDialog.input_symbol  Abacus
    NewSchedulerDialog.click_calendar_button
    CalendarDialog.click_today_button
    NewSchedulerDialog.input_dividend_amount  0.01
    NewSchedulerDialog.click_save_button

    DividendsConfigurationPage.should_contain_scheduler  Abacus
    DividendsConfigurationPage.scheduler_should_have_current_date
    DividendsConfigurationPage.scheduler_should_have_dividend_amount  0.01