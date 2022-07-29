import requests

# APP_ID = 'ddd1b381'
# API_KEY = 'e21a8f0d52280aeecbe6794d8ae0a615'
# exerc_url = 'https://trackapi.nutritionix.com/v2/natural/exercise'

# text = input('Tell me which exercise you did: ')

# header = {'x-app-id': APP_ID,
#           'x-app-key': API_KEY}

# parms = {'query': text,
#          'gender': 'male',
#          'weight_kg': 85,
#          'height_cm': 183,
#          'age': 21}

# response = requests.post(url=exerc_url, json=parms, headers=header)
# print(response.json()['exercises'][0]['name'])

USER = 'gabriel'
sheety_url = f'https://api.sheety.co/652575caca97fec932a72bdf9c7d14c4/exerciseCount/sheet1'
body = {'sheet1':{
    'Duration':15,
    'Date':'13/01/2022'
}}
response = requests.post(url=sheety_url,json=body)
response.raise_for_status()
print(response.status_code)