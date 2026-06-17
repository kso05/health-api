
#Author : Karina Soltanian 

A containerized REST API for managing health records, built with FastAPI and Python.
This project exposes a simple backend service that allows users to create and retrieve health data through HTTP requests.

## Note

This repository is a cleaned and simplified version of the original coursework implementation. The original project was structured in multiple modules and folders as part of the assignment requirements. This version has been reorganized to make the project easier to run, read, and present as a standalone portfolio project.

#Set-up and test intructions 

Pytest
python -m src.health_app.data -- ran from previous oblig 

python -m src.health_app.health -- ran from previous oblig 

python -m src.health_app.main -- ran from previous oblig 

Building docker image:
docker compose build 

To run:
docker compose up

#Fetches data from the / endpoint 
curl -X 'GET' \
  'http://127.0.0.1:8000/' \
  -H 'accept: application/json' 

#Fetches data from the /records endpoint 
curl -X 'GET' \
  'http://127.0.0.1:8000/records' \
  -H 'accept: application/json'

#POST- data, adds data to the databse through CURL using /records
curl -X 'POST' \
  'http://127.0.0.1:8000/records' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "string",
  "weight_kg": 0,
  "height_m": 0
}
