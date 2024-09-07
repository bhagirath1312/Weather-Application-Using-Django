# from django.shortcuts import render

# import requests #for sending request

# # Create your views here.


# def index(request):

#     # Using Weather Api - https://www.weatherapi.com/
#     # 1. Sign up for a free account at [weatherapi.com](https://www.weatherapi.com/), log in, and generate your new API key in the dashboard section.
#     BASE_URL ='https://api.tomorrow.io/v4'

#     # 2. After generating your API key, copy it and then paste it into the "API_KEY" variable as given below:
#     API_KEY = 'dD1GbF1X1TvH187wC7pAzV70mzhsKiS9' # ***************
# #
#     if request.method=='POST':
#         city=request.POST.get('city').lower()
#         print(city)

#         if API_KEY == 'dD1GbF1X1TvH187wC7pAzV70mzhsKiS0':
#             print('Please add your generated API key into the "API_KEY" variable within the views.py')
#             return render(request,'index.html',{'checker':'Please add your generated API key into the "API_KEY" variable within the views.py'})

#         elif (city== ''):
#             print('No value')
#             return render(request,'index.html',{'checker':'Please enter valid info...!'})

#         else:
#             request_url = f"{BASE_URL}/current.json?key={API_KEY}&q={city}&aqi=no"  #checking city with API (Using Weather Api)

#             # print(request_url)

#             response = requests.get(request_url)

#             if response.status_code == 200:
#                 data = response.json()
#                 # print(data)

#                 location=data['location']
#                 weather = data['current']
#                 # print(weather)
#                 print(location['tz_id'])
#                 print(weather['temp_c'])


#                 context = {
#                     'weather':weather['temp_c'],
#                     'city_name':location['name'],
#                     'region':location['region'],
#                     'country':location['country'],
#                     'lat':location['lat'],
#                     'lon':location['lon'],
#                     'localtime':location['localtime'],
#                     'continent':location['tz_id'],
#                     'static_city':city
#                 }

#                 return render(request,'index.html', context)

#             else:
#                 print("An error occurred")
#                 return render(request,'index.html',{'static_city':city,'checker':'Please enter valid city'})


#     return render(request,'index.html',{})

# from django.shortcuts import render
# import requests
# from django.conf import settings

# def index(request):
#     BASE_URL = 'https://api.weatherbit.io/v2.0/current'
#     API_KEY = getattr(settings, 'WEATHER_API_KEY', '')

#     if request.method == 'POST':
#         city = request.POST.get('city', '').strip().lower()

#         if not API_KEY:
#             return render(request, 'index.html', {'checker': 'API key is missing in settings.'})

#         if not city:
#             return render(request, 'index.html', {'checker': 'Please enter a city name.'})

#         # Geocode the city to get latitude and longitude. This is required because Weatherbit API expects lat/lon
#         # You can use a geocoding API like OpenCage or Google Geocoding API for this purpose

#         # Example lat/lon for demonstration purposes
#         # Replace this with actual geocoding logic to get lat/lon based on city
#         latitude = 35.7796
#         longitude = -78.6382

#         request_url = f"{BASE_URL}?lat={latitude}&lon={longitude}&key={API_KEY}&include=minutely"
#         response = requests.get(request_url)

#         # Print or log the response for debugging
#         print("Response Status Code:", response.status_code)
#         print("Response Content:", response.text)

#         if response.status_code == 200:
#             try:
#                 data = response.json()
#                 print("Response JSON Data:", data)  # Print the JSON response

#                 if 'data' in data and len(data['data']) > 0:
#                     weather = data['data'][0]
#                     location = {
#                         'name': city,  # Use city name from request
#                         'lat': weather.get('lat', 'N/A'),
#                         'lon': weather.get('lon', 'N/A'),
#                         'localtime': weather.get('ob_time', 'N/A'),
#                         'continent': weather.get('timezone', 'N/A')
#                     }

#                     context = {
#                         'weather': weather.get('temp', 'N/A'),
#                         'city_name': location['name'],
#                         'region': weather.get('state_code', 'N/A'),
#                         'country': weather.get('country_code', 'N/A'),
#                         'lat': location['lat'],
#                         'lon': location['lon'],
#                         'localtime': location['localtime'],
#                         'continent': location['continent'],
#                         'static_city': city
#                     }

