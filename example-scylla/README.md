# Connecting to Scylla from a Python Flask App

## Package Dependencies

* flask
* cassandra_driver

Run `pip3 install -r requirements.txt` to install required packages.

## Connection String and Certificate

The three connection strings provided by your Compose Scylla deployment should be comma separated and set in an environment variable `COMPOSE_SCYLLA_URLS`. The code will parse the hostnames, port, and credentials.

Download a copy of the [validation chain certificate](https://help.compose.com/docs/scylla-and-certificates) from the Compose help and put its path in an environment variable `PATH_TO_SCYLLA_CERT`.

## Running the Application

To run the app from the command-line, set and environment variable `FLASK_APP=scylla_example.py`, and use the `flask run` command in the same directory as the python file.