import requests
import json

city = 'Yogyakarta'
apikey = "42daca0343e7e45990e0edf6ec9b5a48"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&units=metric"
response = requests.get(url)
json_response = json.loads(response.text)

print(json_response)