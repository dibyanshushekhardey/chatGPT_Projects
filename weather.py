import requests

# Replace 'YOUR_API_KEY' with your actual Weatherstack API key
api_key = '02b8965680a1280868f4f23d5f4f4bc6'
# Replace 'YOUR_LOCATION' with the desired location
location = 'Asansol'

# Make a request to the Weatherstack API
response = requests.get(f'http://api.weatherstack.com/current?access_key={api_key}&query={location}')

if response.status_code == 200:
    data = response.json()
    temperature = data['current']['temperature']
    weather_description = data['current']['weather_descriptions'][0]
    print(f"The temperature in {location} is {temperature} degrees Celsius.")
    print(f"The weather is {weather_description}.")
else:
    print("Error occurred while fetching weather data.")
