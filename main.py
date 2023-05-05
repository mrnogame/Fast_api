from fastapi import FastAPI
from models import User, Gender,Role
from typing import List
from uuid import UUID ,uuid4


app= FastAPI()



db: List[User] = [
    User(
         id=UUID("22ced1d5-5fda-4b17-9923-c50f40e0f0e6"),
         first_name = "Jamila",  
         last_name = "Ahmed",
         gender = Gender.female,
         roles = [Role.student]
          ),
    User(
         id=UUID("d2437a9f-2f92-48b0-b089-75aad27e135a"),
         first_name = "Alex",  
         last_name = "Jones",
         gender = Gender.male,
         roles = [Role.admin, Role.user]
         ),
]
@app.get("/")
def root():
    return{"Hello":"World"}       

@app.get("/api/v1/users")
async def fetch_users():
    return db,

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return{"id":user.id}


