from Resources.BackOffice.SelectWrapper import SelectWrapper
from Resources.BackOffice.ExLibraries import ExLibraries
from Resources.BackOffice.Util import Utils
from Resources.BackOffice.CalendarDialog import CalendarDialog

selectors = {
    "newSchedulerDialog": "css=div[ng-include=\"modal.content\"]",
    "symbolField": "model=ctrl.getItem().copyItem.instrument",
    "symbolDropDownMenu": "css=.dropdown-menu",
    "midPriceInclDiv": "css=span.text-success",
    "dividendAmount": "model=ctrl.getItem().copyItem.amount",
    "saveButton": "css=button[ng-click=\"ctrl.save()\"]"
}


class NewSchedulerDialog(object):
    def __init__(self):
        self.selectWrapper = SelectWrapper()
        self.utils = Utils()
        self.exLib = ExLibraries()
        self.calendar = CalendarDialog()

    def input_symbol(self, symbol):
        self.exLib.ex_selenium2library().input_text(selectors["symbolField"], symbol)
        self.selectWrapper.select_by_title(selectors["symbolDropDownMenu"], symbol)
        self.check_mid_price(10, symbol)

    def click_calendar_button(self):
        self.exLib.ex_selenium2library().click_element(
            self.utils.find_element_in_element(selectors["newSchedulerDialog"],
                                               self.calendar.get_selectors()["calendarButton"]))

    def check_mid_price(self, iteration_count, symbol):
        for i in range(int(iteration_count)):
            mid_price = self.exLib.ex_selenium2library().get_text(
                self.utils.find_element_in_element(selectors["newSchedulerDialog"], selectors["midPriceInclDiv"]))
            if mid_price == '0' and i == int(iteration_count) - 1:
                raise ValueError("Couldn't get value in field \"Mid-Price Incl.Div\"")
            elif mid_price == '0':
                self.input_symbol(symbol)
            else:
                break

    def input_dividend_amount(self, value):
        self.exLib.ex_selenium2library().input_text(selectors["dividendAmount"], value)

    def click_save_button(self):
        self.exLib.ex_selenium2library().click_button(
            self.utils.find_element_in_element(selectors["newSchedulerDialog"], selectors["saveButton"]))
