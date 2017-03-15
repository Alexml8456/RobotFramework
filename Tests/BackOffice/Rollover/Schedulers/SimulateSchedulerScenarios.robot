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
...          RolloverConfigurationPage.delete_all_schedulers  AND
...          NewSchedulerDialog.create_new_scheduler_with_mid_diff  Swiss20  /SIZ7  3.956
Suite Teardown  Run keywords
...             RolloverConfigurationPage.delete_all_schedulers  AND
...             TopMenuPage.click_logout_link  AND
...             End Web Test

*** Test Cases ***
Simulate scheduler
    RolloverConfigurationPage.select_all_schedulers
    RolloverConfigurationPage.click_simulate_now_button

    RolloverConfigurationPage.simulation_message_should_be  Simulation of 'Swiss20' has been finished.
    RolloverConfigurationPage.radio_buttons_should_be_visible