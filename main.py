import requests
import json

class Weather:
    def __init__(self, name, status, description, temperature, humidity, visibility, longitude, latitude):
        
        self.cityName = name
        self.status = status
        self.statusDescription = description.title()
        self.temperature = str(temperature-273.15)+u'\u2103'
        self.humidity = str(humidity)+'%'
        self.visibility = visibility
        self.longitude = str(longitude)
        self.latitude = str(latitude)

    def displayWeatherData(self):

        print('\n'+'*'*10,'Weather in',self.cityName,'*'*10+'\n')
        print()
        print('Temperature:',self.temperature)
        print()
        print('Humidity:',self.humidity)
        print()
        print('Visibility:',self.visibility)
        print()
        print('Weather status:',self.status)
        print()
        print('Description:\n'+' '*5+'* '+self.statusDescription)
        print()
        print('Coordinates:\n'+' '*5+'* Longitude:',self.longitude+'\n'+' '*5+'* Latitude:',self.latitude)
        
if __name__ == '__main__':
    
    url = "http://api.openweathermap.org/data/2.5/weather"

    apiKey = '9b41d6fd6bf6b93bac3fffbc3dd2768b'

    city = input('Enter City name: ')

    link = url+'?q='+city+'&appid='+apiKey

    try:
        response = requests.request("GET", link)

        if response.status_code == 200:
            
            data = json.loads(response.text)

            dataWeather = data['weather'][0]
            dataTemp = data['main']
            dataCoord = data['coord']
            
            weather = Weather(data['name'], dataWeather['main'], dataWeather['description'], dataTemp['temp'], dataTemp['humidity'], data['visibility'], dataCoord['lon'], dataCoord['lat'])

            weather.displayWeatherData()
            
        else:
            print('Invalid City Name')
            
    except Exception as e:
        print('Error Occured, Error:',e)
