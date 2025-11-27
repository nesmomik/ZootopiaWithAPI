import requests

# file paths
HTML_TEMPLATE_FILE = "animals_template.html"
JSON_DATA_FILE = "animals_data.json"
HTML_OUTPUT_FILE = "animals.html"
url = "https://api.api-ninjas.com/v1/animals"
headers = {"X-Api-Key": "67XSw+kVd+LqaXn6YnT+/A==msznqu2bNvMGW8JI"}


def read_template(file_path):
    """Returns the content of the template file as string"""
    with open(file_path, "r") as handle:
        return handle.read()


def create_html_string(search_string):
    """
    Reads the template file and replaces the placeholder
    text with the generated html code
    """
    return read_template(HTML_TEMPLATE_FILE).replace(
        "__REPLACE_ANIMALS_INFO__", format_data(search_string)
    )


def write_html(file_path, html_string):
    """Returns the content of the template file as string"""
    with open(file_path, "w") as handle:
        handle.write(html_string)


def load_data(search_string):
    """Returns the data from the animal api as list"""
    parameter = {"name": search_string}

    response = requests.get(url, headers=headers, params=parameter)

    return response.json()


def format_data(search_string):
    """Aggregates and returns a string from the data"""
    animals_data = load_data(search_string)

    data_string = ""

    if animals_data:
        for animal in animals_data:
            data_string += serialize_animal(animal)
    else:
        data_string += serialize_no_animal(search_string)

    return data_string


def serialize_no_animal(search_string):
    data_string = ""
    data_string += "\t" * 3 + '<li class="cards__item">\n'
    data_string += '<div id="noresults">'
    data_string += f"<h2>Sorry, no results for input {search_string}.</h2>"
    data_string += '<img src="no_results.jpg" alt="November rain.">'
    data_string += "</div>"
    data_string += "</li>\n"

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
        + f"{animal.get('taxonomy').get('scientific_name')}"
        + "</li>\n"
    )
    if animal.get("characteristics").get("diet") is not None:
        data_string += (
            "\t" * 7
            + "<li><strong>Diet:</strong> "
            + f"{animal.get('characteristics').get('diet')}"
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
            + f"{animal.get('characteristics').get('weight')}"
            + "</li>\n"
        )
    if animal.get("characteristics").get("type") is not None:
        data_string += (
            "\t" * 7
            + "<li><strong>Type:</strong> "
            + f"{animal.get('characteristics').get('type')}"
            + "</li>\n"
        )
    if animal.get("characteristics").get("temperament") is not None:
        data_string += (
            "\t" * 7
            + "<li><strong>Temperament:</strong> "
            + f"{animal.get('characteristics').get('temperament')}"
            + "</li>\n"
        )
    if animal.get("characteristics").get("slogan") is not None:
        data_string += (
            "\t" * 7
            + "<li><strong>Slogan:</strong> "
            + f"{animal.get('characteristics').get('slogan')}"
            + "</li>\n"
        )
    data_string += (
        "\t" * 6 + "</ul>\n" + "\t" * 5 + "</div>\n" + "\t" * 4 + "</li>\n"
    )

    return data_string


def cli_interface():
    """
    Asks the user to input an animal name and then generates the html output
    """
    print("Welcome to the Animals Web Generator!")
    while True:
        try:
            print("Type an animal name to search for or press Ctrl+C to exit.")
            search_string = input()
        except KeyboardInterrupt:
            print("\nExiting.")
            break

        if search_string == "":
            print("You entered an empty string.")
        else:
            write_html(HTML_OUTPUT_FILE, create_html_string(search_string))
            print(f"Generated file: {HTML_OUTPUT_FILE}")


def main():
    """
    Calls the command line interface to search for animals which
    then generates a html file as result.
    """
    cli_interface()


if __name__ == "__main__":
    main()
