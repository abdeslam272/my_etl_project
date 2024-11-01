# Start with the official PostgreSQL image
FROM postgres:latest

# Environment variables for PostgreSQL
ENV POSTGRES_USER=my_user
ENV POSTGRES_PASSWORD=my_password
ENV POSTGRES_DB=pagila

# Copy the SQL file into the container
COPY pagila-dataset/pagila-data.sql /docker-entrypoint-initdb.d/

# By default, PostgreSQL runs any scripts in /docker-entrypoint-initdb.d/ at startup.
# This will load the pagila dataset when the container is initialized.
