import json
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.endpoints import HTTPEndpoint

from model.aula_model import AulaModel


class AulaController(HTTPEndpoint):

    async def get(self, request: Request):
        id = request.path_params.get('id')
        if id:
            aula = AulaModel.find_one(id)
            if aula is None:
                return Response(status_code=404)
            response = aula.to_dict()
        else:
            response = AulaModel.find()
        return JSONResponse(response)

    async def post(self, request: Request):
        body = await request.json()
        aula = AulaModel(**body)
        aula.save()
        return Response(status_code=201)

    async def put(self, request: Request):
        body = await request.json()
        id = request.path_params.get('id')
        if id:
            aula = AulaModel.find_one(id)
            if aula:
                aula.update(**body)
                return Response(status_code=200)
            return Response(status_code=404)
        return Response(status_code=400)

    async def delete(self, request: Request):
        id = request.path_params.get('id')
        if id:
            aula = AulaModel.find_one(id)
            if aula:
                aula.delete()
                return Response(status_code=200)
            return Response(status_code=404)
        return Response(status_code=400)
