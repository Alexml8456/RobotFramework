*** Settings ***
Library  ExtendedSelenium2Library

*** Variables ***
${BROWSER}  chrome
${START_URL}  http://192.168.4.127:8901/
${USERNAME}  user2_fd
${PASSWORD}  test

*** Keywords ***
Begin Web Test
    open browser  ${START_URL}  ${BROWSER}
    maximize browser window

End Web Test
    close browser