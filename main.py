import asyncio
from fastapi import FastAPI
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from sse_starlette.sse import EventSourceResponse
from starlette.responses import PlainTextResponse
import uvicorn
import os


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.route("/starlette")
async def starlette_endpoint(request):
    return PlainTextResponse("This is a Starlette endpoint!")


starlette_app = Starlette()

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
	uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT", default=5000), log_level="info")
