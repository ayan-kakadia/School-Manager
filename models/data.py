from .base import ObservableModel
import utils.converters


class Data(ObservableModel):
    def __init__(self, auth):
        super().__init__()
        self.auth = auth

    def create_db(self, database: str):
        if self.auth.connection is None:
            return
        self.auth.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
        self.auth.connection.commit()
        self.auth.cursor.execute(f"USE {database}")

    def create_table(self, name: str, columns: dict):
        if self.auth.connection is None:
            return

        query = f"CREATE TABLE IF NOT EXISTS {name} ("

        for column, datatype in columns.items():
            query += f"{column} {datatype},"

        query = query[:-1]  # Remove the last ","
        query += ")"

        self.auth.cursor.execute(query)
        self.auth.connection.commit()

    def setup_db(self):
        self.create_db("SCHOOL_DATA")
        student_table_columns = {"GR_NO": "INT (225) PRIMARY KEY AUTO_INCREMENT", "FIRST_NAME": "VARCHAR (225)",
                                 "LAST_NAME": "VARCHAR (225)", "GENDER": "VARCHAR (6)", "ADDRESS": "VARCHAR (225)",
                                 "PHONE_NUMBER": "VARCHAR (10)", "BIRTH_DATE": "DATE",
                                 "EMAIL": "VARCHAR(225)", "LANGUAGE": "VARCHAR(225)", "CLASS": "VARCHAR(12)",
                                 "ROLL_NO": "BIGINT", "REMARKS": "VARCHAR(225)"}
        self.create_table("STUDENT_DATA", student_table_columns)

        photo_table_columns = {"GR_NO": "INT(225) PRIMARY KEY REFERENCES STUDENT_DATA(GR_NO)", "IMAGE": "LONGBLOB",
                               "FACE_ENCODING": "LONGBLOB"}
        self.create_table("PHOTO_DATA", photo_table_columns)

        attendance_table_columns = {
            "GR_NO": "INT (225) REFERENCES STUDENT_DATA(GR_NO)", "TIME": "TIME", "DATE": "DATE"}
        self.create_table("STUDENT_ATTENDANCE", attendance_table_columns)

    def new_student(self, first_name=None, last_name=None, gender=None, address=None, phone_no=None, birth_date=None, email=None, language=None, class_=None, roll_no=None, remarks=None, photo_encoding=None, image=None) -> None:
        query = """INSERT INTO STUDENT_DATA (FIRST_NAME, LAST_NAME, GENDER, ADDRESS, PHONE_NUMBER, BIRTH_DATE, EMAIL, LANGUAGE, CLASS, ROLL_NO, REMARKS) 
        VALUES(%s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s)"""
        args = (first_name, last_name, gender, address, phone_no, birth_date,
                email, language, class_, roll_no, remarks)
        self.auth.cursor.execute(query, args)
        self.auth.connection.commit()

        encoding_binary = utils.converters.cvt_2_b64(photo_encoding)
        image_binary = utils.converters.cvt_2_encoding(image)
        self.auth.cursor.execute(
            "SELECT GR_NO FROM STUDENT_DATA ORDER BY GR_NO DESC LIMIT 1")
        gr_no = self.auth.cursor.fetchone()[0]
        query = "INSERT INTO PHOTO_DATA(GR_NO, IMAGE, FACE_ENCODING) VALUE(%s,%s,%s)"
        self.auth.cursor.execute(query, (gr_no, image_binary, encoding_binary))
        self.auth.connection.commit()
        self.trigger_event("student_registered")

    def get_face_encodings(self):
        self.auth.cursor.execute(
            "SELECT STUDENT_DATA.FIRST_NAME, PHOTO_DATA.GR_NO, PHOTO_DATA.FACE_ENCODING FROM STUDENT_DATA, PHOTO_DATA WHERE STUDENT_DATA.GR_NO = PHOTO_DATA.GR_NO")
        face_encodings = {}
        for first_name, gr_no, pickle_obj_list in self.auth.cursor.fetchall():
            face_encodings[(first_name, gr_no)] = utils.converters.cvt_2_encoding(
                pickle_obj_list)

        return face_encodings

    def register_attendance(self, gr_no, date, time):
        self.auth.cursor.execute(
            "INSERT INTO STUDENT_ATTENDANCE (GR_NO, TIME, DATE) VALUES (%s,%s,%s)", (gr_no, time, date))
        self.auth.connection.commit()
        self.trigger_event("attendance_registered")

    def get_attendance_record(self):
        query = """SELECT STUDENT_ATTENDANCE.DATE,STUDENT_ATTENDANCE.TIME,STUDENT_DATA.FIRST_NAME,STUDENT_DATA.LAST_NAME,STUDENT_DATA.GENDER,STUDENT_DATA.ADDRESS,STUDENT_DATA.EMAIL,STUDENT_DATA.CLASS, STUDENT_DATA.PHONE_NUMBER,STUDENT_DATA.ROLL_NO\
              FROM STUDENT_ATTENDANCE INNER JOIN STUDENT_DATA ON STUDENT_ATTENDANCE.GR_NO = STUDENT_DATA.GR_NO"""
        self.auth.cursor.execute(query)
        return self.auth.cursor.fetchall()
