import pathlib 
import json
class ManageDb:
    __address_file = "{}/src/db/dbContacts.json".format(pathlib.Path().absolute())
    
    def read_contacts(self):
        with open(self.__address_file, "r") as data:
            return json.loads(data.read())
    
    def write_contact(self, new_contact):
        with open(self.__address_file, "w",) as data:
            data.write(json.dumps(new_contact))
