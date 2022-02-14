from flight_search import FlightSearch
from data_manager import DataManager
import datetime as dt


class FlightData(FlightSearch, DataManager):
    #This class is responsible for structuring the flight data.
    def __init__(self):
        FlightSearch.__init__(self)
        DataManager.__init__(self)
        self.final_array = []
        pass

    def flight_attributes(self):
        #self.write_iata_codes_to_table()
        self.search_for_flights(self.data_dict)
        for ticket in self.tickets:
            try:
                departure_day=ticket["data"][0]["local_departure"].split("T")[0]
                departure_time=ticket["data"][0]["local_departure"].split("T")[1].split(".")[0]
                arrival_day = ticket["data"][0]["local_arrival"].split("T")[0]
                arrival_time = ticket["data"][0]["local_arrival"].split("T")[1].split(".")[0]
                result={"Flight from:":ticket["data"][0]["cityFrom"], "Flight to:":ticket["data"][0]["cityTo"], "price":ticket["data"][0]["price"], "Departure (local)": f"{departure_time} {departure_day}", "Arrival (local)": f"{arrival_time} {arrival_day}", "how many flights?": len(ticket["data"][0]["route"]), "nights in destination place":ticket["data"][0]["nightsInDest"], "link":ticket["data"][0]["deep_link"]}
                print(result)
                self.final_array.append({f"Flight to:{result['Flight to:'].encode('utf-8')}": result['link']})
            except IndexError:
                pass

