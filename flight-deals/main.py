from data_manager import DataManager
from flight_search import FlightSearch

sheety = DataManager()
sheet_data = sheety.data()
print(sheet_data)

# for each in sheet_data:
#     if each["iataCode"] == "":
#         search_flight = FlightSearch(each["city"])
#         new_code = search_flight.search_code()
#
#         print(new_code)

        # each["iataCode"] = new_code
        # sheety.update_code(each["id"], each["iataCode"])

