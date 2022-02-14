
from flight_search import FlightSearch
import pandas

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        # SHEETY_ENDPOINT = "https://api.sheety.co/7462ab1dc3fc3685cc090a8ef6f0e60f/flightDeals/prices"
        # PUT_ENDPOINT="https://api.sheety.co/7462ab1dc3fc3685cc090a8ef6f0e60f/flightDeals/prices/2"
        # headers_sheety = {
        #     "Authorization": "Bearer bsrhgbdrgbkb5476",
        #     "Content-Type": "application/json"
        # }
        #
        # self.response = requests.get(url=SHEETY_ENDPOINT, headers=headers_sheety)
        # print(self.response.text)
        # self.data = json.loads(self.response.content.decode("utf-8"))["prices"]
        self.data = pandas.read_csv("data.csv")
        #print(self.data)
        self.data_dict = [{"city": row.city, "iataCode": row.iataCode, "lowestPrice": row.lowestPrice} for (index, row) in
                     self.data.iterrows()]
        #print(self.data_dict)


    def write_iata_codes_to_table(self):
        FLight_Search=FlightSearch()
        FLight_Search.get_IATA_codes(self.data_dict)
        self.IATA_codes=FLight_Search.IATA_codes
        #for code in self.IATA_codes:
            # params={
            #     "price":{
            #         "iataCode":code
            #     }
            # }
            # response=requests.put(url=f"https://api.sheety.co/7462ab1dc3fc3685cc090a8ef6f0e60f/flightDeals/prices/{self.IATA_codes.index(code)+2}", json=params, headers=headers_sheety)
            # response = json.loads(response.content.decode("utf-8"))
        # for (index, row) in self.data.iterrows():
        #     row.iataCode=self.IATA_codes[index]
        #     print(row.iataCode)
        new_df={"iataCode":self.IATA_codes}
        self.data.update(new_df)
        self.data.to_csv("data.csv", index=False)





