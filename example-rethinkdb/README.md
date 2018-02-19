# Connecting to RethinkDB from a Python Flask App

## Package Dependencies

* flask
* rethinkdb

Run `pip3 install -r requirements.txt` to install required packages.

## Connection String and Certificate

The connection string provided by your Compose RethinkDB deployment should go into an environment variable `COMPOSE_RETHINKDB_URL`.
Download a copy of the certificate and put it's path in an environment variable `PATH_TO_RETHINKDB_CERT`

## Running the Application

To run the app from the command-line, set and environment variable `FLASK_APP=rethinkdb_example.py`, and use the `flask run` command in the same directory as the python file.
