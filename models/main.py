from .auth import Auth
from .camera import Camera
from .data import Data


class Model:
    def __init__(self):
        self.auth = Auth()
        self.camera = Camera()
        self.data = Data(self.auth)
