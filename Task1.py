import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Configuration
API_KEY = '400c078ffddca5ab97ec49295f8d70a3'
CITY = 'Visakhapatnam'
URL = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

# Fetch data
response = requests.get(URL)
data = response.json()

# Prepare lists
timestamps = []
temperatures = []
humidities = []

# Extract required info
for entry in data['list']:
    dt = datetime.fromtimestamp(entry['dt'])
    temp = entry['main']['temp']
    humidity = entry['main']['humidity']

    timestamps.append(dt)
    temperatures.append(temp)
    humidities.append(humidity)

# Plotting
plt.figure(figsize=(14, 6))

# Temperature
plt.subplot(2, 1, 1)
plt.plot(timestamps, temperatures, color='red', marker='o')
plt.title(f'Temperature Forecast for {CITY}')
plt.xlabel('Date & Time')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.xticks(rotation=45)

# Humidity
plt.subplot(2, 1, 2)
plt.plot(timestamps, humidities, color='blue', marker='s')
plt.title(f'Humidity Forecast for {CITY}')
plt.xlabel('Date & Time')
plt.ylabel('Humidity (%)')
plt.grid(True)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
