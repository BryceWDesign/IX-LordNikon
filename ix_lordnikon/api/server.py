"""
IX-LordNikon REST API

Exposes the sync engine and memory map for external diagnostic tools,
timeline inspection, and anomaly detection from outside the AI core.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from core.sync_engine import SyncEngine

app = FastAPI()
engine = SyncEngine()

class EventIngest(BaseModel):
    source: str
    payload: str

@app.post("/nikon/ingest")
async def ingest_event(event: EventIngest):
    try:
        hashcode = engine.ingest_event(event.source, event.payload)
        return {"status": "OK", "hash": hashcode}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/nikon/recent")
async def recent_logs():
    return {"recent": engine.recent_log()}

@app.get("/nikon/drift")
async def drift_check():
    drift = engine.detect_drift()
    return {"drift_detected": drift}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8086)
