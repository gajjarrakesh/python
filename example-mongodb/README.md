# Connecting to MongoDB from a Python Flask App

## Package Dependencies

* flask
* pymongo

Run `pip3 install -r requirements.txt` to install required packages.

## Connection String

The connection string provided by your Compose MongoDB deployment should go into an environment variable `MONGODB_URL`.

## Running the Application

To run the app from the command-line, set and environment variable `FLASK_APP=mongodb-example.py`, and use the `flask run` command in the same directory as the python file.
