import json
import urllib.request, urllib.parse, urllib.error

address = input('Enter address: ')
uh = urllib.request.urlopen(address)
data = uh.read().decode()

info = json.loads(data)
info1 = info['comments']

ans = 0
for item in info1 :
    ans = ans + item['count']

print(ans)