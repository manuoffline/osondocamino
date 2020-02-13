import requests
from collections import OrderedDict

headers = {'content-type': 'text/html; charset=utf-8'}

seen = OrderedDict()
for line in open('groups.txt'):
    line = line.strip()
    seen[line] = seen.get(line, 0) + 1

print(seen)

for line in seen:
    url = str('http://www.osondocamino.es/release/' + line)
    r = requests.get(url, headers)
    # print(url)
    if r.status_code == 200:
        print(url + ' : ' + str(r.status_code))
