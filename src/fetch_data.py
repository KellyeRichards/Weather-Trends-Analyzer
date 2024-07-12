import sys
import requests

def fetch_weather_data(api_key, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    api_key = 'your_api_key'  # Replace with your actual API key
    city = input("Enter a city name: ")
    data = fetch_weather_data(api_key, city)
    if data:
        print(data)
    else:
        print("Failed to fetch data.")
