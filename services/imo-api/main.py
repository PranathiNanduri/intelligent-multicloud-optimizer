from fastapi import FastAPI
import os, time
from prometheus_fastapi_instrumentator import Instrumentator
app = FastAPI()
@app.get("/hello")
def hello(): return {"msg":"imo-api","pod":os.getenv("HOSTNAME",""),"ts":time.time()}
@app.on_event("startup")
async def _start(): Instrumentator().instrument(app).expose(app)
