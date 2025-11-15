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
    """Creates and returns a string from the data"""
    animals_data = load_data(JSON_DATA_FILE)

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
    write_html(HTML_OUTPUT_FILE, create_html_string())

if __name__ == "__main__":
    main()
