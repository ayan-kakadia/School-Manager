import helpers
from config import Config
import tkinter
import customtkinter as ctk


class LoginView(ctk.CTkFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, bg_color=Config.BG_COLOR, fg_color=Config.BG_COLOR, **kwargs)
        self.PhotoLabelCreator = self.create_photo_label()
        self.LoginFrame = self.create_login_frame()
        self.LoginWidgetsCreator = self.create_login_widgets()

    def create_photo_label(self):
        Creator = helpers.Creator(self)
        height = width = 422
        Creator.create_label('photo-label', dict(rely=0.5, relx=0.75, anchor=tkinter.CENTER),
                             image='login-img.png', height=height, width=width)
        return Creator

    def create_login_frame(self):
        frame = ctk.CTkFrame(self, fg_color=Config.BLUE,
                             corner_radius=0, bg_color=Config.BLUE)
        frame.place(x=0, relheight=1, relwidth=0.5)
        return frame

    def create_login_widgets(self):
        Creator = helpers.Creator(self.LoginFrame)

        Creator.create_label('title-label', placement_args=dict(relx=0.17, rely=0.17),
                             text='Sign in Mysql account', font=ctk.CTkFont('@Malgun Gothic', -35, 'bold'), fg_color=Config.BLUE)

        Creator.create_label('welcome-label', placement_args=dict(relx=0.17, rely=0.25),
                             text='Welcome to the app', font=ctk.CTkFont('@Malgun Gothic', -20, 'bold'), fg_color=Config.BLUE)

        Creator.create_label('setup-label', placement_args=dict(relx=0.62, rely=0.25),
                             text='Setup Mysql', font=ctk.CTkFont('@Malgun Gothic', -20, 'bold', underline=1), fg_color=Config.BLUE)

        Creator.create_labels({'host-label': dict(relx=0.17, rely=0.35, text='Host'),
                               'user-label': dict(relx=0.17, rely=0.481, text='User'),
                               'password-label': dict(relx=0.17, rely=0.612, text='Password')},
                              font=ctk.CTkFont(
                                  'Arial', -20, 'normal'),
                              anchor=tkinter.W, fg_color=Config.BLUE)

        Creator.create_placeholders({'host-placeholder': dict(relx=0.17, rely=0.389, relwidth=0.66, relheight=0.07),
                                     'user-placeholder': dict(relx=0.17, rely=0.52, relwidth=0.66, relheight=0.07),
                                     'password-placeholder': dict(relx=0.17, rely=0.651, relwidth=0.66, relheight=0.07)},
                                    border_width=0, font=ctk.CTkFont('Arial', -18, 'bold'))

        Creator.create_widget('remember-checkbox', dict(relx=0.17, rely=0.743), 'checkbox', text='keep me logged in', font=ctk.CTkFont('Arial', -11, 'bold'),
                              border_width=2, border_color=Config.WHITE, checkmark_color=Config.BLACK, checkbox_width=20, checkbox_height=20, fg_color=Config.WHITE, corner_radius=5, hover_color=Config.WHITE)

        Creator.create_button('register-button', placement_args=dict(relx=0.17, rely=0.834, relheight=0.07, relwidth=0.66),
                              fg_color=Config.RED, text='Sign In', font=ctk.CTkFont('@Malgun Gothic', -20, 'bold'),
                              anchor=tkinter.CENTER, hover_color=Config.DARK_RED)

        return Creator
