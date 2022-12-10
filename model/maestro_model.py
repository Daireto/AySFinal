from model.connection_model import db_connection


class MaestroModel:
    
    __cedula: int | None
    __nombre: str
    __apellido: str
    __correo: str
    __telefono: str

    def __init__(self, nombre, apellido, correo, telefono, cedula=None):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo = correo
        self.__telefono = telefono
        self.__cedula = cedula

    @staticmethod
    def find():
        query = "SELECT * FROM maestros"
        return db_connection.execute(query)

    @classmethod
    def find_one(cls, cedula):
        query = "SELECT * FROM maestros WHERE cedula={0}"
        maestro = db_connection.execute(query, [cedula])
        return cls(**maestro[0]) if maestro else None

    def save(self):
        query = "INSERT INTO maestros VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')"
        values = [self.__cedula, self.__nombre, self.__apellido, self.__correo, self.__telefono]
        return db_connection.execute(query, values)

    def update(self, nombre, apellido, correo, telefono):
        query = "UPDATE maestros SET nombre='{0}', apellido='{1}', correo='{2}', telefono='{3}' WHERE cedula={4}"
        values = [nombre, apellido, correo, telefono, self.__cedula]
        return db_connection.execute(query, values)

    def delete(self):
        query = "DELETE FROM maestros WHERE cedula={0}"
        return db_connection.execute(query, [self.__cedula])

    def to_dict(self):
        return {
            'cedula': self.__cedula,
            'nombre': self.__nombre,
            'apellido': self.__apellido,
            'correo': self.__correo,
            'telefono': self.__telefono
        }
