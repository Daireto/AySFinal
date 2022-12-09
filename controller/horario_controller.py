import json
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.endpoints import HTTPEndpoint

from model.horario_model import HorarioModel


class HorarioController(HTTPEndpoint):
    
    async def get(self, request: Request):
        id = request.path_params.get('id')
        if id:
            horario = HorarioModel.find_one(id)
            if horario is None:
                return Response(status_code=404)
            response = horario.to_dict()
        else:
            response = HorarioModel.find()
        return JSONResponse(response)
    
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
