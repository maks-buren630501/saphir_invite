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

def get_sum_list(num: int) -> list:
    cube = math.pow(num, 3)
    result = []
    a1 = int(cube/3)
    for i in range(a1-2, a1+3, 2):
        result.append(i)
    return result


@app.get("/sum_list")
async def sum_list(num: int):
    return {"message": get_sum_list(num)}