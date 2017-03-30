from robot.libraries.BuiltIn import BuiltIn


class ExLibraries(object):
    def __init__(self):
        self.builtIn = BuiltIn()

    def ex_selenium2library(self):
        return self.builtIn.get_library_instance(name='ExtendedSelenium2Library')
