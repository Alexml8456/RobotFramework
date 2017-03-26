*** Settings ***
Documentation  CFD Rollover Clone Scenarios
Resource  Resources/BackOffice/Common.robot
Library  Resources/BackOffice/LoginPage.py
Library  Resources/BackOffice/TopMenuPage.py
Library  Resources/BackOffice/Rollover/RolloverConfigurationPage.py
Library  Resources/BackOffice/Rollover/NewSchedulerDialog.py
Library  Resources/BackOffice/CalendarDialog.py

Default Tags  Functional
Test Setup  Run keywords
...         Begin Web Test  AND
...         LoginPage.login  ${USERNAME}  ${PASSWORD}  AND
...         RolloverConfigurationPage.delete_all_schedulers  AND
...         NewSchedulerDialog.create_new_scheduler_with_date  SILVER  /SIZ7  May  20
Test Teardown  Run keywords
...            RolloverConfigurationPage.delete_all_schedulers  AND
...            TopMenuPage.click_logout_link  AND
...            End Web Test

*** Test Cases ***
Clone scheduler
    RolloverConfigurationPage.click_clone_button
    NewSchedulerDialog.click_calendar_button
    CalendarDialog.click_today_button
    NewSchedulerDialog.input_symbol  GOLD
    NewSchedulerDialog.input_next_period  /GCF4
    NewSchedulerDialog.input_mid_diff  9.951
    NewSchedulerDialog.click_save_button

    RolloverConfigurationPage.should_contain_symbols_amount  2
    RolloverConfigurationPage.should_contain_scheduler  GOLD
    RolloverConfigurationPage.scheduler_should_have_current_date
    RolloverConfigurationPage.scheduler_should_have_next_period  /GCF4
    RolloverConfigurationPage.scheduler_should_have_mid_diff  9.951