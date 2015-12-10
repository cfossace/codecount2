import requests
import os
import sys

USERNAME = 'crinchiera'
API_KEY = '620744ded9e39f64025e15e1a6ca5501fb3beac4'

for arg in sys.argv:
	email = str(sys.argv[1])

utype = raw_input('Enter the upload type: ')

bucket = raw_input('Enter any buckets (comma separated): ')

src = raw_input('Enter the source of the upload: ')

camp = raw_input('Enter name of Campaign: ')

data = {'upload_type': utype,
	'filedata': email,
        'bucket_list': bucket,
        'source': src,
        'campaign': camp}

url = url = 'http://localhost:8080/api/v1/emails/?username={0}&api_key={1}'.format(USERNAME, API_KEY)


r = requests.post(url, data=data)
print r.text

