------------------
-- Database Schema
------------------

-- Create User table
CREATE TABLE User (
    username VARCHAR PRIMARY KEY NOT NULL,
    email VARCHAR NOT NULL UNIQUE,
    password VARCHAR NOT NULL,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR,
    address VARCHAR NOT NULL,
    phone VARCHAR NOT NULL,
    organisation VARCHAR NOT NULL
);

-- Create Product table
CREATE TABLE Product (
    code VARCHAR PRIMARY KEY NOT NULL,
    name VARCHAR NOT NULL
);

-- Create SupplyChain table
CREATE TABLE SupplyChain (
    id BIGSERIAL PRIMARY KEY NOT NULL,
    time_created TIMESTAMP NOT NULL,
    product BIGINT NOT NULL REFERENCES Product(code),
    user BIGINT NOT NULL REFERENCES User(username)
);

-- Create Shipment table
CREATE TABLE Shipment (
    code VARCHAR PRIMARY KEY NOT NULL,
    supply_chain BIGINT NOT NULL REFERENCES SupplyChain(id),
    time_created TIMESTAMP NOT NULL,
    quantity FLOAT NOT NULL,
    quantity_unit VARCHAR NOT NULL
);

-- Create RolesMap table
CREATE TABLE RolesMap (
    id BIGSERIAL PRIMARY KEY NOT NULL,
    permissions VARCHAR NOT NULL
);

-- Create Role table
CREATE TABLE Role (
    id BIGSERIAL PRIMARY KEY NOT NULL,
    username BIGINT NOT NULL REFERENCES User(username),
    supply_chain BIGINT NOT NULL REFERENCES SupplyChain(id),
    role BIGINT NOT NULL REFERENCES RolesMap(id)
);

-- Create Certificate table
CREATE TABLE Certificate (
    id BIGSERIAL PRIMARY KEY NOT NULL,
    hash VARCHAR NOT NULL,
    time_created TIMESTAMP NOT NULL,
    issuer BIGINT NOT NULL REFERENCES User(username),
    shipment VARCHAR NOT NULL REFERENCES Shipment(code)
);

-- Create Metadata table
CREATE TABLE Metadata (
    id BIGSERIAL PRIMARY KEY NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    latitude VARCHAR,
    longitude VARCHAR,
    temperature VARCHAR,
    present_quality BIGINT,
    expected_quality BIGINT,
    acceptable_quality_lower_bound BIGINT,
    acceptable_quality_upper_bound BIGINT,
    shipment VARCHAR NOT NULL REFERENCES Shipment(code)
);

-- Create Event table
CREATE TABLE Event (
    id BIGSERIAL PRIMARY KEY NOT NULL,
    event VARCHAR NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    shipment VARCHAR NOT NULL REFERENCES Shipment(code)
);
