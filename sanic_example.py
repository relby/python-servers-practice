import httpx
from sanic import Sanic
from sanic.request import Request
from sanic.response import HTTPResponse, json

API_URL = 'https://jsonplaceholder.typicode.com/users/{id}'

app = Sanic('users-app')


@app.get('/users/<user_id:int>')
async def users_handler(request: Request, user_id: int) -> HTTPResponse:
    async with httpx.AsyncClient() as client:
        body = (await client.get(API_URL.format(id=user_id))).json()
        return json(body)
