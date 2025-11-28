import requests
import os
from dotenv import load_dotenv

# using .env file for environment variables
load_dotenv()

# file paths, constants and environment variables
URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = os.getenv("API_KEY")
HEADERS = {"X-Api-Key": API_KEY}


def fetch_data(search_string):
    """Returns the data from the animal api as list"""
    parameter = {"name": search_string}

    response = requests.get(URL, headers=HEADERS, params=parameter)

    return response.json()
