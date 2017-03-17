*** Settings ***
Documentation  CFD Rollover Scenarios
Resource  Resources/BackOffice/Common.robot
Library  Resources/BackOffice/LoginPage.py
Library  Resources/BackOffice/TopMenuPage.py
Library  Resources/BackOffice/Rollover/RolloverConfigurationPage.py
Library  Resources/BackOffice/Rollover/NewSchedulerDialog.py
Library  Resources/BackOffice/CalendarDialog.py
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
Create new scheduler
    RolloverConfigurationPage.click_new_scheduler_button
    NewSchedulerDialog.click_calendar_button
    CalendarDialog.click_today_button
    NewSchedulerDialog.input_symbol  OIL
    NewSchedulerDialog.input_next_period  /CLZ7
    NewSchedulerDialog.click_save_button

    RolloverConfigurationPage.should_contain_scheduler  OIL
    RolloverConfigurationPage.scheduler_should_have_current_date
    RolloverConfigurationPage.scheduler_should_have_next_period  /CLZ7
    RolloverConfigurationPage.cur_mid_diff_should_not_be  N/A

Create new scheduler with auto run
    RolloverConfigurationPage.click_new_scheduler_button
    NewSchedulerDialog.click_calendar_button
    CalendarDialog.date_selector  September  15
    NewSchedulerDialog.input_symbol  CORN
    NewSchedulerDialog.input_next_period  /ZCZ7
    NewSchedulerDialog.input_mid_diff  2
    NewSchedulerDialog.enable_auto_run
    NewSchedulerDialog.click_save_button

    RolloverConfigurationPage.should_contain_scheduler  CORN
    RolloverConfigurationPage.scheduler_should_have_date  September  15
    RolloverConfigurationPage.scheduler_should_have_next_period  /ZCZ7
    RolloverConfigurationPage.cur_mid_diff_should_not_be  N/A
    RolloverConfigurationPage.scheduler_should_have_mid_diff  2
    RolloverConfigurationPage.scheduler_should_be_enabled