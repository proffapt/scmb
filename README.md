# SCMB - Supply Chain Management with Blockchain

## API Usage

The documentation will have `{ip/domain}` referring to the **IP Address/Domain Name** of the machine where this backend is hosted.

### Product

All the endpoints concerning products lie under `http://{ip/domain}/product/`. 

#### GET

##### Unique

- Send a _get_ request on the endpoint with the unique code of a product - `/product/<PRODUCT_CODE>`
- cURL example:
  ```curl
  curl -sS -X GET "http://{ip/domain}/product/P1"
  ```

##### All

- Send a _get_ request on the endpoint with "all" as arguement - `/product/all`
- cURL example:
  ```curl
  curl -sS -X GET "http://{ip/domain}/product/all"
  ```

#### DELETE

- Send a _delete_ request on the endpoint with the unique code of a product - `/product/<PRODUCT_CODE>`
- cURL example:
  ```curl
  curl -sS -X DELETE "http://{ip/domain}/product/P1"
  ```

#### POST and PUT

### Supply Chain

All the endpoints concerning supplychain lie under `http://{ip/domain}/sc/`. 

#### GET

##### Unique

- Send a _get_ request on the endpoint with the unique id of a Supply Chain - `/product/<SUPPLY_CHAIN_INT_ID>`
- cURL example:
  ```curl
  curl -sS -X GET "http://{ip/domain}/sc/1"
  ```

##### All

- Send a _get_ request on the endpoint with "all" as arguement - `/sc/all`
- cURL example:
  ```curl
  curl -sS -X GET "http://{ip/domain}/sc/all"
  ```

#### DELETE

- Send a _delete_ request on the endpoint with the unique code of a supplychain - `/sc/<SUPPLY_CHAIN_INT_ID>`
- cURL example:
  ```curl
  curl -sS -X DELETE "http://{ip/domain}/sc/1"
  ```

#### POST and PUT

### Shipment

All the endpoints concerning shipment lie under `http://{ip/domain}/shipment/`. 

#### GET

##### Unique

- Send a _get_ request on the endpoint with the unique code of a shipment - `/shipment/<SHIPMENT_CODE>`
- cURL example:
  ```curl
  curl -sS -X GET "http://{ip/domain}/shipment/S1"
  ```

##### All

- Send a _get_ request on the endpoint with "all" as arguement - `/shipment/all`
- cURL example:
  ```curl
  curl -sS -X GET "http://{ip/domain}/shipment/all"
  ```

##### By Supplychain

- Send a _get_ request on the endpoint with the unique id of a supplychain - `/shipment/sc/<SUPPLY_CHAIN_INT_ID>`
- cURL example:
  ```curl
  curl -sS -X GET "http://{ip/domain}/shipment/sc/1"
  ```

##### By Product

- Send a _get_ request on the endpoint with the unique code of a poroduct - `/shipment/product/<PRODUCT_CODE>`
- cURL example:
  ```curl
  curl -sS -X GET "http://{ip/domain}/shipment/product/P1"
  ```

##### By Supplychain and Product

- Send a _get_ request on the endpoint with the unique id of a supplychain and code for product - `/shipment/sc/<SUPPLY_CHAIN_INT_ID>/product/<PRODUCT_CODE>`
- cURL example:
  ```curl
  curl -sS -X GET "http://{ip/domain}/shipment/sc/1/product/P1"
  ```

#### DELETE

- Send a _delete_ request on the endpoint with the unique code of a shipment - `/shipment/<SHIPMENT_CODE>`
- cURL example:
  ```curl
  curl -sS -X DELETE "http://{ip/domain}/shipment/S1"
  ```

#### POST and PUT

### Shipment Metadata

All the endpoints concerning shipment metadata lie under `http://{ip/domain}/metadata/`. 

#### GET

##### Unique

- Send a _get_ request on the endpoint with the unique id of a metadata - `/metadata/<METADATA_INT_ID>`
- cURL example:
  ```curl
  curl -sS -X GET "http://{ip/domain}/metadata/1"
  ```

##### All

- Send a _get_ request on the endpoint with "all" as arguement - `/metadata/all`
- cURL example:
  ```curl
  curl -sS -X GET "http://{ip/domain}/metadata/all"
  ```

