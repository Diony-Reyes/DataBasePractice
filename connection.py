import sqlite3
import os.path



class SQLiteConnection:
    __BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    __db_path = os.path.join(__BASE_DIR, "academy.db")
    __conn = None

    def __init__(self):
        self.__conn = sqlite3.connect(self.__db_path, isolation_level=None)

    def connect(self):
        self.__conn = sqlite3.connect(self.__db_path, isolation_level=None)
        return self.__conn

    def disconnect(self):
        self.__conn.close()
