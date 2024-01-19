"""

Copyright @ 2017 

Akshay

"""

from . import helpers


class Cerates(object):
    """
    Cerates is a python module for foreign exchange rates and currency conversion.
    """

    end_point = 'http://api.fixer.io/'

    def __init__(self):
        '''
        Constructor to creata a new Erail object.

        Params : 
        +++++++

        '''

        self.base = ""
        self.date = ""
        self.rates = ""

    def get_rates(self, base="EUR", date=helpers.current_date(), symbols=None):

        """
        Get the foreign exchange rates.By defult rates will be shown of current date.

        Eg >

        >>> cer = Cerates()
        >>> cer.get_rates()
        >>> cer.rates
        >>> {"AUD": 1.3796, "BGN": 1.9558, ...}

        Optional Arguments :

            base    :: Get currency rates according to this base.
            date    :: Get currency rates according to this date.
            symbols :: Get currency rates for this list of symbols only.

        Eg >

        >>> cer = Cerates()
        >>> cer = Cerates()

        >>> cer.get_rates(symbols=["INR","USD"], date="2009-02-24", base="CNY")

        >>> cer.rates
        >>> {'INR': 7.3008, 'USD': 0.14626}

        """

        try:

            assert helpers.vali_date(date) == True

        except AssertionError:

            return "Invalid Date Format, must be 'YYYY-MM-DD'"

        if symbols is None:

            symbols = []

        elif symbols:

            symbols = ",".join(symbols)

        params = {

            'base': base,
            'symbols': symbols

        }

        url = self.end_point + date

        return self.get_result(url, params)

    def get_result(self, url, params):
        '''
        Get result from the JSON response
        '''
        response = helpers.get_json(url, params)

        self.base = response.get("base", None)
        self.date = response.get("date", None)
        self.rates = response.get("rates", None)
