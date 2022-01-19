from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)


def get_state_on_switches(n: int) -> list:
    switches = [True for z in range(n)]
    for i in range(1, n + 1):
        for j, item in enumerate(switches):
            if (j+1) % i == 0:
                switches[j] = False if switches[j] else True
    return [j + 1 for j, item in enumerate(switches) if not item]


@app.get("/state_on_switches")
async def state_on_switches(num: int):
    return {"message": get_state_on_switches(num)}
