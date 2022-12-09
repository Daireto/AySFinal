from model.connection_model import db_connection


class GrupoModel:
    
    __codigo: int | None
    __numero_grupo: int
    __cantidad_estudiantes: int

    def __init__(self, numero_grupo_grupo, cantidad_estudiantes, codigo=None):
        self.__numero_grupo = numero_grupo_grupo
        self.__cantidad_estudiantes = cantidad_estudiantes
        self.__codigo = codigo

    @staticmethod
    def find():
        query = "SELECT * FROM grupos"
        return db_connection.execute(query)

    @classmethod
    def find_one(cls, codigo):
        query = "SELECT * FROM grupos WHERE codigo={0}"
        grupo = db_connection.execute(query, codigo)
        return cls(**grupo[0]) if grupo else None

    def save(self):
        query = "INSERT INTO grupos VALUES (NOT NULL, '{0}', '{1}')"
        values = [self.__numero_grupo, self.__cantidad_estudiantes]
        return db_connection.execute(query, values)

    def update(self, numero_grupo, cantidad_estudiantes):
        query = "UPDATE grupos SET numero_grupo='{0}', cantidad_estudiantes='{1}' WHERE codigo={2}"
        values = [numero_grupo, cantidad_estudiantes, self.__codigo]
        return db_connection.execute(query, values)

    def delete(self):
        query = "DELETE FROM grupos WHERE codigo={0}"
        return db_connection.execute(query, [self.__codigo])

    def to_dict(self):
        return {
            'codigo': self.__codigo,
            'numero_grupo': self.__numero_grupo,
            'cantidad_estudiantes': self.__cantidad_estudiantes
        }
