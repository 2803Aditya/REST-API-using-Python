# Python Image for our container
from python:3.8.0-buster

# Make a directory for our application
WORKDIR /app

# Create copy of requirements.txt file in current work directory
copy requirements.txt .

# pip install all the required libraries/dependencies
Run pip install -r requirements.txt

# Copy our source code
copy . /app 

# Run the application
CMD [ "python", "Flask_RestAPI.py" ]