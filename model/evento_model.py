from model.connection_model import db_connection


class EventoModel:
    
    __codigo: int | None
    __fecha: str
    __duracion: int
    __objetivo: str

    def __init__(self, fecha, duracion, objetivo, codigo=None):
        self.__fecha = fecha
        self.__duracion = duracion
        self.__objetivo = objetivo
        self.__codigo = codigo

    @staticmethod
    def find():
        query = "SELECT * FROM eventos"
        return db_connection.execute(query)

    @classmethod
    def find_one(cls, codigo):
        query = "SELECT * FROM eventos WHERE codigo={0}"
        evento = db_connection.execute(query, codigo)
        return cls(**evento[0]) if evento else None

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
            'numero': self.__fecha,
            'bloque': self.__duracion,
            'descripcion': self.__objetivo
        }
