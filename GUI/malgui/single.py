import requests
import hashlib
import os
import json
import sys

USERNAME = 'crinchiera'
API_KEY = '620744ded9e39f64025e15e1a6ca5501fb3beac4'

for arg in sys.argv:
	malware = str(sys.argv[1])

read_data = open(malware,'r')

md5_data = json.load(read_data)

#file_data = open(malware, 'r').read()

md5 = md5_data['moduleMetadata']['META_HASH']['HASHES']['md5']

realname = md5_data['moduleMetadata']['META_EXIFTOOL']['EXE:OriginalFilename']

data = {
        'upload_type': 'metadata',
        'filename': malware,
        'md5': md5,
        'source': 'Christine',
	'bucket_list': realname}

files = {'filedata': open(malware, 'rb')}

url = 'http://localhost:8080/api/v1/samples/?username={0}&api_key={1}'.format(USERNAME, API_KEY)

r = requests.post(url = url, data = data, files=files)
print r.text
