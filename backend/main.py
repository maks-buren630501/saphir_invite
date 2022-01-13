from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)


class UserRequest(BaseModel):
    list_nums: List[int]


def is_progressions(progression: list):
    if len(set([item - progression[i-1] for i, item in enumerate(progression) if i != 0])) > 0:
        return False
    else:
        return True


def get_sorted_unique_list(list_nums: list):
    return sorted(list(set(list_nums)))


def get_simple_progression_num(list_nums: list) -> int:
    n = 0
    temp_list = []
    for i, item in enumerate(list_nums):
        temp_list.append(item)
        if i % 3 == 0 and len(temp_list) > 0:
            n += 1 if is_progressions(temp_list) else 0
            temp_list = []
    return n


@app.post("/progression")
async def root(user_request: UserRequest):
    return {"num": get_simple_progression_num(get_sorted_unique_list(user_request.list_nums))}
