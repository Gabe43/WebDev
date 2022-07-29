import requests
import smtplib
import time as t
response = requests.get(url='http://api.open-notify.org/iss-now.json')

response.raise_for_status()

iss_lat = float(response.json()['iss_position']['latitude'])
iss_lng = float(response.json()['iss_position']['longitude'])

import datetime as dt
formatted = {'formatted':0}
respons = requests.get('https://api.sunrise-sunset.org/json',params=formatted)
respons.raise_for_status()

data = respons.json()

sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

my_lat = 22.359674
my_lng = 88.431778
time_now = int(dt.datetime.now().hour)

while(True):
    if my_lat-5<=iss_lat<=my_lat+5 and my_lng-5<=iss_lng<=my_lng+5:
        if time_now >=sunset or time_now<=sunrise:
            name = 'gaberialjesus7616@gmail.com'
            password = 'abcd@1234'
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=name,password=password)
                connection.sendmail(from_addr=name,to_addrs='saptarshiabhi21@gmail.com',msg='Subject:ISS NEAR\n\nLook Up')
    t.sleep(60)      
            