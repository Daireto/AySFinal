from starlette.requests import Request
from starlette.responses import HTMLResponse, Response, JSONResponse
from starlette.endpoints import HTTPEndpoint

from model.grupo_model import GrupoModel
from env import response_type


class GrupoController(HTTPEndpoint):

    async def get(self, request: Request):
        try:
            id = request.path_params.get('id')
            if id:
                grupo = GrupoModel.find_one(id)
                if grupo is None:
                    return Response(status_code=404)
                return JSONResponse(grupo.to_dict())
            
            response = GrupoModel.find()
            if response_type == 'json':
                return JSONResponse(response)
            return HTMLResponse(GrupoController.to_html(response)) if response else Response(status_code=404)
        except Exception as e:
            return Response("Ha ocurrido un error: {}".format(e), status_code=400)
    
    async def post(self, request: Request):
        try:
            body = await request.json()
            grupo = GrupoModel(**body)
            grupo.save()
            return Response(status_code=201)
        except Exception as e:
            return Response("Ha ocurrido un error: {}".format(e), status_code=400)
    
    async def put(self, request: Request):
        try:
            body = await request.json()
            id = request.path_params.get('id')
            if id:
                grupo = GrupoModel.find_one(id)
                if grupo:
                    grupo.update(**body)
                    return Response(status_code=200)
                return Response(status_code=404)
            return Response(status_code=400)
        except Exception as e:
            return Response("Ha ocurrido un error: {}".format(e), status_code=400)
    
    async def delete(self, request: Request):
        try:
            id = request.path_params.get('id')
            if id:
                grupo = GrupoModel.find_one(id)
                if grupo:
                    grupo.delete()
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
            <td class="text-sm-left text-center">G-{row["codigo"]}</td> \
            <td class="text-sm-left text-center">{row["numero_grupo"]}</td> \
            <td class="text-sm-left text-center">{row["cantidad_estudiantes"]}</td> \
            <td></td></tr>'
        return table
