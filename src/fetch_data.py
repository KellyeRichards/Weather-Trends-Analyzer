import sys
import requests

def fetch_weather_data(api_key, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Will raise an exception for HTTP error responses
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")  # This will print any connection errors or HTTP errors
        return None

if __name__ == "__main__":
    api_key = '74bc7696616612eb7ddab713bd069ce8'  # Make sure this is your correct API key
    if len(sys.argv) > 1:
        city = sys.argv[1]
        data = fetch_weather_data(api_key, city)
        if data:
            print(data)  # Make sure data is being printed
        else:
            print("No data returned.")
    else:
        print("Usage: python fetch_data.py <city>")  # Inform user of how to use the script
