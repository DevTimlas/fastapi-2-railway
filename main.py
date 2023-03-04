from fastapi import FastAPI, File, UploadFile
import json
import os
import asyncio
import uvicorn
from fastapi import FastAPI, Request
from sse_starlette.sse import EventSourceResponse
import hypercorn
from hypercorn.config import Config
from hypercorn.asyncio import serve

app = FastAPI()

jso = "./database.json"

@app.get("/")
async def root():
	json_data = json.loads(open(jso).read())
	return json_data
	
if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port=os.getenv("PORT", default=5000), log_level="info")
	# config = Config()
	# config.bind = ["0.0.0.0:5000"]
	# asyncio.run(serve(app, config))
"""

@app.get("/")
async def root():
	return {'he':'wrd'}

STREAM_DELAY = 1  # second
RETRY_TIMEOUT = 15000  # milisecond

@app.get('/stream')
async def message_stream(request: Request):
    def new_messages():
        # Add logic here to check for new messages
        yield 'Hello World'
    async def event_generator():
        while True:
            # If client closes connection, stop sending events
            if await request.is_disconnected():
                break

            # Checks for new messages and return them to client if any
            if new_messages():
            	out = {
		                    "event": "new_message",
		                    "id": "message_id",
		                    "retry": RETRY_TIMEOUT,
		                    "data": "message_content"
		            }
            	# for a, b in test():
            		# out["Test"] = a
            		# out['buy/sell'] = b
            	
            	yield out 

            await asyncio.sleep(STREAM_DELAY)

    return EventSourceResponse(event_generator())
    
if __name__ == '__main__':
	config = Config()
	config.bind = ["0.0.0.0:5000"]
	asyncio.run(serve(app, config))
"""
