import json
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.endpoints import HTTPEndpoint

from model.evento_model import EventoModel


class EventoController(HTTPEndpoint):

    async def get(self, request: Request):
        id = request.path_params.get('id')
        if id:
            evento = EventoModel.find_one(id)
            if evento is None:
                return Response(status_code=404)
            response = evento.to_dict()
        else:
            response = EventoModel.find()
        return JSONResponse(response)

    async def post(self, request: Request):
        body = await request.json()
        evento = EventoModel(**body)
        evento.save()
        return Response(status_code=201)

    async def put(self, request: Request):
        body = await request.json()
        id = request.path_params.get('id')
        if id:
            evento = EventoModel.find_one(id)
            if evento:
                evento.update(**body)
                return Response(status_code=200)
            return Response(status_code=404)
        return Response(status_code=400)

    async def delete(self, request: Request):
        id = request.path_params.get('id')
        if id:
            evento = EventoModel.find_one(id)
            if evento:
                evento.delete()
                return Response(status_code=200)
            return Response(status_code=404)
        return Response(status_code=400)
