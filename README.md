# The Grand Tour - Python

A set of example applications that will add word/definition pairs to a database running on Compose.

Find the articles about the Python section of the Compose Grand Tour here:

* [Python and Compose - MongoDB, Elasticsearch and PostgreSQL](https://www.compose.com/articles/python-and-compose-mongodb-elasticsearch-and-postgresql/)
* [Python and Compose - Redis, RethinkDB, and RabbitMQ](https://www.compose.com/articles/python-and-compose-redis-rethinkdb-and-rabbitmq/)
* [Python and Compose - Scylla and Compose for MySQL](https://www.compose.com/articles/python-and-compose-scylla-and-compose-for-mysql/)

This repo contains the apps written in Python 3.6.0 and uses the Flask web framework.

## Running the Example

To run from the command-line:

* navigate to the example-<_db_> directory
* export your Compose connection string as an environment variable
* set the flask app variable: `export FLASK_APP=<_db_>_example.py`
* and then: `flask run`

The application will be served on 127.0.0.1:5000 and can be opened in a browser.
