from pyexpat.errors import codes
import requests
price = [] 
code = []
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def city_codes(self):
        global code
        API_URL = 'https://api.sheety.co/afbe404d9d5cfcd0ff4bb58cc64b6567/flightDetails/sheet1'
        response = requests.get(url=API_URL)
        response.raise_for_status()
        data = response.json()
        cod =[data['sheet1'][item]['iataCode'] for item in range(0,len(data['sheet1']))]
        code[:] = [item for item in cod]
        
        
    def prices(self):
        global price
        API_URL = 'https://api.sheety.co/afbe404d9d5cfcd0ff4bb58cc64b6567/flightDetails/sheet1'
        response = requests.get(url=API_URL)
        response.raise_for_status()
        data = response.json()
        pric = [data['sheet1'][item]['lowestPrice'] for item in range(0,len(data['sheet1']))]
        price[:] = [item for item in pric]
        
        
