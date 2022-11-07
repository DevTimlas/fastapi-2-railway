from fastapi import FastAPI, File, UploadFile
import json

app = FastAPI(debug=True)

jso = "database.json"

@app.get("/")
async def root():
	json_data = json.loads(open(jso).read())
	return json_data
