import os
import psycopg2
import pandas as pd


def get_connection():
    # connect to db
    return psycopg2.connect(
        user=os.environ.get("DB_USER"),  # get conf from env
        password=os.environ.get("DB_PSW"),  # particularly important for the
        host=os.environ.get("DB_HOST"),
        database=os.environ.get("DB_NAME"))


def get_indicator_average(indicator_code: str, year: int) -> str:
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''select r.indicator_code, avg(r.indicator_value)
                                  from records as r
                                  where r.indicator_code = %(country_code)s and year = %(year)s
                                  group by r.indicator_code''',
                           {'country_code': indicator_code,
                            "year": year})  # query is parametric, this also obtain sanitization
            return str(cursor.fetchone()[1])


def get_country_average(indicator_code: str, country_code: int, year_from: int, year_to: int) -> str:
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''select avg(r.indicator_value)
                              from records as r
                              where r.indicator_code = %(indicator_code)s 
                                    and r.country_code=%(country_code)s
                                    and r.year >= %(year_from)s
                                    and r.year <= %(year_to)s
                              group by r.indicator_code,r.country_code''',
                           {'indicator_code': indicator_code,
                            "country_code": country_code,
                            'year_from': year_from,
                            'year_to': year_to
                            })
            return str(cursor.fetchone()[0])


def get_country_data(country_code: str, year: int) -> pd.DataFrame:
    with get_connection() as conn:
        # direct sql to pandas df
        return pd.read_sql('''select i.indicator_code,r.indicator_value,i.short_definition,i.long_definition
                                from records as r
                                join indicators i on r.indicator_code = i.indicator_code
                                where country_code = %(country_code)s and r.year = %(year)s
                                order by r.year ''',
                           conn, params={'country_code': country_code, "year": year})
