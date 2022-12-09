import json
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.endpoints import HTTPEndpoint

from model.inscripcion_model import InscripcionModel


class InscripcionController(HTTPEndpoint):
    
    async def get(self, request: Request):
        id = request.path_params.get('id')
        if id:
            inscripcion = InscripcionModel.find_one(id)
            if inscripcion is None:
                return Response(status_code=404)
            response = inscripcion.to_dict()
        else:
            response = InscripcionModel.find()
        return JSONResponse(response)
    
    async def post(self, request: Request):
        body = await request.json()
        inscripcion = InscripcionModel(**body)
        inscripcion.save()
        return Response(status_code=201)
    
    async def put(self, request: Request):
        body = await request.json()
        id = request.path_params.get('id')
        if id:
            inscripcion = InscripcionModel.find_one(id)
            if inscripcion:
                inscripcion.update(**body)
                return Response(status_code=200)
            return Response(status_code=404)
        return Response(status_code=400)
    
    async def delete(self, request: Request):
        id = request.path_params.get('id')
        if id:
            inscripcion = InscripcionModel.find_one(id)
            if inscripcion:
                inscripcion.delete()
                return Response(status_code=200)
            return Response(status_code=404)
        return Response(status_code=400)
