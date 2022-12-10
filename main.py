import uvicorn
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

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


def shutdown():
    db_connection.close()


routes = [
    Route('/aulas', AulaController),
    Route('/aulas/{id:int}', AulaController),

    Route('/eventos', EventoController),
    Route('/eventos/{id:int}', EventoController),

    Route('/grupos', GrupoController),
    Route('/grupos/{id:int}', GrupoController),

    Route('/horarios', HorarioController),
    Route('/horarios/{id:int}', HorarioController),
    Route('/horarios/list_related_data', HorarioController.get_related_data_list),

    Route('/inscripciones', InscripcionController),
    Route('/inscripciones/{id:int}', InscripcionController),
    Route('/inscripciones/list_related_data', InscripcionController.get_related_data_list),

    Route('/maestros', MaestroController),
    Route('/maestros/{id:int}', MaestroController),

    Route('/materias', MateriaController),
    Route('/materias/{id:int}', MateriaController)
]


middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['DELETE', 'GET', 'POST', 'PUT'])
]


app = Starlette(debug=True, routes=routes, middleware=middleware, on_startup=[startup], on_shutdown=[shutdown])

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)
