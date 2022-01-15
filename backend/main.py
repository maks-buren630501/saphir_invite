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


def get_sorted_unique_list(list_nums: list):
    return sorted(list(set(list_nums)))


def get_simple_progression_num(list_nums: list) -> int:
    n = 0
    for i in range(len(list_nums)):
        for j in range(i + 1, len(list_nums)):
            diff = list_nums[j] - list_nums[i]
            if list_nums[j] + diff in list_nums:
                n=n+1
                print(list_nums[i], list_nums[j], list_nums[j] + diff)
    return n


@app.post("/progression")
async def root(user_request: UserRequest):
    return {"num": get_simple_progression_num(get_sorted_unique_list(user_request.list_nums))}
