from .root import Root
from .login import LoginView
from tkinter import BOTH, messagebox


class View:
    def __init__(self):
        self.root = Root()
        self.frames = {}
        self.cur_frame = None

        self._add_frame(LoginView, 'login')

    def _add_frame(self, frame, name):
        self.frames[name] = frame(self.root)

    def switch(self, name):
        if self.cur_frame is not None:
            self.cur_frame.pack_forget()
        self.frames[name].pack(fill=BOTH, expand=1)
        self.cur_frame = self.frames[name]

    def login_error(self):
        messagebox.showerror(
            'LOGIN ERROR', 'An error occured while logging you in.\n Either the credentials are incorrect or empty.')

    def start(self):
        self.root.mainloop()
