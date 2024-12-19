from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.data.db import get_db

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/users/")
def create_user(user: dict, db: Session = Depends(get_db)):
    return {"username": user["username"], "email": user["email"]}

@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return {"user_id": user_id, "username": f"User{user_id}"}

@app.get("/users/")
def get_all_users(db: Session = Depends(get_db)):
    return [{"username": "John", "email": "john@example.com"}, {"username": "Jane", "email": "jane@example.com"}]