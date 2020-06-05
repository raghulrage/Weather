#import packages
import requests
import json

class Weather:
    
    '''Weather attributes'''
    
    def __init__(self, name, status, description, temperature, humidity, pressure, longitude, latitude, wind):
        
        self.cityName = name
        self.status = status
        self.statusDescription = description
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.longitude = longitude
        self.latitude = latitude
        self.wind = wind

    '''Display weather details'''
    
    def displayWeatherData(self):
        
        print('\n'+'*'*10,'Weather in',self.cityName,'*'*10+'\n')
        print()
        print('Temperature:',round(self.temperature-273.15,2),u'\u2103')
        print()
        print('Humidity:',self.humidity,'%')
        print()
        print('Pressure:',self.pressure,'hpa')
        print()
        print('Wind:',self.wind,'m/s')
        print()
        print('Weather status:',self.status)
        print()
        print('Description:\n'+' '*5+'*',self.statusDescription.title())
        print()
        print('Coordinates:\n'+' '*5+'* Longitude:',self.longitude,'\n'+' '*5+'* Latitude:',self.latitude)

#Get data from open weather app 
def getLink():
    
    city = input('\n\nEnter City name: ')
    
    url = "http://api.openweathermap.org/data/2.5/weather"
    apiKey = '1e67bf59e9e77cca70509fa5dd4fe27a'
    link = url+'?q='+city+'&appid='+apiKey

    return link

#main function
def main():
    
    link = getLink()

    #handle exception
    try:
        response = requests.request("GET", link)

        if response.status_code == 200:
            
            data = json.loads(response.text)

            dataWeather = data['weather'][0]
            dataTemp = data['main']
            dataCoord = data['coord']

            weather = Weather(data['name'], dataWeather['main'], dataWeather['description'], dataTemp['temp'], dataTemp['humidity'], dataTemp['pressure'], dataCoord['lon'], dataCoord['lat'],data['wind']['speed'])

            weather.displayWeatherData()
            
        else:
            print('Invalid City Name')
            
    except requests.exceptions.ConnectionError:
        
        print('\nNo Internet.')
        print('Try:\n\t* Checking the network cables, modem, and router\n\t* Reconnecting to Wi-Fi\n\t* Running Windows Network Diagnostics')

    except Exception as e:
        print('Oops!',e.__class__,'occured.',e)

        
if __name__ == '__main__':

    print('*'*15,'Weather Forcast','*'*15)

    main()

    
    while True:
        option = input('\nDo you want to continue[Y/N]: ').lower()
        
        if option == 'y':
            main()
        else:
            print('\nThank You.')
            break
    



