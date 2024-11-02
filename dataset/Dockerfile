# Use the official PostgreSQL image
FROM postgres:latest

# Set environment variables for PostgreSQL
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=pagila

# Copy the SQL file and the export script into the initialization directory
COPY pagila-dataset/pagila_data.sql /docker-entrypoint-initdb.d/
COPY export_to_csv.sh /docker-entrypoint-initdb.d/

# Give execute permissions to the export script
RUN chmod +x /docker-entrypoint-initdb.d/export_to_csv.sh
