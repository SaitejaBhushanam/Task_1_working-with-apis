from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel,EmailStr
import json

App=FastAPI()

class Login(BaseModel):
    Name:str
    Age:int
    email:EmailStr
    password:str
    gender:Optional[str]=None

class Login_show(BaseModel):
    Name:str
    email:EmailStr
    Age:int
    gender:Optional[str]=None


@App.post("/Login",response_model=Login_show, response_model_exclude_unset=True)
async def login(login:Login):
    return login

