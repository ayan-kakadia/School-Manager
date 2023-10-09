import helpers
from config import Config
import tkinter
import customtkinter as ctk


class HomeView(ctk.CTkFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, bg_color=Config.BG_COLOR, fg_color=Config.BG_COLOR, **kwargs)
        self.WelcomeWidgetsCreator = self.create_welcome_widgets()
        self.FunctionWidgetsCreator = self.create_function_widgets()

    def create_welcome_widgets(self):
        Creator = helpers.Creator(self)

        Creator.create_label("circle-label", dict(relx=1, rely=0.5, anchor=tkinter.CENTER), corner_radius=0, image="blue-circle.png",
                             height=1100, width=1100)
        Creator.create_label("heading-text-label", dict(x=610, y=200), justify=tkinter.LEFT,
                             text="Welcome to the app.", font=ctk.CTkFont("@Malgun Gothic", -46, "bold"), bg_color=Config.BLUE, fg_color=Config.BLUE)
        Creator.create_label("heading-text-label", dict(x=610, y=280), justify=tkinter.LEFT,
                             text="Seemlessly manage\nyour school's student\nrecords and\nattendance data\nthrough this app.", font=ctk.CTkFont("@Malgun Gothic", -32, "normal"), bg_color=Config.BLUE, fg_color=Config.BLUE)

        return Creator

    def create_function_widgets(self):
        Creator = helpers.Creator(self)

        Creator.create_labels({"new-student-label": dict(x=207.4, y=27.1, text="Add new student"),
                               "student-record-label": dict(x=207, y=363.5, text="Student record")},
                              font=ctk.CTkFont("Arial", -22, "bold"), image="blue-box.png", height=76, width=259, text_color=Config.RED)

        Creator.create_labels({"new-attendance-label": dict(x=207.4, y=195.3, text="New attendance"),
                               "attendance-record-label": dict(x=207.4, y=531.7, text="Attendance record")},
                              font=ctk.CTkFont("Arial", -22, "bold"), image="red-box.png", height=76, width=259, text_color=Config.BLUE)

        Creator.create_button("new-student-button", dict(x=128.4, y=103.1), corner_radius=5, width=70, height=70, image="new-student-icon.png",
                              photo_size=(42, 42), fg_color=Config.RED, hover_color=Config.DARK_RED)
        Creator.create_button("new-attendance-button", dict(x=128.4, y=271.3), corner_radius=5, width=70, height=70, image="new-attendance-icon.png",
                              photo_size=(50, 50), fg_color=Config.BLUE, hover_color=Config.DARK_BLUE)
        Creator.create_button("student-record-button", dict(x=128.4, y=439.5), corner_radius=5, width=70, height=70, image="student-record-icon.png",
                              photo_size=(42, 42), fg_color=Config.RED, hover_color=Config.DARK_RED)
        Creator.create_button("attendance-record-button", dict(x=128.4, y=607.7), corner_radius=5, width=70, height=70, image="attendance-record-icon.png",
                              photo_size=(42, 42), fg_color=Config.BLUE, hover_color=Config.DARK_BLUE)

        return Creator
