import flask
from flask import Flask, Response
from data_access.query import get_country_data

app = Flask(__name__)


@app.get('/country_data/<country_code>/<year>')  # defining a get endpoint
def hello(country_code, year):
    return flask.Response(content_type='application/json',
                          response=get_country_data(country_code,
                                                    int(year)).to_json())  # returning a string in the http response
