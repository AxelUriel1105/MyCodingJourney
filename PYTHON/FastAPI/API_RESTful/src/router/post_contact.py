from src.repositories.managedb import ManageDb

def post_contact(new_contact):
    md = ManageDb()
    contacts = md.read_contacts()
    new_contact = new_contact.model_dump()
    contacts.append(new_contact)
    md.write_contact(contacts)

    return {"success": True,
            "message": "Add new contact"}