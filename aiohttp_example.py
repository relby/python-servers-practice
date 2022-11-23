import aiohttp
from aiohttp import web

API_URL = 'https://jsonplaceholder.typicode.com/users/{id}'


async def users_handler(request):
    user_id = request.match_info.get('user_id')
    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL.format(id=user_id)) as response:
            body = await response.json()

    return web.json_response(body)

app = web.Application()
app.add_routes([
    web.get(r'/users/{user_id:\d+}', users_handler),
])

if __name__ == '__main__':
    web.run_app(app)
