from Resources.Jira.ExLibraries import ExLibraries
from Resources.Jira.Utils import Utils

selectors = {
    "headerDetails": "id=user-options",
    "userContent": "id=user-options-content",
    "worklog": "id=worklog",
    "logout": "id=log_out"
}


class Dashboard(object):
    def __init__(self):
        self.exLib = ExLibraries()
        self.utils = Utils()

    def click_user_options(self):
        self.exLib.selenium2library().wait_until_element_is_visible(selectors["headerDetails"])
        self.exLib.selenium2library().click_element(selectors["headerDetails"])

    def click_worklog(self):
        self.exLib.selenium2library().click_element(
            self.utils.find_element_in_element(selectors["userContent"], 'find_element_by_id', selectors["worklog"]))

    def click_logout(self):
        self.exLib.selenium2library().click_element(
            self.utils.find_element_in_element(selectors["userContent"], 'find_element_by_id', selectors["logout"]))
