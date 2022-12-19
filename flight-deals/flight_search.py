import requests
import datetime

api_endpoint = "http://tequila-api.kiwi.com"

headers = {
    "apikey": "4TA90l76BghgCKCKVtnLDteZ0Z84UKG_"
}

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, city_name):
        self.flight_to = city_name

    def search_code(self):
        get_code_json = {
            "term": f"{self.flight_to}",
            "location_types": "city",
        }
        response_get_code = requests.get(url=api_endpoint, headers=headers, json=get_code_json)
        return response_get_code.text

    def search_flight(self):
        tommorow_time = datetime.datetime.today() + datetime.timedelta(days=1)
        date_from = tommorow_time.strftime("%d/%m/%Y")

        end_time = tommorow_time + datetime.timedelta(days=180)
        date_to = end_time.strftime("%d/%m/%Y")

        round_trip_min = tommorow_time + datetime.timedelta(days=7)
        return_from = round_trip_min.strftime("%d/%m/%Y")

        round_trip_max = tommorow_time + datetime.timedelta(days=28)
        return_to = round_trip_max.strftime("%d/%m/%Y")

        currency = "GBP"

        search_json = {
            "fly_from": "LON",
            "fly_to": f"{self.flight_to}",
            "date_from": f"{date_from}",
            "date_to": f"{date_to}",
            "return_from": f"{return_from}",
            "return_to": f"{return_to}",
            "curr": currency,
        }

        response_search_flight = requests.get(url=f"{api_endpoint}/search", headers=headers, json=search_json)
        print(response_search_flight.text)
        return date_from
