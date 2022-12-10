from starlette.requests import Request
from starlette.responses import HTMLResponse, Response, JSONResponse
from starlette.endpoints import HTTPEndpoint

from model.maestro_model import MaestroModel
from env import response_type


class MaestroController(HTTPEndpoint):

    async def get(self, request: Request):
        try:
            id = request.path_params.get('id')
            if id:
                maestro = MaestroModel.find_one(id)
                if maestro is None:
                    return Response(status_code=404)
                return JSONResponse(maestro.to_dict())
            
            response = MaestroModel.find()
            if response_type == 'json':
                return JSONResponse(response)
            return HTMLResponse(MaestroController.to_html(response)) if response else Response(status_code=404)
        except Exception as e:
            return Response("Ha ocurrido un error: {}".format(e), status_code=400)
    
    async def post(self, request: Request):
        try:
            body = await request.json()
            maestro = MaestroModel(**body)
            maestro.save()
            return Response(status_code=201)
        except Exception as e:
            return Response("Ha ocurrido un error: {}".format(e), status_code=400)
    
    async def put(self, request: Request):
        try:
            body = await request.json()
            id = request.path_params.get('id')
            if id:
                maestro = MaestroModel.find_one(id)
                if maestro:
                    maestro.update(**body)
                    return Response(status_code=200)
                return Response(status_code=404)
            return Response(status_code=400)
        except Exception as e:
            return Response("Ha ocurrido un error: {}".format(e), status_code=400)
    
    async def delete(self, request: Request):
        try:
            id = request.path_params.get('id')
            if id:
                maestro = MaestroModel.find_one(id)
                if maestro:
                    maestro.delete()
                    return Response(status_code=200)
                return Response(status_code=404)
            return Response(status_code=400)
        except Exception as e:
            return Response("Ha ocurrido un error: {}".format(e), status_code=400)

    @staticmethod
    def to_html(rows):
        table = ''
        for row in rows:
            table += f'<tr> \
            <td class="text-left">CC-{row["cedula"]}</td> \
            <td class="text-left">{row["nombre"]}</td> \
            <td class="text-left">{row["apellido"]}</td> \
            <td class="text-left">{row["correo"]}</td> \
            <td class="text-left">{row["telefono"]}</td> \
            </tr>'
        return table
