-- Insert dummy data into PRODUCT table
INSERT INTO Product (code, name) VALUES
('P1', 'Product 1'),
('P2', 'Product 2'),
('P3', 'Product 3'),
('P4', 'Product 4'),
('P5', 'Product 5'),
('P6', 'Product 6'),
('P7', 'Product 7'),
('P8', 'Product 8'),
('P9', 'Product 9'),
('P10', 'Product 10'),
('P11', 'Product 11'),
('P12', 'Product 12'),
('P13', 'Product 13'),
('P14', 'Product 14'),
('P15', 'Product 15'),
('P16', 'Product 16'),
('P17', 'Product 17'),
('P18', 'Product 18'),
('P19', 'Product 19'),
('P20', 'Product 20');

-- Insert dummy data into SUPPLYCHAIN table
INSERT INTO Supplychain (name) VALUES
('Supply Chain 1'),
('Supply Chain 2'),
('Supply Chain 3'),
('Supply Chain 4'),
('Supply Chain 5'),
('Supply Chain 6'),
('Supply Chain 7'),
('Supply Chain 8'),
('Supply Chain 9'),
('Supply Chain 10');

-- Insert dummy data into SHIPMENT table
INSERT INTO Shipment (code, supplychain, product, quantity, quantity_unit, acceptable_quality_lower_bound, acceptable_quality_upper_bound, expected_quality) VALUES
('S1', 1, 'P1', 100, 'kg', NULL, NULL, NULL),
('S2', 2, 'P2', 150, 'kg', NULL, NULL, NULL),
('S3', 3, 'P3', 200, 'kg', NULL, NULL, NULL),
('S4', 4, 'P4', 250, 'kg', NULL, NULL, NULL),
('S5', 5, 'P5', 300, 'kg', NULL, NULL, NULL),
('S6', 6, 'P6', 350, 'kg', NULL, NULL, NULL),
('S7', 7, 'P7', 400, 'kg', NULL, NULL, NULL),
('S8', 8, 'P8', 450, 'kg', NULL, NULL, NULL),
('S9', 9, 'P9', 500, 'kg', NULL, NULL, NULL),
('S10', 10, 'P10', 550, 'kg', NULL, NULL, NULL),
('S11', 1, 'P11', 600, 'kg', NULL, NULL, NULL),
('S12', 2, 'P12', 650, 'kg', NULL, NULL, NULL),
('S13', 3, 'P13', 700, 'kg', NULL, NULL, NULL),
('S14', 4, 'P14', 750, 'kg', NULL, NULL, NULL),
('S15', 5, 'P15', 800, 'kg', NULL, NULL, NULL),
('S16', 6, 'P16', 850, 'kg', NULL, NULL, NULL),
('S17', 7, 'P17', 900, 'kg', NULL, NULL, NULL),
('S18', 8, 'P18', 950, 'kg', NULL, NULL, NULL),
('S19', 9, 'P19', 1000, 'kg', NULL, NULL, NULL),
('S20', 10, 'P20', 1050, 'kg', NULL, NULL, NULL),
('S21', 1, 'P1', 1100, 'kg', NULL, NULL, NULL),
('S22', 2, 'P2', 1150, 'kg', NULL, NULL, NULL),
('S23', 3, 'P3', 1200, 'kg', NULL, NULL, NULL),
('S24', 4, 'P4', 1250, 'kg', NULL, NULL, NULL),
('S25', 5, 'P5', 1300, 'kg', NULL, NULL, NULL),
('S26', 6, 'P6', 1350, 'kg', NULL, NULL, NULL),
('S27', 7, 'P7', 1400, 'kg', NULL, NULL, NULL),
('S28', 8, 'P8', 1450, 'kg', NULL, NULL, NULL),
('S29', 9, 'P9', 1500, 'kg', NULL, NULL, NULL),
('S30', 10, 'P10', 1550, 'kg', NULL, NULL, NULL);

