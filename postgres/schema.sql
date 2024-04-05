-- Switch to the newly created database
\c scmb

------------------
-- Database Schema
------------------

-- Table: Person
CREATE TABLE IF NOT EXISTS Person (
    username VARCHAR PRIMARY KEY NOT NULL,
    email VARCHAR NOT NULL,
    password VARCHAR NOT NULL,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR,
    address VARCHAR NOT NULL,
    phone VARCHAR NOT NULL,
    organisation VARCHAR NOT NULL
);

-- Table: Product
CREATE TABLE IF NOT EXISTS Product (
    code VARCHAR PRIMARY KEY NOT NULL,
    name VARCHAR NOT NULL
);

-- Table: Supplychain
CREATE TABLE IF NOT EXISTS Supplychain (
    id BIGSERIAL PRIMARY KEY NOT NULL,
    name VARCHAR NOT NULL
);

-- Table: Shipment
CREATE TABLE IF NOT EXISTS Shipment (
    code VARCHAR PRIMARY KEY NOT NULL,
    supplychain BIGINT REFERENCES Supplychain(id) NOT NULL,
    product VARCHAR REFERENCES Product(code) NOT NULL,
    quantity FLOAT NOT NULL,
    quantity_unit VARCHAR NOT NULL,
    acceptable_quality_lower_bound BIGINT,
    acceptable_quality_upper_bound BIGINT,
    expected_quality BIGINT
);

-- Table: RolesMap
CREATE TABLE IF NOT EXISTS RolesMap (
    id BIGSERIAL PRIMARY KEY NOT NULL,
    permissions VARCHAR NOT NULL
);

-- Table: Role
CREATE TABLE IF NOT EXISTS Role (
    id BIGSERIAL PRIMARY KEY NOT NULL,
    username VARCHAR REFERENCES Person(username) NOT NULL,
    supplychain BIGINT REFERENCES Supplychain(id) NOT NULL,
    role BIGINT REFERENCES RolesMap(id) NOT NULL
);

-- Table: Certificate
CREATE TABLE IF NOT EXISTS Certificate (
    id BIGSERIAL PRIMARY KEY NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    shipment VARCHAR REFERENCES Shipment(code) NOT NULL,
    issuer VARCHAR REFERENCES Person(username) NOT NULL,
    pdf_path VARCHAR NOT NULL,
    pdf_hash VARCHAR NOT NULL
);

-- Table: Shipment_Metadata
CREATE TABLE IF NOT EXISTS Shipment_Metadata (
    id BIGSERIAL PRIMARY KEY NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    shipment VARCHAR REFERENCES Shipment(code) NOT NULL,
    latitude VARCHAR,
    longitude VARCHAR,
    temperature VARCHAR,
    quality BIGINT
);

-- Table: Shipment_Event
CREATE TABLE IF NOT EXISTS Shipment_Event (
    id BIGSERIAL PRIMARY KEY NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    shipment VARCHAR REFERENCES Shipment(code) NOT NULL,
    event VARCHAR NOT NULL
);

-- Table: Sensor_Health_Monitoring_Device
CREATE TABLE Sensor_Health_Monitoring_Device (
   code VARCHAR PRIMARY KEY NOT NULL,
   shipment VARCHAR REFERENCES Shipment(code) NOT NULL,
   description VARCHAR NOT NULL
);

-- Table: SHMD_Event
CREATE TABLE Sensor_Health_Monitoring_Device_Event (
   id BIGSERIAL PRIMARY KEY NOT NULL,
   timestamp TIMESTAMP NOT NULL,
   sensor_health_monitoring_device VARCHAR REFERENCES Sensor_Health_Monitoring_Device(code) NOT NULL,
   remarks VARCHAR NOT NULL
);
