from starlette.requests import Request
from starlette.responses import HTMLResponse, Response, JSONResponse
from starlette.endpoints import HTTPEndpoint

from model.materia_model import MateriaModel
from env import response_type


class MateriaController(HTTPEndpoint):
    
    async def get(self, request: Request):
        try:
            id = request.path_params.get('id')
            if id:
                materia = MateriaModel.find_one(id)
                if materia is None:
                    return Response(status_code=404)
                return JSONResponse(materia.to_dict())
            
            response = MateriaModel.find()
            if response_type == 'json':
                return JSONResponse(response)
            return HTMLResponse(MateriaController.to_html(response)) if response else Response(status_code=404)
        except Exception as e:
            return Response("Ha ocurrido un error: {}".format(e), status_code=400)
    
    async def post(self, request: Request):
        try:
            body = await request.json()
            materia = MateriaModel(**body)
            materia.save()
            return Response(status_code=201)
        except Exception as e:
            return Response("Ha ocurrido un error: {}".format(e), status_code=400)
    
    async def put(self, request: Request):
        try:
            body = await request.json()
            id = request.path_params.get('id')
            if id:
                materia = MateriaModel.find_one(id)
                if materia:
                    materia.update(**body)
                    return Response(status_code=200)
                return Response(status_code=404)
            return Response(status_code=400)
        except Exception as e:
            return Response("Ha ocurrido un error: {}".format(e), status_code=400)
    
    async def delete(self, request: Request):
        try:
            id = request.path_params.get('id')
            if id:
                materia = MateriaModel.find_one(id)
                if materia:
                    materia.delete()
                    return Response(status_code=200)
                return Response(status_code=404)
            return Response(status_code=400)
        except Exception as e:
            return Response("Ha ocurrido un error: {}".format(e), status_code=400)

    @staticmethod
    def to_html(rows):
        table = ''
        for row in rows:
            table += f'<tr><td></td> \
            <td class="text-sm-left text-center">M-{row["codigo"]}</td> \
            <td class="text-left">{row["nombre"]}</td> \
            <td class="text-sm-left text-center">{row["duracion"]} horas</td> \
            <td></td></tr>'
        return table
