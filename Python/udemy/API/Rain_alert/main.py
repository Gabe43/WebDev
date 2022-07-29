import requests
from twilio.rest import Client

Api_Web = 'https://api.openweathermap.org/data/2.5/onecall' 

api_key = 'SKe897e9511777c62fd37f2b720d4d826b'
account_sid = 'ACff06d5339d0e3b4c595223b3cb96feed'
auth_token = '3dcbfffe74d1371d5f25b4a742beae7f'

weather_parms = {'lat':22.572645,
'lon':88.363892,
'exclude':'minutely,daily,current,alerts',
'appid':'5b47e1b09698da5948780b7e4758386e'}

response = requests.get(Api_Web,params=weather_parms)
response.raise_for_status()
will_rain = False

for item in range(0,12):
    weather_data = response.json()['hourly'][item]['weather'][0]['id']
    if weather_data<700:
        will_rain=True
        
if will_rain==True:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It's going to rain today, Remember to bring an ☂️",
                     from_='+18507791980',
                     to='+919875619471'
                 )
    print(message.status)





















