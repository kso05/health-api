[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/t8Ky5Oxm)
# oslomet_oblig_3

#Author : Karina Soltanian 

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