import requests
import os

def main():
    key = os.environ.get('WEATHER_KEY')
    query = {'q': 'minneapolis,us', 'units': 'imperial', 'appid': key}

    url = f'https://api.openweathermap.org/data/2.5/weather'
    data = requests.get(url, params=query).json()
    weather_description = data['weather'][0]['description']

    temp_f = data['main']['temp']
    print(f'The weather is {weather_description}, the tempurature is {temp_f:.2f}F.')

if __name__ == '__main__':
    main()