from Resources.BackOffice.Utils import Utils
from Resources.BackOffice.ExLibraries import ExLibraries

selectors = {
    "symbol": "binding=item.symbol",
    "toolBar": "css=div[role=\"toolbar\"]",
    "newSchedulerButton": "css=span[ng-click=\"userCtrl.hasTradingConfigPermissions && editCtrl.new()\"]",
    "report": "css='a[href=\"/#/rollover-scheduler-reports\"]'",
    "oldSchedulers": "css=label[for=\"old\"]",
    "clearFilters": "css=div[ng-click=\"ctrl.removeAllFilters()\"]",
    "statusFilter": "css=span[popover-title=\"Status filter\"]",
    "statusFilterField": "model=ctrl.statusFilter",
    "selectAll": "css=label[for=\"selectedAll\"]",
    "deleteButton": "css=div[ng-click=\"userCtrl.hasTradingConfigPermissions && ctrl.delete()\"]",
    "symbolDate": "model=model",
    "nextPeriod": "model=item.nextPeriod",
    "midDiff": "css=span[bo-animate-on-change-value=\"item.midPrice\"]",
    "midDiffToUse": "model=item.manMidPrice",
    "enableScheduler": "model=item.enable",
    "simulateNowButton": "css=div[ng-click=\"userCtrl.hasTradingConfigPermissions && ctrl.simulation()\"]",
    "simulationMessage": "binding=alertCtrl.alert.message",
    "playButton": "css=label[uib-btn-radio=\"true\"]",
    "alertMessage": "binding=alertCtrl.alert.message",
    "cloneButton": "css=span[ng-click=\"userCtrl.hasTradingConfigPermissions && editCtrl.cloneItem(item)\"]"
}


class RolloverConfigurationPage():
    def __init__(self):
        self.utils = Utils()
        self.exLib = ExLibraries()

    def get_instrument_values(self):
        return self.utils.get_text_list(selectors["symbol"])

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

    def should_contain_scheduler(self, symbol):
        self.exLib.ex_selenium2library().element_text_should_be(selectors["symbol"], symbol)

    def scheduler_should_have_current_date(self):
        self.exLib.ex_selenium2library().element_attribute_should_contain(selectors["symbolDate"] + "@value",
                                                                          self.utils.get_current_date("%d/%m/%Y"))

    def scheduler_should_have_date(self, month, day):
        self.exLib.ex_selenium2library().element_attribute_should_contain(selectors["symbolDate"] + "@value",
                                                                          str(day) + "/" + self.utils.add_zero(
                                                                              month) + "/" + str(
                                                                              self.utils.get_current_year() + 1))

    def scheduler_should_have_next_period(self, period):
        self.exLib.ex_selenium2library().element_attribute_should_contain(selectors["nextPeriod"] + "@value", period)

    def cur_mid_diff_should_not_be(self, text):
        self.exLib.ex_selenium2library().wait_until_element_does_not_contain(selectors["midDiff"], text)

    def scheduler_should_have_mid_diff(self, value):
        self.exLib.ex_selenium2library().element_attribute_should_contain(selectors["midDiffToUse"] + "@value", value)

    def scheduler_should_be_enabled(self):
        self.exLib.ex_selenium2library().element_should_be_enabled(selectors["enableScheduler"])

    def select_all_schedulers(self):
        self.exLib.ex_selenium2library().click_element(selectors["selectAll"])

    def click_simulate_now_button(self):
        self.exLib.ex_selenium2library().click_element(
            self.utils.find_element_in_element(selectors["toolBar"], selectors["simulateNowButton"]))

    def simulation_message_should_be(self, message, timeout=20):
        self.exLib.ex_selenium2library().wait_until_element_contains(selectors["simulationMessage"], message,
                                                                     timeout=timeout)

    def radio_buttons_should_be_visible(self):
        self.utils.wait_until_elements_is_visible(selectors["playButton"])

    def alert_message_should_contain(self, message):
        self.exLib.ex_selenium2library().wait_until_element_contains(selectors["alertMessage"], message)

    def click_clone_button(self):
        self.exLib.ex_selenium2library().click_element(selectors["cloneButton"])
