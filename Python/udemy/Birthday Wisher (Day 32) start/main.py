# import smtplib

# my_email = 'gabrieljesus7616@gmail.com'
# password = 'abcd@1234'

# with smtplib.SMTP('smtp.gmail.com') as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email,to_addrs='saptarshiabhi21@gmail.com',msg='Subject:Hello\n\nThis is the body of my email')
#     connection.close()

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# print(year)
# date_of_birth = dt.datetime(year=2010,month=5,day=23)
# print(date_of_birth)

import datetime as dt
import smtplib
import random
with open('quotes.txt','r') as file:
    quote=file.readlines()

time = dt.datetime.now()
day = time.weekday()
if day == 4:
    email = 'gabrieljesus7616@gmail.com'
    password = 'abcd@1234'

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(from_addr=email,to_addrs='saptarshiabhi21@gmail.com',msg=f'Subject:Motivational Quote\n\n{random.choice(quote)}')
