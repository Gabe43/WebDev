import email
from twilio.rest import Client
from flight_search import *
from data_manager import *
import random,requests
import smtplib
class NotificationManager:
    def notification(self):
        dm = DataManager()
        dm.city_codes()
        dm.prices()
        fs = FlightSearch()
        fs.search_best()
        if len(comb_dict)>0:
            print('fck')
            res = key, value = random.choice(list(comb_dict.items()))
            mesg = f'Low price alert! Only €{res[1][1]} to fly from {res[0]} to {res[1][0]} , from {now} to {then}.'
            my_eamil = 'gabrieljesus7616@gmail.com'
            password = 'abcd@1234'
            api_ur = 'https://api.sheety.co/afbe404d9d5cfcd0ff4bb58cc64b6567/flight/sheet1'
            response = requests.get(url=api_ur)
            data = response.json()['sheet1']
            print(len(data))
            print(data[0]['email'])
            for item in range(0,len(data)-1):
                with smtplib.SMTP('smtp.gmail.com') as connection:
                    connection.starttls()
                    connection.login(user=my_eamil,password=password)
                    connection.sendmail(from_addr=my_eamil,to_addrs=data[item]['email'],msg=f'Subject:Cheapest Flights\n\n{mesg}'.encode('utf-8'))
                    
        else:
            print('No Flights')
        

