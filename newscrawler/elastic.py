import pandas as pd
import numpy as np
import json

from elasticsearch import Elasticsearch
LOCAL = True
es_client = Elasticsearch(hosts=["localhost" if LOCAL else "elasticsearch"], port=9200)

es_client.ping()

with open('data2.json') as json_data:
    v = json.load(json_data)

QUERY = {
  "query": {
    "multi_match" : {
      "query":    "Smith",
      "fields": [ "title", "overview" ] 
    }
  },
    "sort" : [
        { "popularity" : {"order" : "desc"}}
    ]
}

result = es_client.search(index="movies", body=QUERY)
{elt['_source']['title']:elt['_source']['popularity']  for elt in result["hits"]["hits"]}