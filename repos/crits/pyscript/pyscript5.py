import requests
import hashlib
import os
import json

#USERNAME = 'christine'
#API_KEY = 'd0e4164c2bd99f1f888477fc25cf8c5c104a5cd1'


#Read in the path with user input (or navigate to the directory in the GUI)
#path = '/home/wildcat/Lockheed/laikaboss/malware/' 

os.chdir("/home/chris/malstor/repos/laikaboss")
#print("Hint: /home/wildcat/Lockheed/laikaboss/malware/")

for arg in sys.argv:
	filename = str(sys.argv[1])

path = filename

for f in os.listdir(path):
	os.system("python laika.py {} | jq '.scan_result[]' > /home/chris/malstor/GUI/malware/{}.out".format(os.path.join(path,f), f))

os.chdir("/home/chris/malstor/repos/crits/pyscript/")
path2 = "/home/chris/malstor/GUI/malware/"

for k in os.listdir(path2):
	os.system("python single.py {}".format(k))
	

