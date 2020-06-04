import requests
import json

class Weather:
    def __init__(self, name, status, description, temperature, humidity, pressure, visibility, longitude, latitude, wind):
        
        self.cityName = name
        self.status = status
        self.statusDescription = description
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.visibility = visibility
        self.longitude = longitude
        self.latitude = latitude
        self.wind = wind

    def displayWeatherData(self):

        print('\n'+'*'*10,'Weather in',self.cityName,'*'*10+'\n')
        print()
        print('Temperature:',self.temperature-273.15,u'\u2103')
        print()
        print('Humidity:',self.humidity,'%')
        print()
        print('Pressure:',self.pressure,'hpa')
        print()
        print('Wind:',self.wind,'m/s')
        print()
        print('Visibility:',self.visibility,'meter')
        print()
        print('Weather status:',self.status)
        print()
        print('Description:\n'+' '*5+'*',self.statusDescription.title())
        print()
        print('Coordinates:\n'+' '*5+'* Longitude:',self.longitude,'\n'+' '*5+'* Latitude:',self.latitude)
        
if __name__ == '__main__':
    
    url = "http://api.openweathermap.org/data/2.5/weather"

    apiKey = '1e67bf59e9e77cca70509fa5dd4fe27a'

    city = input('Enter City name: ')

    link = url+'?q='+city+'&appid='+apiKey

    try:
        response = requests.request("GET", link)

        if response.status_code == 200:
            
            data = json.loads(response.text)

            dataWeather = data['weather'][0]
            dataTemp = data['main']
            dataCoord = data['coord']
            
            weather = Weather(data['name'], dataWeather['main'], dataWeather['description'], dataTemp['temp'], dataTemp['humidity'], dataTemp['pressure'], data['visibility'], dataCoord['lon'], dataCoord['lat'],data['wind']['speed'])

            weather.displayWeatherData()
            
        else:
            print('Invalid City Name')
            
    except Exception as e:
        print('Error Occured, Error:',e)
