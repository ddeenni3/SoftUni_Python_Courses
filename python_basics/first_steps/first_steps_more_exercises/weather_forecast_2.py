temperature = float(input())
weather = None

if 26 <= temperature <= 35:
    weather = 'Hot'
elif 20.1 <= temperature <= 25.9:
    weather = 'Warm'
elif 15 <= temperature <= 20:
    weather = 'Mild'
elif 12 <= temperature <= 14.9:
    weather = 'Cool'
elif 5 <= temperature <= 11.9:
    weather = 'Cold'
else:
    weather = 'unknown'

print(weather)
