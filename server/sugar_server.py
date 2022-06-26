# uvicorn sugar_server:app --reload

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.task import repeat_every
from pydantic import BaseModel

from server import handler
from server.routes.sugar import router as RuggerRouter


class SignedMsg(BaseModel):
    msg: str
    signature: str


app = FastAPI()

origins = [
    "http://127.0.0.1:8000",
    "*"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(RuggerRouter, tags=["Rugger"], prefix="/rugger")


@app.post("/prove")
async def prove(s: SignedMsg):
    result = await handler.prove(s.msg, s.signature)
    return result



