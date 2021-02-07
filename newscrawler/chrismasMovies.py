from flask import Flask
from flask import render_template
#from elasticsearch import Elasticsearch
#from elasticsearch.helpers import bulk
#import json

# LOCAL = True
# es_client = Elasticsearch(hosts=["localhost" if LOCAL else "elastic"])

# with open('dataF.json') as json_data:
#     v = json.load(json_data)


# def generate_data_exemple(documents):
#     for docu in documents:
#         yield {
#             "_index": "movies",
#             "_type": "movie",
#             "_source": {k: v if v else None for k, v in docu.items()},
#         }


# bulk(es_client, generate_data_exemple(v))

# def search_by_eval(eval):
#   QUERY = {
#      "query": {
#          "match": {
#              "fields.eval_spect": eval
#              }
#          }
#      }
# result = es_client.search(index="movies", body=QUERY)
# return [elt['_source']['eval_spect']  for elt in result["hits"]["hits"]]

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return "ERROR"


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/search_page/')#, methods=['GET', 'POST'])
def search_page():
    return render_template('elements.html')


@app.route('/info_page/')
def info_page():
    return render_template('generic.html')

    # QUERY = {
    #     "query": {
    #         "match": {
    #             #"fields": {'titre'          }
    #             "sort": [
    #                 {"Evaluation spectateur": {"order": "desc"}}
    #                 ]
    #         }
    #     },
    # }
    # result = es_client.search(index="movies", body=QUERY)
    # {elt['_source']['title']: elt['_source']['popularity'] for elt in result["hits"]["hits"]}
    # return render_template('generic.html')

if __name__ == '__main__':
    #app.run(debug=True, port=5000)
    app.run(host='0.0.0.0')
