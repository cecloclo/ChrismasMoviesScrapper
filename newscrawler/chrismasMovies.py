from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return "ERROR"

@app.route('/') 
def home_page():
    return render_template('index.html')

@app.route('/search_page/') 
def search_page():
    return render_template('elements.html')

@app.route('/info_page/') 
def info_page():
    return render_template('generic.html')

if __name__ == '__main__':
    #app.run(debug=True, port=2745)
    app.run(host='0.0.0.0')