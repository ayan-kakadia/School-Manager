import os
from PIL import Image
import numpy
import customtkinter as ctk
import numpy as np
import face_recognition
import pickle
import base64
import cv2 as cv
import sys


def abs_path(relative_path: str):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def path_2_image(path: str, dimensions: tuple[int, int], rel_path: bool = True, type="CTkImage"):
    if type == "CTkImage":
        height, width = dimensions
        if rel_path:
            path = abs_path(path)
        if height and width:
            return ctk.CTkImage(Image.open(path), size=(width, height))
        else:
            return ctk.CTkImage(Image.open(path))
    elif type == "Image":
        return Image.open(path)


def encoding_2_b64(encoding):
    pickled_face = pickle.dumps(encoding)
    return base64.b64encode(pickled_face)


def photo_2_encoding(frame):
    array_img = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
    encoding_face = face_recognition.face_encodings(array_img)
    if isinstance(encoding_face, np.ndarray) or encoding_face:
        return encoding_face[0]


def cvt_2_tkinter_img(frame, size: tuple[int, int]):
    height, width = size
    if isinstance(frame, numpy.ndarray):
        frame = cv.cvtColor(frame, cv.COLOR_BGRA2RGBA)
        image = Image.fromarray(frame)
        return ctk.CTkImage(image, size=(width, height))


def cvt_2_encoding(obj):
    if isinstance(obj, bytes):
        return pickle.loads(base64.b64decode(obj))


def image_2_array(image):
    return np.array(image)
