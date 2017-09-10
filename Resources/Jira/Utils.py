from Resources.Jira.ExLibraries import ExLibraries


class Utils(object):
    def __init__(self):
        self.exLib = ExLibraries()

    def find_element_in_element(self, parent_element, find_method, child_element):
        return self.exLib.builtIn.call_method(self.exLib.selenium2library().get_webelement(parent_element), find_method,
                                              child_element[child_element.index('=') + 1:])
