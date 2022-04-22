from flask import request_finished
import requests

def ipaddressloc(ip):
    url = "http://ipinfo.io/" + ip + "/json"
    result = requests.get(url)
    if ip != "":
        if result.status_code == 200:
            data = result.json()
            loc=data['loc']
            geolocation = "https://www.google.com.ph/maps/@" + loc + ",15z"
            return geolocation
        geolocation = "https://www.google.com.ph"
        return geolocation
    geolocation = "https://www.google.com.ph"
    return geolocation