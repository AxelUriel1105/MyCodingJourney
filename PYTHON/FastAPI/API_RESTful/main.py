from fastapi import FastAPI
from src.lib.managedb import ManageDb
app = FastAPI()
md = ManageDb()
@app.get("/")
def root():
    return {'message': 'Hi, I am FastAPI'}

@app.get("/api/contacts")
def get_all_contacts():
    