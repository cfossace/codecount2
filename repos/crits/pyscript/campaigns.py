import requests

USERNAME = 'crinchiera'
API_KEY = '620744ded9e39f64025e15e1a6ca5501fb3beac4'

data = {'upload_type': 'campaign',
	'aliases': 'Malstor',
	'description': 'Malstor Campaign',
	'name': 'VU_Malstor'}

url = 'http://localhost:8080/api/v1/campaigns/?username={0}&api_key={1}'.format(USERNAME, API_KEY)

r = requests.post(url, data=data)
print r.text
