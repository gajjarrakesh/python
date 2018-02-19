# Connecting to Elasticsearch from a Python Flask App

## Package Dependencies

* flask
* elasticsearch

Run `pip3 install -r requirements.txt` to install required packages.

## Connection String

The connection string provided by your Compose Elastcisearch deployment should go into an environment variable `COMPOSE_ELASTICSEARCH_URL`.

## Running the Application

To run the app from the command-line, set and environment variable `FLASK_APP=elasticsearch-example.py`, and use the `flask run` command in the same directory as the python file.
