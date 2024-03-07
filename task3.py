import csv


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as fh:
        field_names = ["name","email","phone","favorite"]
        writer = csv.DictWriter(fh, fieldnames=field_names)
        writer.writeheader()
        for dict in contacts:
            name = dict.get("name")
            email = dict.get("email")
            phone = dict.get("phone")
            favorite = dict.get("favorite") 
            writer.writerow({'name': name, "email": email, "phone": phone,"favorite": favorite })
    

def read_contacts_from_file(filename):
    contacts = []
    with open(filename, "r", newline='') as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            row["favorite"] = row["favorite"].lower() == "true"
            contacts.append(row)
    return contacts


            
      
# contacts = [{
#     "name": "Allen Raymond",
#     "email": "nulla.ante@vestibul.co.uk",
#     "phone": "(992) 914-3792",
#     "favorite": False,
# }, 
# {
#     "name": "Raymond",
#     "email": "nulla.ante@vestibul.co.uk",
#     "phone": "88814-3792",
#     "favorite": False,
# }]
filename = "names.csv"
read_contacts_from_file(filename)        



        