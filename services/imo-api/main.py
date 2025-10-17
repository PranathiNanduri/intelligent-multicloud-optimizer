from fastapi import FastAPI
import os
import time
from prometheus_fastapi_instrumentator import Instrumentator
app = FastAPI()
# Register Prometheus instrumentation BEFORE the app starts
Instrumentator().instrument(app).expose(app)  # exposes /metrics
@app.get("/hello")
def hello():
    return {"msg": "imo-api", "pod": os.getenv("HOSTNAME", ""), "ts": time.time()}
@app.get("/healthz")
def healthz():
    return {"status": "ok"}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", "8080")),
        reload=False,
    )

