from fastapi import FastAPI
from uuid import uuid4 as uuid #Nos permite generar id's únicos y uuid4 aleatorios
from pydantic import BaseModel

from src.router.get_contacts import get_contacts
from src.router.get_contact import get_contact
from src.router.post_contact import post_contact
from src.router.put_contact import put_contact
from src.router.delete_contact import delete_contact

class ContactModel(BaseModel):
    id: str = str(uuid())
    name: str
    phone: str
app = FastAPI()

@app.get("/")
def root():
    return {'message': 'Hi, I am FastAPI'}

@app.get("/api/contacts")
def get_all_contacts():
    return get_contacts()

@app.get("/api/contacts/{id_contact}")
def get_single_contact(id_contact:str):
    return get_contact(id_contact)

@app.post('/api/contacts')
def add_contact(new_contact: ContactModel):
    return post_contact(new_contact)

@app.put("/api/contacts/{id_contact}")
def update_contact(id_contact:str, new_contact:ContactModel):
    return put_contact(id_contact, new_contact)

@app.delete("/api/contact/{id_contact}")
def remove_contact(id_contact:str):
    return delete_contact(id_contact)
    
    