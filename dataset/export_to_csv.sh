#!/bin/bash
# Wait for PostgreSQL to be ready
sleep 10

# Export each table to CSV
psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" <<EOF
\copy actor TO '/app/exports/actor.csv' CSV HEADER;
\copy film TO '/app/exports/film.csv' CSV HEADER;
EOF
