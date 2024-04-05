# SCMB - Supply Chain Management with Blockchain

This is repository container the backend codebase for the project named "Supply Cahin Management with Blockchain" under the course of "Information Systems Lab" at IIT Kharagpur for the 2nd semester of 2023-2024 session.

## Codebase

Detailed dbdiagram can be found here: https://dbdiagram.io/d/supply-chain-65e99a55b1f3d4062c5b677b

### Structure

```graphql
.
├── .env                   (Environment file)
├── .env.example           (Example environment file, use this as template to create (.env) file)
├── postgres
│   ├── dummy_data.sql     (Dummy data to populate database on first run)
│   └── schdema.sql        (Database scdhema file)
└── webapp
    ├── api
    │   ├── __init__.py    (API endpoint definitions (mapping endpoints with the function definitions))
    │   ├── ...
    │   └── supplychain.py (API endpoint function definitions concerning SUPPLYCHAIN table)
    ├── middleware
    │   └── auth.py        (API ednpoint wrapper function definitions to perform various authorisations)
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
   JWT_SECRET_KEY=jwt_secret
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

### Signup

- The endpoints concerning signup is `http://{ip/domain}/signup`. 
- Send a _post_ request on the endpoint (`/signup`) with following JSON (`application/json`) data in request body:
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
- cURL example:
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
    http://{ip/domain}/signup
  ```
  
### Login

- The endpoints concerning login is `http://{ip/domain}/login`. 
- Send a _post_ request on the endpoint (`/login`) with following JSON (`application/json`) data in request body:
  ```json
  {
    "username": "proffapt",
    "password": "proffapt@scmb"
  }
  ```
- cURL example:
  ```bash
  curl -sS -X POST \
    -H "Content-Type: application/json" \
    -d '{
            "username": "proffapt",
            "password": "proffapt@scmb"
        }' \
    http://{ip/domain}/login
  ```
- If successfull, a `jwt_token` will be provided in response. This token is required to be sent in Header of any requests made. Following is an example response:
  ```json
  {
    "jwt_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJwcm9mZmFwdCIsImV4cCI6MTcxMjE4MzE0NCwiaWF0IjoxNzEyMTc5NTM0fQ.WsulF1uI9Vz3kSPf_f8QWWI0BeD3_MAGaAzC6eu-TMU"
  }
  ```

### Product

All the endpoints concerning products lie under `http://{ip/domain}/product/`. 

#### GET

##### Unique

- Send a _get_ request on the endpoint with the unique code of a product - `/product/<PRODUCT_CODE>`
- cURL example:
  ```bash
  curl -sS -X GET \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/product/P1"
  ```

##### All

- Send a _get_ request on the endpoint with "all" as arguement - `/product/all`
- cURL example:
  ```bash
  curl -sS -X GET \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/product/all"
  ```

#### DELETE

- Send a _delete_ request on the endpoint with the unique code of a product - `/product/<PRODUCT_CODE>`
- cURL example:
  ```bash
  curl -sS -X DELETE \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/product/P1"
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
    -H "Authorization: Bearer <auth-token>" \
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
  curl -sS -X GET \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/sc/1"
  ```

##### All

- Send a _get_ request on the endpoint with "all" as arguement - `/sc/all`
- cURL example:
  ```bash
  curl -sS -X GET \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/sc/all"
  ```

#### DELETE

- Send a _delete_ request on the endpoint with the unique code of a supplychain - `/sc/<SUPPLY_CHAIN_INT_ID>`
- cURL example:
  ```bash
  curl -sS -X DELETE \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/sc/1"
  ```

#### POST and PUT

- Send a _post_ or a _put_ request on the endpoint (`/sc/`) with following JSON (`application/json`) data along with `Authorization: Bearer <auth-token>` header in request body:
  ```json
  {
    "name": "Vistara :: London<>Mumbai"
  }
  ```
- cURL example (`POST` - for `PUT` replace _POST_ with _PUT_ in the command):
  ```bash
  curl -sS -X POST \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer <auth-token>" \
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
  curl -sS -X GET \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/shipment/S1"
  ```

##### All

- Send a _get_ request on the endpoint with "all" as arguement - `/shipment/all`
- cURL example:
  ```bash
  curl -sS -X GET \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/shipment/all"
  ```

##### By Supplychain

- Send a _get_ request on the endpoint with the unique id of a supplychain - `/shipment/sc/<SUPPLY_CHAIN_INT_ID>`
- cURL example:
  ```bash
  curl -sS -X GET \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/shipment/sc/1"
  ```

##### By Product

- Send a _get_ request on the endpoint with the unique code of a poroduct - `/shipment/product/<PRODUCT_CODE>`
- cURL example:
  ```bash
  curl -sS -X GET \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/shipment/product/P1"
  ```

##### By Supplychain and Product

- Send a _get_ request on the endpoint with the unique id of a supplychain and code for product - `/shipment/sc/<SUPPLY_CHAIN_INT_ID>/product/<PRODUCT_CODE>`
- cURL example:
  ```bash
  curl -sS -X GET \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/shipment/sc/1/product/P1"
  ```

