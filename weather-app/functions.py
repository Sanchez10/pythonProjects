import requests

def get_weather_from_api(api_key: str, city: str) -> dict:
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}"
    response = requests.get(complete_url)

    return response.json()

def get_weather(city_name: str):
    api_key = "02bedfc68309e6d0563c51fbfa750e8e"
    weather_data = get_weather_from_api(api_key, city_name)
    main_info = dict(weather_data.get("main"))
    temp_fahrenheit = float(main_info.get("temp"))
    temp_celcius = f"{temp_fahrenheit - 273.15:.2f}"
    print(temp_celcius, "°C")
