from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import json

app = FastAPI(title="Roman History Facts API")
from fastapi.responses import JSONResponse
from starlette.requests import Request

@app.middleware("http")
async def enforce_utf8(request: Request, call_next):
    response = await call_next(request)
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("roman_history_condensed.json", encoding="utf-8") as f:
    facts = {entry["date"]: entry["fact"] for entry in json.load(f)}

@app.get("/today")
def get_today_fact():
    today = datetime.utcnow().strftime("%m-%d")
    return {"date": today, "fact": facts.get(today, "No fact found.")}

@app.get("/fact")
def get_fact(date: str):
    if date not in facts:
        raise HTTPException(status_code=404, detail="Fact not found for this date.")
    return {"date": date, "fact": facts[date]}
