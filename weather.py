import requests
def weather(city):
    API_key = "your api key"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    Final_url = base_url + "appid=" + API_key + "&q=" + city 
    weather_data = requests.get(Final_url).json()
    
    kword={
        'main':weather_data['main'],
        'weather':weather_data['weather'],
        'wind':weather_data['wind'],
    }

    return kword

# city = input("Enter your location :")
# temperature = round(weather(city)['main']['temp']-273.15)
# desc = weather(city)['weather'][0]['description']
# hum = weather(city)['main']['humidity']
# wind_spd = weather(city)['wind']['speed']

#print(f"The current temperature at {city} is {temperature} degree Celsius. Weather is {desc}. The humidity is {hum}% and wind speed is {wind_spd}kph")
        
