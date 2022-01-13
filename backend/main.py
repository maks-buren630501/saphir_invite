import math

from fastapi import FastAPI

app = FastAPI()


def is_square_part(area: int):
    length = math.sqrt(area)
    if length - int(length) != 0:
        return False
    else:
        return True


@app.get("/square")
async def root(area: int):
    return {"result": is_square_part(area)}



