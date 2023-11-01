import requests

hakusana = input("Give the name of the city: ")

pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={hakusana}&appid=fa18f599808708fd7c36fccf27e6fef3"
vastaus = requests.get(pyyntö).json()
print(vastaus["weather"])
print(vastaus["main"]["temp"]-273)
