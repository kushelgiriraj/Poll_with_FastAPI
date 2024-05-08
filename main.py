import datetime
from typing import List

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel

import databases
from sqlalchemy import engine_from_config, pool
from sqlalchemy.orm import Session
from alembic import context

from db.models import models
from db.db import SessionLocal, engine

from logging.config import fileConfig


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def fetch_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


class User(BaseModel):
    username: str
    email: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


class UserCreate(BaseModel):
    username: str
    email: str


class Poll(BaseModel):
    title: str
    type: str
    is_add_choices_active: bool
    is_voting_active: bool
    created_by: int
    created_at: datetime.datetime
    updated_at: datetime.datetime


def create_new_user(db: Session, user: UserCreate):
    db_user = models.User(email=user.email, username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}

    
@app.get("/polls")
async def root():
    return {"polls": "Hello World"}


@app.get("/users/", response_model=List[User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = fetch_users(db, skip=skip, limit=limit)
    return users


@app.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)  # Check if the user already exists
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Call the db function to create the user
    return create_new_user(db=db, user=user)


@app.post("/polls/")
async def create_poll(poll: Poll):
    return poll