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
    midlValue = cube / num if (cube / num) % 2 else cube / num - 1
    step = math.floor(num / 2)
    result = [int(midlValue)]
    if num % 2:
        for i in range(step):
            result.append(int(midlValue + 2 * (i+1)))
            result.insert(0, int(midlValue - 2 * (i+1)))
    else:
        for i in range(step):
            result.append(int(midlValue + 2 * (i+1)))
            if i > 0:
                result.insert(0, int(midlValue - 2 * (i)))
    return result


@app.get("/sum_list")
async def sum_list(num: int):
    return {"result": get_sum_list(num)}
