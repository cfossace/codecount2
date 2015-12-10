import requests
import os
import sys

USERNAME = 'crinchiera'
API_KEY = '620744ded9e39f64025e15e1a6ca5501fb3beac4'

#camp = raw_input('Enter name of Campaign:')

#src = raw_input('Enter the source of upload:')


for arg in sys.argv:
	thefile = str(sys.argv[1])

file_data = open(thefile, 'rb').read()
data = {'upload_type': 'file',
        'filedata': file_data,
	#'password': 'infected',
	#'file_format': 'zip',
        'source': 'Christine',
	'campaign': 'VU_Malstor'}

files = {'filedata': open(thefile, 'rb')}

url = 'http://localhost:8080/api/v1/samples/?username={0}&api_key={1}'.format(USERNAME, API_KEY)

r = requests.post(url, data=data, files=files)
print r.text 
