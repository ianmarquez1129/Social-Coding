from flask import request_finished
import requests

def ipaddressinfo(ip):
    url = "https://ipapi.co/" + ip + "/json"
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    url = "http://ip-api.com/json/" + ip
    result = requests.get(url)
    return result.json()

