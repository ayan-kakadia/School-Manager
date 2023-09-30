from .login import LoginController


class Controller:
    def __init__(self, model, view) -> None:
        self.model = model
        self.model.auth.start()
        self.view = view
        self.login_controller = LoginController(model, view)

        self.model.auth.add_event_listener(
            "connection_success", self.connection_success)
        self.model.auth.add_event_listener(
            "connection_failed", self.connection_failed)
        self.model.auth.add_event_listener("logout", self.logout)

    def connection_success(self, model):
        print('success')

    def connection_failed(self, model):
        self.view.login_error()

    def logout(self, model):
        pass

    def start(self):
        if not self.model.auth.is_connected:
            self.view.switch('login')

        self.view.start()
