import json

def load_data(file_path):
    """ Loads a json file """
    with open(file_path, "r") as handle:
        return json.load(handle)

 
def main():
    animals_data = load_data('animals_data.json')

    for animal in animals_data:
        print(animal)
        print(f"Name: {animal.get('name')}")
        if animal.get('characteristics').get('diet') is not None:
            print(f"Diet: {animal.get('characteristics').get('diet')}")
        print(f"Location: {animal.get('locations')[0]}")
        if animal.get('characteristics').get('type') is not None:
            print(f"Type: {animal.get('characteristics').get('type')}")

if __name__ == "__main__":
    main()