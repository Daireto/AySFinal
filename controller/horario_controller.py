from starlette.requests import Request
from starlette.responses import HTMLResponse, Response, JSONResponse
from starlette.endpoints import HTTPEndpoint

from model.horario_model import HorarioModel
from model import aula_model, maestro_model, materia_model, grupo_model
from env import response_type


class HorarioController(HTTPEndpoint):
    
    async def get(self, request: Request):
        try:
            id = request.path_params.get('id')
            if id:
                horario = HorarioModel.find_one(id)
                if horario is None:
                    return Response(status_code=404)
                return JSONResponse(horario.to_dict())
            
            response = HorarioModel.find()
            if response_type == 'json':
                return JSONResponse(response)
            return HTMLResponse(HorarioController.to_html(response)) if response else Response(status_code=404)
        except Exception as e:
            return Response("Ha ocurrido un error: {}".format(e), status_code=400)
    
    async def post(self, request: Request):
        try:
            body = await request.json()
            horario = HorarioModel(**body)
            horario.save()
            return Response(status_code=201)
        except Exception as e:
            return Response("Ha ocurrido un error: {}".format(e), status_code=400)
    
    async def put(self, request: Request):
        try:
            body = await request.json()
            id = request.path_params.get('id')
            if id:
                horario = HorarioModel.find_one(id)
                if horario:
                    horario.update(**body)
                    return Response(status_code=200)
                return Response(status_code=404)
            return Response(status_code=400)
        except Exception as e:
            return Response("Ha ocurrido un error: {}".format(e), status_code=400)
    
    async def delete(self, request: Request):
        try:
            id = request.path_params.get('id')
            if id:
                horario = HorarioModel.find_one(id)
                if horario:
                    horario.delete()
                    return Response(status_code=200)
                return Response(status_code=404)
            return Response(status_code=400)
        except Exception as e:
            return Response("Ha ocurrido un error: {}".format(e), status_code=400)
    
    @staticmethod
    async def get_related_data_list(request: Request):
        try:
            response = {}
            response['aulas'] = aula_model.AulaModel.find()
            response['materias'] = materia_model.MateriaModel.find()
            response['maestros'] = maestro_model.MaestroModel.find()
            response['grupos'] = grupo_model.GrupoModel.find()
            return JSONResponse(response)
        except Exception as e:
            return Response("Ha ocurrido un error: {}".format(e), status_code=400)

    @staticmethod
    def to_html(rows):
        table = ''
        for row in rows:
            table += f'<tr> \
            <td class="text-sm-left text-center">H-{row["codigo"]}</td> \
            <td class="text-sm-left text-center">{row["bloque"]}-{row["numero"]}</td> \
            <td class="text-sm-left text-center">{row["nombre"]}</td> \
            <td class="text-sm-left text-center">G-{row["numero_grupo"]}</td> \
            <td class="text-sm-left text-center">{row["maestros.nombre"].title()} {row["apellido"].title()}</td> \
            <td class="text-sm-left text-center">{row["dias"]}</td> \
            <td class="text-sm-left text-center">{row["hora"]}</td> \
            </tr>'
        return table
