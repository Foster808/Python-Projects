import requests
from secrets import api_key
response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={api_key}')

print(response.text)
print(response.status_code)