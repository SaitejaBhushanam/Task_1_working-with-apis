from fastapi import FastAPI
import typing
from pydantic import BaseModel
import json
from fastapi.middleware.cors import CORSMiddleware


emp_db = [{"id": 1, "email": "george.bluth@reqres.in", "first_name": "George", "last_name": "Bluth", "avatar": "https://reqres.in/img/faces/1-image.jpg"}, {"id": 2, "email": "janet.weaver@reqres.in", "first_name": "Janet", "last_name": "Weaver", "avatar": "https://reqres.in/img/faces/2-image.jpg"}, {"id": 3, "email": "emma.wong@reqres.in", "first_name": "Emma", "last_name": "Wong", "avatar": "https://reqres.in/img/faces/3-image.jpg"}, {"id": 4, "email": "eve.holt@reqres.in", "first_name": "Eve", "last_name": "Holt", "avatar": "https://reqres.in/img/faces/4-image.jpg"}, {"id": 5, "email": "charles.morris@reqres.in", "first_name": "Charles", "last_name": "Morris", "avatar": "https://reqres.in/img/faces/5-image.jpg"}, {"id": 6, "email": "tracey.ramos@reqres.in", "first_name": "Tracey", "last_name": "Ramos", "avatar": "https://reqres.in/img/faces/6-image.jpg"}, {"id": 7,"email": "michael.lawson@reqres.in", "first_name": "Michael", "last_name": "Lawson", "avatar": "https://reqres.in/img/faces/7-image.jpg"}, {"id": 8, "email": "lindsay.ferguson@reqres.in", "first_name": "Lindsay", "last_name": "Ferguson", "avatar": "https://reqres.in/img/faces/8-image.jpg"}, {"id": 9, "email": "tobias.funke@reqres.in", "first_name": "Tobias", "last_name": "Funke", "avatar": "https://reqres.in/img/faces/9-image.jpg"}, {"id": 10, "email": "byron.fields@reqres.in", "first_name": "Byron", "last_name": "Fields", "avatar": "https://reqres.in/img/faces/10-image.jpg"}, {"id": 11, "email": "george.edwards@reqres.in", "first_name": "George", "last_name": "Edwards", "avatar": "https://reqres.in/img/faces/11-image.jpg"}, {"id": 12, "email": "rachel.howell@reqres.in", "first_name": "Rachel", "last_name": "Howell", "avatar": "https://reqres.in/img/faces/12-image.jpg"}]

origins = ["*"]



class Respond(BaseModel):
    id:int
    email:str
    first_name:str
    last_name:str

tags=[
    {"name":"Get data","description":"Get all employees data","url": "https://fastapi.tiangolo.com/"},
    {"name":"create Employee","description":"Create an EMployee by providinig the respective fields","url": "https://fastapi.tiangolo.com/"}
]


task2_app=FastAPI(
    title="Employee Api",
    description="We can create almost all the operations present on an Employee DB",
    version="0.1.1",
    license_info={
        "name": "Apache",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    contact={
        "name":"Sai",
        "email":"saihdusgv@gmail.com",
    },
    openapi_tags=tags,
    docs_url="/empdocs",
    redoc_url=None

)

task2_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@task2_app.get("/", tags=["Get Employees Details"])
async def get_objects():
    return emp_db

@task2_app.post("/createEmplyee", response_model=Respond, tags=["CreateEmployee"])
def Employee(id: int,email: str,first_name: str,last_name: str,avatar: str):
    new_dict={}
    new_dict["id"]=id
    new_dict["email"]=email
    new_dict["first_name"]=first_name
    new_dict["last_name"]=last_name
    new_dict["avatar"]=avatar

    return new_dict