from model.connection_model import db_connection


class AulaModel:
    
    __codigo: int | None
    __numero: int
    __bloque: str
    __descripcion: str

    def __init__(self, numero, bloque, descripcion, codigo=None):
        self.__numero = numero
        self.__bloque = bloque
        self.__descripcion = descripcion
        self.__codigo = codigo

    @staticmethod
    def find():
        query = "SELECT * FROM aulas"
        return db_connection.execute(query)

    @classmethod
    def find_one(cls, codigo):
        query = "SELECT * FROM aulas WHERE codigo={0}"
        aula = db_connection.execute(query, [codigo])
        return cls(**aula[0]) if aula else None

    def save(self):
        query = "INSERT INTO aulas VALUES (NOT NULL, '{0}', '{1}', '{2}')"
        values = [self.__numero, self.__bloque, self.__descripcion]
        return db_connection.execute(query, values)

    def update(self, numero, bloque, descripcion):
        query = "UPDATE aulas SET numero='{0}', bloque='{1}', descripcion='{2}' WHERE codigo={3}"
        values = [numero, bloque, descripcion, self.__codigo]
        return db_connection.execute(query, values)

    def delete(self):
        query = "DELETE FROM aulas WHERE codigo={0}"
        return db_connection.execute(query, [self.__codigo])

    def to_dict(self):
        return {
            'codigo': self.__codigo,
            'numero': self.__numero,
            'bloque': self.__bloque,
            'descripcion': self.__descripcion
        }
