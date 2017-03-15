from Resources.SelectWrapper import SelectWrapper
from Resources.ExLibraries import ExLibraries
from Resources.Util import Utils
from CalendarDialog import CalendarDialog
from Resources.RolloverConfigurationPage import RolloverConfigurationPage

selectors = {
    "newSchedulerDialog": "css=div[ng-include=\"modal.content\"]",
    "symbolField": "model=ctrl.getItem().copyItem.symbol",
    "symbolDropDownMenu": "css=div[ng-class=\"{'has-error':ctrl.isValid('symbol')}\"] .dropdown-menu",
    "currentPeriod": "model=ctrl.getItem().copyItem.currentPeriod",
    "cancelButton": "css=button[ng-click=\"modal.close()\"]",
    "nextPeriod": "model=ctrl.getItem().copyItem.nextPeriod",
    "nextPeriodDropDownMenu": "css=div[ng-class=\"{'has-error':ctrl.isValid('nextPeriod')}\"] .dropdown-menu",
    "middiff": "model=ctrl.getItem().copyItem.manMidPrice",
    "disabledEnabled": "css=label[for=\"enable\"]",
    "saveButton": "css=button[ng-click=\"ctrl.save()\"]"
}


class NewSchedulerDialog(object):
    def __init__(self):
        self.selectWrapper = SelectWrapper()
        self.utils = Utils()
        self.exLib = ExLibraries()
        self.calendar = CalendarDialog()
        self.rolloverConfigurationPage = RolloverConfigurationPage()

    def input_symbol(self, symbol):
        self.exLib.ex_selenium2library().input_text(selectors["symbolField"], symbol)
        self.selectWrapper.select_by_title(selectors["symbolDropDownMenu"], symbol)
        self.check_current_period(10, symbol)

    def click_cancel_button(self):
        self.exLib.ex_selenium2library().click_button(
            self.utils.find_element_in_element(selectors["newSchedulerDialog"], selectors["cancelButton"]))

    def click_calendar_button(self):
        self.exLib.ex_selenium2library().click_element(
            self.utils.find_element_in_element(selectors["newSchedulerDialog"],
                                               self.calendar.get_selectors()["calendarButton"]))

    def check_current_period(self, iteration_count, symbol):
        for i in range(int(iteration_count)):
            period = self.exLib.ex_selenium2library().get_value(selectors["currentPeriod"])
            if period == '' and i == int(iteration_count) - 1:
                raise ValueError("Couldn't get value in field \"Current MDD Period\"")
            elif period == '':
                self.input_symbol(symbol)
            else:
                break

    def input_next_period(self, symbol):
        self.exLib.ex_selenium2library().input_text(selectors["nextPeriod"], symbol)
        self.selectWrapper.select_by_title(selectors["nextPeriodDropDownMenu"], symbol)

    def click_save_button(self):
        self.exLib.ex_selenium2library().click_button(selectors["saveButton"])

    def input_mid_diff(self, value):
        self.exLib.ex_selenium2library().input_text(selectors["middiff"], value)

    def enable_auto_run(self):
        self.exLib.ex_selenium2library().click_element(selectors["disabledEnabled"])

    def create_new_scheduler(self, symbol, next_period):
        self.rolloverConfigurationPage.click_new_scheduler_button()
        self.click_calendar_button()
        self.calendar.click_today_button()
        self.input_symbol(symbol)
        self.check_current_period(10, symbol)
        self.input_next_period(next_period)
        self.click_save_button()

    def create_new_scheduler_with_mid_diff(self, symbol, next_period, mid_diff):
        self.rolloverConfigurationPage.click_new_scheduler_button()
        self.click_calendar_button()
        self.calendar.click_today_button()
        self.input_symbol(symbol)
        self.check_current_period(10, symbol)
        self.input_next_period(next_period)
        self.input_mid_diff(mid_diff)
        self.click_save_button()
