import json
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.endpoints import HTTPEndpoint

from model.grupo_model import GrupoModel


class GrupoController(HTTPEndpoint):

    async def get(self, request: Request):
        id = request.path_params.get('id')
        if id:
            grupo = GrupoModel.find_one(id)
            if grupo is None:
                return Response(status_code=404)
            response = grupo.to_dict()
        else:
            response = GrupoModel.find()
        return JSONResponse(response)
    
    async def post(self, request: Request):
        body = await request.json()
        grupo = GrupoModel(**body)
        grupo.save()
        return Response(status_code=201)
    
    async def put(self, request: Request):
        body = await request.json()
        id = request.path_params.get('id')
        if id:
            grupo = GrupoModel.find_one(id)
            if grupo:
                grupo.update(**body)
                return Response(status_code=200)
            return Response(status_code=404)
        return Response(status_code=400)
    
    async def delete(self, request: Request):
        id = request.path_params.get('id')
        if id:
            grupo = GrupoModel.find_one(id)
            if grupo:
                grupo.delete()
                return Response(status_code=200)
            return Response(status_code=404)
        return Response(status_code=400)
