import json
import requests

parms = {'amount':10,
'category':18,
'type':'boolean'}
response = requests.get(url='https://opentdb.com/api.php',params=parms)
response.raise_for_status()
data = response.json()['results']
question_data = data


