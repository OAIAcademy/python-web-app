import os
import psycopg2
import pandas as pd


def get_connection():
    return psycopg2.connect(
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PSW"),
        host=os.environ.get("DB_HOST"),
        database=os.environ.get("DB_NAME"))


def get_country_data(country_code: str,year:int):
    with get_connection() as conn:
        return pd.read_sql('''select i.indicator_code,r.indicator_value,i.short_definition,i.long_definition
                                from records as r
                                join indicators i on r.indicator_code = i.indicator_code
                                where country_code = %(country_code)s and r.year = %(year)s
                                order by r.year ''',
                           conn, params={'country_code': country_code,"year":year})
