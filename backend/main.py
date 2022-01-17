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
    days_absence: List[int]
    bonus: int


def get_bonus_list(days_absence: list, bonus: int) -> list:
    employees = len(days_absence)
    ABC = 1
    down = 0
    for i in range(employees):
        ABC = ABC * days_absence[i]
    for i in range(employees):
        down = down + ABC/days_absence[i]
    return [(ABC*bonus)/(down*days_absence[i]) for i in range(employees)]


@app.post("/bonus_list")
async def bonus_list(user_request: UserRequest):
    return {"message": get_bonus_list(user_request.days_absence, user_request.bonus)}
