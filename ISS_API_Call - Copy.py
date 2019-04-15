import urllib.parse
import requests
import time

url = 'http://api.open-notify.org/iss/v1/?lat=11.411860&lon=76.710200'
json_data = requests.get(url).json()
print(json_data)
epoch = json_data['response'][0]['risetime']
next_pass = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(epoch))
print("The next ISS pass will be: " + (next_pass))
