from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()

DATA_FILE = "data.json"


if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []
else:
    data = []


class User(BaseModel):
    name: str
    age: int

def get_next_id():
    return max([user["id"] for user in data], default=0) + 1

@app.get("/greet/{user_id}")
def greet(user_id: int):
    """Greet the user based on their saved ID."""
    user = next((item for item in data if item["id"] == user_id), None)
    if user:
        return {"message": f"Hello, {user['name']}! You are {user['age']} years old."}
    raise HTTPException(status_code=404, detail="User not found. Please save the user first!")

@app.post("/save_data")
def save_data(user: User): 
    new_entry = {"id": get_next_id(), "name": user.name, "age": user.age}
    data.append(new_entry)

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

    return {"message": "Data saved successfully", "data": new_entry}

@app.get("/get_saved_data")
def get_saved_data():
    return data