#                     return render(request, 'index.html', context)
#                 else:
#                     return render(request, 'index.html', {'static_city': city, 'checker': 'Unexpected response format from API.'})

#             except ValueError:
#                 return render(request, 'index.html', {'static_city': city, 'checker': 'Error decoding JSON response.'})
#         else:
#             return render(request, 'index.html', {'static_city': city, 'checker': f'Error retrieving weather data: {response.status_code} - {response.text}'})

#     return render(request, 'index.html', {})

from django.shortcuts import render
import requests
from django.conf import settings
import logging


from datetime import datetime

def convert_to_12_hour_format(localtime):
    try:
        # Parse the 'localtime' string into a datetime object
        dt_object = datetime.strptime(localtime, '%Y-%m-%d %H:%M')
        
        # Format it into 12-hour time format with AM/PM
        return dt_object.strftime('%I:%M %p')
    except ValueError:
        # If parsing fails, return 'N/A' as a fallback
        return 'N/A'















# Set up logging
logger = logging.getLogger(__name__)

def get_lat_lon(city):
    """Function to get latitude and longitude from city name using a geocoding API."""
    api_key = '66ba2cd592014928224432vwoee80e5'
    geocode_url = f"https://geocode.maps.co/search?q={city}&api_key={api_key}"
    try:
        response = requests.get(geocode_url)
        if response.status_code == 200:
            data = response.json()
            # Pick the most relevant result based on your criteria
            if data and len(data) > 0:
                # Assuming the first result is the most relevant
                return data[0]['lat'], data[0]['lon']
        logger.error(f"Geocoding API error: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        logger.error(f"Geocoding request failed: {e}")
    return None, None

def index(request):
    """View function to handle weather information requests."""
    BASE_URL = 'https://api.weatherbit.io/v2.0/current'
   
    API_KEY = getattr(settings, 'WEATHER_API_KEY', '')

    if request.method == 'POST':
        city = request.POST.get('city', '').strip().lower()

        if not API_KEY:
            return render(request, 'index.html', {'checker': 'API key is missing in settings.'})

        if not city:
            return render(request, 'index.html', {'checker': 'Please enter a city name.'})

        latitude, longitude = get_lat_lon(city)
        if latitude is None or longitude is None:
            return render(request, 'index.html', {'checker': 'Unable to geocode city.'})

        request_url = f"{BASE_URL}?lat={latitude}&lon={longitude}&key={API_KEY}&include=minutely"
        try:
            response = requests.get(request_url)
            logger.debug(f"Weather API response status code: {response.status_code}")
            logger.debug(f"Weather API response content: {response.text}")

            if response.status_code == 200:
                try:
                    data = response.json()
                    logger.debug(f"Weather API response JSON data: {data}")

                    if 'data' in data and len(data['data']) > 0:
                        weather = data['data'][0]
                        location = {
                            'name': city,
                            'lat': weather.get('lat', 'N/A'),
                            'lon': weather.get('lon', 'N/A'),
                            'localtime': weather.get('ob_time', 'N/A'),
                            'continent': weather.get('timezone', 'N/A')
                        }

                        context = {
                            'weather': weather.get('temp', 'N/A'),
                            'city_name': location['name'],
                            'region': weather.get('state_code', 'N/A'),
                            'country': weather.get('country_code', 'N/A'),
                            'lat': location['lat'],
                            'lon': location['lon'],
                            'localtime': convert_to_12_hour_format(location['localtime']),
                            'continent': location['continent'],
                            'static_city': city
                        }

                        return render(request, 'index.html', context)
                    else:
                        return render(request, 'index.html', {'static_city': city, 'checker': 'Unexpected response format from API.'})

                except ValueError:
                    return render(request, 'index.html', {'static_city': city, 'checker': 'Error decoding JSON response.'})
            else:
                return render(request, 'index.html', {'static_city': city, 'checker': f'Error retrieving weather data: {response.status_code} - {response.text}'})
        except requests.RequestException as e:
            logger.error(f"Weather API request failed: {e}")
            return render(request, 'index.html', {'static_city': city, 'checker': 'Error retrieving weather data.'})

    return render(request, 'index.html', {})