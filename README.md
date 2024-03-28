# SCMB - Supply Chain Management with Blockchain

This is repository container the backend codebase for the project named "Supply Cahin Management with Blockchain" under the course of "Information Systems Lab" at IIT Kharagpur for the 2nd semester of 2023-2024 session.

## Codebase

### Structure

```graphql
.
├── postgres
│   ├── dummy_data.sql     (Dummy data to populate database on first run)
│   └── schdema.sql        (Database scdhema file)
└── webapp
    ├── api
    │   ├── __init__.py    (API endpoint definitions (mapping endpoints with the function definitions))
    │   ├── ...
    │   └── supplychain.py (API endpoint function definitions concerning SUPPLYCHAIN table)
    ├── database
    │   ├── __init__.py    (Contains flask_SQLAlchemy db object definition)
    │   ├── ...
    │   └── supplychain.py (Database operations concerning SUPPLYCHAIN table)
    └── models             
        ├── error.py       (Error type classes)
        ├── ...
        └── supplychain.py (DatabaseStructs, DatabaseTypes (python type classes) & serializers (Database Models -> Database Types))
```

### Deployment

1. Clone this repository
   ```bash
   git clone https://github.com/proffapt/scmb
   cd scmb/
   ```
2. Install `docker` and `docker-compose`
   ```bash
   sudo apt update
   sudo apt install -y docker.io docker-compose 
   ```
3. Create `.env` file. Copy the `.env.example` as `.env` and fill out the values for ENVs. Following is an exmple:
   ```env
   POSTGRES_DB=scmb
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres-scmb-db
   HASH_SALT=bcrypt_hash_salt
   ```
4. Build the docker images
   ```bash
   sudo docker-compose build
   ```
5. Run the containers using `docker-compose`
   ```bash
   sudo docker-compose up -d
   ```

## API Usage

The documentation will have `{ip/domain}` referring to the **IP Address/Domain Name** of the machine where this backend is hosted.

### Product

All the endpoints concerning products lie under `http://{ip/domain}/product/`. 

#### GET

##### Unique

- Send a _get_ request on the endpoint with the unique code of a product - `/product/<PRODUCT_CODE>`
- cURL example:
  ```bash
  curl -sS -X GET "http://{ip/domain}/product/P1"
  ```

##### All

- Send a _get_ request on the endpoint with "all" as arguement - `/product/all`
- cURL example:
  ```bash
  curl -sS -X GET "http://{ip/domain}/product/all"
  ```

#### DELETE

- Send a _delete_ request on the endpoint with the unique code of a product - `/product/<PRODUCT_CODE>`
- cURL example:
  ```bash
  curl -sS -X DELETE "http://{ip/domain}/product/P1"
  ```

#### POST and PUT

- Send a _post_ or a _put_ request on the endpoint (`/product/`) with following JSON (`application/json`) data in request body:
  ```json
  {
    "code": "P1", 
    "name": "Mango"
  }
  ```
- cURL example (`POST` - for `PUT` replace _POST_ with _PUT_ in the command):
  ```bash
  curl -sS -X POST \
    -H "Content-Type: application/json" \
    -d '{
          "code":"P1", 
          "name":"Apple"
        }' \
    http://{ip/domain}/product
  ```

### Supply Chain

All the endpoints concerning supplychain lie under `http://{ip/domain}/sc/`. 

#### GET

##### Unique

- Send a _get_ request on the endpoint with the unique id of a Supply Chain - `/product/<SUPPLY_CHAIN_INT_ID>`
- cURL example:
  ```bash
  curl -sS -X GET "http://{ip/domain}/sc/1"
  ```

##### All

- Send a _get_ request on the endpoint with "all" as arguement - `/sc/all`
- cURL example:
  ```bash
  curl -sS -X GET "http://{ip/domain}/sc/all"
  ```

#### DELETE

- Send a _delete_ request on the endpoint with the unique code of a supplychain - `/sc/<SUPPLY_CHAIN_INT_ID>`
- cURL example:
  ```bash
  curl -sS -X DELETE "http://{ip/domain}/sc/1"
  ```

#### POST and PUT

- Send a _post_ or a _put_ request on the endpoint (`/sc/`) with following JSON (`application/json`) data in request body:
  ```json
  {
    "name": "Vistara :: London<>Mumbai"
  }
  ```
- cURL example (`POST` - for `PUT` replace _POST_ with _PUT_ in the command):
  ```bash
  curl -sS -X POST \
    -H "Content-Type: application/json" \
    -d '{
          "name":"Vistara :: London<>Mumbai"
        }' \
    http://{ip/domain}/sc
  ```

### Shipment

All the endpoints concerning shipment lie under `http://{ip/domain}/shipment/`. 

#### GET

##### Unique

- Send a _get_ request on the endpoint with the unique code of a shipment - `/shipment/<SHIPMENT_CODE>`
- cURL example:
  ```bash
  curl -sS -X GET "http://{ip/domain}/shipment/S1"
  ```

