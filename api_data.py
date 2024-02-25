import json

import requests


parameters = {
    "api_key": "c12e906204c3c91a1a80432db52b73aa",
    "q": "Courtney",
    "Country": "CA"
}

ENDPOINT = "api.openweathermap.org"
# example api call format : api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=c12e906204c3c91a1a80432db52b73aa

# response = requests.get(url=ENDPOINT, params=)
# TODO Below is returning 401 unauthorized I guess it's not the one call site so I do need to do some reading
# TODO this seems to be the breakdown site for what I need: https://openweathermap.org/api/one-call-3#current
    # TODO 1 try to get a basic call and see what it returns so I can get it working properly
    # TODO 2 may need to learn about the geocoder to translate city to lat and lon coding properly
    # TODO 3 may be really cool to look at the solar info one, says it can predict solar generation!

response = requests.get(url="https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=c12e906204c3c91a1a80432db52b73aa")
response.raise_for_status()
data = response.json()
load = json.loads(data)
easy_read = json.dumps(load, indent=1)
print(easy_read)
