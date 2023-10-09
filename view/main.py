from .root import Root
from .login import LoginView
from .entry import EntryView
from .home import HomeView
from tkinter import BOTH, filedialog


class View:
    def __init__(self):
        self.root = Root()
        self.frames = {}
        self.cur_frame = None

        self._add_frame(LoginView, "login")
        self._add_frame(HomeView, "home")
        self._add_frame(EntryView, "entry")

    def _add_frame(self, frame, name):
        self.frames[name] = frame(self.root)

    def switch(self, name):
        if self.cur_frame is not None:
            self.cur_frame.pack_forget()
        self.frames[name].pack(fill=BOTH, expand=1)
        self.cur_frame = self.frames[name]

    def browse_file(self, master, filetypes=[("Images", ("*.jpg", "*.jpeg", "*.png"))]):
        return filedialog.askopenfilename(filetypes=filetypes, parent=master, title="BROWSE FILES")

    def start(self):
        self.root.mainloop()
