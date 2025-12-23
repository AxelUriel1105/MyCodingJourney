from fastapi import FastAPI, HTTPException
from uuid import uuid4 as uuid #Nos permite generar id's únicos y uuid4 aleatorios
from src.repositories.managedb import ManageDb
from pydantic import BaseModel

class ContactModel(BaseModel):
    id: str = str(uuid())
    name: str
    phone: str
app = FastAPI()
md = ManageDb()

@app.get("/")
def root():
    return {'message': 'Hi, I am FastAPI'}

@app.get("/api/contacts")
def get_all_contacts():
    return md.read_contacts()

@app.get("/api/contacts/{id_contact}")
def get_single_contact(id_contact:str):
    contacts = md.read_contacts()
    for contact in contacts:
        if contact["id"] == id_contact:
            return contact
    raise HTTPException(status_code=404, detail="Contact not found")

@app.post('/api/contacts')
def add_contact(new_contact: ContactModel):
    contacts = md.read_contacts()
    new_contact = new_contact.model_dump()
    contacts.append(new_contact)
    md.write_contact(contacts)

    return {"success": True,
            "message": "Add new contact"}

@app.put("/api/contacts/{id_contact}")
def update_contact(id_contact:str, new_contact:ContactModel):
    contacts = md.read_contacts()
    
    for index, contact in enumerate(contacts):
        if contact["id"] == id_contact:
            contacts[index] = new_contact.model_dump()
            if new_contact.name == "":
                contacts[index]["name"] = contact["name"]
            if new_contact.phone =="":
                contacts[index]["phone"] = contact["phone"]
            md.write_contact(contacts)
            return {
                "success": True,
                "message": "update contact"
                }
    raise HTTPException(status_code=404, detail="contact not found")

@app.delete("/api/contact/{id_contact}")
def remove_contact(id_contact):
    contacts = md.read_contacts()

    for index, contact in enumerate(contacts):
        if contact["id"] == id_contact:
            contacts.pop(index)
            md.write_contact(contacts)
            return {
                "success": True,
                "message": "Delete contact"
            }
    return HTTPException(status_code=404, detail="contact not found")
    
    