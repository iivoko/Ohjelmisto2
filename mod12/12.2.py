import requests

hakusana = input("Give the name of the city: ")

pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={hakusana}&appid=fa18f599808708fd7c36fccf27e6fef3"
vastaus = requests.get(pyyntö).json()
säätila = vastaus["weather"][0]["description"]
lämpötila = vastaus["main"]["temp"] - 273.15
print(f"Säätila kaupungissa {hakusana}: {säätila}")
print("Lämpötila: {:.1f}°C".format(lämpötila))
