from starlette.requests import Request
from starlette.responses import HTMLResponse, Response, JSONResponse
from starlette.endpoints import HTTPEndpoint

from model.inscripcion_model import InscripcionModel
from env import response_type


class InscripcionController(HTTPEndpoint):
    
    async def get(self, request: Request):
        id = request.path_params.get('id')
        if id:
            inscripcion = InscripcionModel.find_one(id)
            if inscripcion is None:
                return Response(status_code=404)
            return JSONResponse(inscripcion.to_dict())
        
        response = InscripcionModel.find()
        if response_type == 'json':
            return JSONResponse(response)
        return HTMLResponse(InscripcionController.to_html(response)) if response else Response(status_code=404)
    
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

    @staticmethod
    def to_html(rows):
        table = ''
        for row in rows:
            table += f'<tr><td></td> \
            <td class="text-sm-left text-center">IN-{row["codigo"]}</td> \
            <td class="text-sm-left text-center">G-{row["codigo_grupo"]}</td> \
            <td class="text-sm-left text-center">E-{row["codigo_evento"]}</td> \
            <td></td></tr>'
        return table
