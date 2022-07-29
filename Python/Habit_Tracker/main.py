import requests
import datetime as dt

TOKEN = 'thisissecret'
USERNAME = 'gabriel7616'

pixela_endpoint = 'https://pixe.la/v1/users'

parmas = {'token': TOKEN,
          'username': USERNAME,
          'agreeTermsOfService': 'yes',
          'notMinor': 'yes'}

# response =requests.post(url=pixela_endpoint, json=parmas)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_parms = {'id': 'graph1',
               'name': 'Programming Graph',
               'unit': 'Hours',
               'type': 'int',
               'color': 'sora'}

headers = {'X-USER-TOKEN': TOKEN}

# response = requests.post(url=graph_endpoint, json=graph_parms,headers=headers)
# print(response.text)

pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/graph1'

today = dt.datetime.now()
date_format = today.strftime("%Y%m%d")

pixel_parms = {'date':f'{date_format}',
'quantity': '5',}

# response = requests.post(pixel_endpoint,json=pixel_parms,headers=headers)
# print(response.text)

update_pixel_endpoint = f'{pixel_endpoint}/{date_format}'

update_parms = {'quantity':'2'}

# response = requests.put(update_pixel_endpoint,json=update_parms,headers=headers)
# print(response.text)

# response = requests.delete(update_pixel_endpoint,headers=headers)
# print(response.text)