##### By Shipment

- Send a _get_ request on the endpoint with the unique code of a shipment - `/metadata/shipment/<SHIPMENT_CODE>`
- cURL example:
  ```curl
  curl -sS -X GET "http://{ip/domain}/metadata/shipment/S1"
  ```

#### DELETE

- Send a _delete_ request on the endpoint with the unique id of a metadata - `/metadata/<METADATA_INT_ID>`
- cURL example:
  ```curl
  curl -sS -X DELETE "http://{ip/domain}/metadata/1"
  ```

#### POST and PUT

### Shipment Events

All the endpoints concerning shipment events lie under `http://{ip/domain}/event/`. 

#### GET

##### Unique

- Send a _get_ request on the endpoint with the unique id of an event - `/event/<EVENT_INT_ID>`
- cURL example:
  ```curl
  curl -sS -X GET "http://{ip/domain}/event/1"
  ```

##### All

- Send a _get_ request on the endpoint with "all" as arguement - `/event/all`
- cURL example:
  ```curl
  curl -sS -X GET "http://{ip/domain}/event/all"
  ```

##### By Shipment

- Send a _get_ request on the endpoint with the unique code of a shipment - `/event/shipment/<SHIPMENT_CODE>`
- cURL example:
  ```curl
  curl -sS -X GET "http://{ip/domain}/event/shipment/S1"
  ```

#### DELETE

- Send a _delete_ request on the endpoint with the unique id of an event - `/event/<EVENT_INT_ID>`
- cURL example:
  ```curl
  curl -sS -X DELETE "http://{ip/domain}/event/1"
  ```

#### POST and PUT

### Person

All the endpoints concerning person lie under `http://{ip/domain}/person/`. 

#### GET

##### Unique

- Send a _get_ request on the endpoint with the unique username of a person - `/person/<USERNAME>`
- cURL example:
  ```curl
  curl -sS -X GET "http://{ip/domain}/person/proffapt"
  ```

##### All

- Send a _get_ request on the endpoint with "all" as arguement - `/person/all`
- cURL example:
  ```curl
  curl -sS -X GET "http://{ip/domain}/person/all"
  ```

#### DELETE

- Send a _delete_ request on the endpoint with the unique username of a person - `/person/<USERNAME>`
- cURL example:
  ```curl
  curl -sS -X DELETE "http://{ip/domain}/person/proffapt"
  ```

#### POST and PUT

### Certificates

All the endpoints concerning shipment certificates lie under `http://{ip/domain}/certificate/`. 

#### GET

##### Unique

- Send a _get_ request on the endpoint with the unique id of a certificate - `/certificate/<CERTIFICATE_INT_ID>`
- cURL example:
  ```curl
  curl -sS -X GET "http://{ip/domain}/certificate/1"
  ```

##### All

- Send a _get_ request on the endpoint with "all" as arguement - `/certificate/all`
- cURL example:
  ```curl
  curl -sS -X GET "http://{ip/domain}/certificate/all"
  ```

##### By Shipment

- Send a _get_ request on the endpoint with the unique code of a shipment - `/certificate/shipment/<SHIPMENT_CODE>`
- cURL example:
  ```curl
  curl -sS -X GET "http://{ip/domain}/certificate/shipment/S1"
  ```

##### By Issuer

- Send a _get_ request on the endpoint with the unique username of the issuer - `/certificate/issuer/<USERNAME>`
- cURL example:
  ```curl
  curl -sS -X GET "http://{ip/domain}/certificate/issuer/proffapt"
  ```

##### Download

- Send a _get_ request on the endpoint with the unique id of the certificate - `/certificate/<CERTIFICATE_INT_ID>/download`
- cURL example:
  ```curl
  curl -sS -X GET "http://{ip/domain}/certificate/1/download"
  ```

#### DELETE

- Send a _delete_ request on the endpoint with the unique id of an event - `/certificate/<CERTIFICATE_INT_ID>`
- cURL example:
  ```curl
  curl -sS -X DELETE "http://{ip/domain}/certificate/1"
  ```

#### POST and PUT
