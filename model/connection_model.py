from typing import Any
import pymysql
from pymysql import Connection, cursors

class SingletonMeta(type):

    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class ConnectionModel(metaclass=SingletonMeta):
    
    __db: Connection
    
    def connect(self, host, db, user, passwd="") -> None:
        try:
            self.__db = pymysql.connect(
                host=host,
                db=db,
                user=user,
                passwd=passwd,
                )
        except Exception as e:
            print("Ha ocurrido un error: {}".format(e))
        
    
    def execute(self, query: str, values: list[Any] | None = None) -> tuple | None:
        try:
            with self.__db.cursor(cursors.DictCursor) as cursor:
                cursor.execute(query.format(*values) if values else query)
                result = cursor.fetchall()
                self.__db.commit()
                return result if result else None
        except Exception as e:
            print("Ha ocurrido un error: {}".format(e))
            self.__db.rollback()
            return None
    
    def close(self):
        self.__db.close()

db_connection = ConnectionModel()
