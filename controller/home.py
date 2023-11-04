import datetime


class HomeController:
    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["home"]

        self._bind()

    def _bind(self):
        FunctionWidgetsCreator = self.frame.FunctionWidgetsCreator
        FunctionWidgetsCreator.get(
            "new-student-button", "widget").configure(command=self.open_entry)
        FunctionWidgetsCreator.get(
            "new-attendance-button", "widget").configure(command=self.open_attendance)
        FunctionWidgetsCreator.get(
            "student-record-button", "widget").configure(command=self.open_student_record)
        FunctionWidgetsCreator.get(
            "attendance-record-button", "widget").configure(command=self.open_attendance_record)

    def open_entry(self):
        self.view.switch("entry")

    def open_attendance(self):
        face_encodings = self.model.data.get_face_encodings()
        gr_no = self.model.camera.identify_face(face_encodings)

        if gr_no == "No Known Faces":
            self.view.show_error(
                "No Data Error", "No Students Are Registered Yet.\nKindly add some faces in data to compare.")

        elif gr_no:
            now = datetime.datetime.now()
            self.model.data.register_attendance(gr_no, now.date(), now.time())

    def open_student_record(self):
        pass

    def open_attendance_record(self):
        pass
