import json

from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Docker Training</h1><p>Enjoy version 1.0</p>"


@app.route('/api/', methods=['GET'])
def rest():
    mydict = {1: 'python', 
              2: 'docker'}
    return mydict

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
