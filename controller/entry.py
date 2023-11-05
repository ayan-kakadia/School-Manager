from utils import frame_func
from utils import converters
import re


class EntryController:
    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["entry"]
        self.image = None

        self._bind()

    def _bind(self):
        PhotoWidgetsCreator = self.frame.PhotoWidgetsCreator
        PhotoWidgetsCreator.get("take-photo-button",
                                "widget").configure(command=self.take_photo)
        PhotoWidgetsCreator.get("browse-file-button",
                                "widget").configure(command=self.browse_photo)
        PhotoWidgetsCreator.get(
            "reset-button", "widget").configure(command=self.reset)
        PhotoWidgetsCreator.get(
            "register-button", "widget").configure(command=self.register)

    def take_photo(self):
        frame = self.model.camera.click_picture()
        radius = int(max(frame.shape[0], frame.shape[1])/2)
        circle_frame = frame_func.circle_img(
            frame, (int(frame.shape[1]/2), int(frame.shape[0]/2)), radius)
        image = converters.cvt_2_tkinter_img(circle_frame, (280, 280))
        label = self.frame.PhotoWidgetsCreator.get("photo-label", "widget")
        self.frame.replace_photo(label, image)
        self.image = frame

    def browse_photo(self):
        path = self.view.browse_file(self.frame)
        if not path:
            return
        image = converters.path_2_image(path, (0, 0), rel_path=0, type="Image")
        frame = converters.image_2_array(image)
        new_size = int(min(frame.shape[0], frame.shape[1]))
        frame = frame_func.crop_frame(frame, new_size, new_size)
        radius = int(new_size/2)
        circle_frame = frame_func.circle_img(
            frame, (radius, radius), radius)
        image = converters.cvt_2_tkinter_img(circle_frame, (280, 280))
        label = self.frame.PhotoWidgetsCreator.get("photo-label", "widget")
        self.frame.replace_photo(label, image)
        self.image = frame

    def reset(self):
        self.frame.InfoWidgetsCreator.reset_placeholders()
        if self.image is not None:
            self.frame.PhotoWidgetsCreator.reset_photo("photo-label")
            self.image = None

    def register(self):
        InfoPlaceholdersDict = {"first_name": "first-name-placeholder",
                                "last_name": "last-name-placeholder",
                                "gender": "gender-box",
                                "address": "address-placeholder",
                                "phone_no": "phone-no-placeholder",
                                "birth_date": "birth-date-placeholder",
                                "email": "email-placeholder",
                                "language": "language-placeholder",
                                "class_": "class-box",
                                "roll_no": "roll-no-placeholder",
                                "remarks": "remarks-box"}

        args = dict()
        for variable, placeholders_title in InfoPlaceholdersDict.items():
            value = self.frame.InfoWidgetsCreator.get(
                placeholders_title, "placeholder_text")[:225]
            if not value:
                self.frame.display_error("empty")
                return
            args[variable] = value

        if not re.search("[0-9][0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9]", args["birth_date"]):
            self.frame.display_error("date")
            return

        if not args["roll_no"].isdigit():
            self.frame.display_error("roll")
            return

        if not len(args["phone_no"]) == 10:
            self.frame.display_error("phone")
            return

        if self.image is None:
            self.frame.display_error("empty")
            return

        PhotoEncoding = converters.photo_2_encoding(self.image)
        if PhotoEncoding is None:
            self.frame.display_error("face")
            return
        args["photo_encoding"] = PhotoEncoding
        args["image"] = self.image

        self.model.data.new_student(**args)
