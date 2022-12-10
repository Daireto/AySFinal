from starlette.requests import Request
from starlette.responses import HTMLResponse, Response, JSONResponse
from starlette.endpoints import HTTPEndpoint

from model.aula_model import AulaModel
from env import response_type

class AulaController(HTTPEndpoint):

    async def get(self, request: Request):
        try:
            id = request.path_params.get('id')
            if id:
                aula = AulaModel.find_one(id)
                if aula is None:
                    return Response(status_code=404)
                return JSONResponse(aula.to_dict())
            
            response = AulaModel.find()
            if response_type == 'json':
                return JSONResponse(response)
            return HTMLResponse(AulaController.to_html(response)) if response else Response(status_code=404)
        except Exception as e:
            return Response("Ha ocurrido un error: {}".format(e), status_code=400)

    async def post(self, request: Request):
        try:
            body = await request.json()
            aula = AulaModel(**body)
            aula.save()
            return Response(status_code=201)
        except Exception as e:
            return Response("Ha ocurrido un error: {}".format(e), status_code=400)

    async def put(self, request: Request):
        try:
            body = await request.json()
            id = request.path_params.get('id')
            if id:
                aula = AulaModel.find_one(id)
                if aula:
                    aula.update(**body)
                    return Response(status_code=200)
                return Response(status_code=404)
            return Response(status_code=400)
        except Exception as e:
            return Response("Ha ocurrido un error: {}".format(e), status_code=400)

    async def delete(self, request: Request):
        try:
            id = request.path_params.get('id')
            if id:
                aula = AulaModel.find_one(id)
                if aula:
                    aula.delete()
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
            <td class="text-sm-left text-center">{row["codigo"]}</td> \
            <td class="text-sm-left text-center">{row["numero"]}</td> \
            <td class="text-sm-left text-center">{row["bloque"]}</td> \
            <td class="text-left">{row["descripcion"]}</td> \
            <td></td></tr>'
        return table