#### DELETE

- Send a _delete_ request on the endpoint with the unique code of a shipment - `/shipment/<SHIPMENT_CODE>`
- cURL example:
  ```bash
  curl -sS -X DELETE \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/shipment/S1"
  ```

#### POST and PUT

- Send a _post_ or a _put_ request on the endpoint (`/shipment/`) with following JSON (`application/json`) data along with `Authorization: Bearer <auth-token>` header in request body:
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
  curl -X POST \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer <auth-token>" \
    -d '{
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

All the endpoints concerning shipment metadata lie under `http://{ip/domain}/shipment/metadata/`. 

#### GET

##### Unique

- Send a _get_ request on the endpoint with the unique id of a metadata - `/shipment/metadata/<METADATA_INT_ID>`
- cURL example:
  ```bash
  curl -sS -X GET \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/shipment/metadata/1"
  ```

##### All

- Send a _get_ request on the endpoint with "all" as arguement - `/shipment/metadata/all`
- cURL example:
  ```bash
  curl -sS -X GET \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/shipment/metadata/all"
  ```

##### By Shipment

- Send a _get_ request on the endpoint with the unique code of a shipment - `/shipment/metadata/shipment/<SHIPMENT_CODE>`
- cURL example:
  ```bash
  curl -sS -X GET \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/shipment/metadata/shipment/S1"
  ```

#### DELETE

- Send a _delete_ request on the endpoint with the unique id of a metadata - `/shipment/metadata/<METADATA_INT_ID>`
- cURL example:
  ```bash
  curl -sS -X DELETE \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/shipment/metadata/1"
  ```

#### POST and PUT

- Send a _post_ or a _put_ request on the endpoint (`/shipment/metadata/`) with following JSON (`application/json`) data along with `Authorization: Bearer <auth-token>` header in request body:
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
    -H "Authorization: Bearer <auth-token>" \
    -d '{
      "shipment": "S1",
      "latitude": "40.7128",
      "longitude": "-74.0060",
      "temperature": "25°C",
      "quality": 95
    }' \
    http://{ip/domain}/shipment/metadata/
  ```

### Shipment Events

All the endpoints concerning shipment events lie under `http://{ip/domain}/shipment/event/`. 

#### GET

##### Unique

- Send a _get_ request on the endpoint with the unique id of an event - `/shipment/event/<EVENT_INT_ID>`
- cURL example:
  ```bash
  curl -sS -X GET \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/shipment/event/1"
  ```

##### All

- Send a _get_ request on the endpoint with "all" as arguement - `/shipment/event/all`
- cURL example:
  ```bash
  curl -sS -X GET \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/shipment/event/all"
  ```

##### By Shipment

- Send a _get_ request on the endpoint with the unique code of a shipment - `/shipment/event/shipment/<SHIPMENT_CODE>`
- cURL example:
  ```bash
  curl -sS -X GET \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/shipment/event/shipment/S1"
  ```

#### DELETE

- Send a _delete_ request on the endpoint with the unique id of an event - `/shipment/event/<EVENT_INT_ID>`
- cURL example:
  ```bash
  curl -sS -X DELETE \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/shipment/event/1"
  ```

#### POST and PUT

- Send a _post_ or a _put_ request on the endpoint (`/shipment/event/`) with following JSON (`application/json`) data along with `Authorization: Bearer <auth-token>` header in request body:
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
    -H "Authorization: Bearer <auth-token>" \
    -d '{
          "shipment": "S1",
          "event": "Arrived at warehouse"
        }' \
    http://{ip/domain}/shipment/event/
  ```

### Shipment Health Monitoring Device

All the endpoints concerning shipment health monitoring device lie under `http://{ip/domain}/shmd/`. 

#### GET

##### Unique

- Send a _get_ request on the endpoint with the unique code of a device - `/shmd/<SHIPMENT_HEALTH_MONITORING_DEVICE_CODE>`
- cURL example:
  ```bash
  curl -sS -X GET \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/shmd/SHM001"
  ```

##### All

- Send a _get_ request on the endpoint with "all" as arguement - `/shmd/all`
- cURL example:
  ```bash
  curl -sS -X GET \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/shmd/all"
  ```

##### By Shipment

- Send a _get_ request on the endpoint with the unique code of a shipment - `/shmd/shipment/<SHIPMENT_CODE>`
- cURL example:
  ```bash
  curl -sS -X GET \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/shmd/shipment/S1"
  ```

#### DELETE

- Send a _delete_ request on the endpoint with the unique code of a device - `/shmd/shipment/<SHIPMENT_HEALTH_MONITORING_DEVICE_CODE>`
- cURL example:
  ```bash
  curl -sS -X DELETE \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/shmd/SHM001"
  ```

#### POST and PUT

- Send a _post_ or a _put_ request on the endpoint (`/shmd/`) with following JSON (`application/json`) data along with `Authorization: Bearer <auth-token>` header in request body:
  ```json
  {
    "code": "SHM001",
    "shipment": "S1",
    "description": "Temperature Sensor"
  }
  ```
