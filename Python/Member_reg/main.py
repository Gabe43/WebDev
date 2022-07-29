import requests
print("Welcome to Saptarshi's Flght Club.\nWe find the best flight deals and email you.")

first_name = input("What's your first name? ")
last_name = input("What's your last name? ")
email = input('Enter your email? ')
verify = input('Type your email again. ')

if email == verify:
    print("You're in the club")

api_url = 'https://api.sheety.co/afbe404d9d5cfcd0ff4bb58cc64b6567/flight/sheet1/2'
parms = {'sheet1': {'email': email,'firstName':first_name,'lastName':last_name}}
response = requests.put(url=api_url, json=parms)
response.raise_for_status()
