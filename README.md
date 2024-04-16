# FastAPI Video Ask Service

## Description
This project provides endpoints to manage video asks using FastAPI.

## Installation
```
git clone https://github.com/imadmi/videoask_backend.git
```

- Install dependencies using pipenv:
```
pipenv install
```
- Install dependencies without pipenv:
```
cd videoask_backend
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
1- Run the FastAPI server:

```
uvicorn main:app --reload
```
2- Access the API documentation at http://localhost:8000/docs or http://localhost:8000/redoc.

3- Use the provided endpoints to interact with the service.

## Endpoints
- POST /saveVideoAsk: Save multiple video ask objects in the database.
- GET /getVideoAsks: Retrieve all video ask objects from the database.
- GET /getVideoAsk/{id}: Retrieve a video ask object by its ID from the database.
- POST /uploadfile: Upload a file and return the URL.
- DELETE /deleteAllVideoAsks: Delete all video ask objects from the database. (Dev mode)
- DELETE /deleteVideoAsk/{id}: Delete a video ask object by its ID from the database. (Dev mode)
