import requests
import hashlib
import os
import json

USERNAME = 'christine'
API_KEY = 'd0e4164c2bd99f1f888477fc25cf8c5c104a5cd1'

myfile = 'doc.txt'

read_data = open(myfile,'r')

md5_data = json.load(read_data)

file_data = open(myfile, 'r').read()

md5 = md5_data['moduleMetadata']['META_HASH']['HASHES']['md5']

realname = md5_data['moduleMetadata']['META_EXIFTOOL']['EXE:OriginalFilename']

parsed = myfile.split(".")
file_type = parsed[1]
data = {'upload_type': 'metadata',
        'filename': myfile,
        'md5': md5,
        'filedata': file_data,
        'bucket_list': realname,
        'file_format': file_type,
        'source': 'Christine', 
        'campaign':VU_Malstor}
files = {'filedata': open(myfile, 'rb')}

url = 'http://localhost:8080/api/v1/samples/?username={0}&api_key={1}'.format(USERNAME, API_KEY)

r = requests.post(url, data=data, files=files)
print r.text

print realname
