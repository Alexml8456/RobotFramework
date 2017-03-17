from Resources.BackOffice.ExLibraries import ExLibraries
from Resources.BackOffice.Util import Utils

selectors = {
    "sideBar": "css=md-sidenav[md-component-id=\"sidebar\"]",
    "dividendsConfiguration": "css=a[href=\"/#/dividends-configuration\"]"
}


class SideBarNavigation(object):
    def __init__(self):
        self.exLib = ExLibraries()
        self.utils = Utils()

    def click_dividends_configuration(self):
        links = self.exLib.ex_selenium2library().get_webelements(
            self.utils.find_element_in_element(selectors["sideBar"], selectors["dividendsConfiguration"])
        )
        self.exLib.ex_selenium2library().click_link(links[1])
