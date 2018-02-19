# Connecting to Compose for MySQL from a Python Flask App

## Package Dependencies

* flask
* mysql.connector

Run `pip3 install -r requirements.txt` to install required packages.

## Connection String

The connection string provided by your Compose for MySQL deployment should go into an environment variable `COMPOSE_MYSQL_URL`.
Download a copy of the certificate and put it's path in an environment variable `PATH_TO_MYSQL_CERT`.

## Running the Application

To run the app from the command-line, set and environment variable `FLASK_APP=mysql_example.py`, and use the `flask run` command in the same directory as the python file.