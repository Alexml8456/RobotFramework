from Resources.Jira.ExLibraries import ExLibraries

selectors = {
    "userName": "id=login-form-username",
    "password": "id=login-form-password",
    "logInButton": "id=login",
    "frame": "gadget-0"
}


class LoginPage(object):
    def __init__(self):
        self.exLib = ExLibraries()

    def input_username(self, text):
        self.exLib.selenium2library().input_text(selectors["userName"], text)

    def input_password(self, text):
        self.exLib.selenium2library().input_text(selectors["password"], text)

    def click_login_button(self):
        self.exLib.selenium2library().click_button(selectors["logInButton"])

    def alert_message_should_contain(self, text):
        self.exLib.selenium2library().element_should_contain(selectors["dangerAlert"], text)

    def login(self, user, password):
        self.input_username(user)
        self.input_password(password)
        self.click_login_button()

    def should_contain_sing_in_button(self):
        self.exLib.selenium2library().page_should_contain_button(selectors["signInButton"])
