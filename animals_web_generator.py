import json


def load_data(file_path):
    """Returns the date from the json file as dict"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def read_template(file_path):
    """Returns the content of the template file as string"""
    with open(file_path, "r") as handle:
        return handle.read()
        

def format_data():
    """ Creates and returns a string from the data"""
    animals_data = load_data("animals_data.json")

    data_string = ""

    for animal in animals_data:
        data_string += f"Name: {animal.get('name')}\n"
        if animal.get("characteristics").get("diet") is not None:
            data_string += f"Diet: {animal.get('characteristics').get('diet')}\n"
        data_string += f"Location: {animal.get('locations')[0]}\n"
        if animal.get("characteristics").get("type") is not None:
            data_string += f"Type: {animal.get('characteristics').get('type')}\n"
    
    return data_string
    

def main():

    print(format_data())
    print(read_template("animals_template.html"))


if __name__ == "__main__":
    main()
