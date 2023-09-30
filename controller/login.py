import customtkinter as ctk
import webbrowser


class LoginController:
    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames['login']

        self._bind()

    def _bind(self):
        LoginWidgetsCreator = self.frame.LoginWidgetsCreator
        setup_label = LoginWidgetsCreator.get('setup-label', 'widget')
        setup_label.bind(
            "<Button-1>", lambda e: webbrowser.open_new('https://www.mysql.com'))
        setup_label.bind("<Enter>", lambda e: setup_label.configure(require_redraw=1,
                                                                    font=ctk.CTkFont('@Malgun Gothic', -20, 'bold', underline=0)))
        setup_label.bind("<Leave>", lambda e: setup_label.configure(require_redraw=1,
                                                                    font=ctk.CTkFont('@Malgun Gothic', -20, 'bold', underline=1)))

        LoginWidgetsCreator.get(
            'register-button', 'widget').configure(command=self.login)

    def login(self):
        LoginWidgetsCreator = self.frame.LoginWidgetsCreator
        host = LoginWidgetsCreator.get('host-placeholder', 'placeholder_text')
        password = LoginWidgetsCreator.get(
            'password-placeholder', 'placeholder_text')
        user = LoginWidgetsCreator.get('user-placeholder', 'placeholder_text')
        remember = LoginWidgetsCreator.get('remember-checkbox', 'widget').get()
        self.model.auth.connect(host, user, password, remember)