##### All

- Send a _get_ request on the endpoint with "all" as arguement - `/shipment/all`
- cURL example:
  ```bash
  curl -sS -X GET "http://{ip/domain}/shipment/all"
  ```

##### By Supplychain

- Send a _get_ request on the endpoint with the unique id of a supplychain - `/shipment/sc/<SUPPLY_CHAIN_INT_ID>`
- cURL example:
  ```bash
  curl -sS -X GET "http://{ip/domain}/shipment/sc/1"
  ```

##### By Product

- Send a _get_ request on the endpoint with the unique code of a poroduct - `/shipment/product/<PRODUCT_CODE>`
- cURL example:
  ```bash
  curl -sS -X GET "http://{ip/domain}/shipment/product/P1"
  ```

##### By Supplychain and Product

- Send a _get_ request on the endpoint with the unique id of a supplychain and code for product - `/shipment/sc/<SUPPLY_CHAIN_INT_ID>/product/<PRODUCT_CODE>`
- cURL example:
  ```bash
  curl -sS -X GET "http://{ip/domain}/shipment/sc/1/product/P1"
  ```

#### DELETE

- Send a _delete_ request on the endpoint with the unique code of a shipment - `/shipment/<SHIPMENT_CODE>`
- cURL example:
  ```bash
  curl -sS -X DELETE "http://{ip/domain}/shipment/S1"
  ```

#### POST and PUT

- Send a _post_ or a _put_ request on the endpoint (`/shipment/`) with following JSON (`application/json`) data in request body:
  ```json
  {
    "code": "S1",
    "supplychain": 1,
    "product": "P1",
    "quantity": 100,
    "quantity_unit": "kg",
    "acceptable_quality_lower_bound": 90,
    "acceptable_quality_upper_bound": 95,
    "expected_quality": 92
  }
  ```
- cURL example (`POST` - for `PUT` replace _POST_ with _PUT_ in the command):
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{
    "code": "S1",
    "supplychain": 1,
    "product": "P1",
    "quantity": 100,
    "quantity_unit": "kg",
    "acceptable_quality_lower_bound": 90,
    "acceptable_quality_upper_bound": 95,
    "expected_quality": 92
  }' http://{ip/domain}/shipment
  ```

### Shipment Metadata

All the endpoints concerning shipment metadata lie under `http://{ip/domain}/metadata/`. 

#### GET

##### Unique

- Send a _get_ request on the endpoint with the unique id of a metadata - `/metadata/<METADATA_INT_ID>`
- cURL example:
  ```bash
  curl -sS -X GET "http://{ip/domain}/metadata/1"
  ```

##### All

- Send a _get_ request on the endpoint with "all" as arguement - `/metadata/all`
- cURL example:
  ```bash
  curl -sS -X GET "http://{ip/domain}/metadata/all"
  ```

##### By Shipment

- Send a _get_ request on the endpoint with the unique code of a shipment - `/metadata/shipment/<SHIPMENT_CODE>`
- cURL example:
  ```bash
  curl -sS -X GET "http://{ip/domain}/metadata/shipment/S1"
  ```

#### DELETE

- Send a _delete_ request on the endpoint with the unique id of a metadata - `/metadata/<METADATA_INT_ID>`
- cURL example:
  ```bash
  curl -sS -X DELETE "http://{ip/domain}/metadata/1"
  ```

#### POST and PUT

- Send a _post_ or a _put_ request on the endpoint (`/metadata/`) with following JSON (`application/json`) data in request body:
  ```json
  {
    "shipment": "S1",
    "latitude": "40.7128",
    "longitude": "-74.0060",
    "temperature": "25°C",
    "quality": 95
  }
  ```
- cURL example (`POST` - for `PUT` replace _POST_ with _PUT_ in the command):
  ```bash
  curl -X POST \
    -H "Content-Type: application/json" \
    -d '{
      "shipment": "S1",
      "latitude": "40.7128",
      "longitude": "-74.0060",
      "temperature": "25°C",
      "quality": 95
    }' \
    http://{ip/domain}/metadata
  ```

### Shipment Events

All the endpoints concerning shipment events lie under `http://{ip/domain}/event/`. 

#### GET

##### Unique

- Send a _get_ request on the endpoint with the unique id of an event - `/event/<EVENT_INT_ID>`
- cURL example:
  ```bash
  curl -sS -X GET "http://{ip/domain}/event/1"
  ```

##### All

- Send a _get_ request on the endpoint with "all" as arguement - `/event/all`
- cURL example:
  ```bash
  curl -sS -X GET "http://{ip/domain}/event/all"
  ```

##### By Shipment

- Send a _get_ request on the endpoint with the unique code of a shipment - `/event/shipment/<SHIPMENT_CODE>`
- cURL example:
  ```bash
  curl -sS -X GET "http://{ip/domain}/event/shipment/S1"
  ```

