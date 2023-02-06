import requests
import json
from flask import Flask, jsonify
import api_keys

app = Flask(__name__)

# Places API key, global variable
api_key = api_keys.places

def get_shopping(coordinates,radius):
    location = coordinates
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&type=shopping_mall&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        shopping_malls = data["results"]
        names=[]
        for shopping_mall in shopping_malls:
            name=shopping_mall.get("name","N/A")
            names.append(name)
    else:
        return(f"Request failed with status code {response.status_code}")

    return names
    

#print(get_shopping("33.755960,-84.405130",5000))
