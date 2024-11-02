#!/bin/bash

# Wait for PostgreSQL to be ready
until pg_isready -h localhost -p 5432 -U "$POSTGRES_USER"; do
  echo "Waiting for PostgreSQL to start..."
  sleep 2
done

# Connect to the database and export tables to CSV
export PGPASSWORD=$POSTGRES_PASSWORD

# Specify the tables to export
tables=("film" "actor" "customer" "payment")  # Adjust table names as needed

for table in "${tables[@]}"; do
  psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "\COPY $table TO '/csv-output/${table}.csv' WITH CSV HEADER;"
done

echo "Data export to CSV completed."
