from requests import get

url = 'https://danepubliczne.imgw.pl/api/data/synop'

response = get(url)

weather_rows = response.json()

for weather_row in weather_rows:
    print(weather_row['stacja'], weather_row['temperatura'])


