import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url)
    print(response.text)

get_weather("Mumbai")
