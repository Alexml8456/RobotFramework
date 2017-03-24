*** Settings ***
Documentation  CFD Rollover Validation Scenarios
Resource  Resources/BackOffice/Common.robot
Library  Resources/BackOffice/LoginPage.py
Library  Resources/BackOffice/TopMenuPage.py
Library  Resources/BackOffice/Rollover/RolloverConfigurationPage.py
Library  Resources/BackOffice/Rollover/NewSchedulerDialog.py
Library  Resources/BackOffice/CalendarDialog.py
Library  Resources/BackOffice/Utils.py
Default Tags  Functional
Suite Setup  Run keywords
...          Begin Web Test  AND
...          LoginPage.login  ${USERNAME}  ${PASSWORD}  AND
...          RolloverConfigurationPage.delete_all_schedulers  AND
...          Get Current Date  AND
...          NewSchedulerDialog.create_new_scheduler_with_mid_diff  ${symbol}  ${period}  3.957
Suite Teardown  Run keywords
...             RolloverConfigurationPage.delete_all_schedulers  AND
...             TopMenuPage.click_logout_link  AND
...             End Web Test

*** Variables ***
${symbol}  OIL
${period}  /CLZ8

*** Test Cases ***
Validation schedulers with identical date and next period
    NewSchedulerDialog.create_new_scheduler  ${symbol}  ${period}
    NewSchedulerDialog.alert_message_should_contain  Scheduler with instrument ${symbol} and on ${CURRENT_DATE} already exists. Scheduler with periods /CLZ7 : ${period} already exists.
    [Teardown]  NewSchedulerDialog.click_cancel_button

Validation schedulers with identical date
    NewSchedulerDialog.create_new_scheduler  ${symbol}  /CLF6
    NewSchedulerDialog.alert_message_should_contain  Scheduler with instrument ${symbol} and on ${CURRENT_DATE} already exists.
    [Teardown]  NewSchedulerDialog.click_cancel_button

Validation schedulers with identical next period
    NewSchedulerDialog.create_new_scheduler_with_date  ${symbol}  ${period}  May  20
    NewSchedulerDialog.alert_message_should_contain  Scheduler with periods /CLZ7 : ${period} already exists.
    [Teardown]  NewSchedulerDialog.click_cancel_button

Validation for simulate schedulers
    NewSchedulerDialog.create_new_scheduler_with_date  ${symbol}  /CLF6  June  15
    RolloverConfigurationPage.select_all_schedulers
    RolloverConfigurationPage.click_simulate_now_button
    RolloverConfigurationPage.alert_message_should_contain  Simulation can't be run due to validation errors

*** Keywords ***
Get Current Date
    ${CURRENT_DATE}  Utils.get_current_date  %Y-%m-%d
    set suite variable  ${CURRENT_DATE}