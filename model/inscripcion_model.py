from model.connection_model import db_connection


class InscripcionModel:
    
    __codigo: int | None
    __codigo_grupo: int
    __codigo_evento: int

    def __init__(self, codigo_grupo, codigo_evento, codigo=None):
        self.__codigo_grupo = codigo_grupo
        self.__codigo_evento = codigo_evento
        self.__codigo = codigo

    @staticmethod
    def find():
        query = "SELECT * FROM inscripciones"
        return db_connection.execute(query)

    @classmethod
    def find_one(cls, codigo):
        query = "SELECT * FROM inscripciones WHERE codigo={0}"
        inscripcion = db_connection.execute(query, [codigo])
        return cls(**inscripcion[0]) if inscripcion else None

    def save(self):
        query = "INSERT INTO inscripciones VALUES (NOT NULL, '{0}', '{1}')"
        values = [self.__codigo_grupo, self.__codigo_evento]
        return db_connection.execute(query, values)

    def update(self, codigo_grupo, codigo_evento):
        query = "UPDATE inscripciones SET codigo_grupo='{0}', codigo_evento='{1}' WHERE codigo={2}"
        values = [codigo_grupo, codigo_evento, self.__codigo]
        return db_connection.execute(query, values)

    def delete(self):
        query = "DELETE FROM inscripciones WHERE codigo={0}"
        return db_connection.execute(query, [self.__codigo])

    def to_dict(self):
        return {
            'codigo': self.__codigo,
            'codigo_grupo': self.__codigo_grupo,
            'codigo_evento': self.__codigo_evento
        }
