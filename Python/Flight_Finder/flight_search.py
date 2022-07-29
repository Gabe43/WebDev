import json
from operator import le
from pyexpat.errors import codes
from threading import local
import requests
import random
from data_manager import *
import datetime as dt


dm = DataManager()
now = dt.datetime.now().strftime('%d/%m/%Y')
then = dt.datetime(year=2022, month=7, day=13).strftime('%d/%m/%Y')
dm.city_codes()
dm.prices()
list_places = code
list_prices = price
cit_lis = []
prc_list = []
cit_frm=[]
class FlightSearch:
    def search_best(self):
        global cit_lis
        global prc_list
        ct = []
        pl = []
        cf = []
        API = '6An6QgO4Ij2VX9_gjuADtEuQtHdhjiut'
        API_URL = 'https://tequila-api.kiwi.com/v2/search'
        header = {'apikey': API}
        for item in range(0,len(list_places)-1):
            parms = {'fly_from': 'LHR',
                'fly_to':list_places[item],
                 'date_from': now,
                 'date_to': then}
            response = requests.get(url=API_URL, params=parms, headers=header)
            response.raise_for_status()
            data = response.json()['data']
            if len(data)>0:
                no = random.randint(0,len(data)-1)
                fl_price = data[no]['price']
                is_on = True
                while is_on:
                    if fl_price<list_prices[item]:
                        pl.append(fl_price)
                        ct.append(data[no]['cityTo'])
                        cf.append(data[no]['cityFrom'])
                        is_on=False
                    else:
                        is_on=False
            else :
                break
        cit_lis[:]=[item for item in ct]
        prc_list[:]=[itm for itm in pl]
        cit_frm[:] = [it for it in cf]
        
fs = FlightSearch()       
fs.search_best()
comb_dict = {cit_frm[item]:[cit_lis[item],prc_list[item]] for item in range(0,len(cit_lis)-1)}


