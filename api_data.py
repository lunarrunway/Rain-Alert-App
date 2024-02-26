# TODO 1 try to get a basic call and see what it returns so I can get it working properly
# TODO 2 may need to learn about the geocoder to translate city to lat and lon coding properly
# TODO 3 may be really cool to look at the solar info one, says it can predict solar generation!

import requests
import datetime as dt

OWAPIKEY = "c12e906204c3c91a1a80432db52b73aa"
OWENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
GCENDPOINT = "http://api.openweathermap.org/geo/1.0/direct"

geo_code_parameters = {
    "q": "Nanaimo, CA",
    "appid": OWAPIKEY,
}


def geocode_api_call():
    geocode_response = requests.get(url=GCENDPOINT, params=geo_code_parameters)
    geocode_response.raise_for_status()
    geo_data = geocode_response.json()
    city_lat = float(geo_data[0]["lat"])
    city_lon = float(geo_data[0]["lon"])
    return city_lat, city_lon


geo_tuple = geocode_api_call()

ow_parameters = {
    "lat": geo_tuple[0],
    "lon": geo_tuple[1],
    "appid": OWAPIKEY,
    "exclude": ['current','minutely','hourly','alerts'],
    "units": "metric"
}

ow_response = requests.get(url=f"https://api.openweathermap.org/data/3.0/onecall?"
                               f"lat={ow_parameters['lat']}&"
                               f"lon={ow_parameters['lon']}&"
                               f"exclude={ow_parameters['exclude']}&"
                               f"appid={ow_parameters['appid']}"
                           )
ow_response.raise_for_status()
print(type(ow_response))
print(ow_response.json())

# TODO try to figure out what format of data I'm getting back from open weather, it's giving single quote json
#  style but I can't use that without double quotes so what's the solution
# ts = int(ow_response["current"]["dt"])
# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case
# print(dt.datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))

