import smtplib
from flight_data import FlightData

my_email="hung.days.of.code.sender@gmail.com"
password="2708hung.days.of.code.sender"
receiver_email="v_konopleva@yahoo.com"

class NotificationManager(FlightData):
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        super().__init__()
        pass


    def sent_notification(self):
        self.flight_attributes()
        # print(self.final_array)
        if self.final_array!=[]:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=receiver_email, msg=f"Subject: Here are some tickets!\n\n"
                                                                                         f"{self.final_array}")