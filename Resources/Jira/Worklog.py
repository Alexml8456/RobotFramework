from Resources.Jira.ExLibraries import ExLibraries
from Resources.Jira.Utils import Utils

selectors = {
    "table": "id=worklog-report",
    "tbody": "xpath=//*[@id=\"worklog-report\"]/tbody/tr",
    "cancelButton": "id=cancel"
}


class Worklog(object):
    def __init__(self):
        self.exLib = ExLibraries()
        self.utils = Utils()

    def select_table_rows(self):
        self.exLib.selenium2library().wait_until_element_is_visible(selectors["table"])
        elements = self.exLib.selenium2library()._element_find(selectors["tbody"], False, True)
        for index, element in enumerate(elements, start=1):
            if "Sat" in element.text or "Sun" in element.text:
                continue
            else:
                self.exLib.selenium2library().click_element(
                    selectors["tbody"] + "[" + str(index) + "]/td[2]/button/span")
                self.exLib.selenium2library().click_element(selectors["cancelButton"])
