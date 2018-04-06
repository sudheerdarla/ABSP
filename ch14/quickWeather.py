#! python3
# quickWeather.py - Prints the weather for a location from the
# command line. (cmd input "py quickWeather.py 1176734") Hyderabad's ID


import json, requests, sys

# Compute location from the command line arguments.
if len(sys.argv) < 2:
	print('Usage: quickWeather.py location')
	sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
url = 'http://api.openweathermap.org/data/2.5/forecast?id=%s&APPID=fad674ff9db230340c10d5d49aa898ed' %(location)
response = requests.get(url)
response.raise_for_status()
# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# Print weather descriptions.
w = weatherData['list']
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])