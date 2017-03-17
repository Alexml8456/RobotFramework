from Resources.BackOffice.Util import Utils
from Resources.BackOffice.ExLibraries import ExLibraries

selectors = {
    "toolBar": "css=div[role=\"toolbar\"]",
    "newSchedulerButton": "css=span[ng-click=\"userCtrl.hasTradingConfigPermissions && editCtrl.new()\"]"
}


class DividendsConfigurationPage():
    def __init__(self):
        self.utils = Utils()
        self.exLib = ExLibraries()

    def click_new_scheduler_button(self):
        self.exLib.ex_selenium2library().click_element(
            self.utils.find_element_in_element(selectors["toolBar"], selectors["newSchedulerButton"]))

    def delete_all_schedulers(self):
        self.exLib.ex_selenium2library().click_element(selectors["oldSchedulers"])
        self.exLib.ex_selenium2library().click_element(selectors["statusFilter"])
        self.exLib.ex_selenium2library().input_text(selectors["statusFilterField"], 'New')
        self.exLib.ex_selenium2library().click_element(selectors["statusFilter"])
        if self.exLib.ex_selenium2library()._is_element_present(selectors["symbol"]):
            self.exLib.ex_selenium2library().click_element(selectors["selectAll"])
            self.exLib.ex_selenium2library().click_element(selectors["deleteButton"])
            self.exLib.ex_selenium2library().click_element(selectors["clearFilters"])
            self.exLib.ex_selenium2library().click_element(selectors["oldSchedulers"])
        else:
            self.exLib.ex_selenium2library().click_element(selectors["clearFilters"])
            self.exLib.ex_selenium2library().click_element(selectors["oldSchedulers"])

