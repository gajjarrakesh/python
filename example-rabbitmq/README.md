# example-rabbitmq

A Compose Grand Tour example for Python, RabbitMQ

## Connecting to RabbitMQ from a Python Flask App

## Package Dependencies

* flask
* pika

Run `pip3 install -r requirements.txt` to install required packages.

### Connection String

The connection string provided by your Compose Redis deployment should go into an environment variable `COMPOSE_RABBITMQ_URL`.

### Running the Application

To run the app from the command-line, set and environment variable `FLASK_APP=rabbitmq_example.py`, and use the `flask run` command in the same directory as the python file.