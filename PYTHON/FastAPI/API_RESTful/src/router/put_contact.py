from fastapi import HTTPException
from src.repositories.managedb import ManageDb

def put_contact(id_contact, new_contact):
    md = ManageDb()
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