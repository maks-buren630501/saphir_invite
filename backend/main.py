from fastapi import FastAPI

app = FastAPI()


def get_factorial(n: int):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def get_factorial_length(factorial: int):
    return len(str(factorial))


@app.get("/factorial_size")
async def factorial_size(num: int):
    return {"result": get_factorial_length(get_factorial(num))}
