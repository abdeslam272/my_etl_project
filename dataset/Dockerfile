# Start with the official PostgreSQL image
FROM postgres:latest

# Set environment variables for PostgreSQL
ENV POSTGRES_USER=my_user
ENV POSTGRES_PASSWORD=my_password
ENV POSTGRES_DB=pagila

# Create an exports directory for CSV files
RUN mkdir -p /app/exports

# Copy the Pagila dataset into the Docker image
COPY pagila-dataset/pagila-data.sql /docker-entrypoint-initdb.d/pagila-data.sql

# Install bash to ensure the script can run
RUN apt-get update && apt-get install -y bash && rm -rf /var/lib/apt/lists/*

# Copy the export_to_csv.sh script to the initialization directory
COPY export_to_csv.sh /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/export_to_csv.sh
