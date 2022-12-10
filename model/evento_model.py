from datetime import date, datetime

from model.connection_model import db_connection


class EventoModel:
    
    __codigo: int | None
    __fecha: date
    __duracion: int
    __objetivo: str

    def __init__(self, fecha, duracion, objetivo, codigo=None):
        self.__fecha = datetime.strptime(fecha, '%Y-%m-%d').date()
        self.__duracion = duracion
        self.__objetivo = objetivo
        self.__codigo = codigo
    
    @staticmethod
    def format_date(row: dict):
        row['fecha'] = row['fecha'].strftime('%Y-%m-%d')
        return row

    @staticmethod
    def find():
        query = "SELECT * FROM eventos"
        result = db_connection.execute(query)
        if result is None:
            return None
        return list(map(EventoModel.format_date, result))

    @classmethod
    def find_one(cls, codigo):
        query = "SELECT * FROM eventos WHERE codigo={0}"
        evento = db_connection.execute(query, [codigo])
        if evento is None:
            return None
        return cls(**EventoModel.format_date(evento[0]))

    def save(self):
        query = "INSERT INTO eventos VALUES (NOT NULL, '{0}', '{1}', '{2}')"
        values = [self.__fecha, self.__duracion, self.__objetivo]
        return db_connection.execute(query, values)

    def update(self, fecha, duracion, objetivo):
        query = "UPDATE eventos SET fecha='{0}', duracion='{1}', objetivo='{2}' WHERE codigo={3}"
        values = [fecha, duracion, objetivo, self.__codigo]
        return db_connection.execute(query, values)

    def delete(self):
        query = "DELETE FROM eventos WHERE codigo={0}"
        return db_connection.execute(query, [self.__codigo])

    def to_dict(self):
        return {
            'codigo': self.__codigo,
            'fecha': self.__fecha.strftime('%Y-%m-%d'),
            'duracion': self.__duracion,
            'objetivo': self.__objetivo
        }
