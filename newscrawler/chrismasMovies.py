from flask import Flask
from flask import render_template
import pymongo

client = pymongo.MongoClient()
data_films = client['allocine']
collection = data_films['filmNoel']

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return "ERROR"

@app.route('/') 
def home_page():
    return render_template('index.html')

@app.route('/') 
def search_page():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=2745) 