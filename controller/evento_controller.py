from starlette.requests import Request
from starlette.responses import HTMLResponse, Response, JSONResponse
from starlette.endpoints import HTTPEndpoint

from model.evento_model import EventoModel
from env import response_type


class EventoController(HTTPEndpoint):

    async def get(self, request: Request):
        try:
            id = request.path_params.get('id')
            if id:
                evento = EventoModel.find_one(id)
                if evento is None:
                    return Response(status_code=404)
                return JSONResponse(evento.to_dict())
            
            response = EventoModel.find()
            if response_type == 'json':
                return JSONResponse(response)
            return HTMLResponse(EventoController.to_html(response)) if response else Response(status_code=404)
        except Exception as e:
            return Response("Ha ocurrido un error: {}".format(e), status_code=400)

    async def post(self, request: Request):
        try:
            body = await request.json()
            evento = EventoModel(**body)
            evento.save()
            return Response(status_code=201)
        except Exception as e:
            return Response("Ha ocurrido un error: {}".format(e), status_code=400)

    async def put(self, request: Request):
        try:
            body = await request.json()
            id = request.path_params.get('id')
            if id:
                evento = EventoModel.find_one(id)
                if evento:
                    evento.update(**body)
                    return Response(status_code=200)
                return Response(status_code=404)
            return Response(status_code=400)
        except Exception as e:
            return Response("Ha ocurrido un error: {}".format(e), status_code=400)

    async def delete(self, request: Request):
        try:
            id = request.path_params.get('id')
            if id:
                evento = EventoModel.find_one(id)
                if evento:
                    evento.delete()
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
            <td class="text-sm-left text-center">E-{row["codigo"]}</td> \
            <td class="text-sm-left text-center">{row["fecha"]}</td> \
            <td class="text-sm-left text-center">{row["duracion"]} horas</td> \
            <td class="text-left">{row["objetivo"]}</td> \
            <td></td></tr>'
        return table
