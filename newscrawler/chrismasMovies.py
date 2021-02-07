from flask import Flask
from flask import render_template, request
import json
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

LOCAL = True
es_client = Elasticsearch(hosts=["localhost" if LOCAL else "elastic"])
es_client.indices.delete(index='movies', ignore= [400,404])

with open('dataFin.json') as json_data:
    v = json.load(json_data)


def generate_data_exemple(documents):
    for docu in documents:
        yield {
            "_index": "movies",
            "_type": "movie",
            "_source": {k: v if v else None for k, v in docu.items()},
        }

bulk(es_client, generate_data_exemple(v))

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return "ERROR"


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/search_page/', methods=['GET', 'POST'])
def search_page():

    response = []
    for document in v:
        response.append(document)

    if request.method == 'POST':
        search = request.form["input"]

        def search_by_word(film):
            QUERY = {
                "query": {
                    "multi_match": {
                        "query":    film,
                        "fields": ["titre", "overview"]
                    }
                }
            }
            result = es_client.search(index="movies", body=QUERY)
            return result

        return render_template('elements.html', res=search_by_word(search))
    else:
        return render_template("elements.html", movies=response)


@app.route('/info_page/')
def info_page():

    QUERY = {
        "sort": [
            {"Evaluation spectateur": {"order": "desc"}},
        ],
        "query": {
            "match_all": {}
        }
    }
    result = es_client.search(index="movies", body=QUERY)

    return render_template('generic.html', res=result)

if __name__ == '__main__':
    #app.run(debug=True, port=5000)
    app.run(host='localhost')
    #app.run()
