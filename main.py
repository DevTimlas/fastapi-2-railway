from fastapi import FastAPI
from starlette.responses import PlainTextResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.route("/starlette")
async def starlette_endpoint(request):
    return PlainTextResponse("This is a Starlette endpoint!")
