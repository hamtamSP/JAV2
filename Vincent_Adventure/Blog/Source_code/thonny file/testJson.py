{
    "username": "wifiuser",
    "password": "wifipass",
    "api_key": "googlemapsapikey"
}

import ujson as json

with open("/flash/settings.json") as fp:
    settings = json.loads(fp.read())