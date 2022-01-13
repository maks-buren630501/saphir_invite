from fastapi import FastAPI

app = FastAPI()


def get_state_on_switches(n: int) -> list:
    switches = [True for i in range(n)]
    for i in range(1, n+1):
        for j, item in enumerate(switches):
            if (j+1) % i == 0:
                switches[j] = False if switches[j] else True
    return [i+1 for i, item in enumerate(switches) if not item]


@app.get("/state_on_switches")
async def state_on_switches(num: int):
    return {"message": get_state_on_switches(num)}
