import requests
import json
import datetime as dt
from datetime import timedelta
import pprint
import os
from dotenv import load_dotenv

load_dotenv()


TEQUILA_ID=os.getenv('TEQUILA_ID')
TEQUILA_KEY=os.getenv('TEQUILA_KEY')
TEQUILA_ENDPOINT="https://tequila-api.kiwi.com/locations/query"
TEQUILA_ENDPOINT_SEARCH="https://tequila-api.kiwi.com/v2/search"
HEADERS={
    "apikey":TEQUILA_KEY,
    "accept": "application/json"
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.IATA_codes=[]
        self.tickets=[]


    def get_IATA_codes(self, result):
        for city in result:
            city_name=city["city"]
            params = {
                "term": city_name,
                "location_types": "airport"
            }
            response=requests.get(url=TEQUILA_ENDPOINT, params=params, headers=HEADERS)
            data = json.loads(response.content.decode("utf-8"))
            self.IATA_codes.append(data["locations"][0]["city"]["code"])

    def search_for_flights(self, data1):
        import pprint
        today=dt.datetime.now().strftime("%d/%m/%Y")
        today_unformated=dt.datetime.now()
        delta2=timedelta(weeks=25)
        delta=timedelta(weeks=27)
        date_from=(today_unformated+delta2).strftime("%d/%m/%Y")
        date_to=(today_unformated+delta).strftime("%d/%m/%Y")
        params=[{
            "fly_from":"MOW",
            "fly_to": city["iataCode"],
            "date_from":"21/08/2022",
            "date_to":"16/09/2022",
            "nights_in_dst_from":"4",
            "nights_in_dst_to":"14",
            "curr":"RUB",
            "price_to":int(city["lowestPrice"]),
            "vehicle_type":"aircraft",
            "limit":1

        } for city in data1]
        response=[requests.get(url=TEQUILA_ENDPOINT_SEARCH, params=step, headers=HEADERS) for step in params]
        self.tickets = [json.loads(resp.content.decode("utf-8")) for resp in response]
        pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(self.tickets)
