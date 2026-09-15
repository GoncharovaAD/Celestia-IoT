weather = fetch_weather()

print(weather["main"]["temp"])
print(weather["main"]["humidity"])
print(weather["wind"]["speed"])