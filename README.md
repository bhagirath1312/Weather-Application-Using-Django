# Weather Application Using Django

## Overview

This Django-based weather application allows users to get the current weather details for any city. The application integrates with the Weatherbit API to fetch weather data and the Maps Geocoding API to get latitude and longitude based on the city name.

## Features

- Retrieve current weather information for any city.
- Display weather details such as temperature, local time, and geographical coordinates.
- Convert UTC time to local time with 12-hour format.

## Prerequisites

1. **Python**: Ensure Python 3.8 or higher is installed.
2. **Django**: Install Django using pip.

## Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/bhagirath1312/Weather-Application-Using-Django.git
   cd Weather-Application-Using-Django

2. **Set Up a Virtual Environment**
   
   ```sh
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install Dependencies**
   ```sh
   Django>=4.0
   requests

4. **Change API keys**
   ```sh
   # Change Geocoding API on mainapp view.py
   api_key = " your_api_key "

   # Change Weather API key on Weather settings.py
   WEATHER_API_KEY = " your_api_key "

5. **Apply Migrations**
   ```sh
   python manage.py migrate

6. **Run the Development Server**
   ```sh
   python manage.py runserver

##
The application will be available at http://127.0.0.1:8000/.
