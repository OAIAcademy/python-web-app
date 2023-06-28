import flask
from flask import Flask, Response, request
from data_access.query import get_country_data, get_indicator_average, get_country_average

app = Flask(__name__)


@app.get('/country_data/<country_code>/<year>')  # defining a get endpoint
def country(country_code, year):
    return Response(content_type='application/json',
                    response=get_country_data(country_code,
                                              int(year)).to_json())  # returning a string in the http response


@app.get('/indicator_avg/<indicator_code>/<year>')  # defining a get endpoint
def average(indicator_code, year):
    return get_indicator_average(indicator_code, int(year))  # returning a string in the http response


@app.get('/country_avg/<country_code>/<indicator_code>')  # defining a get endpoint
def country_average(country_code, indicator_code):
    year_from = request.args.get("year-from", 0)
    year_to = request.args.get("year-to", 10000)
    return get_country_average(indicator_code, country_code,year_from,year_to)  # returning a string in the http response
