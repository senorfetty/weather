import requests

api_key= '8b7273e4827aecc37a1424f63c3345bd'

city= input('Enter City Name')
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response= requests.get(url)

if response.status_code == 200:
    data= response.json()
    temp = data['main']['temp']
    desc= data['weather'][0]['description']
    print(f'Temperature: {temp} K')
    print(f'Description: {desc}')

else:
    print('Error')