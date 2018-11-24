from random import random

import requests
import json

latitude = 42.9842 # 42N
longitude = -81.2487 # 81W
url = "https://api.yelp.com/v3/businesses/search"

querystring = {"term":"pizza","latitude":str(latitude),"longitude":str(longitude),"radius":"5000","price":"1"}

headers = {
    'authorization': "Bearer L4RBBm1-rBl8-4LwvRXLGCK2vlnsStli1zQ3gHCPqFEp-qpMEQSD1exxFgMwIDMY56UqdLwnNCrSi9kuPAbhntjY2rDesyRr29n-PqEcIWPlzk1NgQQ8tpHxhJD5W3Yx",
    'cache-control': "no-cache",
    'postman-token': "771cd1a1-8bdf-0dcd-b7fe-8ea1c297602e"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

json_response = response.text

parsed_json_response = json.loads(json_response)

cheap_businesses = []
for business in parsed_json_response["businesses"]:
    if business["price"] == "$":
        cheap_businesses.append(business["name"])

print (cheap_businesses[0])