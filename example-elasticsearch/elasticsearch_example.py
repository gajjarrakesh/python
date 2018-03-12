"""Elasticsearch example for Compose Python Grand Tour"""

import os
from urllib.parse import urlparse
import json

from flask import Flask
from flask import render_template
from flask import request

from elasticsearch import Elasticsearch


app = Flask(__name__)

# connection string and connection initialization
compose_elasticsearch_url = os.environ['COMPOSE_ELASTICSEARCH_URL']
url1,url2 = compose_elasticsearch_url.split(",")

cstr1 = urlparse(url1)
cstr2 = urlparse(url2)

es = Elasticsearch(
    [cstr1.hostname, cstr2.hostname],
    http_auth=(cstr1.username, cstr1.password),
    port=cstr1.port,
    use_ssl=True,
    verify_certs=True
)

# index access/creation
if not es.indices.exists(index="words"):
    es.indices.create(index="words")


@app.route('/')
# top-level page display
def serve_page():
    return render_template('index.html')


@app.route('/words', methods=['PUT'])
# triggers on hitting the 'Add' button; inserts word/definition into index, refreshes index
def handle_words():
    new_word = {"word":request.form['word'], "definition":request.form['definition']}
    # Insert the new word into the index
    es.index(index="words", doc_type="word", body=new_word)
    # Refresh index.
    es.indices.refresh(index="words")
    return ('', 204)


@app.route('/words', methods=['GET'])
# query for all the words in the index, returns as json for display on the page.
def display_search():
    # Run a search for all existing words
    res = es.search(index="words", doc_type="word", body={})
    #Pull the word object from each hit in the search results
    hit_list = (res['hits']['hits'])
    # List word objects, appending the contents from the search hit's _source field.
    words_list = []
    for hit in hit_list:
        words_list.append(hit['_source'])
    # JSON-ify the list of words.
    return json.dumps(words_list)


if __name__ == "__main__":
    app.run()
