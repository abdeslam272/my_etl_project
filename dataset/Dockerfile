# Use the official PostgreSQL image
FROM postgres:latest

# Set environment variables for PostgreSQL
ENV POSTGRES_USER=my_user
ENV POSTGRES_PASSWORD=my_password
ENV POSTGRES_DB=my_database

# Create a directory for initialization scripts
COPY pagila-dataset/* /docker-entrypoint-initdb.d/
COPY export_to_csv.sh /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/export_to_csv.sh

# (Optional) Add the path to any SQL files if needed
COPY pagila-dataset/*.sql /docker-entrypoint-initdb.d/
