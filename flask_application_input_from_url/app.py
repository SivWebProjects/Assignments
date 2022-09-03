# Setup a flask server with an endpoint '/function' in Local Host to serve the myFunction which
# takes input and function return value will be strings.

from markupsafe import escape
from flask import Flask
import os

app = Flask(__name__)
print(__name__)


@app.route('/')
def hello():
    return '<h1>Hi! This is a Flask web application.</h1>'


@app.route('/function/<word>/')
def myFunction(word):
    return '<h1>{} is your entered input.</h1>'.format(escape(word))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
