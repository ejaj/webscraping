from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
from urllib.request import urlopen

html = urlopen('https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src':re.compile('.jpg')})
for image in images:
    print(image['src']+'\n')



r = requests.get("https://analytics.usa.gov/data/live/browsers.json")
print("90 days of visits broken down by browser for all sites:")
print(r.json()['totals']['browser'])



html = urlopen("https://en.wikipedia.org/wiki/Python")
bsObj = BeautifulSoup(html)
for link in bsObj.findAll("a"):
  if 'href' in link.attrs:
    print(link.attrs['href'])