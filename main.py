from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Users(BaseModel):
    user_name: str
    email: str
    user_id: int 
    # created_at: float
    # updated_at: float


class Poll(BaseModel):
    title: str
    type: str
    is_add_choices_active: bool
    is_voting_active: bool
    # created_by: str | None


@app.get("/")
async def root():
    return {"message": "Hello, Welcome to Poll with FastAPI"}


@app.get("/users/")
async def get_users():
    return {"message": "Hello, Users"}


@app.post("/users/")
async def create_users(user: Users):
    return {"user": user}

@app.post("/poll/")
async def create_poll(poll: Poll):
    return {"poll": poll}