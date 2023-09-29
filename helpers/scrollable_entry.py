import customtkinter as ctk


class ScrollableEntry(ctk.CTkEntry):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def xview(self, cmd, *args):
        if cmd == 'moveto':
            self.xview_moveto(*args)
        if cmd == 'scroll':
            self.xview_scroll(*args)
