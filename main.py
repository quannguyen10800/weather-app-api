import requests

API_KEY = '17832240a6cfa9438c92eeb066b99461' # API key from openweathermap
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city):
    url = BASE_URL + "q=" + city + "&appid=" + API_KEY + "&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]

        
        temperature = main['temp']
        humidity = main['humidity']
        description = weather['description']

        
        print(f"\nCity: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather Description: {description}\n")
    else:
        print(f"Error: City not found! Status code: {response.status_code}\n")


if __name__ == "__main__":
    print("Weather app starting...")
    
    while True:
        city = input("Enter city name (or type 'exit' to quit): ").strip()
        
        if city.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        
        get_weather(city)

        
        another_city = input("Do you want to check another city? (yes/no): ").strip().lower()
        
        if another_city != 'yes':
            print("Goodbye!")
            break