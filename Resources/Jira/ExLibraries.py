from robot.libraries.BuiltIn import BuiltIn


class ExLibraries(object):
    def __init__(self):
        self.builtIn = BuiltIn()

    def selenium2library(self):
        return self.builtIn.get_library_instance(name='Selenium2Library')