#### DELETE

- Send a _delete_ request on the endpoint with the unique id of an event - `/event/<EVENT_INT_ID>`
- cURL example:
  ```bash
  curl -sS -X DELETE "http://{ip/domain}/event/1"
  ```

#### POST and PUT

- Send a _post_ or a _put_ request on the endpoint (`/event/`) with following JSON (`application/json`) data in request body:
  ```json
  {
    "shipment": "S1",
    "event": "Arrived at warehouse"
  }
  ```
- cURL example (`POST` - for `PUT` replace _POST_ with _PUT_ in the command):
  ```bash
  curl -X POST \
    -H "Content-Type: application/json" \
    -d '{
          "shipment": "S1",
          "event": "Arrived at warehouse"
        }' \
    http://{ip/domain}/event
  ```

### Person

All the endpoints concerning person lie under `http://{ip/domain}/person/`. 

#### GET

##### Unique

- Send a _get_ request on the endpoint with the unique username of a person - `/person/<USERNAME>`
- cURL example:
  ```bash
  curl -sS -X GET "http://{ip/domain}/person/proffapt"
  ```

##### All

- Send a _get_ request on the endpoint with "all" as arguement - `/person/all`
- cURL example:
  ```bash
  curl -sS -X GET "http://{ip/domain}/person/all"
  ```

#### DELETE

- Send a _delete_ request on the endpoint with the unique username of a person - `/person/<USERNAME>`
- cURL example:
  ```bash
  curl -sS -X DELETE "http://{ip/domain}/person/proffapt"
  ```

#### POST and PUT

- Send a _post_ or a _put_ request on the endpoint (`/person/`) with following JSON (`application/json`) data in request body:
  ```json
  {
    "username": "proffapt",
    "email": "proffapt@gmail.com",
    "password": "proffapt@scmb",
    "first_name": "Arpit",
    "last_name": "Bhardwaj",
    "address": "F-211 JCB Hall",
    "phone": "1234567890",
    "organisation": "IS LAB"
  }
  ```
- cURL example (`POST` - for `PUT` replace _POST_ with _PUT_ in the command):
  ```bash
  curl -X POST \
    -H "Content-Type: application/json" \
    -d '{
          "username": "proffapt",
          "email": "proffapt@gmail.com",
          "password": "proffapt@scmb",
          "first_name": "Arpit",
          "last_name": "Bhardwaj",
          "address": "F-211 JCB Hall",
          "phone": "1234567890",
          "organisation": "IS LAB"
        }' \
    http://{ip/domain}/person
  ```

### Certificate

All the endpoints concerning shipment certificates lie under `http://{ip/domain}/certificate/`. 

#### GET

##### Unique

- Send a _get_ request on the endpoint with the unique id of a certificate - `/certificate/<CERTIFICATE_INT_ID>`
- cURL example:
  ```bash
  curl -sS -X GET "http://{ip/domain}/certificate/1"
  ```

##### All

- Send a _get_ request on the endpoint with "all" as arguement - `/certificate/all`
- cURL example:
  ```bash
  curl -sS -X GET "http://{ip/domain}/certificate/all"
  ```

##### By Shipment

- Send a _get_ request on the endpoint with the unique code of a shipment - `/certificate/shipment/<SHIPMENT_CODE>`
- cURL example:
  ```bash
  curl -sS -X GET "http://{ip/domain}/certificate/shipment/S1"
  ```

##### By Issuer

- Send a _get_ request on the endpoint with the unique username of the issuer - `/certificate/issuer/<USERNAME>`
- cURL example:
  ```bash
  curl -sS -X GET "http://{ip/domain}/certificate/issuer/proffapt"
  ```

##### Download

- Send a _get_ request on the endpoint with the unique id of the certificate - `/certificate/<CERTIFICATE_INT_ID>/download`
- cURL example:
  ```bash
  curl -sS -X GET "http://{ip/domain}/certificate/1/download"
  ```

#### DELETE

- Send a _delete_ request on the endpoint with the unique id of an event - `/certificate/<CERTIFICATE_INT_ID>`
- cURL example:
  ```bash
  curl -sS -X DELETE "http://{ip/domain}/certificate/1"
  ```

#### POST and PUT

- Send a _post_ or a _put_ request on the endpoint (`/certificate/`) with following files data (`mutipart/form-data`) in files request:
  ```json
    "pdf_file=@test.pdf"
    "pdf_name=test.pdf"
    "shipment=S1"
    "issuer=proffapt"
  ```
- cURL example (`POST` - for `PUT` replace _POST_ with _PUT_ in the command):
  ```bash
  curl -X POST \
    -H "Content-Type: multipart/form-data" \
    -F "pdf_file=@test.pdf" \
    -F "pdf_name=test.pdf" \
    -F "shipment=S1" \
    -F "issuer=proffapt" \
    http://{ip/domain}/certificate
  ```
