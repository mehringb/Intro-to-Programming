#Bethany Mehring
#3/5/2022
import json, requests #importing json and requests

apiKey="" #my api key given to me by openweather *purposely left out

def get_weather_zipcode(zipcode):#getting the correct url 
    url = 'http://api.openweathermap.org/data/2.5/weather?zip=%s&appid=%s' % (zipcode, apiKey) 
    return url

def get_weather_city(city):#getting the correct url 
    url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' % (city, apiKey)
    return url

def main():

    options=input('Hello, please enter city or zipcode: ')
    if options.isnumeric(): #if opetion is of a numeric value enter it into the zipcode function
        url=get_weather_zipcode(options)

    else : #otherwise assume it's a city and search by city name
        url=get_weather_city(options)

    r= requests.get(url)#importing requests

    try: #check if it is succesful or not
        r.raise_for_status()
    except:
        print('That entry was invalid')
        print('')
        main() #take them to the beginning if invalid

    #pull the data 
    data = requests.get(url).json()
    #find temp. calculate it from kelvin to fahrenheit
    temp = data['main']['temp']
    format_temp=temp*1.8-459.67
    format_calc_fahrenheit="{:.2f}".format(format_temp)
        
    #find wind speed convert from meter per second to mph
    wind = data['wind']['speed']
    calc_wind= wind*2.237
    format_calc_wind="{:.2f}".format(calc_wind)

    #find what the temp feels like convert to fahrenheit
    feels_like = data['main']['feels_like']
    format_feels= feels_like *1.8-459.67
    format_feels_like="{:.2f}".format(format_feels)

    #find humidity level
    humidity = data['main']['humidity']

    #find current max temp convert to fahrenheit
    max_temp = data['main']['temp_max']
    format_max= max_temp *1.8-459.67
    format_max_temp="{:.2f}".format(format_max)

    #find current min temp and convert
    min_temp = data['main']['temp_min']
    format_min= min_temp *1.8-459.67
    format_min_temp="{:.2f}".format(format_min)

    #display the data
    print('')
    print(f'Current Temperature is: '+format_calc_fahrenheit +' degrees Fahrenheit')
    print(f'Current Windspeed is: '+format_calc_wind+' MPH' )
    print(f'Currently feels like: '+str(format_feels_like)+ ' degress Fahrenheit')
    print(f'Current Humidity is: '+str(humidity)+'%')
    print(f'Maximum Temperature currently: '+format_max_temp +' degrees Fahrenheit')
    print(f'Minimun Temperature currently: '+format_min_temp +' degrees Fahrenheit')
    print('')

    #prompting if user would like to go again. Taking them to the start of main if they do or exiting application
    while True:
        try: #validating input
            again= input('Would you like to enter a new location? Please answer with yes or no: ')
            if again=='yes':
                print('')
                print('')
                main()
            if again=='no':
                print('')
                print('Thank you for using this app to find your weather information. ')
                print('')
                print('Goodbye.')
                break
            else:
                print('')
                print('**You must either enter yes or no.**')
                print('')
        except:
            continue

main()

    
