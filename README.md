
# ZootopiaWithAPI

Generates an HTML page after entering a search term for an animal name on the command line. The data is fetched from the [Animal API](https://api-ninjas.com/api/animals) at API Ninjas. 

Install by executing in a terminal 
``
git clone https://github.com/nesmomik/ZootopiaWithAPI.git
``

Change into the directory with 
``
cd ZootopiaWithAPI
``

For the script to work a free API key from API Ninjas is required. Please create a
``
.env
``
in the program directory and add your API key like in the following example 
``
API_KEY = 'your_secret_key'
``

Also please install the dependencies with
``
pip install -r requirements.txt 
``
or
``
uv add -r requirements.txt 
``

Then you can start generating html file with 
``
python snowman.py
``
The html file is created in the same directory with the name
``
animals.html
``

Enjoy!