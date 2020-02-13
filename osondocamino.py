import requests
import re
from collections import OrderedDict

url = 'http://www.osondocamino.es/release/'
filename = 'groups.txt'
headers = {'content-type': 'text/html; charset=utf-8'}
seen = OrderedDict()


def formatstring(string):
    s = string.strip()
    s = " ".join(s.split())
    s = s.replace(" ", "-")
    print(s.lower())
    return s.lower()


for line in open(filename):
    line = line.strip()
    line = formatstring(line)
    seen[line] = seen.get(line, 0) + 1

print("Ejecutando programa:\n")

for line in seen:
    url = str(url + line)
    r = requests.get(url, headers)
    if r.status_code == 200:
        print(url + ' : ' + str(r.status_code))
