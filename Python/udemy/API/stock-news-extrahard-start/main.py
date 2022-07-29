import requests
from twilio.base import values
from twilio.rest import Client


def twilio(stock_name,percent,sign,title,body):
    account_sid = 'ACff06d5339d0e3b4c595223b3cb96feed'
    auth_token = '3dcbfffe74d1371d5f25b4a742beae7f'
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body=f"{stock_name}: {sign}{percent}%\n\n{title}\n{body}",
                     from_='+18507791980',
                     to='+919875619471'
                 )
    print(message.status)



# News Api Information
news_parms = {'q':'UPL',
              'apiKey': '564dc72e20294dac88f19fc5c38d4918'}
news = requests.get('https://newsapi.org/v2/everything',params=news_parms)
news.raise_for_status()
news_data = news.json()['articles']
news_head = [news_data[item]['title'] for item in range(0,3)]
news_body = [news_data[item]['description'] for item in range(0,3)]


# Stock Api Information
STOCK = "UPL"
COMPANY_NAME = "Tesla Inc"
stock_parms = {'function': 'TIME_SERIES_DAILY',
               'symbol': f'{STOCK}.BSE', 'apikey': 'WAND5N2EGD0V0COS'}
stocks = requests.get('https://www.alphavantage.co/query', params=stock_parms)
stocks.raise_for_status()
stock_data = stocks.json()['Time Series (Daily)']
stock_data_list = [value for (key,value) in stock_data.items()]
today_closing_value = float(stock_data_list[0]['4. close'])
yesterday_closing_value = float(stock_data_list[1]['4. close'])

if yesterday_closing_value > today_closing_value:
    sign = '🔺'
    perc = 100*((yesterday_closing_value-today_closing_value)/today_closing_value)
    print(perc)
    if perc > 0.2:
        for item in range(0,3):
            twilio(stock_name=STOCK,percent=perc,sign=sign,title=news_head[item],body=news_body[item])
elif today_closing_value > yesterday_closing_value:
    sign = '🔻'
    perc = 100*((today_closing_value-yesterday_closing_value)/today_closing_value)
    print(perc)
    if perc > 0.2:
        for item in range(0,3):
            twilio(stock_name=STOCK,percent=perc,sign=sign,title=news_head[item],body=news_body[item])