-- Insert dummy data into Shipment_Metadata table
INSERT INTO Shipment_Metadata (timestamp, shipment, latitude, longitude, temperature, quality) VALUES
('2024-03-20 08:00:00', 'S1', '40.7128', '-74.0060', '25°C', 95),
('2024-03-20 09:00:00', 'S1', '34.0522', '-118.2437', '22°C', 90),
('2024-03-20 10:00:00', 'S1', '51.5074', '-0.1278', '18°C', 85),
('2024-03-20 11:00:00', 'S1', '48.8566', '2.3522', '20°C', 80),
('2024-03-20 12:00:00', 'S1', '35.6895', '139.6917', '28°C', 75),
('2024-03-20 13:00:00', 'S1', '52.5200', '13.4050', '23°C', 70),
('2024-03-20 14:00:00', 'S2', '41.8781', '-87.6298', '27°C', 65),
('2024-03-20 15:00:00', 'S2', '55.7558', '37.6176', '15°C', 60),
('2024-03-20 16:00:00', 'S2', '37.7749', '-122.4194', '24°C', 55),
('2024-03-20 17:00:00', 'S3', '40.4168', '-3.7038', '19°C', 50),
('2024-03-20 18:00:00', 'S3', '52.3667', '4.8945', '21°C', 45);

-- Insert dummy data into Shipment_Event table
INSERT INTO Shipment_Event (timestamp, shipment, event)
VALUES
    ('2024-03-21T07:52:55', 'S1', 'Arrived at port'),
    ('2024-03-22T08:30:12', 'S1', 'Loaded onto truck'),
    ('2024-03-23T10:15:42', 'S1', 'In transit'),
    ('2024-03-24T12:45:21', 'S1', 'Arrived at warehouse'),
    ('2024-03-25T15:20:36', 'S1', 'Delivered to customer'),
    ('2024-03-21T07:52:55', 'S2', 'Arrived at port'),
    ('2024-03-22T08:30:12', 'S2', 'Loaded onto truck'),
    ('2024-03-23T10:15:42', 'S2', 'In transit');

-- Insert dummy data into Person table
INSERT INTO Person (username, email, password, first_name, last_name, address, phone, organisation) VALUES
('john_doe', 'john@example.com', 'password123', 'John', 'Doe', '123 Main St, Anytown, USA', '123-456-7890', 'Company A'),
('jane_smith', 'jane@example.com', 'password456', 'Jane', 'Smith', '456 Elm St, Othertown, USA', '987-654-3210', 'Company B'),
('alice_jackson', 'alice@example.com', 'password789', 'Alice', 'Jackson', '789 Oak St, Anycity, USA', '456-789-0123', 'Company C'),
('bob_johnson', 'bob@example.com', 'passwordabc', 'Bob', 'Johnson', '321 Maple St, Othercity, USA', '789-012-3456', 'Company D'),
('susan_williams', 'susan@example.com', 'passwordxyz', 'Susan', 'Williams', '654 Pine St, Anyvillage, USA', '012-345-6789', 'Company E');

-- Insert dummy data into Certificate table
INSERT INTO Certificate (timestamp, shipment, issuer, pdf_path, pdf_hash) VALUES
('2024-03-25 10:00:00', 'S1', 'john_doe', '/app/certificates/test.pdf', '1358251341bd5fe67118d310e088e33353e2bc10151ac2eb14aac0aab164db61');

-- Insert dummy data into Sensor_Health_Monitoring_Device table
INSERT INTO Sensor_Health_Monitoring_Device (code, shipment, description) VALUES
('SHM001', 'S1', 'Temperature Sensor'),
('SHM002', 'S2', 'Humidity Sensor'),
('SHM003', 'S3', 'Shock Sensor');

-- Insert dummy data into Sensor_Health_Monitoring_Device_Event table
INSERT INTO Sensor_Health_Monitoring_Device_Event (sensor_health_monitoring_device, timestamp, remarks) VALUES
('SHM001', '2024-03-21T08:00:00', 'Sensor activated'),
('SHM001', '2024-03-22T10:30:00', 'Temperature within acceptable range'),
('SHM001', '2024-03-23T14:45:00', 'Temperature slightly elevated, but still within range'),
('SHM001', '2024-03-24T18:15:00', 'Temperature returned to normal'),
('SHM002', '2024-03-21T09:15:00', 'Sensor activated'),
('SHM002', '2024-03-22T12:00:00', 'Humidity levels normal'),
('SHM002', '2024-03-23T16:30:00', 'Humidity levels slightly high, but still within range'),
('SHM002', '2024-03-24T20:00:00', 'Humidity levels returned to normal'),
('SHM003', '2024-03-21T10:45:00', 'Sensor activated'),
('SHM003', '2024-03-22T14:20:00', 'No significant shocks detected'),
('SHM003', '2024-03-23T18:10:00', 'Minor shock detected, but within acceptable limits'),
('SHM003', '2024-03-24T22:30:00', 'No shocks detected');