# REST API with flask and JWT Authentication

This is a simple CRUD API application made with flask that uses JWT Authentication and Authorization for described endpoints.

## Usage

```python
# clone repo
git clone 

# go to repo
cd <path-to-my-project>

# create virtual env
python -m venv venv

# activate virtual env (Linux/Mac)
source venv/bin/activate

# activate virtual env (Windows)
venv\Scripts\activate.bat or venv\Scripts\Activate.ps1

# install packages
pip install -r requirements.txt

# run the application
python app.py

# open application in you browser with next address
http://localhost:5000
```

## API Endpoints

- http://localhost:5000/signup
- http://localhost:5000/login (to get a token you must provide email and password in json)
- http://localhost:5000/address (use GET method to get list of addresses or use POST to create new one)
- http://localhost:5000/address/id (you can use this endpoint to update, delete, or get an address. "id" is an integer and index of an address)