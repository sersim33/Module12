import pickle


def write_contacts_to_file(filename, contacts):
    
    file_name = 'data.bin'

    with open(file_name, "wb") as fh:
        pickle.dump(filename, contacts, fh)
        


def read_contacts_from_file(filename):
    with open(filename, "rb") as fh:
        unpacked = pickle.load(fh)