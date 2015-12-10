import requests
import os
import sys
import time

for arg in sys.argv:
        filename = str(sys.argv[1])

path = filename

for f in os.listdir(path):
        os.system("python meta_sample.py {}".format(os.path.join(path,f), f))
        time.sleep(3)
