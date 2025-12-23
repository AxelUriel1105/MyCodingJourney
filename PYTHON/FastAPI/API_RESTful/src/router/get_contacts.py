from src.repositories.managedb import ManageDb

def get_contacts():
    md = ManageDb()
    return md.read_contacts()
 