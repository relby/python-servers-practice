import httpx
from fastapi import FastAPI

API_URL = 'https://jsonplaceholder.typicode.com/users/{id}'

app = FastAPI()


@app.get('/users/{id}')
async def users_handler(user_id: int):
    async with httpx.AsyncClient() as client:
        return (await client.get(API_URL.format(id=user_id))).json()
