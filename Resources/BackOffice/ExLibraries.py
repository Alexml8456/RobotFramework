from robot.libraries.BuiltIn import BuiltIn


class ExLibraries(object):
    def ex_selenium2library(self):
        return BuiltIn().get_library_instance(name='ExtendedSelenium2Library')
