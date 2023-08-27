import requests, os

os.system('cls')
print("Weather Forecast by DNw")

apikey = "78448c0080cb7511f61c4371c831a80b"
city = input("Type your city: ") #"Przyszowice"

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={apikey}")
#print(response.status_code)

#for col in response.json():
#    print(col,end=" ")
#    print(str(response.json()[col]))

print(f"Actual weather for {response.json()['name']}")
print(f"Temperature: {round(response.json()['main']['temp'],1)}°C")
print(f"Sky: {response.json()['weather'][0]['description']}")
print(f"Humidity: {response.json()['main']['humidity']}%")
print(f"Wind speed: {round(response.json()['wind']['speed'] * (1/1000)/(1/3600))}km/h")
print(f"Pressure: {response.json()['main']['pressure']}hPa")