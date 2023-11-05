import helpers
from config import Config
import customtkinter as ctk


class StudentRecordView(ctk.CTkFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, bg_color=Config.BG_COLOR, fg_color=Config.BG_COLOR, **kwargs)
