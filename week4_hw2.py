import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import requests
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

lst1 = list()
lst2 = list()
lst3 = list()
url = "http://py4e-data.dr-chuck.net/known_by_Darwyn.html"
for i in range(8):
    r = urllib.request.urlopen(url)
    r = r.read().decode()
    soup = BeautifulSoup(r,"html.parser")
    sels = soup.select("a")
    for sel in sels :
        lst1 = sel.get("href").split("_")
        lst2 = lst1[2].split(".")
        lst3.append(lst2[0])
    print("本頁的URL為"+url)
    url = "http://py4e-data.dr-chuck.net/known_by_" + lst3[17] + ".html"
    lst3 = []