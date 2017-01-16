import json
import os

import requests

KEY = os.environ.get('WUNDERGROUND_KEY')
URL = 'http://api.wunderground.com/api/%s' % KEY


class Weather(object):

    def __init__(self, zip_code):
        super(Weather, self).__init__()
        self.zip_code = zip_code

    def get_current(self):
        data = get_data_from_zipcode('/conditions/q/%s.json' % self.zip_code)
        return data['current_observation']

    def get_current_text(self):
        data = self.get_current()
        return '%s %s' % (self.get_current_temp(data), self.get_current_humidity(data))

    def get_three_day_forecast(self):
        data = get_data_from_zipcode('/forecast/q/%s.json' % self.zip_code)
        days = data['forecast']['txt_forecast']['forecastday']
        text = ''
        for d in days:
            text += '%s: %s\n' % (d['title'], d['fcttext'])
        return text

    def get_ten_day_forecast(self):
        data = get_data_from_zipcode(
            '/forecast10day/q/%s.json' % self.zip_code)
        days = data['forecast']['txt_forecast']['forecastday']
        text = ''
        for d in days:
            text += '%s: %s\n' % (d['title'], d['fcttext'])
        return text

    def get_current_temp(self, data):
        temp = data['temperature_string']
        return 'The current temp is %s. ' % temp

    def get_current_humidity(self, data):
        return 'With %s humidity' % data['relative_humidity']

    def get_commands(self):
        return {
            'get current weather': self.get_current_text,
            'get three day forecast': self.get_three_day_forecast,
            'get ten day forecast': self.get_ten_day_forecast,
        }


def get_data_from_zipcode(url):
    url = URL + url
    req = requests.get(url)
    data = req.json()
    return data
