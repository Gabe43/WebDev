##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime as dt
import random
import smtplib
import pandas
time = dt.datetime.now()
day = time.day
mnth = time.month
dta = pandas.read_csv('birthdays.csv')
date = dta['day']
month = dta['month']
if day == int(date) and mnth == int(month):
    choice = ['letter_templates/letter_1.txt','letter_templates/letter_2.txt','letter_templates/letter_3.txt']
    x = random.choice(choice)
    print(x)
    with open(x,'r') as file:
        data = file.read()
        data = data.replace('NAME','Gabriel')

    email = 'gabrieljesus7616@gmail.com'
    password  = 'abcd@1234'

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(from_addr=email,to_addrs='saptarshiabhi21@gmail.com',msg=f'Subject:Birthday\n\n{data}')





