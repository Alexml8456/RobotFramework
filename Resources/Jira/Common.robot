*** Settings ***
Library  Selenium2Library

*** Variables ***
${BROWSER}  chrome
${START_URL}  https://jira.internal-services.com
${USERNAME}
${PASSWORD}

*** Keywords ***
Begin Web Test
    open browser  ${START_URL}  ${BROWSER}
    maximize browser window

End Web Test
    close browser