import json
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.endpoints import HTTPEndpoint

from model.materia_model import MateriaModel


class MateriaController(HTTPEndpoint):
    
    async def get(self, request: Request):
        id = request.path_params.get('id')
        if id:
            materia = MateriaModel.find_one(id)
            if materia is None:
                return Response(status_code=404)
            response = materia.to_dict()
        else:
            response = MateriaModel.find()
        return JSONResponse(response)
    
    async def post(self, request: Request):
        body = await request.json()
        materia = MateriaModel(**body)
        materia.save()
        return Response(status_code=201)
    
    async def put(self, request: Request):
        body = await request.json()
        id = request.path_params.get('id')
        if id:
            materia = MateriaModel.find_one(id)
            if materia:
                materia.update(**body)
                return Response(status_code=200)
            return Response(status_code=404)
        return Response(status_code=400)
    
    async def delete(self, request: Request):
        id = request.path_params.get('id')
        if id:
            materia = MateriaModel.find_one(id)
            if materia:
                materia.delete()
                return Response(status_code=200)
            return Response(status_code=404)
        return Response(status_code=400)
