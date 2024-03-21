FROM postgres:latest

# Configure IST Timezone
ENV TZ="Asia/Kolkata"

# Copy the schema.sql file into the container
COPY schema.sql /docker-entrypoint-initdb.d/01_schema.sql

# Copy the dummy_data.sql file into the container
COPY dummy_data.sql /docker-entrypoint-initdb.d/02_dummy_data.sql