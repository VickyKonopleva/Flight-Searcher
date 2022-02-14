from flight_data import FlightData
from notification_manager import NotificationManager



#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# Data_Manager=DataManager()
# Data_Manager.write_iata_codes_to_table()

# print(sheet_content.data)
# print(sheet_content.IATA_codes)
#

Flight_Data=FlightData()
Notify=NotificationManager()

Flight_Data.flight_attributes()
Notify.sent_notification()


