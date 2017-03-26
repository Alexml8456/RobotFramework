from Resources.BackOffice.ExLibraries import ExLibraries
from robot.libraries.BuiltIn import BuiltIn
import time
import calendar
from datetime import datetime


class Utils(object):
    def __init__(self):
        self.exLib = ExLibraries()
        self.builtIn = BuiltIn()

    def get_text_list(self, locator):
        texts = []
        elements = self.exLib.ex_selenium2library()._element_find(locator, False, True)
        for element in elements:
            if element is not None:
                texts.append(element.text)
        return texts if texts else None

    def find_element_in_element(self, parent_element, child_element):
        return parent_element + " " + child_element[child_element.index('=') + 1:]

    def get_current_date(self, date_format):
        return time.strftime(date_format)

    def add_zero(self, month):
        month_index = list(calendar.month_name).index(month)
        if month_index < 10:
            return "0" + str(month_index)
        else:
            return str(month_index)

    def get_current_year(self):
        return datetime.now().year

    def wait_until_elements_is_visible(self, locator):
        elements = self.exLib.ex_selenium2library().get_webelements(locator)
        for element in elements:
            self.exLib.ex_selenium2library().wait_until_element_is_visible(element)

    def number_of_items_should_be(self, locator, length):
        elements = self.exLib.ex_selenium2library().get_webelements(locator)
        self.builtIn.length_should_be(elements, length)
