from model.connection_model import db_connection


class MateriaModel:
    
    __codigo: int | None
    __nombre: str
    __duracion: int

    def __init__(self, nombre, duracion, codigo=None):
        self.__nombre = nombre
        self.__duracion = duracion
        self.__codigo = codigo

    @staticmethod
    def find():
        query = "SELECT * FROM materias"
        return db_connection.execute(query)

    @classmethod
    def find_one(cls, codigo):
        query = "SELECT * FROM materias WHERE codigo={0}"
        materia = db_connection.execute(query, codigo)
        return cls(**materia[0]) if materia else None

    def save(self):
        query = "INSERT INTO materias VALUES (NOT NULL, '{0}', '{1}')"
        values = [self.__nombre, self.__duracion]
        return db_connection.execute(query, values)

    def update(self, nombre, duracion):
        query = "UPDATE materias SET nombre='{0}', duracion='{1}' WHERE codigo={2}"
        values = [nombre, duracion, self.__codigo]
        return db_connection.execute(query, values)

    def delete(self):
        query = "DELETE FROM materias WHERE codigo={0}"
        return db_connection.execute(query, [self.__codigo])

    def to_dict(self):
        return {
            'codigo': self.__codigo,
            'nombre': self.__nombre,
            'duracion': self.__duracion
        }
