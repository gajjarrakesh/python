# Connecting to PostgreSQL from a Python Flask App

## Package Dependencies

* psycopg2
* flask

Run `pip3 install -r requirements.txt` to install required packages.

## Connection String

The connection string provided by your Compose PostgreSQL deployment should go into an environment variable `COMPOSE_POSTGRES_URL`.
Download a copy of the certificate and put it's path in an environment variable `PATH_TO_POSTGRESQL_CERT`.

## Running the Application

To run the app from the command-line, set and environment variable `FLASK_APP=postgresql_example.py`, and use the `flask run` command in the same directory as the python file.
