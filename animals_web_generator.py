import json


# file paths
HTML_TEMPLATE_FILE = "animals_template.html"
JSON_DATA_FILE = "animals_data.json"
HTML_OUTPUT_FILE = "animals.html"


def read_template(file_path):
    """Returns the content of the template file as string"""
    with open(file_path, "r") as handle:
        return handle.read()


def create_html_string():
    """
    Reads the template file and replaces the placeholder
    text with the generated html code
    """
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

    data_string = ""

    for animal in animals_data:
        data_string += serialize_animal(animal)

    return data_string


def serialize_animal(animal):
    """wraps data retrieved from a single object in html code"""
    data_string = ""
    # add html and data to output string
    data_string += "\t" * 3 + '<li class="cards__item">\n'
    data_string += (
        "\t" * 4 + f'<div class="card__title">{animal.get("name")}</div>\n'
    )
    data_string += "\t" * 5 + '<div class="card__text">\n' + "\t" * 6 + "<ul>\n"
    data_string += (
        "\t" * 7
        + "<li><strong>Scientific Name:</strong> "
        + {animal.get('taxonomy').get('scientific_name')}
        + "</li>\n"
    )
    if animal.get("characteristics").get("diet") is not None:
        data_string += (
            "\t" * 7
            + "<li><strong>Diet:</strong> "
            + {animal.get('characteristics').get('diet')}
            + "</li>\n"
        )
    data_string += (
        "\t" * 7
        + f"<li><strong>Location(s):</strong> {animal.get('locations')[0]}"
    )
    for i in range(1, len(animal.get("locations"))):
        data_string += f", {animal.get('locations')[i]}"
    data_string += "</li>\n"
    if animal.get("characteristics").get("weight") is not None:
        data_string += (
            "\t" * 7
            + "<li><strong>Weight:</strong> "
            + {animal.get('characteristics').get('weight')}
            + "</li>\n"
        )
    if animal.get("characteristics").get("type") is not None:
        data_string += (
            "\t" * 7
            + "<li><strong>Type:</strong> "
            + {animal.get('characteristics').get('type')}
            + "</li>\n"
        )
    if animal.get("characteristics").get("temperament") is not None:
        data_string += (
            "\t" * 7
            + "<li><strong>Temperament:</strong> "
            + {animal.get('characteristics').get('temperament')}
            + "</li>\n"
        )
    if animal.get("characteristics").get("slogan") is not None:
        data_string += (
            "\t" * 7
            + "<li><strong>Slogan:</strong> "
            + {animal.get('characteristics').get('slogan')}
            + "</li>\n"
        )
    data_string += (
        "\t" * 6 + "</ul>\n" + "\t" * 5 + "</div>\n" + "\t" * 4 + "</li>\n"
    )

    return data_string


def main():
    """
    Reads a template html file, adds html derived form json data
    and writes the result to new file.
    """
    write_html(HTML_OUTPUT_FILE, create_html_string())


if __name__ == "__main__":
    main()
