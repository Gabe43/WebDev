import requests
from bs4 import BeautifulSoup
import smtplib
response = requests.get(url='https://www.amazon.com/Rechargeable-Windproof-Flameless-Indicator-Cigarette/dp/B07L61G21Q/ref=sr_1_2?keywords=lighters+for+smoking&qid=1643220989&sprefix=lighter%2Caps%2C677&sr=8-2', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                                                                                                                                'Accept-Language': 'en-US,en;q=0.9'})
data = response.text

bm = BeautifulSoup(data,'html.parser')

price = float(bm.find_all(class_='a-offscreen')[1].string.split('$')[1])

if price<10:
    email = 'gabrieljesus7616@gmail.com'
    password = 'abcd@1234'
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(from_addr=email,to_addrs='saptarshiabhi21@gmail.com',msg=f'Subject:Discount On item\n\nLighter, Electric Arc Lighter USB Rechargeable Lighter Windproof Flameless Lighter Plasma Lighter with Battery Indicator (Upgraded) for Fire, Cigarette, Candle - Outdoors Indoors (Bright-Black)::\n\n\n Is now availabe at ${price}, Go and buy now quickly..Happy Shopping')


