from flight_data import FlightData
from notification_manager import NotificationManager
import datetime as dt


#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# Data_Manager=DataManager()
# Data_Manager.write_iata_codes_to_table()

# print(sheet_content.data)
# print(sheet_content.IATA_codes)
#
if str(dt.datetime.now().time()).split(':')[0]=='16':
    Flight_Data=FlightData()
    Notify=NotificationManager()

    Flight_Data.flight_attributes()
    Notify.sent_notification()


