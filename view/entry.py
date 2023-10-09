import helpers
from config import Config
import tkinter
import tkinter.messagebox
import customtkinter as ctk


class EntryView(ctk.CTkFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, bg_color=Config.BG_COLOR, fg_color=Config.BG_COLOR, **kwargs)
        self.PhotoWidgetsCreator = self.create_photo_widgets()
        self.InfoFrame = self.create_info_frame()
        self.InfoWidgetsCreator = self.create_info_widgets()

    def create_photo_widgets(self):
        Creator = helpers.Creator(self)
        Creator.create_label("photo-label", placement_args=dict(
            relx=0.1875, rely=0.26, anchor=tkinter.CENTER), image="unknown-avatar.png", height=280, width=280, fg_color=Config.WHITE)

        Creator.create_button("take-photo-button", placement_args=dict(relx=0.0625, rely=0.53), image="camera-icon.png", width=61, height=47,
                              fg_color=Config.RED, text_color=Config.BLACK, photo_size=(34, 42), hover_color=Config.LIGHT_RED)
        Creator.create_button("browse-file-button", placement_args=dict(relx=0.0625, rely=0.65), image="files-icon.png", width=61, height=47,
                              fg_color=Config.BLUE, text_color=Config.BLACK, photo_size=(34, 42), hover_color=Config.DARK_BLUE)
        Creator.create_button("reset-button", placement_args=dict(relx=0.0625, rely=0.77), image="reset-icon.png", width=61, height=47,
                              fg_color=Config.RED, text_color=Config.BLACK, photo_size=(32, 32), hover_color=Config.LIGHT_RED)
        Creator.create_button("register-button", placement_args=dict(relx=0.1875, rely=0.925, relwidth=0.3, relheight=0.06, anchor=tkinter.CENTER), fg_color=Config.BLUE, text="REGISTER",
                              font=ctk.CTkFont("Berlin Sans FB Demi", -32, "bold"), text_color=Config.WHITE, hover_color=Config.DARK_BLUE)

        Creator.create_label("take-button-label", dict(relx=0.14, rely=0.54), text="Take a photo",
                             text_color=Config.RED, font=ctk.CTkFont("@Malgun Gothic", -23, "bold"))
        Creator.create_label("browse-file-label", dict(relx=0.14, rely=0.66), text="Upload a photo",
                             text_color=Config.BLUE, font=ctk.CTkFont("@Malgun Gothic", -23, "bold"))
        Creator.create_label("reset-button-label", dict(relx=0.14, rely=0.78), text="Reset all fields",
                             text_color=Config.RED, font=ctk.CTkFont("@Malgun Gothic", -23, "bold"))

        return Creator

    def create_info_frame(self):
        frame = ctk.CTkFrame(self, fg_color=Config.BLUE,
                             corner_radius=0, height=701, width=700)
        frame.place(y=0, x=421)
        return frame

    def create_info_widgets(self):
        Creator = helpers.Creator(self.InfoFrame)

        Creator.create_labels({"first-name-label": dict(relx=0.1, rely=0.063, text="First name"),
                               "last-name-label": dict(relx=0.55, rely=0.063, text="Last name"),
                               "birth-date-label": dict(relx=0.1, rely=0.203, text="Birth date"),
                               "language-label": dict(relx=0.55, rely=0.203, text="Language"),
                               "phone-no-label": dict(relx=0.1, rely=0.343, text="Ph no."),
                               "email-label": dict(relx=0.55, rely=0.343, text="Email"),
                               "gender-label": dict(relx=0.1, rely=0.483, text="Gender"),
                               "address-label": dict(relx=0.55, rely=0.483, text="Address"),
                               "class-label": dict(relx=0.1, rely=0.623, text="Class"),
                               "roll-no-label": dict(relx=0.55, rely=0.623, text="Roll no."),
                               "remarks-label": dict(relx=0.1, rely=0.763, text="Remarks")},
                              font=ctk.CTkFont("Malgun Gothic", -17, "bold"),
                              text_color=Config.WHITE, anchor=tkinter.W, fg_color=Config.BLUE)

        Creator.create_placeholders({"first-name-placeholder": dict(relx=0.1, rely=0.1, relwidth=0.35, relheight=0.063),
                                     "last-name-placeholder": dict(relx=0.55, rely=0.1, relwidth=0.35, relheight=0.063),
                                     "birth-date-placeholder": dict(relx=0.1, rely=0.24, relwidth=0.35, relheight=0.063, vcmd="date"),
                                     "language-placeholder": dict(relx=0.55, rely=0.24, relwidth=0.35, relheight=0.063),
                                     "phone-no-placeholder": dict(relx=0.1, rely=0.38, relwidth=0.35, relheight=0.063, vcmd="phone"),
                                     "email-placeholder": dict(relx=0.55, rely=0.38, relwidth=0.35, relheight=0.063),
                                     "address-placeholder": dict(relx=0.55, rely=0.52, relwidth=0.35, relheight=0.063),
                                     "roll-no-placeholder": dict(relx=0.55, rely=0.66, relwidth=0.35, relheight=0.063, vcmd="int")},
                                    font=ctk.CTkFont("Arial", -18, "bold"))

        Creator.create_widget("class-box", dict(relx=0.1, rely=0.66, relwidth=0.35, relheight=0.063), "optionmenu", font=ctk.CTkFont("Arial", -18, "bold"), values=["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI - Sci", "XI - Commerce", "XI - Arts", "XII - Sci", "XII - Commerce", "XII - Arts"], anchor=tkinter.CENTER, corner_radius=5,
                              fg_color=Config.WHITE, dropdown_fg_color=Config.WHITE, dropdown_hover_color=Config.BLUE, button_color=Config.WHITE, button_hover_color=Config.WHITE, text_color=Config.BLACK, dropdown_text_color=Config.BLACK)
        Creator.create_widget("gender-box", dict(relx=0.1, rely=0.52, relwidth=0.35, relheight=0.063), "optionmenu", font=ctk.CTkFont("Arial", -18, "bold"), values=["Male", "Female", "Other"], anchor=tkinter.CENTER, corner_radius=5,
                              fg_color=Config.WHITE, dropdown_fg_color=Config.WHITE, dropdown_hover_color=Config.BLUE, button_color=Config.WHITE, button_hover_color=Config.WHITE, text_color=Config.BLACK, dropdown_text_color=Config.BLACK)

        Creator.create_widget("remarks-box", dict(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.155), "textbox", border_color=Config.BLUE, border_width=2, fg_color=Config.WHITE, corner_radius=5,
                              scrollbar_button_color=Config.ULTRA_LIGHT_BLUE, scrollbar_button_hover_color=Config.LIGHT_BLUE, text_color=Config.BLACK)

        return Creator

    def replace_photo(self, label, photo):
        label.configure(image=photo)

    def display_error(self, error):
        if error == "empty":
            tkinter.messagebox.showerror(
                "EMPTY FIELD", "One or more of the fields is empty or the image is not upoaded.\nKindly fill all the fields.")
        if error == "date":
            tkinter.messagebox.showerror(
                "INVALID DATE", "Invalid date format.\nMake sure it is in following format:\n YYYY-MM-DD")
        if error == "roll":
            tkinter.messagebox.showerror(
                "INVALID ROLL NO", "Invalid roll no.\nMake sure it is only a number.")
        if error == "phone":
            tkinter.messagebox.showerror(
                "INVALID PHONE NUMBER", "Invalid phone number.\nMake sure it is a 10 digit number.")
        if error == "face":
            tkinter.messagebox.showerror(
                "DETECTION ERROR", "An error occured while detecting face from photo.\nMake sure face is clear and detectable.")
