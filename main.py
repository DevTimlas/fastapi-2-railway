from flask import Flask
import asyncio
import uvicorn
import os
import hypercorn
from hypercorn.config import Config
from hypercorn.asyncio import serve

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from sse_starlette.sse import EventSourceResponse

starlette_app = Starlette()

@starlette_app.route('/api/data')
async def get_data(request):
    data = {'value': 42}
    return JSONResponse(data)


async def app(scope, receive, send):
    await starlette_app(scope, receive, send)
    


@starlette_app.route('/sse')
async def sse(request):
    async def event_generator():
        for i in range(5):
            yield {'event': 'message', 'data': 'Hello {}'.format(i)}
            await asyncio.sleep(1)

    return EventSourceResponse(event_generator())


if __name__ == '__main__':
	config = Config()
	config.bind = ["0.0.0.0:$PORT"]
	asyncio.run(serve(app, config))

