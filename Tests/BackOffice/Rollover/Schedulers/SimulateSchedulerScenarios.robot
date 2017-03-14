*** Settings ***
Documentation  CFD Rollover Simulate Scenarios
Resource  Resources/Common.robot
Library  Resources/LoginPage.py
Library  Resources/TopMenuPage.py
Library  Resources/RolloverConfigurationPage.py
Library  Resources/NewSchedulerDialog.py
Library  Resources/CalendarDialog.py
Default Tags  Functional
Suite Setup  Run keywords
...          Begin Web Test  AND
...          LoginPage.login  ${USERNAME}  ${PASSWORD}  AND
...          RolloverConfigurationPage.delete_all_schedulers
Suite Teardown  Run keywords
...             TopMenuPage.click_logout_link  AND
...             End Web Test
Test Teardown  RolloverConfigurationPage.delete_all_schedulers

*** Test Cases ***
Simulate scheduler
    RolloverConfigurationPage.click_new_scheduler_button
    NewSchedulerDialog.click_calendar_button
    CalendarDialog.click_today_button
    NewSchedulerDialog.input_symbol  OIL
    NewSchedulerDialog.input_next_period  /CLZ7
    NewSchedulerDialog.click_save_button