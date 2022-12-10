from starlette.requests import Request
from starlette.responses import HTMLResponse, Response, JSONResponse
from starlette.endpoints import HTTPEndpoint

from model.horario_model import HorarioModel
from env import response_type


class HorarioController(HTTPEndpoint):
    
    async def get(self, request: Request):
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
    
    async def post(self, request: Request):
        body = await request.json()
        horario = HorarioModel(**body)
        horario.save()
        return Response(status_code=201)
    
    async def put(self, request: Request):
        body = await request.json()
        id = request.path_params.get('id')
        if id:
            horario = HorarioModel.find_one(id)
            if horario:
                horario.update(**body)
                return Response(status_code=200)
            return Response(status_code=404)
        return Response(status_code=400)
    
    async def delete(self, request: Request):
        id = request.path_params.get('id')
        if id:
            horario = HorarioModel.find_one(id)
            if horario:
                horario.delete()
                return Response(status_code=200)
            return Response(status_code=404)
        return Response(status_code=400)

    @staticmethod
    def to_html(rows):
        table = ''
        for row in rows:
            table += f'<tr> \
            <td class="text-sm-left text-center">H-{row["codigo"]}</td> \
            <td class="text-sm-left text-center">{row["codigo_aula"]}</td> \
            <td class="text-sm-left text-center">M-{row["codigo_materia"]}</td> \
            <td class="text-sm-left text-center">CC-{row["cedula_maestro"]}</td> \
            <td class="text-sm-left text-center">G-{row["codigo_grupo"]}</td> \
            <td class="text-sm-left text-center">{row["dias"]}</td> \
            <td class="text-sm-left text-center">{row["hora"]}</td> \
            </tr>'
        return table
