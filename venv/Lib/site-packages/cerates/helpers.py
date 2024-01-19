import requests
import sys
from datetime import datetime


def get_json(end_point, params):
    '''
    Make request to http://api.fixer.io/
    '''

    try:

        r = requests.get(end_point, params=params)

    except requests.exceptions.RequestException as e:

        print(e)

        sys.exit(1)

    return r.json()


def vali_date(date):
    '''
    Validate the date in the format YYYY-MM-DD

    Eg "2017-02-27"

    '''

    try:

        datetime.strptime(date, '%Y-%m-%d')

        return True

    except ValueError:

        return False


def current_date():

    return datetime.now().strftime("%Y-%m-%d")
