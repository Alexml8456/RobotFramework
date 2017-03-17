from Resources.BackOffice.ExLibraries import ExLibraries

selectors = {
    "userName": "model=authCtrl.credentials.username",
    "password": "model=authCtrl.credentials.password",
    "signInButton": "css=[ng-disabled=\"loginForm.$invalid\"]",
    "dangerAlert": "binding=authCtrl.error.message"
}


class LoginPage(object):
    def __init__(self):
        self.exLib = ExLibraries()

    def input_username(self, text):
        self.exLib.ex_selenium2library().input_text(selectors["userName"], text)

    def input_password(self, text):
        self.exLib.ex_selenium2library().input_text(selectors["password"], text)

    def click_sing_in_button(self):
        self.exLib.ex_selenium2library().click_button(selectors["signInButton"])

    def alert_message_should_contain(self, text):
        self.exLib.ex_selenium2library().element_should_contain(selectors["dangerAlert"], text)

    def login(self, user, password):
        self.input_username(user)
        self.input_password(password)
        self.click_sing_in_button()

    def should_contain_sing_in_button(self):
        self.exLib.ex_selenium2library().page_should_contain_button(selectors["signInButton"])
