from .base import ObservableModel
import cv2 as cv
import numpy as np
import utils.frame_func
import face_recognition as fr


class Camera(ObservableModel):
    def __init__(self):
        super().__init__()

    def click_picture(self):
        capture = cv.VideoCapture(0, cv.CAP_DSHOW)
        rval = True
        while rval:
            rval, frame = capture.read()
            frame = utils.frame_func.crop_frame(frame, 384, 354)
            text_pos = [(0, 384), (354, 354)]
            text_image = utils.frame_func.add_text(
                frame, "PRESS SPACEBAR TO CLICK PHOTO", position=text_pos)
            cv.circle(text_image, (177, 177), 150,
                      (255, 255, 255), 2, cv.LINE_AA)
            cv.imshow("EMPLOYEE PHOTO", text_image)
            key = cv.waitKey(20)
            if key == ord(" "):
                cv.destroyAllWindows()
                return cv.cvtColor(frame[27:327, 27:327], cv.COLOR_BGR2RGB)

            if cv.getWindowProperty("EMPLOYEE PHOTO", cv.WND_PROP_VISIBLE) < 1:
                return None

    def identify_face(self, face_encodings: dict):
        capture = cv.VideoCapture(0, cv.CAP_DSHOW)
        if not capture.isOpened():
            return "NO CAMERA"
        known_encodings = list(face_encodings.values())
        identities = list(face_encodings.keys())
        counter = 0
        while True:
            _, frame = capture.read()
            if counter % 3 == 0:
                small_frame_rgb = cv.cvtColor(
                    cv.resize(frame, (0, 0), fx=0.5, fy=0.5), cv.COLOR_BGR2RGB)
                face_locations = fr.face_locations(small_frame_rgb)
                unknown_encoding = fr.face_encodings(
                    small_frame_rgb, face_locations)
                if unknown_encoding:
                    unknown_encoding = unknown_encoding[0]
                    matches = fr.compare_faces(
                        known_encodings, unknown_encoding, tolerance=0.45)
                    best_match = np.argmin(fr.face_distance(
                        known_encodings, unknown_encoding))
                    if matches[best_match]:
                        first_name, gr_no = identities[best_match]
                    else:
                        gr_no = None
            counter += 1
            for top, right, bottom, left in face_locations:
                top *= 2
                bottom *= 2
                right *= 2
                left *= 2
                if id:
                    cv.rectangle(frame, (left-20, top-20),
                                 (right+20, bottom+20), (0, 255, 0), 3)
                    cv.putText(frame, first_name, (left-20, top-30),
                               cv.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
                else:
                    cv.rectangle(frame, (left-20, top-20),
                                 (right+20, bottom+20), (0, 0, 255), 3)
                    cv.putText(frame, "NO MATCH", (left-20, top-30),
                               cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))
            cv.imshow("FACE RECOGNITION", frame)
            key = cv.waitKey(1)
            if key == ord("q"):
                capture.release()
                cv.destroyAllWindows()
                return None

            if key == ord(" "):
                capture.release()
                cv.destroyAllWindows()
                return gr_no
