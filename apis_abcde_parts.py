from fastapi import FastAPI
import typing
from pydantic import BaseModel
import json


app1 = FastAPI()  # creating an object of Fastapi
# path params GET

emp_db = [{"id": 1, "email": "george.bluth@reqres.in", "first_name": "George", "last_name": "Bluth", "avatar": "https://reqres.in/img/faces/1-image.jpg"}, {"id": 2, "email": "janet.weaver@reqres.in", "first_name": "Janet", "last_name": "Weaver", "avatar": "https://reqres.in/img/faces/2-image.jpg"}, {"id": 3, "email": "emma.wong@reqres.in", "first_name": "Emma", "last_name": "Wong", "avatar": "https://reqres.in/img/faces/3-image.jpg"}, {"id": 4, "email": "eve.holt@reqres.in", "first_name": "Eve", "last_name": "Holt", "avatar": "https://reqres.in/img/faces/4-image.jpg"}, {"id": 5, "email": "charles.morris@reqres.in", "first_name": "Charles", "last_name": "Morris", "avatar": "https://reqres.in/img/faces/5-image.jpg"}, {"id": 6, "email": "tracey.ramos@reqres.in", "first_name": "Tracey", "last_name": "Ramos", "avatar": "https://reqres.in/img/faces/6-image.jpg"}, {"id": 7,"email": "michael.lawson@reqres.in", "first_name": "Michael", "last_name": "Lawson", "avatar": "https://reqres.in/img/faces/7-image.jpg"}, {"id": 8, "email": "lindsay.ferguson@reqres.in", "first_name": "Lindsay", "last_name": "Ferguson", "avatar": "https://reqres.in/img/faces/8-image.jpg"}, {"id": 9, "email": "tobias.funke@reqres.in", "first_name": "Tobias", "last_name": "Funke", "avatar": "https://reqres.in/img/faces/9-image.jpg"}, {"id": 10, "email": "byron.fields@reqres.in", "first_name": "Byron", "last_name": "Fields", "avatar": "https://reqres.in/img/faces/10-image.jpg"}, {"id": 11, "email": "george.edwards@reqres.in", "first_name": "George", "last_name": "Edwards", "avatar": "https://reqres.in/img/faces/11-image.jpg"}, {"id": 12, "email": "rachel.howell@reqres.in", "first_name": "Rachel", "last_name": "Howell", "avatar": "https://reqres.in/img/faces/12-image.jpg"}]

class Response(BaseModel):
    id:int
    email:str
    first_name:str
    last_name:str

@app1.get("/")  # root path
async def root():
    return emp_db

# path params get


@app1.get("/employee/{id_search}")  # accepts only integer
async def user(id_search: int):
    for item in emp_db:
        if item.get("id") == id_search:
            return item
    else:
        return "no employee found"

# @app1.get("/path/{filepath}")
# async def fileloc(filepath : str):
#     return filepath

# Query params GET


@app1.get("/search/")
async def search(id: int = 0):
    for item in emp_db:
        if item.get("id") == id:
            return item
    else:
        return "no employee found"

# Request schema Post

class Employee(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


@app1.post("/create_employee/", response_model=Response)
async def create(emp: Employee ):

    input_emp_json = emp.json()
    input_dict = json.loads(input_emp_json)
    emp_db.append(input_dict)
    return emp_db

# Query params post
@app1.post("/createEmployee")
def createEmployee(id: int,email: str,first_name: str,last_name: str,avatar: str):
    new_dict={}
    new_dict["id"]=id
    new_dict["email"]=email
    new_dict["first_name"]=first_name
    new_dict["last_name"]=last_name
    new_dict["avatar"]=avatar

    return new_dict

# Delete using Query params
@app1.delete("/deleteEmployee")
def deleteEmployee(id: int):
    for index,item in enumerate(emp_db):
        if(item["id"]==id):
            return emp_db.pop(index)

    else:
        return "Object Not Found"

    






        




