from Resources.ExLibraries import ExLibraries

selectors = {
    "logoutLink": "css=[ng-click=\"mainCtrl.logout()\"]",
    "welcome": "binding=mainCtrl.user.name"
}


class TopMenuPage(object):
    def __init__(self):
        self.exLib = ExLibraries()

    def should_contain_logout_link(self):
        self.exLib.ex_selenium2library().page_should_contain_link(selectors["logoutLink"])

    def click_logout_link(self):
        self.exLib.ex_selenium2library().click_link(selectors["logoutLink"])

    def should_contain_text(self, text):
        self.exLib.ex_selenium2library().element_should_contain(selectors["welcome"], text)
