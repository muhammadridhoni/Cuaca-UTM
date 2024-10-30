import requests
from datetime import datetime

def get_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        wind = data['wind']
        
        print(f"\nCuaca di {city_name.capitalize()}:")
        print(f"Suhu: {main['temp']}°C")
        print(f"Kelembapan: {main['humidity']}%")
        print(f"Deskripsi: {weather['description'].capitalize()}")
        print(f"Kecepatan Angin: {wind['speed']} m/s")
    else:
        print("Data cuaca tidak ditemukan. Coba periksa nama kota atau API key.")

# API key dari user
api_key = "42daca0343e7e45990e0edf6ec9b5a48"

# Meminta pengguna memasukkan nama kota
city_name = input("Masukkan nama kota yang ingin Anda lihat data cuacanya: ")
get_weather(city_name, api_key)
