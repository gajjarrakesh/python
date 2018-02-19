# Connecting to Redis from a Python Flask App

## Package Dependencies

* flask
* redis

Run `pip3 install -r requirements.txt` to install required packages.

## Connection String

The connection string provided by your Compose Redis deployment should go into an environment variable `COMPOSE_REDIS_URL`.

## Running the Application

To run the app from the command-line, set and environment variable `FLASK_APP=redis_example.py`, and use the `flask run` command in the same directory as the python file.
