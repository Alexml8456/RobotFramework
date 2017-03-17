from Resources.BackOffice.ExLibraries import ExLibraries

selectors = {
    "calendarButton": "css=.btn.btn-outline",
    "buttonText": "button=",
    "monthYearButton": "css=button[role=\"heading\"]",
    "rightArrowButton": "css=button[ng-click=\"move(1)\"]"
}


class CalendarDialog(object):
    def __init__(self):
        self.exLib = ExLibraries()

    def click_today_button(self):
        self.exLib.ex_selenium2library().click_button(selectors["buttonText"] + "Today")

    def get_selectors(self):
        return selectors

    def date_selector(self, month, day):
        self.exLib.ex_selenium2library().click_button(selectors["monthYearButton"])
        self.exLib.ex_selenium2library().click_button(selectors["rightArrowButton"])
        self.exLib.ex_selenium2library().click_button(selectors["buttonText"] + month)
        self.exLib.ex_selenium2library().click_button(selectors["buttonText"] + day)
