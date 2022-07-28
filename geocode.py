import requests
geo_url = 'http://maps.googleapis.com/maps/api/geocode/json'
my_address = {'address': '21 Ramkrishana Road, Burdwan, East Burdwan, West Bengal, India',
             'language': 'en'}
response = requests.get(geo_url, params = my_address)
results = response.json()['results']
my_geo = results[0]['geometry']['location']
print("Longitude:",my_geo['lng'],"\n","Latitude:",my_geo['lat'])
