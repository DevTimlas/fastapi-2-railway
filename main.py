from fastapi import FastAPI, File, UploadFile
import json
import os
import uvicorn

app = FastAPI()

jso = "database.json"

@app.get("/")
async def root():
	json_data = json.loads(open(jso).read())
	return json_data
	
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT", default=5000), log_level="info")