- cURL example (`POST` - for `PUT` replace _POST_ with _PUT_ in the command):
  ```bash
  curl -X POST \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer <auth-token>" \
    -d '{
        "code": "SHM001",
        "shipment": "S1",
        "description": "Temperature Sensor"
    }' \
    http://{ip/domain}/shmd/
  ```

### Shipment Health Monitoring Device Event

All the endpoints concerning shipment health monitoring device events lie under `http://{ip/domain}/shmd/event/`. 

#### GET

##### Unique

- Send a _get_ request on the endpoint with the unique id of a event - `/shmd/event/<EVENT_INT_ID>`
- cURL example:
  ```bash
  curl -sS -X GET \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/shmd/event/1"
  ```

##### All

- Send a _get_ request on the endpoint with "all" as arguement - `/shmd/all`
- cURL example:
  ```bash
  curl -sS -X GET \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/shmd/event/all"
  ```

##### By Sensor Health Monitoring Device

- Send a _get_ request on the endpoint with the unique code of a shmd device - `/shmd/event/sensor/<SHMD_CODE>`
- cURL example:
  ```bash
  curl -sS -X GET \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/shmd/event/sensor/SHM001"
  ```

#### DELETE

- Send a _delete_ request on the endpoint with the unique id of an event - `/shmd/shipment/<EVENT_INT_ID>`
- cURL example:
  ```bash
  curl -sS -X DELETE \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/shmd/event/1"
  ```

#### POST and PUT

- Send a _post_ or a _put_ request on the endpoint (`/shmd/event/`) with following JSON (`application/json`) data along with `Authorization: Bearer <auth-token>` header in request body:
  ```json
  {
    "sensor_health_monitoring_device": "SHM001",
    "remarks": "Dangerous Level"
  }
  ```
- cURL example (`POST` - for `PUT` replace _POST_ with _PUT_ in the command):
  ```bash
  curl -X POST \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer <auth-token>" \
    -d '{
        "sensor_health_monitoring_device": "SHM001",
        "remarks": "Dangerous Level"
    }' \
    http://{ip/domain}/shmd/event/
  ```

### Person

All the endpoints concerning person lie under `http://{ip/domain}/person/`. 

#### GET

##### Unique

- Send a _get_ request on the endpoint with the unique username of a person - `/person/<USERNAME>`
- cURL example:
  ```bash
  curl -sS -X GET \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/person/proffapt"
  ```

##### All

- Send a _get_ request on the endpoint with "all" as arguement - `/person/all`
- cURL example:
  ```bash
  curl -sS -X GET \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/person/all"
  ```

#### DELETE

- Send a _delete_ request on the endpoint with the unique username of a person - `/person/<USERNAME>`
- cURL example:
  ```bash
  curl -sS -X DELETE \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/person/proffapt"
  ```

#### PUT

> [!Note]
> This endpoint doesn't support `POST` method as that is covered by [signup](#signup)

- Send a _put_ request on the endpoint (`/person/`) with following JSON (`application/json`) data along with `Authorization: Bearer <auth-token>` header in request body:
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
- cURL example:
  ```bash
  curl -X PUT \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer <auth-token>" \
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
  curl -sS -X GET \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/certificate/1"
  ```

##### All

- Send a _get_ request on the endpoint with "all" as arguement - `/certificate/all`
- cURL example:
  ```bash
  curl -sS -X GET \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/certificate/all"
  ```

##### By Shipment

- Send a _get_ request on the endpoint with the unique code of a shipment - `/certificate/shipment/<SHIPMENT_CODE>`
- cURL example:
  ```bash
  curl -sS -X GET \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/certificate/shipment/S1"
  ```

##### By Issuer

- Send a _get_ request on the endpoint with the unique username of the issuer - `/certificate/issuer/<USERNAME>`
- cURL example:
  ```bash
  curl -sS -X GET \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/certificate/issuer/proffapt"
  ```

##### Download

- Send a _get_ request on the endpoint with the unique id of the certificate - `/certificate/<CERTIFICATE_INT_ID>/download`
- cURL example:
  ```bash
  curl -sS -X GET \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/certificate/1/download"
  ```

#### DELETE

- Send a _delete_ request on the endpoint with the unique id of an event - `/certificate/<CERTIFICATE_INT_ID>`
- cURL example:
  ```bash
  curl -sS -X DELETE \
    -H "Authorization: Bearer <auth-token>" \
    "http://{ip/domain}/certificate/1"
  ```

#### POST and PUT

- Send a _post_ or a _put_ request on the endpoint (`/certificate/`) with following files data (`mutipart/form-data`) along with `Authorization: Bearer <auth-token>` header in files request:
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
    -H "Authorization: Bearer <auth-token>" \
    -F "pdf_file=@test.pdf" \
    -F "pdf_name=test.pdf" \
    -F "shipment=S1" \
    -F "issuer=proffapt" \
    http://{ip/domain}/certificate
  ```
