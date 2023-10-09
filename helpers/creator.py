import customtkinter as ctk
import tkinter
from config import Config
from utils import converters
from typing import Literal
from .scrollable_entry import ScrollableEntry


class Creator:
    def __init__(self, master) -> None:
        self.master = master
        self._widgets = dict()
        self._widget_args = dict()

    def create_label(self, title, placement_args, corner_radius=5, image=None, bg_color="transparent", fg_color=Config.BG_COLOR, text="", height=0, width=0, resize_img=True, photo_size: tuple[int, int] | None = None, text_color=Config.WHITE, **kwargs):
        if image:
            if not resize_img:
                image = converters.path_2_image(
                    f"images\\{image}", (None, None))
            elif not photo_size:
                image = converters.path_2_image(
                    f"images\\{image}", (height, width))
            else:
                image = converters.path_2_image(f"images\\{image}", photo_size)

        args = dict(corner_radius=corner_radius, image=image, bg_color=bg_color,
                    fg_color=fg_color, text=text, height=height, width=width, text_color=text_color) | kwargs
        label = ctk.CTkLabel(self.master, **args)
        label.place(**placement_args)
        self._widgets[title] = label
        self._widget_args[title] = args | placement_args
        return label

    def create_labels(self, labels_dict: dict, **kwargs):

        for title, lbl_args in labels_dict.items():
            kwargs.update(dict(text=lbl_args.pop("text", "")))
            self.create_label(title, lbl_args, **kwargs)

    def create_button(self, title, placement_args, corner_radius=5, image=None, bg_color="transparent", fg_color=Config.BG_COLOR, text="", height=0, width=0, resize_img=True, photo_size: tuple[int, int] | None = None, **kwargs):
        if image:
            if not resize_img:
                image = converters.path_2_image(f"images\\{image}", (0, 0))
            if not photo_size:
                image = converters.path_2_image(
                    f"images\\{image}", (height, width))
            else:
                image = converters.path_2_image(f"images\\{image}", photo_size)

        args = dict(corner_radius=corner_radius, image=image, bg_color=bg_color,
                    fg_color=fg_color, text=text, height=height, width=width) | kwargs

        button = ctk.CTkButton(self.master, **args)
        button.configure(corner_radius=corner_radius)
        button.place(**placement_args)
        self._widgets[title] = button
        self._widget_args[title] = args | placement_args
        return button

    def create_placeholder(self, title, placement_args, corner_radius=5, text_color=Config.BLACK, fg_color=Config.WHITE, bg_color="transparent", border_color=Config.BG_COLOR, border_width=2, scrollable: bool = False, vcmd: Literal["date", "phone"] | None = None, **kwargs):
        args = dict(text_color=text_color, bg_color=bg_color, corner_radius=corner_radius,
                    fg_color=fg_color, border_color=border_color, border_width=border_width) | kwargs

        if vcmd:
            args["validate"] = "key"
        if scrollable:
            placeholder = ScrollableEntry(self.master, **args)
        else:
            placeholder = ctk.CTkEntry(self.master, **args)
        if vcmd == "date":
            validatecmd = (placeholder.register(
                self.validate_date), "%d", "%s", "%S", "%W")
            placeholder.configure(validatecommand=validatecmd)
        elif vcmd == "phone":
            validatecmd = (placeholder.register(
                self.validate_phone), "%d", "%s", "%S")
            placeholder.configure(validatecommand=validatecmd)
        elif vcmd == "int":
            validatecmd = (placeholder.register(
                self.validate_int), "%d", "%s", "%S")
            placeholder.configure(validatecommand=validatecmd)

        placeholder.place(**placement_args)
        self._widgets[title] = placeholder
        self._widget_args[title] = args | placement_args | dict(vcmd=vcmd)
        return placeholder

    def create_placeholders(self, placeholders_dict: dict, **kwargs):

        for title, placeholder_args in placeholders_dict.items():
            kwargs["vcmd"] = placeholder_args.pop("vcmd", None)
            self.create_placeholder(title, placeholder_args, **kwargs)

    def validate_date(self, action: str, old_string: str, character: str, widget_id):
        if not action == "1":
            return True
        if not character.isdigit():
            return False
        widget: ctk.CTkEntry = self.master.nametowidget(widget_id)
        if len(old_string) == 3:
            widget.insert(tkinter.END, f"{character}-")
            widget.after_idle(lambda: widget.configure(validate="key"))
        elif len(old_string) == 6:
            widget.insert(tkinter.END, f"{character}-")
            widget.after_idle(lambda: widget.configure(validate="key"))
        elif len(old_string) == 10:
            return False
        return True

    def validate_phone(self, action: str, old_str: str, character: str):
        if not action == "1":
            return True
        if not character.isdigit():
            return False
        elif len(old_str) == 10:
            return False
        return True

    def validate_int(self, action: str, old_str: str, character: str):
        if not action == "1":
            return True
        if not character.isdigit():
            return False
        return True

    def create_widget(self, title, placement_args, type: Literal["checkbox", "frame", "canvas", "textbox", "optionmenu"], **kwargs):
        if type == "canvas":
            widget = ctk.CTkCanvas(self.master, **kwargs)
        if type == "checkbox":
            widget = ctk.CTkCheckBox(self.master, **kwargs)
        if type == "frame":
            widget = ctk.CTkFrame(self.master, **kwargs)
        if type == "optionmenu":
            widget = ctk.CTkOptionMenu(self.master, **kwargs)
        if type == "textbox":
            widget = ctk.CTkTextbox(self.master, **kwargs)
        widget.place(**placement_args)
        self._widgets[title] = widget
        self._widget_args[title] = kwargs | placement_args

        return widget

    def reset_placeholders(self):
        for widget in self._widgets.values():
            if isinstance(widget, ctk.CTkEntry):
                widget.delete(0, tkinter.END)
            elif isinstance(widget, ctk.CTkTextbox):
                widget.delete(1.0, tkinter.END)

    def reset_photo(self, title: str):
        widget = self._widgets.get(title)
        image = self._widget_args.get(title).get("image")
        corner_radius = self._widget_args.get(title).get("corner_radius")
        widget.configure(
            image=image, corner_radius=corner_radius, require_redraw=1)

    def get(self, widget_name, key):
        if key == "widget":
            return self._widgets.get(widget_name)

        elif key == "placeholder_text":
            widget = self._widgets.get(widget_name)
            if isinstance(widget, ctk.CTkTextbox):
                return widget.get(1.0, tkinter.END)
            return widget.get()

        else:
            return self._widget_args.get(widget_name).get(key)
