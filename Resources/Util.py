from Resources.ExLibraries import ExLibraries
import time
import calendar
from datetime import datetime


class Utils(object):
    def __init__(self):
        self.exLib = ExLibraries()

    def get_text_list(self, locator):
        texts = []
        elements = self.exLib.ex_selenium2library()._element_find(locator, False, True)
        for element in elements:
            if element is not None:
                texts.append(element.text)
        return texts if texts else None

    def find_element_in_element(self, parent_element, child_element):
        return parent_element + " " + child_element[child_element.index('=') + 1:]

    def get_current_date(self):
        return time.strftime("%d/%m/%Y")

    def add_zero(self, month):
        month_index = list(calendar.month_name).index(month)
        if month_index < 10:
            return "0" + str(month_index)
        else:
            return str(month_index)

    def get_current_year(self):
        return datetime.now().year
