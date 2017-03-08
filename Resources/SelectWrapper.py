from Resources.ExLibraries import ExLibraries


class SelectWrapper(object):
    def __init__(self):
        self.exLib = ExLibraries()

    def select_by_title(self, locator, value):
        self.exLib.ex_selenium2library().click_element(locator + " a[title=\"%s\"]" % value)
