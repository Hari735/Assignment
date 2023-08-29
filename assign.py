import requests
import json

# API URL
api_url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

# Function to get temperature for a specific date and time
def get_temperature(data, target_date_time):
    for entry in data['list']:
        if entry['dt_txt'] == target_date_time:
            return entry['main']['temp']
    return None

# Function to get wind speed for a specific date and time
def get_wind_speed(data, target_date_time):
    for entry in data['list']:
        if entry['dt_txt'] == target_date_time:
            return entry['wind']['speed']
    return None

# Function to get pressure for a specific date and time
def get_pressure(data, target_date_time):
    for entry in data['list']:
        if entry['dt_txt'] == target_date_time:
            return entry['main']['pressure']
    return None

# Main function
def main():
    # Fetch data from API
    response = requests.get(api_url)
    weather_data = json.loads(response.text)
    
    while True:
        print("1. Get Temperature\n2. Get Wind Speed\n3. Get Pressure\n0. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            target_date_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            temperature = get_temperature(weather_data, target_date_time)
            if temperature is not None:
                print(f"Temperature at {target_date_time}: {temperature} K")
            else:
                print("Data not found for the provided date and time.")
        elif choice == '2':
            target_date_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            wind_speed = get_wind_speed(weather_data, target_date_time)
            if wind_speed is not None:
                print(f"Wind Speed at {target_date_time}: {wind_speed} m/s")
            else:
                print("Data not found for the provided date and time.")
        elif choice == '3':
            target_date_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            pressure = get_pressure(weather_data, target_date_time)
            if pressure is not None:
                print(f"Pressure at {target_date_time}: {pressure} hPa")
            else:
                print("Data not found for the provided date and time.")
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()