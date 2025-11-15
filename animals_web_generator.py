import json


HTML_TEMPLATE_FILE = "animals_template.html"
JSON_DATA_FILE = "animals_data.json"
HTML_OUTPUT_FILE = "animals.html"

def read_template(file_path):
    """Returns the content of the template file as string"""
    with open(file_path, "r") as handle:
        return handle.read()


def create_html_string():
    return read_template(HTML_TEMPLATE_FILE).replace(
        "__REPLACE_ANIMALS_INFO__", format_data()
    )


def write_html(file_path, html_string):
    """Returns the content of the template file as string"""
    with open(file_path, "w") as handle:
        handle.write(html_string)


def load_data(file_path):
    """Returns the date from the json file as dict"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def format_data():
    """Aggregates and returns a string from the data"""
    animals_data = load_data(JSON_DATA_FILE)

    data_string = ''

    for animal in animals_data:
        data_string += serialize_animal(animal)

    return data_string


def serialize_animal(animal):
    data_string = ''
    data_string += '<li class="cards__item">'
    data_string += f'<div class="card__title">{animal.get('name')}</div>\n'
    data_string += '<p class="card__text">'
    data_string += f"<strong>Scientific Name:</strong> {animal.get('taxonomy').get('scientific_name')}<br/>\n"
    if animal.get("characteristics").get("diet") is not None:
        data_string += f"<strong>Diet:</strong> {animal.get('characteristics').get('diet')}<br/>\n"
    data_string += f"<strong>Location(s):</strong> {animal.get('locations')[0]}"
    for i in range(1, len(animal.get('locations'))):
        data_string += f", {animal.get('locations')[i]}"
    data_string += "<br/>\n"
    if animal.get("characteristics").get("weight") is not None:
        data_string += f"<strong>Weight:</strong> {animal.get('characteristics').get('weight')}<br/>\n"
    if animal.get("characteristics").get("type") is not None:
        data_string += f"<strong>Type:</strong> {animal.get('characteristics').get('type')}<br/>\n"
    if animal.get("characteristics").get("temperament") is not None:
        data_string += f"<strong>Temperament:</strong> {animal.get('characteristics').get('temperament')}<br/>\n"
    if animal.get("characteristics").get("slogan") is not None:
        data_string += f"<strong>Slogan:</strong> {animal.get('characteristics').get('slogan')}<br/>\n"
    data_string += '</li>'
    
    return data_string


def main():
    write_html(HTML_OUTPUT_FILE, create_html_string())

if __name__ == "__main__":
    main()
