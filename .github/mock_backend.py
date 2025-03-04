from datetime import datetime, timedelta
from fastapi import FastAPI, Request, Response, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

FRONTEND_URL = "http://localhost:8088"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.post("/api/v1/move")
async def move(request: Request):
    return JSONResponse({
        "health": 3,
        "current_position": [1, 5]
    })

@app.get("/api/v1/reset")
async def reset_game(response: Response, username: str):
    return JSONResponse({
        "current_position": [1, 0]
    })

@app.post("/api/v1/login")
async def login(request: Request, response: Response):
    return JSONResponse({})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
