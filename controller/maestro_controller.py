import json
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.endpoints import HTTPEndpoint

from model.maestro_model import MaestroModel


class MaestroController(HTTPEndpoint):

    async def get(self, request: Request):
        id = request.path_params.get('id')
        if id:
            maestro = MaestroModel.find_one(id)
            if maestro is None:
                return Response(status_code=404)
            response = maestro.to_dict()
        else:
            response = MaestroModel.find()
        return JSONResponse(response)
    
    async def post(self, request: Request):
        body = await request.json()
        maestro = MaestroModel(**body)
        maestro.save()
        return Response(status_code=201)
    
    async def put(self, request: Request):
        body = await request.json()
        id = request.path_params.get('id')
        if id:
            maestro = MaestroModel.find_one(id)
            if maestro:
                maestro.update(**body)
                return Response(status_code=200)
            return Response(status_code=404)
        return Response(status_code=400)
    
    async def delete(self, request: Request):
        id = request.path_params.get('id')
        if id:
            maestro = MaestroModel.find_one(id)
            if maestro:
                maestro.delete()
                return Response(status_code=200)
            return Response(status_code=404)
        return Response(status_code=400)
