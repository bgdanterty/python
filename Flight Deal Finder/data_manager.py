import requests
from requests.auth import HTTPBasicAuth

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/2126ff04ad89ea8ebb5025b7b7e7441d/flightDeals/prices/"
BASIC = HTTPBasicAuth('bgdanterty', 'bod3563993')


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        endpoint = "https://api.sheety.co/2126ff04ad89ea8ebb5025b7b7e7441d/flightDeals/prices"
        response = requests.get(url=endpoint, auth=BASIC)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data


    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=BASIC
            )