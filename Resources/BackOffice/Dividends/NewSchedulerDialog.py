from Resources.BackOffice.SelectWrapper import SelectWrapper
from Resources.BackOffice.ExLibraries import ExLibraries
from Resources.BackOffice.Util import Utils
from Resources.BackOffice.CalendarDialog import CalendarDialog
from Resources.BackOffice.Rollover.RolloverConfigurationPage import RolloverConfigurationPage

selectors = {
    "symbolField": "model=ctrl.getItem().copyItem.symbol",
    "symbolDropDownMenu": "css=div[ng-class=\"{'has-error':ctrl.isValid('symbol')}\"] .dropdown-menu"
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