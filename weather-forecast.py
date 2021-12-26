# we're going to create the weather cast of the particular city
# pprint used for represnting the smoothing representation of the data
import requests
# when we make request to the openweathermap.org/api_keys then i
# give the json format. To make it easy we using pprint that will
# make tree dictionary format.
from pprint import pprint
# Here we will make request using Api key
API_KEY = "6816f97c850698ada526c130afa5674f"
city = input('Enter a city name: ')
# we've to make the request to the base url
base_url ="https://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+"&q="+city
# we want to send the request to the above url using city & api key
# make the request in json format
r = requests.get(base_url).json()
# make the json format to readable format
pprint(r)
city2 = input("Enter your 2nd city name: ")

base2_url = "https://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+"&q="+city2
s = requests.get(base2_url).json()
pprint(s)

r.items()
print(city+" has clouds",r['clouds'])
s.items()
print(city2+" has clouds",s["clouds"])

    

