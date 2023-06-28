import flask
from flask import Flask, Response, request
from data_access.query import get_country_data, get_indicator_average, get_country_average
from service.auth import check_password

app = Flask(__name__)


# catch reqeust and check authentication before passing request to "real" endpoints
@app.before_request
def auth():
    try:
        if not check_password(request.headers.get("token")):
            return Response("Invalid token", status=403)
    except Exception as e:
        return Response("No auth token", status=403)


@app.get('/country_data/<country_code>/<year>')
def country(country_code, year):
    # convert df to json and return
    return Response(content_type='application/json',
                    response=get_country_data(country_code,
                                              int(year)).to_json())


@app.get('/indicator_avg/<indicator_code>/<year>')
def average(indicator_code, year):
    return get_indicator_average(indicator_code, int(year))


@app.get('/country_avg/<country_code>/<indicator_code>')
def country_average(country_code, indicator_code):
    year_from = request.args.get("year-from", 0) # read arguments and give default
    year_to = request.args.get("year-to", 10000)
    return get_country_average(indicator_code, country_code, year_from,
                               year_to)
