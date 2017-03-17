*** Settings ***
Documentation  CFD Rollover Simulate Scenarios
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
...         NewSchedulerDialog.create_new_scheduler_with_mid_diff  Swiss20  /SIZ7  3.957
Test Teardown  Run keywords
...            RolloverConfigurationPage.delete_all_schedulers  AND
...            TopMenuPage.click_logout_link  AND
...            End Web Test

*** Test Cases ***
Simulate scheduler
    RolloverConfigurationPage.select_all_schedulers
    RolloverConfigurationPage.click_simulate_now_button

    RolloverConfigurationPage.simulation_message_should_be  Simulation of 'Swiss20' has been finished.
    RolloverConfigurationPage.radio_buttons_should_be_visible