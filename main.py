import uvicorn
from starlette.applications import Starlette
from starlette.routing import Route

from model.connection_model import db_connection
from controller.aula_controller import AulaController
from controller.evento_controller import EventoController
from controller.grupo_controller import GrupoController
from controller.horario_controller import HorarioController
from controller.inscripcion_controller import InscripcionController
from controller.maestro_controller import MaestroController
from controller.materia_controller import MateriaController


def startup():
    db_connection.connect(
        host="localhost",
        db="ays",
        user="root",
        passwd=""
    )
    print('Base de datos conectada')


def shutdown():
    db_connection.close()
    print('Aplicación cerrada')


routes = [
    Route('/aulas', AulaController),
    Route('/aulas/{id:int}', AulaController),

    Route('/eventos', EventoController),
    Route('/eventos/{id:int}', EventoController),

    Route('/grupos', GrupoController),
    Route('/grupos/{id:int}', GrupoController),

    Route('/horarios', HorarioController),
    Route('/horarios/{id:int}', HorarioController),

    Route('/inscripciones', InscripcionController),
    Route('/inscripciones/{id:int}', InscripcionController),

    Route('/maestros', MaestroController),
    Route('/maestros/{id:int}', MaestroController),

    Route('/materias', MateriaController),
    Route('/materias/{id:int}', MateriaController)
]

app = Starlette(debug=True, routes=routes, on_startup=[startup], on_shutdown=[shutdown])

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)