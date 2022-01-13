import math

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)

def is_square_part(area: int):
    length = math.sqrt(area)
    if length - int(length) != 0:
        return False
    else:
        return True


@app.get("/square")
async def root(area: int):
    return {"result": is_square_part(area)}



