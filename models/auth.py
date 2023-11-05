from .base import ObservableModel
import mysql.connector as mysql
import json


class Auth(ObservableModel):
    def __init__(self) -> None:
        super().__init__()
        self.is_connected = False
        self.connection = None
        self.start()

    def start(self):
        self.creds = credentials("creds.json")
        if self.creds.mysql_host and self.creds.mysql_pass and self.creds.mysql_user:
            try:
                self.connection = mysql.connect(user=self.creds.mysql_user, host=self.creds.mysql_host,
                                                password=self.creds.mysql_pass)
                self.cursor = self.connection.cursor()
                self.is_connected = True
            except Exception:
                pass

    def connect(self, host, user, password, remember):
        try:
            self.connection = mysql.connect(user=user, host=host,
                                            password=password)
            self.cursor = self.connection.cursor()
            self.is_connected = True
            if remember:
                self.creds.new_creds(user, password, host)
            self.trigger_event("connection_success")

        except:
            self.trigger_event("connection_failed")

    def logout(self):
        if self.is_connected:
            self.connection.close()
            self.connection = None
            self.is_connected = False
        self.creds.delete_creds()
        self.trigger_event("logout")


class credentials:
    def __init__(self, file: str) -> None:
        self.file = file
        try:
            with open(file, "r") as fp:
                creds = json.load(fp=fp)
                self.mysql_user = creds.get("MYSQL_USER")
                self.mysql_pass = creds.get("MYSQL_PASS")
                self.mysql_host = creds.get("MYSQL_HOST")
        except Exception:
            self.mysql_user = None
            self.mysql_pass = None
            self.mysql_host = None

    def new_creds(self, user, password, host):
        self.mysql_user = user
        self.mysql_pass = password
        self.mysql_host = host
        creds_dict = {"MYSQL_USER": f"{user}",
                      "MYSQL_PASS": f"{password}",
                      "MYSQL_HOST": f"{host}"}

        with open(self.file, "w") as fp:
            json.dump(creds_dict, fp=fp)

    def delete_creds(self):
        with open(self.file, "w") as fp:
            json.dump({}, fp=fp)
