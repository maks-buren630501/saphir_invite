from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)


def get_state_on_switches(n: int) -> list:
    i=1
    switches = list()
    while (i*i)<=n:
        switches.append(i*i)
        i+=1
    return switches


@app.get("/state_on_switches")
async def state_on_switches(num: int):
    return {"message": get_state_on_switches(num)}
