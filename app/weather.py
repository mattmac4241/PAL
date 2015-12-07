import requests
import json 

KEY = '2a414f8ccd5023fa'
URL = 'http://api.wunderground.com/api/%s' % KEY

#get current conditions
def get_current(zipCode):
    url = URL + '/conditions/q/%s.json' % zipCode
    req = requests.get(url)
    data = req.json()
    return data['current_observation']

def get_current_temp(data):
    temp = data['temperature_string']
    return 'The current temp is %s. ' % temp

def get_current_humidity(data):
    return 'With %s humidity' % data['relative_humidity']

def get_current_text(zipCode):
    data = get_current(zipCode)
    return '%s %s' % (get_current_temp(data),get_current_humidity(data))

def get_three_day_forecast(zipCode):
    url = URL + '/forecast/q/%s.json' % zipCode
    req = requests.get(url)
    data = req.json()
    days = data['forecast']['txt_forecast']['forecastday']
    text = ''
    for d in days:
        text+= '%s: %s\n' % (d['title'],d['fcttext'])
    return text    

def get_ten_day_forecast(zipCode):
    url = URL + '/forecast10day/q/%s.json' % zipCode
    req = requests.get(url)
    data = req.json()
    days = data['forecast']['txt_forecast']['forecastday']
    text = ''
    for d in days:
        text+= '%s: %s\n' % (d['title'],d['fcttext'])
    return text    

#check if zipcode is valid using geolookup
def valid_zip_code(zipCode):
    url = URL + '/geolookup/q/%s.json' % zipCode
    req = requests.get(url)
    data = req.text
    if 'error' in data:
        return False
    else:
        return True


print valid_zip_code(60453)
print valid_zip_code(00000)