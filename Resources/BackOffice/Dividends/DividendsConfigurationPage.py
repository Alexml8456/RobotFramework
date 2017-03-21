from Resources.BackOffice.Utils import Utils
from Resources.BackOffice.ExLibraries import ExLibraries

selectors = {
    "symbol": "binding=item.instrument",
    "toolBar": "css=div[role=\"toolbar\"]",
    "newSchedulerButton": "css=span[ng-click=\"userCtrl.hasTradingConfigPermissions && editCtrl.new()\"]",
    "selectAll": "css=label[for=\"selectedAll\"]",
    "deleteButton": "css=div[ng-click=\"userCtrl.hasTradingConfigPermissions && ctrl.delete()\"]",
    "symbolDate": "model=model",
    "dividendAmount": "model=item.amount"
}


class DividendsConfigurationPage():
    def __init__(self):
        self.utils = Utils()
        self.exLib = ExLibraries()

    def click_new_scheduler_button(self):
        self.exLib.ex_selenium2library().click_element(
            self.utils.find_element_in_element(selectors["toolBar"], selectors["newSchedulerButton"]))

    def delete_all_schedulers(self):
        if self.exLib.ex_selenium2library()._is_element_present(selectors["symbol"]):
            self.exLib.ex_selenium2library().click_element(selectors["selectAll"])
            self.exLib.ex_selenium2library().click_element(selectors["deleteButton"])

    def scheduler_should_have_current_date(self):
        self.exLib.ex_selenium2library().element_attribute_should_contain(selectors["symbolDate"] + "@value",
                                                                          self.utils.get_current_date("%d/%m/%Y"))

    def should_contain_scheduler(self, symbol):
        self.exLib.ex_selenium2library().element_text_should_be(selectors["symbol"], symbol)

    def scheduler_should_have_dividend_amount(self, value):
        self.exLib.ex_selenium2library().element_attribute_should_contain(selectors["dividendAmount"] + "@value", value)