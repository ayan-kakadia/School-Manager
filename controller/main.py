from .login import LoginController
from .home import HomeController
from .entry import EntryController


class Controller:
    def __init__(self, model, view) -> None:
        self.model = model
        self.model.auth.start()
        self.view = view
        self.login_controller = LoginController(model, view)
        self.home_controller = HomeController(model, view)
        self.entry_controller = EntryController(model, view)

        self.model.auth.add_event_listener(
            "connection_success", self.connection_success)
        self.model.auth.add_event_listener(
            "connection_failed", self.connection_failed)
        self.model.auth.add_event_listener("logout", self.logout)

    def connection_success(self, model):
        self.model.data.setup_db()

    def connection_failed(self, model):
        self.view.show_error(
            "LOGIN ERROR", "An error occured while logging you in.\n Either the credentials are incorrect or empty.")

    def logout(self, model):
        self.view.switch('login')

    def start(self):
        if not self.model.auth.is_connected:
            self.view.switch('login')
        else:
            self.view.switch('home')
            self.model.data.setup_db()

        self.view.start()
