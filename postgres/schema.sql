-- Switch to the newly created database
\c scmb

------------------
-- Database Schema
------------------

-- Table: Person
CREATE TABLE IF NOT EXISTS Person (
    username VARCHAR PRIMARY KEY NOT NULL,
    email VARCHAR PRIMARY KEY NOT NULL,
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

-- Table: SupplyChain
CREATE TABLE IF NOT EXISTS SupplyChain (
    id BIGSERIAL PRIMARY KEY NOT NULL,
    time_created TIMESTAMP NOT NULL
);

-- Table: Shipment
CREATE TABLE IF NOT EXISTS Shipment (
    code VARCHAR PRIMARY KEY NOT NULL,
    time_created TIMESTAMP NOT NULL,
    supply_chain BIGINT REFERENCES SupplyChain(id) NOT NULL,
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
    supply_chain BIGINT REFERENCES SupplyChain(id) NOT NULL,
    role BIGINT REFERENCES RolesMap(id) NOT NULL
);

-- Table: Certificate
CREATE TABLE IF NOT EXISTS Certificate (
    id BIGSERIAL PRIMARY KEY NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    shipment VARCHAR REFERENCES Shipment(code) NOT NULL,
    issuer VARCHAR REFERENCES Person(username) NOT NULL,
    hash VARCHAR NOT NULL
);

-- Table: Metadata
CREATE TABLE IF NOT EXISTS Metadata (
    id BIGSERIAL PRIMARY KEY NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    shipment VARCHAR REFERENCES Shipment(code) NOT NULL,
    latitude VARCHAR,
    longitude VARCHAR,
    temperature VARCHAR,
    quality BIGINT
);

-- Table: Event
CREATE TABLE IF NOT EXISTS Event (
    id BIGSERIAL PRIMARY KEY NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    shipment VARCHAR REFERENCES Shipment(code) NOT NULL,
    event VARCHAR NOT NULL
);
