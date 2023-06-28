import flask
from flask import Flask, Response
from data_access.query import get_country_data, get_indicator_average

app = Flask(__name__)


@app.get('/country_data/<country_code>/<year>')  # defining a get endpoint
def country(country_code, year):
    return flask.Response(content_type='application/json',
                          response=get_country_data(country_code,
                                                    int(year)).to_json())  # returning a string in the http response


@app.get('/indicator_avg/<indicator_code>/<year>')  # defining a get endpoint
def average(indicator_code, year):
    return get_indicator_average(indicator_code, int(year))  # returning a string in the http response
