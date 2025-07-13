import requests

city = "ludHiana"
api_key = "6e41eebbd2ec46415a019146b6393f16"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

print("DEBUG Response:", data)

if data.get("cod") == 200:
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    print(f"\nWeather in {city}: {desc}")
    print(f"Temperature: {temp}°C")
else:
    print("\nCity not found or API error.")
