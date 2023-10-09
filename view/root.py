import customtkinter as ctk
import utils.converters
from config import Config


class Root(ctk.CTk):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        height = 700
        width = 1120
        start_title = "School Manager"
        icon = utils.converters.abs_path("images\icon.ico")

        self.center_win(height, width)
        self.title(start_title)
        self.iconbitmap(icon)
        self.resizable(0, 0)
        self.config(background=Config.BG_COLOR)

    def center_win(self, height, width):
        screen_height = self.winfo_screenheight()
        screen_width = self.winfo_screenwidth()
        self.geometry(
            f"{width}x{height}+{int(screen_width/2 - width/2)}+{int(screen_height/2-height/2)}")
