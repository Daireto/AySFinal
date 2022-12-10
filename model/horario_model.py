from model.connection_model import db_connection


class HorarioModel:
    
    __codigo: int | None
    __codigo_aula: int
    __codigo_materia: int
    __cedula_maestro: int
    __codigo_grupo: int
    __dias: str
    __hora: str

    def __init__(self, codigo_aula, codigo_materia, cedula_maestro, codigo_grupo, dias, hora, codigo=None):
        self.__codigo_aula = codigo_aula
        self.__codigo_materia = codigo_materia
        self.__cedula_maestro = cedula_maestro
        self.__codigo_grupo = codigo_grupo
        self.__dias = dias
        self.__hora = hora
        self.__codigo = codigo

    @staticmethod
    def find():
        query = "SELECT * FROM horarios"
        return db_connection.execute(query)

    @classmethod
    def find_one(cls, codigo):
        query = "SELECT * FROM horarios WHERE codigo={0}"
        horario = db_connection.execute(query, [codigo])
        return cls(**horario[0]) if horario else None

    def save(self):
        query = "INSERT INTO horarios VALUES (NOT NULL, '{0}', '{1}', '{2}', '{3}', '{4}', '{5}')"
        values = [self.__codigo_aula, self.__codigo_materia, self.__cedula_maestro, self.__codigo_grupo, self.__dias, self.__hora]
        return db_connection.execute(query, values)

    def update(self, codigo_aula, codigo_materia, cedula_maestro, codigo_grupo, dias, hora):
        query = "UPDATE horarios SET codigo_aula='{0}', codigo_materia='{1}', cedula_maestro='{2}', codigo_grupo='{3}', dias='{4}', hora='{5}' WHERE codigo={6}"
        values = [codigo_aula, codigo_materia, cedula_maestro, codigo_grupo, dias, hora, self.__codigo]
        return db_connection.execute(query, values)

    def delete(self):
        query = "DELETE FROM horarios WHERE codigo={0}"
        return db_connection.execute(query, [self.__codigo])

    def to_dict(self):
        return {
            'codigo': self.__codigo,
            'codigo_aula': self.__codigo_aula,
            'codigo_materia': self.__codigo_materia,
            'cedula_maestro': self.__cedula_maestro,
            'codigo_grupo': self.__codigo_grupo,
            'dias': self.__dias,
            'hora': self.__hora
        }
