import asyncio
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from handlers import routers

app = FastAPI()

for router in routers:
    app.include_router(router)


class Person(BaseModel):
    name: str | None = None
    age: int



@app.get(
        "/person",
        description="Get Hello",
        response_model=Person
        )
def get_person():
    return Person(name="Helo", age="25")

""" async def get_users():
    await asyncio.sleep(3)
    return

async def get_wiki():
    await asyncio.sleep(3)
    return """


@app.post(
        "/person",
        description="Create Hello",
        response_model=Person,
        response_model_exclude_none=True
        )
def create_person(person: Person):
    #users = await get_users()
    #wiki = await get_wiki()
    return person

