import requests
from pprint import pprint

SHEET_GET_URL = "https://api.sheety.co/0d6e2ed4f1956a05037825f71abfc856/flightDeals/prices"
SHEET_USER_NAME = "24pigboqf"
SHEET_PASSWORD = "wsg25YS45shg"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.response_add = requests.get(url=SHEET_GET_URL, auth=(SHEET_USER_NAME, SHEET_PASSWORD))

    def data(self):
        self.data = self.response_add.json()
        # sheet_data = self.data["prices"]
        return self.data

    def update_code(self, row_number, iata_code):

        change_body = {
            "price": {
                "iataCode": iata_code,
            }
        }

        sheet_edit = f"https://api.sheety.co/0d6e2ed4f1956a05037825f71abfc856/flightDeals/prices/{row_number}"
        self.response_edit = requests.put(url=sheet_edit, auth=(SHEET_USER_NAME, SHEET_PASSWORD), json=change_body)
