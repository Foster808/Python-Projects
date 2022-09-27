import requests
from secrets import api_key
response = requests.get('https://w3schools.com/python/demopage.htm')

print(response.text)