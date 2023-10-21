
from flask import Flask, request, render_template, redirect, url_for
import requests

app = Flask(__name__)

# Predefined list of assets with name and location
assets = [
    
]

# Mapping of weather conditions to their possible effects on equipment
weather_effects = {
    'clear': 'Ok',
    'clouds': 'No generation',
    'rain': 'Panels can be harmed - warning!',
    # Add more mappings as needed
}

# Home route to display and add assets via a form
@app.route('/', methods=['GET', 'POST'])
def index():
    # Updating weather effect for each asset based on current weather
    for asset in assets:
        location = asset['location'].replace(' ', '%20')  # Encoding location for URL
        weather_data = get_weather_data(location)
        asset['weather_effect'] = weather_data['effect']
        asset['temperature'] = weather_data['temperature']
        asset['condition'] = weather_data['condition']

    # If there is a POST request to add a new asset
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        asset = {'id': len(assets) + 1, 'name': name, 'location': location, 'weather_effect': None, 'temperature': None, 'condition': None}
        assets.append(asset)
        return redirect(url_for('index'))
    return render_template('index.html', assets=assets)

def get_weather_data(location):
    api_key = 'Write the API key'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}'
    response = requests.get(url)
    if response.ok:
        data = response.json()
        condition = data['weather'][0]['main']
        # Convert temperature from Kelvin to Celsius
        temperature = round(data['main']['temp'] - 273.15, 2)  
        effect = weather_effects.get(condition.lower(), 'Weather effect unknown')
        return {'effect': effect, 'temperature': temperature, 'condition': condition}
    return {'effect': 'Cannot retrieve weather data', 'temperature': 'N/A', 'condition': 'N/A'}

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, render_template, redirect, url_for
import requests
import json
from datetime import datetime, timedelta

app = Flask(__name__)

# Predefined list of assets with name and location
assets = [
    {'id': 1, 'name': 'Solar Panel', 'location': 'North Sea', 'weather_effect': None, 'temperature': None, 'condition': None},
    {'id': 2, 'name': 'Battery Storage', 'location': 'North Sea', 'weather_effect': None, 'temperature': None, 'condition': None},
    {'id': 3, 'name': 'Inverter', 'location': 'North Sea', 'weather_effect': None, 'temperature': None, 'condition': None}
]

# Mapping of weather conditions to their possible effects on equipment
weather_effects = {
    'clear': 'Ok',
    'clouds': 'No generation',
    'rain': 'Panels can be harmed - warning!',
}

@app.route('/', methods=['GET', 'POST'])
def index():
    for asset in assets:
        location = asset['location'].replace(' ', '%20')  # Encoding location for URL
        weather_data = get_weather_data(location)
        asset.update(weather_data)

    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        asset = {'id': len(assets) + 1, 'name': name, 'location': location, 'weather_effect': None, 'temperature': None, 'condition': None}
        assets.append(asset)
        return redirect(url_for('index'))

    return render_template('index.html', assets=assets)

def get_weather_data(location):
    api_key = 'YOUR_API_KEY'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}'
    response = requests.get(url)
    if response.ok:
        data = response.json()
        condition = data['weather'][0]['main']
        temperature = round(data['main']['temp'] - 273.15, 2)  # Convert temperature from Kelvin to Celsius
        effect = weather_effects.get(condition.lower(), 'Weather effect unknown')
        return {'weather_effect': effect, 'temperature': temperature, 'condition': condition}
    return {'weather_effect': 'Cannot retrieve weather data', 'temperature': 'N/A', 'condition': 'N/A'}

@app.route('/history/<location>')
def weather_history(location):
    # Pseudocode for fetching historical data (you need to replace this with the actual code depending on the API you choose)
    api_key = 'YOUR_API_KEY'

    # Replace the following with the actual URL and parameters as per the specific API
    start_timestamp = int((datetime.now() - timedelta(days=15)).timestamp())
    
    # This is a placeholder and should be replaced with actual API endpoint and parameters
    url = f'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=LATITUDE&lon=LONGITUDE&dt={start_timestamp}&appid={api_key}'
    
    response = requests.get(url)
    if response.ok:
        data = response.json()  # Replace this line to extract the actual data points you need
        dates = [datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d') for item in data['daily']]
        temperatures = [item['temp']['day'] - 273.15 for item in data['daily']]  # Convert Kelvin to Celsius

        return render_template('history.html', dates=json.dumps(dates), temperatures=json.dumps(temperatures), location=location)

    return "Unable to fetch historical data"

if __name__ == '__main__':
    app.run(debug=True)

